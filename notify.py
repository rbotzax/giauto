import os
from urllib import parse
from settings import log, req


class Notify(object):
    """Push all in one
    :param TG_BOT_API: Telegram Bot's api address, used to reverse the proxy Telegram API address.
    :param TG_BOT_TOKEN: Telegram Bot token. Generated when applying for bot from bot father.
    :param TG_USER_ID: The user ID of the Telegram push object.
    :param PUSH_CONFIG: Custom push configuration in JSON format.
        format:
            {"method":"post","url":"","data":{},"text":"","code":200,"data_type":"data","show_title_and_desp":false, "set_data_title":"","set_data_sub_title":"","set_data_desp":""}
        Description:
            method: required, request method. Default: post.
            url: required, complete custom push link.
            data: Optional, sent data. The default is empty, you can add additional parameters.
            text: required, the key of the status code returned by the response body. For example: the server sauce is errno.
            code: Required, the value of the status code returned by the response body. For example, the value of the server sauce is 0.
            data_type: Optional, the method of sending data, optional params|json|data, default: data.
            show_title_and_desp: Optional, whether to merge the title (application name + running status) with the running result. Default: false.
            set_data_title: Required, fill in the key of the message title in the push method data. For example: server sauce is text.
            set_data_sub_title: Optional, fill in the key of the message body in the push method data. The key of the body of the push method has a secondary structure,
                Need to cooperate with set_data_title to construct children, mutually exclusive with set_data_desp.
                For example: In the enterprise WeChat, set_data_title fills in text, set_data_sub_title fills in content.
            set_data_desp: Optional, fill in the key of the message body in the push method data. For example: the server sauce is desp.
                Mutually exclusive with set_data_sub_title, if both are filled, this item will not take effect.
    """
    # Github Actions users, please go to Repo's Settings->Secrets to set variables, the variable name must be exactly the same as the above parameter variable name, otherwise it will be invalid!!!
    # Name=<variable name>,Value=<obtained value>

    # Telegram Bot
    TG_BOT_API = 'api.telegram.org'
    TG_BOT_TOKEN = ''
    TG_USER_ID = ''
    # Custom Push Config
    PUSH_CONFIG = ''

    def __init__(self):
        # Custom Push Config
        self.PUSH_CONFIG = ''
        if 'PUSH_CONFIG' in os.environ:
            self.PUSH_CONFIG = os.environ['PUSH_CONFIG']
        # telegram
        self.TG_BOT_TOKEN = ''
        if 'TG_BOT_TOKEN' in os.environ:
            TG_BOT_TOKEN = os.environ['TG_BOT_TOKEN']

        self.TG_USER_ID = ''
        if 'TG_USER_ID' in os.environ:
            TG_USER_ID = os.environ['TG_USER_ID']

        token = ''
        if TG_BOT_TOKEN and TG_USER_ID:
            token = 'token'

        self.TG_BOT_API = ''
        if 'TG_BOT_API' in os.environ:
            TG_BOT_API = os.environ['TG_BOT_API']

    def pushTemplate(self, method, url, params=None, data=None, json=None, headers=None, **kwargs):
        name = kwargs.get('name')
        # needs = kwargs.get('needs')
        token = kwargs.get('token')
        text = kwargs.get('text')
        code = kwargs.get('code')
        if not token:
            log.info(f'{name}')
            # log.info(f'{needs} required for {name} push is not set, skipping...')
            return
        try:
            response = req.to_python(req.request(
                method, url, 2, params, data, json, headers).text)
            rspcode = response[text]
        except Exception as e:
            # : disabled; :success; :fail
            log.error(f'{name}\n{e}')
        else:
            if rspcode == code:
                log.info(f'{name}')
            # Telegram Bot
            elif name == 'Telegram Bot' and rspcode:
                log.info(f'{name}')
            elif name == 'Telegram Bot' and response[code] == 400:
                log.error(f'{name}\nPlease send a message to bot and check if TG_USER_ID is correct')
            elif name == 'Telegram Bot' and response[code] == 401:
                log.error(f'{name}\nTG_BOT_TOKEN error')
            else:
                log.error(f'{name}\n{response}')

    def tgBot(self, text, status, desp):
        TG_BOT_TOKEN = self.TG_BOT_TOKEN
        if 'TG_BOT_TOKEN' in os.environ:
            TG_BOT_TOKEN = os.environ['TG_BOT_TOKEN']

        TG_USER_ID = self.TG_USER_ID
        if 'TG_USER_ID' in os.environ:
            TG_USER_ID = os.environ['TG_USER_ID']

        token = ''
        if TG_BOT_TOKEN and TG_USER_ID:
            token = 'token'

        TG_BOT_API = self.TG_BOT_API
        if 'TG_BOT_API' in os.environ:
            TG_BOT_API = os.environ['TG_BOT_API']

        url = f'https://{TG_BOT_API}/bot{TG_BOT_TOKEN}/sendMessage'
        data = {
            'chat_id': TG_USER_ID,
            'text': f'{text} {status}\n\n{desp}',
            'disable_web_page_preview': True
        }
        conf = ['Telegram Bot', 'TG_BOT_TOKEN and TG_USER_ID', token, 'ok', 'error_code']
        name, needs, token, text, code  = conf

        return self.pushTemplate('post', url, data=data, name=name, needs=needs, token=token, text=text, code=code)

    def custPush(self, text, status, desp):
        PUSH_CONFIG = self.PUSH_CONFIG
        if 'PUSH_CONFIG' in os.environ:
            PUSH_CONFIG = os.environ['PUSH_CONFIG']

        if not PUSH_CONFIG:
            return log.info(f'Custom push')
        cust = req.to_python(PUSH_CONFIG)
        title = f'{text} {status}'
        if cust['show_title_and_desp']:
            title = f'{text} {status}\n\n{desp}'
        if cust['set_data_title'] and cust['set_data_sub_title']:
            cust['data'][cust['set_data_title']] = {
                cust['set_data_sub_title']: title
            }
        elif cust['set_data_title'] and cust['set_data_desp']:
            cust['data'][cust['set_data_title']] = title
            cust['data'][cust['set_data_desp']] = desp
        elif cust['set_data_title']:
            cust['data'][cust['set_data_title']] = title
        conf = [cust['url'], cust['data'], 'Custom push', cust['text'], cust['code']]
        url, data, name, text, code  = conf

        if cust['method'].upper() == 'GET':
            return self.pushTemplate('get', url, params=data, name=name, token='token', text=text, code=code)
        elif cust['method'].upper() == 'POST' and cust['data_type'].lower() == 'json':
            return self.pushTemplate('post', url, json=data, name=name, token='token', text=text, code=code)
        else:
            return self.pushTemplate('post', url, data=data, name=name, token='token', text=text, code=code)

    def send(self, **kwargs):
        app = 'GI Daily Check in'
        status = kwargs.get('status', '')
        msg = kwargs.get('msg', '')
        hide = kwargs.get('hide', '')
        if isinstance(msg, list) or isinstance(msg, dict):
            # msg = self.to_json(msg)
            msg = '\n\n'.join(msg)
        if not hide:
            log.info(f'Check-in result: {status}\n\n{msg}')
        log.info('Prepare push notification...')

        self.tgBot(app, status, msg)
        self.custPush(app, status, msg)


if __name__ == '__main__':
    Notify().send(app='GI Daily Check in', status='Sign-in status', msg='Details')