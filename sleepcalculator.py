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

	one_cycle = time_cycle(bedtime, 1)
	two_cycles = time_cycle(bedtime, 2)
	three_cycles = time_cycle(bedtime, 3)
	four_cycles = time_cycle(bedtime, 4)
	five_cycles = time_cycle(bedtime, 5)
	six_cycles = time_cycle(bedtime, 6)
	seven_cycles = time_cycle(bedtime, 7)
	eight_cycles = time_cycle(bedtime, 8)

	print('You should wake up at one of these times (at least 4-5 cycles recommended):\n', one_cycle, two_cycles, three_cycles,four_cycles,'\n', five_cycles, six_cycles, seven_cycles, eight_cycles)

	if not rerun():
		print("Have a Nice Day")
		break