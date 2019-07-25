# Vinson Aiono
# July 2019

# Python script to send notifications about battery life
# to stay unplugged while above 80% and to plug in once I 
# reach 40%

import os
import subprocess
import time

def notify(title, text):
    os.system("""
        osascript -e 'display notification "{}" with title "{}"'
    """.format(text, title))

def print_message(batt, src):
    print("*"*80)
    print("Battery Percentage: ")
    print(batt)
    print("Source of Power: ")
    print(src)
    print("*"*80)

while True:
    # Get battery percentage
    battery = 'pmset -g batt | grep -Eo "\d+%" | cut -d% -f1'
    bat = subprocess.Popen(
        battery, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    batt_output = bat.communicate()[0]
    # get power source
    power_source = 'pmset -g batt | grep -E "Power"'
    src = subprocess.Popen(
        power_source, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    src_output = src.communicate()[0]

    src_split = src_output.split(" ")
    print_message(batt_output, src_output)
    # print(src_split)
    if int(batt_output) >= 80 and src_split[3] == "'AC":
        print("pulling from AC")
        notify("Battery Notification", "You battery percentage has reached 80% . You may unplugg your charger")
    elif int(batt_output) <= 40 and src_split[3] == "'Battery":
        notify("Battery Notification", "You battery percentage has reached below 40% . Plug in your charger until you've reached 80%")
        print("pulling from Battery")
    
    time.sleep(900)