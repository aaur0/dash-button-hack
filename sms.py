from twilio.rest import TwilioRestClient

# put your own credentials here
ACCOUNT_SID = ""
AUTH_TOKEN = ""


def send(msg, recievers, sender="+12626313635"):
    try:
        client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
        for reciever in recievers:
            client.messages.create(to=reciever, from_=sender, body=msg)
            print 'message to ' + reciever + " sent."
    except Exception, e:
        print str(e)


if __name__ == '__main__':
    sender = "+12626313635"
    reciever = ["+18055700763"]
