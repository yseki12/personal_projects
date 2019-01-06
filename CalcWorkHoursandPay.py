import datetime

#Ask user for starting time
def start_time():

	while True:

		try:
		    a = datetime.datetime.strptime(input('What is your starting time??\nEnter in HH:MM(AM/PM) format (Ex. 08:00AM): '), "%I:%M%p")
		    ##print(a.strftime("%I:%M%p"))
		    return a
		    break
		except:
		    print('Please enter correct time in HHMM format')

#Ask user how long lunch break is
def lunch_time():

	while True:

		try:
			time = int(input("How long is your lunch break (in minutes)? "))
			return time
			break

		except:
			print('Please enter an integer value')

#Ask user for end time
def end_time():

	while True:

		try:
		    a = datetime.datetime.strptime(input('What is your ending time??\nEnter in HH:MM(AM/PM) format (Ex. 08:00AM): '), "%I:%M%p")
		    ##print(a.strftime("%I:%M%p"))
		    return a
		    break
		except:
		    print('Please enter correct time in HHMM format')


def calc_day_pay(timedelta):
    
    #convert timedelta object to hours
    hours = timedelta.seconds / 3600
    
    rate = float(input("Hourly Rate? "))
    
    overtime_rate = 0
    
    #convert pay according to hours worked and if any overtime
    if hours > 8:
        overtime_rate = rate * 1.5
        return round((rate*8 + overtime_rate * (hours-8)),2)
    else: 
        return round(hours * rate,2)

#Rerun program
def rerun():

	rerun = ' '

	while rerun[0] != 'y' and rerun[0] != 'n':
		rerun = input("Rerun program? (y/n) ").lower()

	if rerun[0] == 'y':
		return True
	else:
		return False

while True:

	startime = start_time()

	lunch_time_object = lunch_time()

	endtime = end_time()

	#Total time worked
	difference_time = endtime - startime - datetime.timedelta(minutes=lunch_time_object)

	difference_time_formatted = str(difference_time).split(':')
	print(difference_time_formatted[0] , 'hours', difference_time_formatted[1], 'minutes worked')

	#Ask user if he wants pay calculated
	calc_pay = ' '
	while calc_pay[0] != 'y' and calc_pay[0] != 'n':
		calc_pay = input("Calculate Pay (Net)? (y/n) ").lower()

	if calc_pay[0] == 'y':
		day_pay = calc_day_pay(difference_time)
		print('Here is your calculated pay, assuming 5 days per week, 4 weeks per month, and 12 months per year')
		print('Daily Pay: ', day_pay)
		print('Weekly Pay: ', day_pay*5)
		print('Monthly Pay: ', day_pay*5*4)
		print('Yearly Pay: ', day_pay*5*4*12)

	if not rerun():
		print("Have a Nice Day")
		break
