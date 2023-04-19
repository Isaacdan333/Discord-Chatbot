import json
import re
import random
import random_jokes
import requests

def load_json(file):
    with open(file) as bot_responses:
        print(f"Loaded '{file}' successfully!")
        return json.load(bot_responses)
    
responses_data = load_json("bot.json")

def get_responses(input_string):
    #if input_string[0] == '$':
    #    input_string = input_string[1:]
        split_message = re.split(r'\s+|[,;?!.-]\s*', input_string.lower())
        score_list = []

        for response in responses_data:
            response_score = 0
            required_score = 0
            required_words = response["required_words"]

            if required_words:
                for word in split_message:
                    if word in required_words:
                        required_score += 1

            if required_score == len(required_words):
                for word in split_message:
                    if word in response["user_input"]:
                        response_score += 1

            score_list.append(response_score)

        best_response = max(score_list)
        response_index = score_list.index(best_response)
        if input_string == "":
            return "Please type something"

        if best_response != 0:
            return responses_data[response_index]["bot_response"]

        p_message = input_string.lower()  # to ignore upper/lowercase
        #word_list = p_message.split()  # puts all the words into a list

        if split_message[0] == 'im':
            greet = "Hello" + p_message[2:] + ', I am Daddy.'
            return greet
        if split_message[0] == 'i\'m':
            greet = "Hello" + p_message[3:] + ', I am Daddy.'
            return greet
        if input_string == 'roll':
            num1 = random.randint(1, 6)
            num2 = random.randint(1, 6)
            str1 = str(num1)
            str2 = str(num2)
            roll = str1 + ' ' + str2
            if num1 == num2:
                return roll + ' - Congrats on rolling the same number!'
            else:
                return roll
        if split_message[0] == 'how' and split_message[1] == 'do' and split_message[2] == "i":
            suggest = "Try searching: '" + p_message + "' on Google"
            return suggest

        if p_message == 'is nathan dead?':
            return 'He is but he can make a resurrection.(-_-!)'

        if p_message == 'help':
            response = '`Words I will respond to: \n'
            response = response + 'hello\n'
            response = response + 'game\n'
            response = response + '(A message that starts with im or i\'m)\n'
            response = response + 'roll\n'
            response = response + 'help`'
            return response
        
        if p_message == 'joke':
            url = "https://v2.jokeapi.dev/joke/Dark"

            response = requests.get(url, 
                headers={
                "Accept": "application/json"
                })

            if json.loads(response.text)['type'] == 'single':
                joke = json.loads(response.text)['joke']

            elif json.loads(response.text)['type'] == 'twopart':
                joke = json.loads(response.text)['setup'] + ' ' + json.loads(response.text)['delivery']

            return joke
        
        if p_message == 'w':
          return random_jokes.random_insult()

        if p_message == 'h':
          return random_jokes.random_insult()
        
        if input_string[0:8] == 'p!rule34':
            return "thank you"
        
        else:
            return 'I do not understand the current message sent.'
        

while True:
    user_input = input("You: ")
    print("Bot: ", get_responses(user_input))
    if user_input == 'bye':
        break
