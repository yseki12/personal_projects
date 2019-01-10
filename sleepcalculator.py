## Will calculate what time to wake up based on 90 min sleep cycles##

import datetime

#Take in user sleep time
def bed_time():

	while True:

		try:
		    x = datetime.datetime.strptime(input('What time will you go to sleep?\nEnter in HH:MM(AM/PM) format (Ex. 08:00AM): '), "%I:%M%p")
		    return x
		    break
		except:
		    print('Please enter correct time in HHMM format')

#Return wake up time based on sleep time and how many sleep cycles)
def time_cycle(time, cycle):
    
    time = time + datetime.timedelta(minutes=90) * cycle
    return time.strftime("%I:%M%p")

def rerun():

	rerun = ' '

	while rerun[0] != 'y' and rerun[0] != 'n':
		rerun = input("Rerun program? (y/n) ").lower()

	if rerun[0] == 'y':
		return True
	else:
		return False

while True:

	print('Hello, this program will calculate optimal times to wake up based on 90 minute sleep cycles')

	bedtime = bed_time()

	print("You should wake up at one of these times (at least 4-5 cycles recommended):")

	for i in range(1,9):
		print(time_cycle(bedtime, i))
	
	if not rerun():
		print("Have a Nice Day")
		break
