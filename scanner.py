import os
import json
import gspread
from datetime import datetime, timedelta
from oauth2client.client import SignedJwtAssertionCredentials
from sms import send
import time

path_to_key = '/Users/agupta/Downloads/dash-hack-d97e3300488b.json'
path_to_google_doc = 'https://docs.google.com/spreadsheets/d/1lspOWRGh1W5LXML-z35ng4L-Oa6yweY0UD3-ytdy-pk/edit?usp' \
                     '=sharing'

watchers = ["+18055700763"]

def auth_and_fetch():
    try:
        json_key = json.load(open(path_to_key))
        scope = ['https://spreadsheets.google.com/feeds']
        #auth
        credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'], scope)
        gc = gspread.authorize(credentials)
        #get the doc
        document = gc.open_by_url(path_to_google_doc)
        sheet = document.sheet1
        return sheet
    except Exception, e:
        raise  Exception('unable to authenticate and fetch the doc : ' + str(e))

def record(event):
    try:
        sheet = auth_and_fetch()
        row_count = sheet.row_count
        sheet.resize(row_count)
        sheet.append_row(event)
        print 'event has been recorded'
    except Exception, e:
        print 'event couldn\'t be added : ' + str(e)

def scan():
    try:
        sheet = auth_and_fetch()
        row_count = sheet.row_count
        if row_count > 1:
            last_updated_row = row_count
            last_row_content = sheet.row_values(row_count)
            last_update_time  = datetime.strptime(last_row_content[0], "%d/%m/%Y %H:%M:%S")
            if last_update_time < datetime.now() - timedelta(days=2):
                print 'sending reminder'
                reminder_message = 'fish was last feed at : {0}. It\'s time to feed the fish'.format(str(
                    last_update_time))
                send(reminder_message, watchers)
                #sleep for 2 hours
                time.sleep(2*3600)
                print 'proces will wake up in 2 hrs'

            else:
                # sleep until the next feeding time
                next_feed_time = last_update_time + timedelta(days=2)
                next_check = ((next_feed_time + timedelta(minutes=60)) - datetime.now()).seconds
                print 'sleeping for {0} seconds'.format(next_check)
                time.sleep(next_check)
    except Exception, e:
        print str(e)

if __name__ == '__main__':
    while(True): # *facepalm*
        try:
            scan()
        except Exception, e:
            print "error : " + str(e)
            print time.sleep(500)