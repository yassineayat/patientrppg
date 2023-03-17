# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

# Set environment variables for your credentials
# Read more at http://twil.io/secure
account_sid = "AC93347a234d4f1e30e1abd3366488364d"
auth_token = "1dabaebf1113627102d0cc39f0251c04"
client = Client(account_sid, auth_token)

message = client.messages.create(
  body="Hello from Twilio",
  from_="+13212443412",
  to="+212681938214"
)

print(message.sid)