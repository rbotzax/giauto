# Genshin Impact Check-In Helper

[Daily Check-In](https://webstatic-sea.mihoyo.com/ys/event/signin-sea/index.html?act_id=e202102251931481&lang=en-us)

[Original Repository (defunct)](https://github.com/y1ndan/genshin-impact-helper)

[TakaGG fork](https://github.com/takagg/genshin-impact-helper)

[Napkatti fork](https://github.com/napkatti/genshin-impact-helper/)

## Heroku Method

[Heroku Branch](https://github.com/am-steph/genshin-impact-helper/tree/heroku)


## Running Locally

Inside `genshin-os.py` ctrl+f and look for `os.environ`, add a line above the if statement `OS_COOKIE = <YOUR COOKIE>`, this will hard code your cookie, but not a problem if you run locally. 

Look up a guide on setting up task scheduler to run genshin-os.py daily or at a specific time.

## Getting Your Cookie

1. Go to the Daily Check-In event website https://webstatic-sea.mihoyo.com/ys/event/signin-sea/index.html?act_id=e202102251931481&lang=en-us
2. Log in with your MiHoYo/Genshin Impact account.
3. Open the developer tools on your web browser (F12 on firefox/chrome)
4. Click on the "Console" tab
5. Type in `document.cookie` in the console
6. Copy the text output from the console  
   ![](https://imgur.com/eWP1OyO.png)

## Discord Webhooks
1. Edit channel settings. (Create your own discord server or private channel for this)
![](https://i.imgur.com/Q0KFNzv.png)
2. Go into Integrations and view webhooks.
![](https://i.imgur.com/Z4pfACE.png)
3. Create a new webhook and copy the URL.
![](https://i.imgur.com/b3ZL3m3.png)
4. Go back to the "Secrets" tab on the repository and add a new secret called DISCORD_WEBHOOK.
![](https://i.imgur.com/YusKz6V.png)
5. Run the github action again and check for message in the channel you set the webhook in
![](https://i.imgur.com/0FMvJHW.png)
