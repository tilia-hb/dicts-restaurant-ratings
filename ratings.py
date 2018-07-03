"""Restaurant rating lister."""


# put your code here
file = open("scores.txt","r")


restaurant_scores_dict = {}

for line in file:
	line = line.rstrip().split(":")
	name = line[0]
	score = line[1]
	restaurant_scores_dict[name] = score

def validate_rating():
	while True:
		rating = input("What is the rating of the restaurant? ")

		if (rating.isdecimal() == False 
			or int(rating) < 1
			or int(rating) > 5 ):

			print("Please enter a rating 1 though 5. ")
			continue
		else:
			return rating


def update_restaurant_score():
	while True:
		name = input("Please enter the name of the restaurant to update: ")
		if name not in restaurant_scores_dict.keys():
			print("I haven't recorded that restaurant yet.")
			continue
		rating = validate_rating()
		restaurant_scores_dict[name] = rating


def get_user_choice(restaurant_scores_dict):
	while True:
		print("\n(V) View Ratings -- (A) Add New Restaurant -- (U) -- Update a Score -- (Q) -- Quit ")
		user_choice = input("Please select an option: ")
		user_choice = user_choice[0].lower()
		if user_choice == "v":
			print_restaurant_scores(restaurant_scores_dict)
		elif user_choice == "a":
			return  get_new_restaurant(restaurant_scores_dict)
		elif user_choice == "u":
			update_restaurant_score()

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


def print_restaurant_scores(restaurant_scores_dict):

#	restaurant_keys_sorted = list(restaurant_scores_dict.keys())
#	restaurant_keys_sorted.sort()

	for restaurant in sorted(restaurant_scores_dict.keys()):
		print(restaurant + " is rated at " + restaurant_scores_dict[restaurant] + ".")

#restaurant_scores_dict = get_new_restaurant(restaurant_scores_dict)

#print_restaurant_scores(restaurant_scores_dict)

restaurant_scores_dict = get_user_choice(restaurant_scores_dict)







file.close()