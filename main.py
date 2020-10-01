# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from twilio.rest import Client

# Find these values at https://twilio.com/user/account
account_sid = "XXXXXXXXXX"
auth_token = "XXXXXXXXXX"

client = Client(account_sid, auth_token)

client.api.account.messages.create(
    to="+XXXXXXXX",
    from_="+XXXXXXXX",
    body="Sample text!")