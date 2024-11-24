import random

def randomJokes(void):
    #opens file randomjokes.txt and reads it
    with open('02 - Alexa tell me a joke/randomjokes.txt', 'r') as file:
        #empty list to store the jokes in a tuple
        jokes = []
        #for every line in the file separate into two after the "?"
        for line in file:
            full_joke = line.split('?')

            #if full_joke is divided into two, first element(before "?") is assigned to question variable, second is assigned to the 
            # punchline (after "?")
            if len(full_joke) == 2:
                question = full_joke[0] + '?'  
                punchline = full_joke[1] 

                #append items to jokes list
                jokes.append((question, punchline))
        return jokes


#keeps asking until quit is entered   
while True:
    user = input("Type 'Alexa, tell me a Joke' or 'quit': ")

    if user == "Alexa, tell me a Joke":
        #using the random library, im able to randomize the jokes
        question, punchline = random.choice(randomJokes('02 - Alexa tell me a joke/randomjokes.txt'))
        
        print(question)
        
        input("'Enter'")
        
        print(punchline) 

    elif user == 'quit':
        print("Goodbye!")
        break

    else:
        print("I don't understand. Please type 'Alexa tell me a Joke' or 'quit': ")


