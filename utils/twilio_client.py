from twilio.rest import Client
from config.settings import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def send_message(to, from_, body):
    print(f"\033[94mSending text to {to} from {from_}, message is {body[:100]}...\033[0m")
    return client.messages.create(to=to, from_=from_, body=body)

def health_check():
    try:
        print("\033[94mStarting health check for Twilio API and current balance...\033[0m")
        get_balance = float(client.api.account.balance.fetch().balance)
        if get_balance > 0:
            print(f"\033[92mTwilio API access confirmed and balance is OK: ${get_balance}.\033[0m")
        else:  
            print(f"\033[91mTwilio health check failed, balance too low: {get_balance}.\033[0m")
            raise Exception(f"Twilio health check failed, balance too low: {get_balance}.")
        return True
    except Exception as e:
        print(f"\033[91mTwilio health check failed, error: '{e}'.\033[0m")
        return False