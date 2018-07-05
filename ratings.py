"""Restaurant rating lister."""

from os import listdir
# put your code here

curr_directory = listdir(path='.')
curr_directory = curr_directory[1:]

def import_file_as_dictionary(filename):
	"""gets a file name, and returns a dictionary of the content

	"""
	file = open(filename,"r")

	dictionary = {}

	for line in file:
		line = line.rstrip().split(":")
		name = line[0]
		score = line[1]
		dictionary[name] = score
	file.close()
	return dictionary 




def validate_rating():
	"""asks the user for a restaurant rating, and returns a string, 1-5


	"""
	while True:
		rating = input("What is the rating of the restaurant? ")

		if (rating.isdecimal() == False 
			or int(rating) < 1
			or int(rating) > 5 ):

			print("Please enter a rating 1 though 5. ")
			continue
		else:
			return rating


def update_restaurant_score(working_dictionary):
	while True:
		name = input("\nPlease enter the name of the restaurant to update: ")
		if name not in working_dictionary.keys():
			print("I haven't recorded that restaurant yet.")
			continue
		rating = validate_rating()
		working_dictionary[name] = rating
		return working_dictionary

def change_dictionary(working_dictionary):
	print(curr_directory)

	filename = input("What file would you like to use? ")
	if filename in curr_directory:
		return import_file_as_dictionary(filename)
	elif filename.lower()[0] == "q":
		return working_dictionary		
	else:
		print("Please enter a valid filename or type (Q) Quit to return to the main menu. ")

	

def get_user_choice(working_dictionary):
	"""Asks the user for a choice, and then calls various other functions

	the input to the function is the restaurant scores dict

	"""

	while True:
		print("Current files Available:")
		print("\n\
(V) View Ratings -- \
(A) Add New Restaurant -- \
(U) Update a Score -- \
(C) Change Dictionaries -- \
(Q) Quit ")
		user_choice = input("Please select an option: ")
		user_choice = user_choice[0].lower()
		if user_choice == "v":
			print_restaurant_scores(working_dictionary)
		elif user_choice == "a":
			working_dictionary = get_new_restaurant(working_dictionary)
		elif user_choice == "u":
			working_dictionary = update_restaurant_score(working_dictionary)
		elif user_choice == "c":
			working_dictionary = change_dictionary(working_dictionary)

		elif user_choice == "q":
			break
		else: 
			print("Please Enter a valid choice. ")
			continue



def get_new_restaurant(dct):
	name = input("What is the name of the restaurant? ").title()
	rating = validate_rating()
	dct[name] = rating
	return dct


#print (restaurant_list_sorted)


def print_restaurant_scores(working_dictionary):

#	restaurant_keys_sorted = list(working_dictionary.keys())
#	restaurant_keys_sorted.sort()

	for restaurant in sorted(working_dictionary.keys()):
		print(restaurant + " is rated at " + working_dictionary[restaurant] + ".")


restaurant_scores_orig = import_file_as_dictionary("scores.txt")

get_user_choice(restaurant_scores_orig)







