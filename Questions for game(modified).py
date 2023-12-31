questions = ("Which of the following is the best options to reduce pollution?: ",
             "Which of the following habitats are most affected the most due to an increase in temperature?: ",
             "Which animal population is drastically being affected due to melting ice caps?: ",
             "Which of the following cases is a result of climate change?: ",
             "Which of the following is a greenhouse gas? (Bonus points for the correct answer, increased point deduction for the incorrect answer): ",
             "Global warming leads to climate change. Is this statement true or false?: ",
             "What has been the main cause of climate change since the 1800s?: ",
             "Fishing is a cause of climate change. Is this statement true or false?: ",
             "Which of the following is a contributer to climate change?: ",
             "In which of the following cases resembles a case where humans are most impacted by climate change?: ")

options = (("Option A: Plant lesser trees" ,"Option B: Make use of solar power instead of fossil fuels", "Option C: Burn more forests" ,"Option D: Make use of cars which operate on petrol?"),
           ("A: Ice caps", "B: Deserts", "C: Rainforests", "D: Wetlands"),
           ("A: Tigers", "B: Elephants", "C: Dogs", "D: Polar bears"),
           ("A: Excessive rainfall", "B: Heat waves", "C: Drought", "D: All of the above"),
           ("A: CH2","B:CO2","C: Water vapour","D: All of the above"),
           ("A:True", "B:False", "C:Both", "D:None of the above"),
           ("A: Human activities", "B:Natural causes", "C:Neither A nor B", "D:Both A and B"),
           ("A:True", "B:False", "C: Both", "D:None of the above"),
           ("A:Smoke from a factory", "B:CO2 taken in by trees in a forest", "C:Carpooling", "D:Energy generated by solar panels"),
           ("A:Floods destryoing people's homes causing them to not migrate", "B:Floods which affect crop production", "C:Extreme heat waves causing people to sweat more", "D:Forest fires destroying natural vegetation causing the air to become more polluted resulting in breathing problems for humans and animals"))

Correct_Answers = ("B", "A", "D", "D", "D", "A", "A", "B", "A","D")
score = 0
user_answer = ()
question_number = 0

for question in questions:
    print("\n")
    print(question)
    for option in options[question_number]:
        print(option)
        
    while True:
        user_answer = input("A or B or C or D: ").upper()
        if user_answer in ('A', 'B', 'C', 'D'):
            break
        else:
            print("INVALID OPTION. ENTER VALID OPTION")
            
    
    if user_answer == Correct_Answers[question_number]:
        score = score + 5
        print("Answer is correct and your score is " + str(score))
    else:
        score = score - 10
        print("Answer is incorrect and your score is " + str(score))

    question_number = question_number + 1
print('\n')
print("You have successfully answered all the question and your final score is " + str(score))
print("If you wish to play more, you can head to the other fun games available on the website")
           
           
                      
             
