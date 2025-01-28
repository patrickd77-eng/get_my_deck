# get_my_deck's intent
A simple stock checker which checks the Steam Deck Refurb page for stock and then texts you when it finds stock.
Since there doesn't seem to be any for refurbs out there and definitely no official way of doing this. Other options for webscrapers were paid.
You can filter for one model or all of them.
You must read all the steps below.

# Instructions for running on Windows 10/11 - Start Here

This app will run on Windows (and also should run on Linux), provided you have the necessary dependencies installed. The only files you need to consider are main.py, this readme and an environment variables file. Here are the steps to ensure it runs correctly:

# First - Download Me!
Just download the repo via GitHub or use git clone if you're able to. If it comes compressed, then extract it. It should be a folder. This link should work and will download the develop branch: https://github.com/patrickd77-eng/get_my_deck/archive/refs/heads/develop.zip

1. **REQUIRED: Install Python**:
Make sure Python is installed on your system. You can download the latest stable Windows copy from [python.org](https://www.python.org/downloads/). This will allow you to use 'pip' (python package installer) too. E.g. use 'Windows installer (64-bit)'.

2. **REQUIRED: Chrome Browser**:
Ensure you have [Google Chrome](https://www.google.com/chrome/) installed on your system. This is required so that selenium can use it. You will never see the browser when the app is running, this is intended, it's called 'headless' mode.

3. **REQUIRED: Install Required Packages**:
Navigate to the get_my_deck folder. Open a command prompt here, or already be in the terminal.
You can do this easily by clicking the explorer navigation bar and typing cmd. You can also press WIN+R and then cmd + ENTER.
The command terminal MUST be scoped to the correct folder (get_my_deck). You can't just open terminal anywhere and type this stuff in.

First, let's ensure you have the latest Python package installer.

    ```sh
    py -m pip install --upgrade pip    
    ```
Then after that:

    ```sh
    py -m pip install -r requirements.txt
    ```

If you extend this then you can add any new packages that you might add to the requirements file. If you don't want to install packages globally (not a big deal), you can make a virtual env or something.

4. **REQUIRED: Make a Twilio Individual account**
You'll need a government ID and a trial account. The money should last a good while, it's like 15 USD.
You'll need to buy a phone number with the trial money, register a 'bundle' so that you're using it legally (hence the government ID) and also verify your own number so you can send to it.
Once done, Twilio is ready.
There's plenty of guides online on how to do this.

5. **REQUIRED: Setup Local Environments Variables File**: 

Create a file called '.env' in the same folder as the codebase. It doesn't need a name, just the extension, so it should indeed just look like .env. Then use the example below to populate it... Where it says "get your own!" you'll need to change those before it'll run.

```
# Twilio Credentials
TWILIO_ACCOUNT_SID="get your own!"
# ^From 'Account Info' in console.twilio.com
TWILIO_AUTH_TOKEN="get your own!"
# ^From 'Account Info' in console.twilio.com
TWILIO_FROM_NUMBER="get your own!"
# ^'Get a phone number' in console.twilio.com. You just need SMS capabilities.
TWILIO_TO_NUMBER="get your own!"
# ^Where do you want to send notifications to? Should match the country of the above, ideally, or you might spend your money fast!

CHECK_INTERVAL=20
# ^This is in seconds. How often do you want to check?
## Lower = Higher chance of quicker notficiation, but also more chance of being blocked by Steam as spam.
## Lower = Safer but slower.

DEBUG_MODE_ON=False
# ^True if you want to see the browser and simulate a testing environment, False if not. If you want to use this seriously, leave it as False. If True, the following apply:
# - The max number of stock checks before the app stops for good is 10. 
# - The app will check every 5 seconds and ignore your CHECK_INTERVAL setting. 
# - The app will show you the browser and scroll to the stock area. 
# - The app will also simulate 'in stock' alerts and 'errors' based on a low random chance, to prove I'd work. 
# - The app will not send SMS messages to you in this mode, you will NOT spend Twilio credits.
# - The app will display additional details in the output area (console).

SEND_FAILURE_NOTIFICATION_BY_SMS=True
# ^True if you want to be notified when the app crashes while running, via SMS (will cost Twilio credits). False if not. HIGHLY suggest leaving this True.

# Default Model
REQUIRED_MODEL="OLED_512GB"
# ^MUST match the text of the examples below EXACTLY.
#Models
# "OLED_512GB"
# "OLED_1TB"
# "LCD_64GB"
# "LCD_256GB"
# "LCD_512GB"
# "Any" -> This will respond to ANY stock level changes, regardless of model. If you just want a steam deck refurb no matter what, use this.

STORE_URL="https://store.steampowered.com/sale/steamdeckrefurbished/"
# ^Used to determine which storefront the app will use. Only tested with UK, sorry!
```

6. **Now, how do I run the program?**: Execute the script using Python. Open a terminal or command prompt, navigate to the get_my_deck containing main.py, and run:

```
python main.py
```    

That's it. Just leave it running. So long as the terminal window is open and it's writing stuff out, it's active. If it crashes, it'll tell you. If it finds stock, it'll tell you. In either case, you'd need to start it again. To do that, you just repeat the same command in this step.

#FAQs
## Where should I run this? (Hosting)
It will need to be running 24/7 somewhere and be uninterrupted. Whether that's a spare PC/Laptop somewhere, or a cloud service, is your call. I personally run it on a Windows 11 mini PC in my home which is only accessed remotely. I heavily tested this and it's very reliable. The only thing I can think of would be that you might have trouble with environment variables or logging files when hosting in a cloud environment, such as Azure Functions.

## How do I uninstall?
Just delete the folder get_my_deck. That's it. The tools you installed can be uninstalled via Control Panel / Windows Settings etc. But they're useful to have and small in size.

## Is it safe?
Yes, you can read all the code, it's open source. If you don't know how, you can use GPT to tell you whether it's safe or not. It has no hidden code (no compiled files) and no executables. Check with VirusTotal if you're not sure. Also, you won't get in trouble for using it, but don't monetise it. I will never ask for money for this, and anyone asking for money is likely scamming you.

## Anything else I need?
You should have permissions to create files/folders wherever you're hosting it. It'll make some basic .txt logs. Obviously it'll need internet too...

## Disclaimer
I am not a Python dev by trade, and this is not meant to be a lesson in engineering. There are likely many "non pythonic" things, bad practises and violations of things like DRY/KIS etc. It was a quick hobby project over a few hours, so that I could find out when my preferred SD was in stock. If you like to critique open source repos, feel free to make PRs and I will test and merge when I have time. The code and logging is intentionally verbose so that people who don't code can figure it out and understand what it is doing.
Please note that changes to the Steam Store's page structure will immediately break the app, this could be silent and overnight. Only a debug and codefix will sort it out.
This is a heavily modified fork of https://github.com/maroofc/get_my_deck. Thanks to the original authors.

# Original author's instructions (for Linux) 

Thanks to https://github.com/maroofc/get_my_deck for starting the idea back in 2023. See their notes below. NOTE: The original author wrote this for a linux environment. It's not tested with my changes for Windows. Their comments relate to the main branch of their repo, which is mentioned above.

"The parts that need editing are in the ## comments.

Requirements: 
Python - Latest is fine
Selenium Chrome Drivers for Python via PIP
https://tecadmin.net/setup-selenium-with-python-on-ubuntu-debian/

Free Twilio Account and installation via PIP
pip install twilio 

Pycharm(or another IDE) - optional
If you require a different model size, then a tiny bit of googling/coding to change the text params to capture the different size model

To Run:

Command line - python main.py

This is my first bit of public code - however I put a continuous checker for 20 secs and measures to reloop and rerun if things go wrong.
I've been able to keep it running straight off my Linux based laptop for over a week so far."

## Potential improvements (for me or anyone who cares)
Would be nice to have better country/locale support.
Ability to select multiple models, rather than 1 or all.
Add a UI.
Prevent logging spam from Selenium.
Add email support.
Code refactoring/tidy up.
Figure out if there's a way to construct a checkout URL that automatically adds a deck to your basket?
Exponential backoff failure transient error handling.
Migrate to .Net C# perhaps.
Ensure it's hostable in cloud environments.