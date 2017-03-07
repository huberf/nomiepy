from pynomie import Nomie
import time

url = 'your_url'
username = 'your_db_user'
myNomie = Nomie(url, username)
allEvents = myNomie.eventList()
events = allEvents['rows']

instances = []
name = "Shower"
for i in events:
    if i['name'] == name:
        instances += [i]

tooLong = 0
# Set threshold of seven days
threshold = 7*24*60*60*1000
now = time.time()
for i in instances:
    if int(i['time']) > (now*1000) - threshold:
        tooLong += 1

if not tooLong:
    print "You need to take a shower! Now!"
else:
    print "You should smell fine. You've showered ", tooLong, " times in the past week."
