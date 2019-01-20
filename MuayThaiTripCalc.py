import re

#take user input on duration of trip; only accept certain strings
def trip_length():
    
    wordlist = ['days','day', 'week', 'weeks', 'months','month','years','year']
    while True:
        x = input("How long will your trip be? (ex. 5 days, 3 weeks, 7 months): ")
        if not re.match(r'\d+\s*\w+', x):
                print('Enter in correct format')
        else:
            if any(word in x for word in wordlist) == True:
                break
            else:
                print ('Enter in correct format')
                
    if ' ' in x:
        length, unit = re.split(r'\s+',x)
    else:
        split_input = re.split(r'(\D+)', x)
        length = split_input[0]
        unit = split_input[1]

    return (int(length), unit)

#return cost of training 
def training_cost(length,unit):

	once_a_day = {"day": 400, "week": 2000, "month": 6000, "year": 50000 }
	twice_a_day = {"day": 700, "week": 3000, "month": 10000, "year": 80000 }
	
	while True:
		try:
			freq = int(input("Do you plan on training 1x or 2x a day? (enter 1 or 2): "))
			if freq != 1 and freq != 2:
				raise ValueError
			break
		except ValueError:
			print('Please enter 1 or 2')

	if freq == 1:
		if unit[0] == 'm':
			return once_a_day["month"] * length
		elif unit[0] == 'w':
			return once_a_day["week"] * length
		elif unit[0] == 'd':
			return once_a_day["day"] * length
		elif unit[0] == 'y':
			return once_a_day["year"] * length
	elif freq == 2:
		if unit[0] == 'm':
			return twice_a_day["month"] * length
		elif unit[0] == 'w':
			return twice_a_day["week"] * length
		elif unit[0] == 'd':
			return twice_a_day["day"] * length
		elif unit[0] == 'y':
			return twice_a_day["year"] * length

#return cost of accomodation
def accommodation_cost(length,unit):
	
	basic_comfort = {'day': 300, 'week': 1500, 'month': 6000, 'year': 50000}
	medium_comfort = {'day': 800, 'week': 4000, 'month': 12000, 'year': 100000}
	high_comfort = {'day': 1500, 'week': 8000, 'month': 25000, 'year': 200000}

	while True:
		try:
			comfort = int(input('How comfortable would you like your accommodation? (1 - Basic, 2- Comfortable, 3 - Very Comfortable): '))
			if comfort < 1 or comfort > 3:
				raise ValueError
			break
		except ValueError:
			print("Please enter a number 1-3")			
	

	if comfort == 1:
		if unit[0] == 'm':
			return basic_comfort["month"] * length
		elif unit[0] == 'w':
			return basic_comfort["week"] * length
		elif unit[0] == 'd':
			return basic_comfort["day"] * length
		elif unit[0] == 'y':
			return basic_comfort["year"] * length

	elif comfort == 2:
		if unit[0] == 'm':
			return medium_comfort["month"] * length
		elif unit[0] == 'w':
			return medium_comfort["week"] * length
		elif unit[0] == 'd':
			return medium_comfort["day"] * length
		elif unit[0] == 'y':
			return medium_comfort["year"] * length	

	elif comfort == 3:
		if unit[0] == 'm':
			return high_comfort["month"] * length
		elif unit[0] == 'w':
			return high_comfort["week"] * length
		elif unit[0] == 'd':
			return high_comfort["day"] * length
		elif unit[0] == 'y':
			return high_comfort["year"] * length	

#return cost of meals
def food_cost(length,unit):

	daily_food_cost = {'thai': 200, 'mixed': 400, 'western': 800}
	
	while True:
		try:
			food_pref = int(input('What will be your food preference? (1 - Only Thai, 2 - Mixed, 3- All Western/Foreign): '))
			if food_pref < 1 or food_pref > 3:
				raise ValueError
			break
		except:
			print("Please enter a number 1-3")

	if food_pref == 1:
		if unit[0] == 'm':
			return daily_food_cost['thai'] * 30 * length
		elif unit[0] == 'w':
			return daily_food_cost['thai'] * 7 * length
		elif unit[0] == 'd':
			return daily_food_cost['thai'] * 1 * length
		elif unit[0] == 'y':
			return daily_food_cost['thai'] * 365 * length

	elif food_pref == 2:
		if unit[0] == 'm':
			return daily_food_cost['mixed'] * 30 * length
		elif unit[0] == 'w':
			return daily_food_cost['mixed'] * 7 * length
		elif unit[0] == 'd':
			return daily_food_cost['mixed'] * 1 * length
		elif unit[0] == 'y':
			return daily_food_cost['mixed'] * 365 * length

	elif food_pref == 3:
		if unit[0] == 'm':
			return daily_food_cost['western'] * 30 * length
		elif unit[0] == 'w':
			return daily_food_cost['western'] * 7 * length
		elif unit[0] == 'd':
			return daily_food_cost['western'] * 1 * length
		elif unit[0] == 'y':
			return daily_food_cost['western'] * 365 * length

