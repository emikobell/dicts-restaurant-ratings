def read_rating_from_file(fileName, inputs=None):
    """Restaurant rating lister."""

    restaurants_rating_dict = {}
    socres_file = open(fileName)
    for line in socres_file:
        line = line.rstrip().split(":")
        restaurants_rating_dict[line[0]] = line[1]
    
    return restaurants_rating_dict

def validate_input(restaurant_name, restaurant_rating):
    """Validate user input."""
        
    while not restaurant_name or not restaurant_rating:
        restaurant_name = input("Please enter the restaurant name: ")
        
        restaurant_rating = input("Please enter the restaurant rating: ")

    while True:
        try:
            restaurant_rating = int(restaurant_rating)
            if restaurant_rating < 1 or restaurant_rating > 5:
                raise Exception("Out of range")
        except:
            restaurant_rating = input("Invalid rating. Please enter a number between 1-5: ")
        else:
            break
    return [restaurant_name, restaurant_rating]

def input_new_restaurant(restaurants_dict, restaurant_name = None, restaurant_rating = None):

    [restaurant_name, restaurant_rating] = validate_input(restaurant_name, restaurant_rating)
    restaurants_dict[restaurant_name] = restaurant_rating

    return restaurants_dict



def sort_restaurants(restaurants_dict): 

    sorted_restaurants = sorted(restaurants_dict)
    for restaurant in sorted_restaurants:
        print(f"{restaurant} is rated at {restaurants_dict[restaurant]}.")
        

restaurants = read_rating_from_file('scores.txt')

updated_restaurants = input_new_restaurant(restaurants)
sort_restaurants(updated_restaurants)

# In the new function
# Run read_rating_from_file
# While true
# Ask for decision
# If see all ratings, run sort_restaurants
# If add new restaurant, run input_new_restaurant
# If quit, break.