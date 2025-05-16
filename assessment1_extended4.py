from collections import OrderedDict
import random
from string import ascii_lowercase


run_quiz = True #Initialize run_quiz as True to run for the first time
user_info = {}

#This function ask the username and return it
def ask_username():
    while True:
        user_name = input("Please enter your name:")
        #Handling empty input and allow other types as it is name
        if user_name:
            return user_name
            break
        else:
            print("Please enter a valid username\n")

#This function ask the user the number of questions to be generate
#User input error are handled by using exception
def ask_num_questions():
    while True:
            try:
                num_questions = int(input("Please enter the number of question you wish to take(1 to 15):"))
                return num_questions
            except ValueError:
                print("Please enter the integer value of question numbers.")


#####while loop to end the asking question loop and calculate score#####
while run_quiz!=False:
    current_username = ask_username()
    userreq_questions = ask_num_questions()
    score = 0

#Questions are referenced from https://www.ef.com/wwen/blog/language/questions-virtual-pub-quiz/ 
    questions_db = {
                    "How many time zones are there in Russia?": ["11", "12", "13", "14"],
                    "What\'s the national flower of Japan?": ["Cherry blossom", "Orchid", "Rose", "Tulip"],
                    "How many stripes are there on US flag?": ["13","14","10","12"],
                    "What\'s the national animal of Australia?": ["Kangaroo", "Tiger", "Panda", "Koala"],
                    "How many days does it take for the earth to orbit the Sun?": ["365","153","663","120"],
                    "Which of the following empires had no written language?": ["Incan","Aztec", "Egyptian", "Roman"],
                    "Until 1923, what was the Turkish city of Istanbul called?": ["Constantinople","Yangon", "Jerusalem","Cairo"],
                    "What\'s the smallest country in the world?": ["Vartican City", "Monaco", "Nauru", "Tuvalu"],
                    "What\'s the capital of Canada?": ["Ottawa","Montreal","Quebec","Toronto"],
                    "Name the longest river in the world?": ["Nile", "Amazon River", "Yangtze", "Ayeyarwady"],
                    "Name the best-selling book series of the 21st century?": ["Harry Potter","A Tale of Two Cities", "The Hobbit", "Alice's Adventures in Wonderland"],
                    "How many keys does a classic piano have?": ["88","124","96","56"], 
                    "Where was the first modern Olympic Games held?": ["Athens","Milan", "Olympia","Amazon"],
                    "Name the Disney\'s first flim?":["Snow White","Beauty and the Beast","Cinderella","Sleeping Beauty"],
                    "What was the most-watched series on Netflix in 2019?": ["Stranger Things","Lucifer","13 Reasons Why","The Umbrella Academy"]
                }


    adj_questions = min(userreq_questions, len(questions_db)) #Find the minimum of user requested question and available questions 
    
    questions = random.sample(list(questions_db.items()),k=adj_questions) #generate shuffled questions set by user using random sample with k = adjusted questions
    
#####for loop to ask questions and print marks#####
#Multiple choice is used to reduce user input errors
    #use for loop and list the question starting from 1 using enumerate
    for num, (question, possible_answers) in enumerate(questions, start=1): 
        print(f"\nQuestion {num}: {question}")
        correct_answer = possible_answers[0] #keep the correct answer

        possibleans_list = dict(zip(ascii_lowercase, random.sample(possible_answers, k=len(possible_answers)))) #all answers listed with the small letter are randomly generated
        for list, all_ans in possibleans_list.items(): #use enumerate to generate the list numbers
            print(f"{list}. {all_ans}")
        
        #User input error handling when the input is not the alphabet listed in the choices
        while (answer_list := input ("\nYour answer: ")) not in possibleans_list:
            print(f"Please answer the alphabet in the list only")
         #take user input answer
        answer = possibleans_list[answer_list] #retrieve the answer value using list value
        if answer == correct_answer:
            score += 1
            print (f"Correct! You score : {score}\n")
        else:
            print(f"Opps! The correct answer is {correct_answer}.")

    score_percent = (score/adj_questions) * 100
    print (f"\nGreat {current_username}! You get correct {score} questions out of {adj_questions}.\nTotal socre: {score_percent}%\n" )

    #Record the username and score into user_info dictionary
    user_info [current_username] = score

    #ask if there is anyone alse to take the quiz 
    another_user = input ("Is there anyone else to take the quiz? \n(y/n)").lower()
    if another_user == "y" or another_user=="yes":
        run_quiz = True
    else:
        run_quiz = False

#####Find the maximum scorer of all users#####

#uses sort and OrderDict to re-arrange the dictionary from maximum to minimum
sorted_userscore = OrderedDict(sorted(user_info.items(), key=lambda item:item[1], reverse=True))

#Print the highest scorer and score
print("\nRanking from the highest scorer to the lowest scorer")
for k, v in sorted_userscore.items():
    print (f"{k} : {v}")

#Find the average of all players
avg = 0
for val in user_info.values():
    avg += val
avg = avg / len (sorted_userscore)
print("Average score of all players : " + str (avg))
