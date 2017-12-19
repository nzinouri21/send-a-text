from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC014f1d5728fa7df4e8e39021dcf55162"
# Your Auth Token from twilio.com/console
auth_token  = "f14dafcf9cfc44e4e366e533eaa41482"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+15558675309",
    from_="+15017250604",
    body="Hello from Python!")

print(message.sid)
