from twilio.rest import Client
from config.settings import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def send_message(to, from_, body):
    print(f"\033[94msending text to {to} from {from_}, message is {body[:20]}...\033[0m")
    print(f"\033[94mRaw SMS: {client.messages.create(to=to, from_=from_, body=body)}\033[0m")
    return client.messages.create(to=to, from_=from_, body=body)