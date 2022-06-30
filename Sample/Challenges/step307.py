from datetime import datetime
import pytz

tz_1 = pytz.timezone('America/Los_Angeles')
tz_2 = pytz.timezone('America/New_York')
tz_3 = pytz.timezone('Europe/London')

timePortland = datetime.now(tz_1)
timeNewYork = datetime.now(tz_2)
timeLondon = datetime.now(tz_3)

print("Current Time is:", timePortland.hour)
print("Current Time is:", timeNewYork.hour)
print("Current Time is:", timeLondon.hour)

branches = [timePortland,timeNewYork,timeLondon]
branchName = ['Portland','New York','London']
print(branches)



if timePortland < timeNewYork:
    print(1)
else:
    print(2)

print(type(timePortland))

print("\n")

x = 0
for i in branches:
    if i.hour > 9 or i.hour > 17:
        status = 'open'
    else:
        status = 'closed'
    print('The {} branch is {}.'.format(branchName[x],status))
    x = x + 1

'''
now = datetime.datetime.now()
print(now)

portland = datetime.datetime
'''


























#if __name__ == "__main__":
    
