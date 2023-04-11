from random import choice

def read_rating_from_file(fileName, inputs=None):
    """Read a file of restaurant ratings
    in the format restaurant:rating per line.
    """

    restaurants_rating_dict = {}
    socres_file = open(fileName)
    for line in socres_file:
        line = line.rstrip().split(":")
        restaurants_rating_dict[line[0]] = line[1]
    
    return restaurants_rating_dict

def validate_rating(restaurant_rating):
        while True:
            try:
                restaurant_rating = int(restaurant_rating)
                if restaurant_rating < 1 or restaurant_rating > 5:
                    raise Exception("Out of range")
            except:
                restaurant_rating = input("Invalid rating. Please enter a number between 1-5: ")
            else:
                break
            
        return restaurant_rating


def input_restaurant(restaurant_name, restaurant_rating):
    """Asks user to enter a restaurant name and rating,
    then validates the input.
    """
        
    while not restaurant_name or not restaurant_rating:
        restaurant_name = input("Please enter the restaurant name: ")
        
        restaurant_rating = input("Please enter the restaurant rating: ")

    restaurant_rating = validate_rating(restaurant_rating)

    return [restaurant_name, restaurant_rating]


def input_new_restaurant(restaurants_dict, restaurant_name = None, restaurant_rating = None):
    """Create a new restaurant review and adds that to the restaurant dictionary."""

    [restaurant_name, restaurant_rating] = input_restaurant(restaurant_name, restaurant_rating)
    restaurants_dict[restaurant_name] = restaurant_rating

    return restaurants_dict


def sort_restaurants(restaurants_dict): 
    """Sort the dictionary of restaurants ratings 
    in alphabetical order and prints them.
    """

    sorted_restaurants = sorted(restaurants_dict)
    for restaurant in sorted_restaurants:
        print(f"{restaurant} is rated at {restaurants_dict[restaurant]}.")

def edit_random_restaurant(restaurants_dict):
    """Choose a random restaurant and
    ask the end-user to edit the rating.
    """

    random_restaurant = choice(list(restaurants_dict))

    restaurant_rating = input(f"Please enter {random_restaurant}'s rating: ")

    restaurant_rating = validate_rating(restaurant_rating)

    restaurants_dict[random_restaurant] = restaurant_rating


def update_selected_restaurant(restaurants_dict):
    """Update selected restaurant's ratings."""

    restaurant_selection = input("\nPlease enter the restaurant "
                                 + "name you would like to rate: ")
    
    while restaurant_selection not in restaurants_dict:
        restaurant_selection = input("\nInvalid entry. "
                                     +"Please enter the restaurant "
                                     + "name you would like to rate: ")
        
    restaurant_rating = input(f"\nPlease enter {restaurant_selection}'s rating: ")
        
    restaurants_dict[restaurant_selection] = validate_rating(restaurant_rating)

    
def interactive_restaurant_rating(fileName):
    """An interative dictionary of restaurant ratings.
    """

    restaurant_ratings = read_rating_from_file(fileName)
    
    while True:
        print("\nWould you like to see all restaurant ratings, "
              + "add a new restaurant and rating, or quit? \n"
              + "a: See all restaurant ratings \n"
              + "b: Add a new restaurant and rating \n"
              + "c: Edit a random restaurant's rating \n"
              + "d: Update an existing restaurant's rating \n"
              + "q: Quit\n"
              )
        decision = input("Please enter your decision: ")
        
        if decision.lower() == "a":
            sort_restaurants(restaurant_ratings)
        elif decision.lower() == "b":
            restaurant_ratings = input_new_restaurant(restaurant_ratings)
        elif decision.lower() == "c":
            edit_random_restaurant(restaurant_ratings)
        elif decision.lower() == "d":
            sort_restaurants(restaurant_ratings)
            update_selected_restaurant(restaurant_ratings)
        elif decision.lower() == "q":
            break
        else:
            print("Invalid input.")
            continue

interactive_restaurant_rating('scores.txt')