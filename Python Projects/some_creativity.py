from twilio.rest import Client
import time

# Twilio credentials
account_sid = 'YOUR_ACCOUNT_SID'
auth_token = 'YOUR_AUTH_TOKEN'
twilio_phone_number = 'YOUR_TWILIO_PHONE_NUMBER'
recipient_phone_number = 'RECIPIENT_PHONE_NUMBER'

# Initialize Twilio client
client = Client(account_sid, auth_token)

# List of messages to send
messages = [
    "Hello!",
    "How are you?",
    "Just checking in.",
    "Have a great day!"
]

# Send messages repeatedly
while True:
    for message in messages:
        message = client.messages.create(
            body=message,
            from_='whatsapp:' + twilio_phone_number,
            to='whatsapp:' + recipient_phone_number
        )
        print(f"Message sent: {message.sid}")
        time.sleep(5)  # Adjust the delay between messages (in seconds) as needed
