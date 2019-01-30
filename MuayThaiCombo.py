import random

## Muay thai techiniques ##

punches = ('Jab','Cross','Right Uppercut', 'Left Uppercut', 'Left Hook (Head)', 'Left Hook (Body)', 'Right Hook (Head)', 'Right Hook (Body)', 'Superman', 
	'Spinning Backfist','Overhand')
kicks = ('Right Body Kick', 'Right Head Kick', 'Right Low Kick', 'Left Body Kick', 'Left Head Kick', 'Left Low Kick', "Spinning Back Kick")
teeps = ('Front Teep', 'Rear Teep', 'Jump Teep', 'Side Teep')
elbows = ('Horizontal Elbow', 'Uppercut Elbow', 'Slashing Elbow', 'Spinning Back Elbow', 'Diagonal Elbow')
knees = ('Right Knee', 'Left Knee', 'Jump Knee')
defense = ('Block', 'Evade', 'Parry', 'Avoid', 'Check', 'Catch', 'Redirect', 'Disrupt')


## User input asking length of combination ##
def combo_length():

	while True:

		try:
			combo_length_var = int(input('How long would you like your combination (Enter Number)? '))

		except:
			print("Please enter a number")

		else:
			return combo_length_var

## User input asking what type of combination ##
def menu_choice():

	while True:

		try:
			choice = int(input("Please choose one of the following options:\n 1. All Offensive Combination \n \
2. All Offensive Combination with Defense\n 3. Upper Body Strikes (Punches, Elbows) \n 4. Lower Body Strikes (Kicks, Knees, Teeps)\
\n 5. Punches + Kicks \n 6. Knees + Elbows: "))
			if choice not in range (1,7):
				raise ValueError
		except TypeError:
			print("Please enter a number")

		except ValueError:
			print("Please choose a menu item 1-6")

		else:
			return choice


print("Welcome to Muay Thai Combo Generator")

while True:

	combolength = combo_length()

	menuchoice = menu_choice()

	if menuchoice == 1:
		combo1 = random.sample(punches + kicks + teeps + elbows + knees, combolength)
		print(' + '.join(combo1))

	elif menuchoice == 2:
		combo2 = random.sample(punches + kicks + teeps + elbows + knees + defense, combolength)

		#Make sure at least one defense maneuver is in combination
		while any(i in combo2 for i in defense) == False:
			combo2 = random.sample(punches + kicks + teeps + elbows + knees + defense, combolength)
			if any(i in combo2 for i in defense) == True:
				break
		print(' + '.join(combo2))

	elif menuchoice == 3:
		combo3 = random.sample(punches + elbows, combolength)
		print(' + '.join(combo3))

	elif menuchoice == 4:
		combo4 = random.sample(kicks + teeps + knees, combolength)
		print(' + '.join(combo4))

	elif menuchoice == 5:
		combo5 = random.sample(punches + kicks + teeps, combolength)
		print(' + '.join(combo5))

	elif menuchoice == 6:
		combo6 = random.sample(knees + elbows, combolength)
		print(' + '.join(combo6))

	replay = input("Would you like another combo (y/n)? ").lower()

	if replay[0] == 'y':
		continue
	else:
		print("Thanks for using the Muay Thai Combo Generator")
		break