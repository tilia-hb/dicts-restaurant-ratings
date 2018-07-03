"""Restaurant rating lister."""


# put your code here
file = open("scores.txt","r")


restaurant_scores_dict = {}

for line in file:
	line = line.rstrip().split(":")
	name = line[0]
	score = line[1]
	restaurant_scores_dict[name] = score

def get_user_choice(restaurant_scores_dict):
	while True:
		print("\n(V) View Ratings -- (A) Add New Restaurant -- (Q) -- Quit ")
		user_choice = input("Please select an option: ")
		user_choice = user_choice[0].lower()
		if user_choice == "v":
			print_restaurant_scores(restaurant_scores_dict)
		elif user_choice == "a":
			return  get_new_restaurant(restaurant_scores_dict)
		elif user_choice == "q":
			break
		else: 
			print("Please Enter a valid choice. ")
			continue



def get_new_restaurant(dct):
	name = input("What is the name of the restaurant? ").title()
	rating_is_valid = False
	while rating_is_valid == False:
		rating = input("What is the restaurant rating? ")
		if (rating.isdecimal() == False 
			or int(rating) < 1
			or int(rating) > 5 ):

			print("Please enter a rating 1 though 5. ")
			continue
		else:
			rating_is_valid = True


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