#return cost of tansportation
def transportation_cost(length,unit):

	motorbike = {'day': 200, 'week': 1000, 'month': 3000, 'year': 30000}
	taxi = {'little': 50, 'some': 150, 'lot': 300}

	moto_cost = 0
	taxi_cost = 0

	rent = ' '

	while rent[0] != 'y' and rent[0] !='n':
		rent = input('Will you be renting a motorbike/scooter? (y/n): ').lower()

	if rent[0] == 'y':
		if unit[0] == 'm':
			moto_cost = motorbike["month"] * length
		elif unit[0] == 'w':
			moto_cost = motorbike["week"] * length
		elif unit[0] == 'd':
			moto_cost = motorbike["day"] * length
		elif unit[0] == 'y':
			moto_cost = motorbike["year"] * length
	else:
		moto_cost = 0

	while True:
		try:
			taxi_input = int(input('How often will you rely on taxis and other public transportation? (1 - Seldom, 2 - Sometimes, 3 - Often): '))
			if taxi_input < 1 or taxi_input >3:
				raise ValueError
			break

		except ValueError:
			print("Please enter a number 1-3")

	if taxi_input == 1:
		if unit[0] == 'm':
			taxi_cost = taxi['little'] * 30 * length
		elif unit[0] == 'w':
			taxi_cost = taxi['little'] * 7 * length
		elif unit[0] == 'd':
			taxi_cost = taxi['little'] * 1 * length
		elif unit[0] == 'y':
			taxi_cost = taxi['little'] * 365 * length

	elif taxi_input == 2:
		if unit[0] == 'm':
			taxi_cost = taxi['some'] * 30 * length
		elif unit[0] == 'w':
			taxi_cost = taxi['some'] * 7 * length
		elif unit[0] == 'd':
			taxi_cost = taxi['some'] * 1 * length
		elif unit[0] == 'y':
			taxi_cost = taxi['some'] * 365 * length

	elif taxi_input == 3:
		if unit[0] == 'm':
			taxi_cost = taxi['lot'] * 30 * length
		elif unit[0] == 'w':
			taxi_cost = taxi['lot'] * 7 * length
		elif unit[0] == 'd':
			taxi_cost = taxi['lot'] * 1 * length
		elif unit[0] == 'y':
			taxi_cost = taxi['lot'] * 365 * length

	return moto_cost + taxi_cost

#return cost of entertainment
def entertainment_cost(length,unit):

	cost_dict = {'no':0, 'little':100,'yes':300}
	party_cost = 0
	massage_cost = 0

	while True:
		try:
			party_input = int(input('Do you like to party? (1 - No, 2 - A Little, 3 - Yes): '))
			if party_input < 1 or party_input > 3:
				raise ValueError
			break

		except ValueError:
			print("Please enter a number 1-3")


	if party_input == 1:
		party_cost = 0
	elif party_input == 2:
		if unit[0] == 'm':
			party_cost = cost_dict['little'] * 30 * length
		elif unit[0] == 'w':
			party_cost = cost_dict['little'] * 7 * length
		elif unit[0] == 'd':
			party_cost = cost_dict['little'] * 1 * length
		elif unit[0] == 'y':
			party_cost = cost_dict['little'] * 365 * length
	elif party_input == 3:
		if unit[0] == 'm':
			party_cost = cost_dict['yes'] * 30 * length
		elif unit[0] == 'w':
			party_cost = cost_dict['yes'] * 7 * length
		elif unit[0] == 'd':
			party_cost = cost_dict['yes'] * 1 * length
		elif unit[0] == 'y':
			party_cost = cost_dict['yes'] * 365 * length

	while True:
		try:
			massage_input = int(input('Do you like massages? (1 - No, 2 - A Little, 3 - Yes): '))
			if massage_input < 1 or massage_input > 3:
				raise ValueError
			break

		except ValueError:
			print("Please enter a number 1-3")

	if massage_input == 1:
		massage_cost = 0
	elif massage_input == 2:
		if unit[0] == 'm':
			massage_cost = cost_dict['little'] * 30 * length
		elif unit[0] == 'w':
			massage_cost = cost_dict['little'] * 7 * length
		elif unit[0] == 'd':
			massage_cost = cost_dict['little'] * 1 * length
		elif unit[0] == 'y':
			massage_cost = cost_dict['little'] * 365 * length
	elif massage_input == 3:
		if unit[0] == 'm':
			massage_cost = cost_dict['yes'] * 30 * length
		elif unit[0] == 'w':
			massage_cost = cost_dict['yes'] * 7 * length
		elif unit[0] == 'd':
			massage_cost = cost_dict['yes'] * 1 * length
		elif unit[0] == 'y':
			massage_cost = cost_dict['yes'] * 365 * length

	return party_cost + massage_cost
	
