from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC014f1d5728fa7df4e8e39021dcf55162"
# Your Auth Token from twilio.com/console
auth_token  = "f14dafcf9cfc44e4e366e533eaa41482"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+18155172222",
    from_="+16308825017",
    body="Hello from Python!")

print (message.sid)


#A few things about classes and instances from this mini-chapter!
#
#What is a class?
#Classes provide means to bundle data and functionality together.
#Creating a new class creates a new type of object, allowing new instances of
#that type to be made.
