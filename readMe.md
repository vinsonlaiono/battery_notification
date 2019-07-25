### Battery Notification for Mac
- After some research showing that the sweet spot for a battery life was between 40% and 80%
I wanted a script that would notify me to unplug my charger once i reach 80% and to let me know when im
at 40% and to charge it up again. I dont know that this is helpful for an updated mac but I though it would be fun to write it anyway.
This is nothing special but it kinda works

### Run script as a background service
```
nohup python battery_notification.py -u &
```