#return cost of flight/insurance
def flight_cost(length, unit):

	ins_dict = {'day': 150, 'week': 750, 'month': 2500, 'year': 25000 }


	airfair_cost = 0
	ins_cost = 0

	airfair_input = ' '

	while airfair_input[0] != 'y' and airfair_input[0] !='n':
		airfair_input = input('Do you want to include flight costs? (y/n): ').lower()

	if airfair_input[0] == 'y':
		airfair_cost = 25000
	else:
		airfair_cost = 0

	ins_input = ' '

	while ins_input[0] != 'y' and ins_input[0] !='n':
		ins_input = input('Will you buy travel insurance? (y/n): ').lower()

	if ins_input[0] == 'y':
		if unit[0] == 'm':
			ins_cost = ins_dict["month"] * length
		elif unit[0] == 'w':
			ins_cost = ins_dict["week"] * length
		elif unit[0] == 'd':
			ins_cost = ins_dict["day"] * length
		elif unit[0] == 'y':
			ins_cost = ins_dict["year"] * length
	else:
		ins_cost = 0

	return ins_cost + airfair_cost


def misc_cost(length,unit):

	misc_cost = 0

	if unit[0] == 'm':
		misc_cost = 50 * 30 * length
	elif unit[0] == 'w':
		misc_cost = 50 * 7 * length
	elif unit[0] == 'd':
		misc_cost = 50 * 1 * length
	elif unit[0] == 'y':
		misc_cost = 50 * 365 * length	

	return misc_cost
	

#convert currency from baht to usd - formatted
def convert_currency(cost):

	cost_usd = cost * .031
	string = '${:0,.2f}'.format(cost_usd)
	return string

#format int to baht currency
def format_baht(cost):
	return ('฿{:,}'.format(cost))

#ask user to rerun program
def rerun():

	rerun = ' '

	while rerun[0] != 'y' and rerun[0] != 'n':
		rerun = input("Rerun program? (y/n) ").lower()

	if rerun[0] == 'y':
		return True
	else:
		return False

#start of main program
while True:
	print("Welcome to the Muay Thai Trip Estimator!")
	print("This will give you a rough estimate on how much it costs to live and train in Thailand")

	total_cost = 0

	length, unit = trip_length()

	cost_training = training_cost(length,unit)
	cost_accomodation = accommodation_cost(length,unit)
	cost_food = food_cost(length,unit)
	cost_transport = transportation_cost(length,unit)
	cost_entertainment = entertainment_cost(length,unit)
	cost_flight = flight_cost(length,unit)
	cost_misc = misc_cost(length,unit)

	total_cost = cost_training + cost_accomodation + cost_food + cost_transport + cost_entertainment + cost_flight

	print('\nHere is a summary of your costs for your trip\n' )

	print('Item          |    Cost in Baht    |    Cost in USD')
	print('---------------------------------------------------')
	print('Training      |', format_baht(cost_training).rjust(18,' '), '|', convert_currency(cost_training).rjust(14,' '))
	print('---------------------------------------------------')
	print('Accommodation |', format_baht(cost_accomodation).rjust(18,' '), '|', convert_currency(cost_accomodation).rjust(14,' '))
	print('---------------------------------------------------')
	print('Food          |', format_baht(cost_food).rjust(18,' '), '|', convert_currency(cost_food).rjust(14,' '))
	print('---------------------------------------------------')
	print('Transportation|', format_baht(cost_transport).rjust(18,' '), '|', convert_currency(cost_transport).rjust(14,' '))
	print('---------------------------------------------------')
	print('Entertainment |', format_baht(cost_entertainment).rjust(18,' '), '|', convert_currency(cost_entertainment).rjust(14,' '))
	print('---------------------------------------------------')
	print('Travel        |', format_baht(cost_flight).rjust(18,' '), '|', convert_currency(cost_flight).rjust(14,' '))
	print('---------------------------------------------------')
	print('Misc          |', format_baht(cost_misc).rjust(18,' '), '|', convert_currency(cost_misc).rjust(14,' '))
	print('---------------------------------------------------')
	print('Total         |', format_baht(total_cost).rjust(18,' '), '|', convert_currency(total_cost).rjust(14,' '))

	if not rerun():
		print('Hope this helps!')
		break
