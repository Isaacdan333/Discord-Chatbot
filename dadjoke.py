# Import modules
import random
import requests
import json

# Saving the URL in a variable
url = "https://icanhazdadjoke.com/search"

# Creating a function to get user's input for a type of joke
# Then taking that input and searching the API for that topic and returning a random joke
def get_joke():

    # Gets user input for the term to search using GET request
    search_term = input("Let me tell you a joke! Give me a topic: ")

    # Get request with JSON header and parameter term to search from users input
    response = requests.get(
        url,
        headers = {
            "Accept": "application/json"
        },
        params = {
            "term": search_term
        }
    )
    print(json.loads(response.text))

    # converts the JSON file to a python dict
    data = response.json()

    # Uses the key total_jokes from dict to get a value
    total = data["total_jokes"]

    # Based on if a joke on the search term was found and how many, will return the joke from the
    # request. Data is a dictionary, results is a key that returns a list value that holds dictionaries.
    if total == 1:
        print(f"I have got one joke about {search_term}.")
        print(data["results"][0]["joke"])
        
    # Selects a random joke from total amount of jokes found if there is more than one   
    elif total > 1:
        print(f"I have found {total} jokes about {search_term}.")
        rand_num = random.randint(0, total - 1)
        print(data["results"][rand_num]["joke"])
    
    # No joke found
    else:
        print(f"I'm sorry. I could not find any jokes on {search_term}.")
        
        
get_joke()