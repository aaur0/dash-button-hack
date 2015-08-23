from twilio.rest import TwilioRestClient

# put your own credentials here
ACCOUNT_SID = "ACee0b4908490e9c73d4d7cdbdd137aab1"
AUTH_TOKEN = "b9506408de46a07c32d92c37a310d01d"


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
