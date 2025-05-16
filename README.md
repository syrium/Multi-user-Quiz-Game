# Multi-user-Quiz-Game
This is a beginner project I made for my software engineering assignment. This program has deficiencies and is not perfect. Any suggestion is gladly welcome.

# How to use

1. Enter username
2. Enter the number of questions you wish to answer
3. When the questions are displayed, choose the correct answer
    by selecting the listing alphabets (a. b. c. d. etc.)
    - if the answer is incorrect, it will display the correct answer
    - Total score will be displayed each time.
4. After the selected number of questions are answered,
    you will be asked if there is any other player/user to take the quiz.
    Type (y) if there is another user, else type (n).
5. If (y) is typed in, steps 1-4 will be repeated.
6. If (n) is typed in, the program will calculate the highest scorer among all users and
    the 
    the average score of all users will be calculated.
    - The program will exit.

# Features of the program

This is a small console-based quiz in Python which performs the description given below.

- The quiz asks the user(s) 10 questions. Some of my quizzes are referenced from https://www.ef.com/wwen/blog/language/questions-virtual-pub-quiz/
- This is a program which reads in, from the console (command line), ten quiz questions and ten correct answers, one correct answer for each question.

Once these questions are added to the program, the console (command line) interface is extended so that it:

- Asks the user their name
- Runs through all questions of the quiz and keeps a running score of the number of correctly answered questions;
- Once the user has answered all the questions, the system prints out their score out of 10 as well as a percentage score on the screen;
- The program then prompts to ask if anybody else wants to take the quiz. It should then perform steps 1-4 again for the next user;
- Once all the users have finished the quiz, the program displays:
    - The name of the user with the highest score (as well as other users’ scores).
    - The average score of all users.
- It makes use of conditional statements, iterative statements, functions, data structures, etc., in the program.
- The program handles user errors (e.g., incorrect input type, such as empty answer or name, etc.).

Additional features:

- Produce a quiz which can ask any number of questions (i.e. user can specify the number of questions they want to answer, e.g., 15 questions).
- The system displays questions in random order each time the quiz is taken.
- The user is shown which questions they got correct and which they got incorrect (as well as showing the correct answer for any questions they answered incorrectly).
