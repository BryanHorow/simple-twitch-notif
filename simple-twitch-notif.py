import time
import twitch
import urllib.request
helix = twitch.Helix('<CLIENT_ID>', 'CLIENT_SECRET')
while(True):
    broadcasterType = helix.user('<BROADCASTER_NAME>').broadcaster_type
    if broadcasterType == 'affiliate' or broadcasterType == 'partner':
        urllib.request.urlopen(
            'http://api.callmebot.com/text.php?user=@<TELEGRAM_USERNAME_OR_PHONE>&text=GOT')
        break
    time.sleep(30)
