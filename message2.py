from twilio.rest import Client

# Your Twilio account SID and auth token
account_sid = 'ACf190a14960edff87d8282418b0dd58e5'  # Replace with your Account SID
auth_token = '83a342012a42426b4704283ef5bfc8c7'
client = Client(account_sid, auth_token)

# Define the recipient and sender phone numbers
to_phone_number = '+917389662355'       # Replace with the recipient's phone number
from_phone_number = '+17628883013'    # Replace with your Twilio phone number

# URL of the image accessible publicly on the internet
media_url = 'https://th.bing.com/th/id/OIP.7GhirOfe7je18WsmZJ063wHaJ4?w=208&h=277&c=7&r=0&o=7&cb=iwp2&dpr=1.3&pid=1.7&rm=3'
message = client.messages.create(
    body='Here is your alert image!',
    from_=from_phone_number,
    to=to_phone_number,
    media_url=[media_url]
)

print(f'Message sent with SID: {message.sid}')
