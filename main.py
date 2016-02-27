import time, tweepy
from datetime import datetime
from pytz import timezone
import pytz

def main():
    CONSUMER_KEY = ''
    CONSUMER_SECRET = ''
    ACCESS_KEY = ''
    ACCESS_SECRET = ''

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)

    utc = datetime.utcnow().replace(tzinfo=pytz.utc)
    current_time = utc.astimezone(pytz.timezone('Europe/Stockholm'))
    current_hour = current_time.hour

    time.sleep(current_hour * 60)

    beating_heart_emoji = '\xF0\x9F\x92\x93'
    
    api.update_status(status="%s %02d:%02d %s" % (beating_heart_emoji, current_hour, current_hour, beating_heart_emoji))

if __name__ == '__main__':
    main()