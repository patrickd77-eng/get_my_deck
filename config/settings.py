import os
from dotenv import load_dotenv

print("\033[94mLoading your environment variables...\033[0m")
load_dotenv()

#Credentials for Twilio
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_FROM_NUMBER = os.getenv("TWILIO_FROM_NUMBER") 
TWILIO_TO_NUMBER = os.getenv("TWILIO_TO_NUMBER")

#Debugging/Error handling
SEND_FAILURE_NOTIFICATION_BY_SMS = os.getenv("SEND_FAILURE_NOTIFICATION_BY_SMS", "True").lower() == "true"
DEBUG_MODE_ON = os.getenv("DEBUG_MODE_ON", "False").lower() == "true"

#Running settings
REQUIRED_MODEL = os.getenv("REQUIRED_MODEL")
STORE_URL = os.getenv("STORE_URL", "https://store.steampowered.com/sale/steamdeckrefurbished/")
CHECK_INTERVAL = int(os.getenv("CHECK_INTERVAL", 20))

#Validate required ones
required_env_vars = {
    "TWILIO_ACCOUNT_SID": TWILIO_ACCOUNT_SID,
    "TWILIO_AUTH_TOKEN": TWILIO_AUTH_TOKEN,
    "TWILIO_FROM_NUMBER": TWILIO_FROM_NUMBER,
    "TWILIO_TO_NUMBER": TWILIO_TO_NUMBER,
    "REQUIRED_MODEL": REQUIRED_MODEL
}

#Notify user of missing environment variables
for var_name, var_value in required_env_vars.items():
    if var_value.lower() in (None, 'get your own!'):
        raise ValueError(f'Please set the {var_name} environment variable in the .env file')