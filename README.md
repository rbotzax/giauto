# Genshin Impact Check-In Helper

[Daily Check-In](https://webstatic-sea.mihoyo.com/ys/event/signin-sea/index.html?act_id=e202102251931481&lang=en-us)

[Original Repository (defunct)](https://github.com/y1ndan/genshin-impact-helper)

[TakaGG fork](https://github.com/takagg/genshin-impact-helper)

[Napkatti fork](https://github.com/napkatti/genshin-impact-helper/)


# Running Locally

Check out napkatti fork on setting variables and running locally
[napkatti fork](https://github.com/napkatti/genshin-impact-helper/tree/master)

# Heroku

[Broken Down Instructions](https://github.com/am-steph/genshin-impact-helper/wiki)

Click button at bottom for next step

[<img src="https://raw.githubusercontent.com/am-steph/genshin-impact-helper/master/arrow.png" width=75>](https://github.com/am-steph/genshin-impact-helper/wiki)

### Update
*A procfile has been added on the [heroku branch](https://github.com/am-steph/genshin-impact-helper/tree/heroku) for those that want to run from a heroku worker dyno, this does not require credit card for validation. 
~~however it will **only run for 23 days a month** as you are only allotted 550 dyno hours a month (you get another 450 hours after you validate with a credit card but if you are going to validate with a CC, might as well just use Heroku Scheduler)*If you are fine with it only operating 23 days a month, for the first step make sure to clone the heroku branch instead with~~

https://devcenter.heroku.com/articles/free-dyno-hours

Currently testing, will need more information as to if this consumes hours constantly. 

`git clone --branch heroku https://github.com/am-steph/genshin-impact-helper.git`

## Requirements
You will need to install Git and Heroku if you wish to use Heroku for the login helper.

[Git Downloads](https://git-scm.com/downloads)

[Heroku Signup](https://signup.heroku.com/)

[Heroku CLI](https://devcenter.heroku.com/articles/getting-started-with-python#set-up)

Follow the instructions and sign into Heroku after installing the CLI from either command prompt or terminal whichever you use.

A GitHub account is not required/needed to clone this repo, you only need a Heroku account.

**You need a credit card for the heroku-scheduler portion, don't worry they will not charge you (this is just to prevent abuse). You can use a prepaid credit card or similar for this if you don't want to use your actual card.**

## Usage

### 1. Clone this branch

This will create a new folder `genshin-impact-helper` in the working directory path you executed the command, when you first open command prompt it'll usually take you to `C:\Users\YOUR-NAME`, you can type `start .` in command prompt to see where it will be cloned.

```
git clone https://github.com/am-steph/genshin-impact-helper.git
```
**Do not close the command prompt, keep it open**

### 2. Create a Heroku App

  [Heroku Dashboard](https://dashboard.heroku.com/apps)

  You can either create a app from your Heroku dashboard or just run `heroku create`
  
  *If you use `heroku create`, it will make a random app name (e.g. alphine-15735)*

  ![](https://i.imgur.com/iqbP3Ah.png)


### 3. Follow instructions in app dashboard to deploy your code to Heroku

  ![](https://i.imgur.com/v0fgQ31.png)

  **This is a repeat of the instructions in the image above for copy and pasting/clarification**
  
  Login to Heroku if you haven't already. It should bring up a webpage to login.
  
  ```
  heroku login
  ```
  
  Navigate to your project folder, because we cloned this repo we enter `cd genshin-impact-helper`
  
  ```
  cd genshin-impact-helper
  
  git init
  
  heroku git:remote -a YOUR-APP-NAME-HERE  #replace YOUR-APP-NAME-HERE with the app name of your heroku application 
  ```

  ```
  git add .
  
  git commit -am "initial commit"
  
  git push heroku master
  ```

  This is roughly what it should look like and the expected output when you enter in the commands.
  ![](https://i.imgur.com/3LzuI7o.png)


If for some magical reason it fails to push, try `git push heroku HEAD:master` (Thanks to doraemon#9784 for finding this)


### 4. Next we need to grab our cookie

  To get your cookie go to the Daily Check-In event website https://webstatic-sea.mihoyo.com/ys/event/signin-sea/index.html?act_id=e202102251931481&lang=en-us

  Log in with your MiHoYo/Genshin Impact account.  
   *If you have never checked in before, manually check in once to ensure that your cookies are set properly.*

   Open the developer tools on your web browser (F12 on firefox/chrome)

   Click on the "Console" tab

   Type in `document.cookie` in the console
   
### 5. Copy the text output from the console  
   ![](https://imgur.com/eWP1OyO.png)

 If you are getting `list index out of range`

**Don't copy the quotation marks**

Value should look like: login_ticket=xxx; account_id=696969; cookie_token=xxxxx; ltoken=xxxx; ltuid=696969; mi18nLang=en-us; _MHYUUID=xxx

The semi-colons seperate the values (e.g. `login_ticket=` and `account_id=` are different values), the order these values are in doesn't matter, it can start with `login_ticket` or it could start with `ltoken`, but make sure you have every value listed above. 

### 6. Next we need to set up environment variables, navigate to settings and click Reveal Config Vars

   ![](https://i.imgur.com/5fBviLV.png)
   
   Go to Google and type 'what is my user agent' and copy your user agent 
   
   ![](https://i.imgur.com/4zXcZAU.png)
   
   Enter `USER_AGENT` in KEY and your user agent you copied in VALUE and click Add.
   
   ![](https://i.imgur.com/U592b4t.png)

### 7. Enter `OS_COOKIE` in KEY and paste in your copied cookie in VALUE

  ![](https://i.imgur.com/POIwX3J.png)
    
  Your token should look like this
  
  ![](https://i.imgur.com/eng0eF7.png)
    
    **IF YOU WANT TO CHECK-IN MULTIPLE GENSHIN ACCOUNTS:**
    1. Paste your first cookie into the Value box on Heroku, but do not click "Add" yet.
    2. Open a new private browsing / Incognito window
    3. Go to the MiHoYo event website on your new browser instance, and log in with your second account
    4. Copy the `document.cookie` as before
    5. Go back to the Heroku page, and type a hash `#` at the end of your first cookie
    6. Paste your second cookie immediately after the `#` and remove the quotation marks "" if needed
    7. Click "Add"


  You can always click the pencil icon later on to edit your OS_COOKIE value if you want to add another account

  If you wish to add a Discord webhook to receive notifications when the login helper runs, you can add another key value `DISCORD_WEBHOOK`. Look at the end of the page to see where you can get your webhook.

8. Go to Resources tab and add the Heroku Scheduler add-on, don't worry this is free

  ![](https://i.imgur.com/q8GXou0.png)
  ![](https://i.imgur.com/zYpVcBN.png)
  ![](https://i.imgur.com/7SP6tQu.png)

9. Create a new job, set it to run everyday at the time you wish (time is in UTC)

  ![](https://i.imgur.com/sbYkhcX.png)

  For the command, put `python run.py`

  ![](https://i.imgur.com/Co9dyvP.png)

If you want to test to see if your script will run go back to your command window and type `heroku run bash`. After you are loaded in, type `python run.py` and check.

![](https://i.imgur.com/MCPBp6J.png)

There is a random sleep time inserted in the script, if it says sleeping for x amount of time just wait it out.

**If you no longer want to check in automatically, you can disable/delete the scheduler**


## Discord Webhooks
This is an **OPTIONAL** step to let the script send you a notification on Discord whenever it runs a check-in.

1. Edit channel settings. (Create your own discord server or private channel for this)
   ![](https://i.imgur.com/Q0KFNzv.png)
2. Go into Integrations and view webhooks.
   ![](https://i.imgur.com/Z4pfACE.png)
3. Create a new webhook and copy the URL.
   ![](https://i.imgur.com/b3ZL3m3.png)
4. Go back to the "Settings" tab on the app and add a new KEY called DISCORD_WEBHOOK and paste in the URL.

To stop receiving Discord notifications, delete your DISCORD_WEBHOOK secret.


