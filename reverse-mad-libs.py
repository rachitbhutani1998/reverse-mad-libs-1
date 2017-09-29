# Question for first_level 
first_level = """__1__ is a performing art form consisting of purposefully selected sequences of __2__ movement.
 This movement has aesthetic and symbolic __3__ , and is acknowledged as dance by performers and observers within a particular culture.
  Dance can be categorized and described by its __4__ ,
 by its repertoire of movements, or by its historical period or __5__ of origin."""
# Answer for first_level
first_level_answers = ['dance', 'value', 'human', 'choreography', 'place']


# Question for second_level
second_level ="""__1__ shopping is a form of electronic commerce which allows __2__ to directly buy goods or services from a seller over the Internet using a web browser. 
Consumers find a product of interest by visiting the __3__ of the retailer directly or by searching among alternative vendors using a shopping search engine,
 which displays the same product's availability.
 As of 2016, customers can __4__ online using a __5__ of different computers and devices, including desktop computers, laptops, tablet computers and smartphones."""
# Answer for second_level 
second_level_answers = ['online', 'consumers', 'website', 'shop', 'range']



# Question string for third_level 
third_level ="""A 100 gram serving of milk __1__ supplies 540 __2__.
 It is 59% carbohydrates , 30% fat and 8% protein .Approximately 65% of the __3__ in milk chocolate is saturated,
  composed mainly of palmitic __4__ and stearic acid, while the predominant unsaturated fat is __5__ acid."""
# Answer for third_level 
third_level_answers = ['chocolate', 'calories', 'fat', 'acid', 'oleic']



def levels():
    '''
The function has no input .This function asks the user for hardness of the level and then returns the level asked by user.
'''

    level = raw_input('''Enter easy for first_level medium for second_level hard for third_level \n''')
    if level == 'easy':
        print str(first_level)
        game_play(first_level, first_level_answers)
    elif level == 'medium':
        print str(second_level)
        game_play(second_level, second_level_answers)
    elif level == 'hard':
        print str(third_level)
        game_play(third_level, third_level_answers)
    else:
        print 'You entered a wrong choice\n'
        levels()



def game_play(level_ques,level_ans):
    count=0
    number=4
    question = level_ques
    while count<len(level_ans):
        level_ques = question
        answer = raw_input('What is the answer for blank __'
                           + str(count + 1) + '__ ?\n')
        if correct_ans(count,level_ans,answer):
           question = replacement(level_ques,level_ans,count,answer)
           print question
           count += 1
           
           print("\n Congrats!! It is a  right answer! \n")
        
        else:
           number -= 1 

           #it reduces the number of attempts after a wrong answer
           
           print("\n It is a wrong answer...Try again, " + str(number) +" attempts remaining\n")
           if number == 0:
            break
 




def correct_ans(count,level_ans,answer ):
    if answer == level_ans[count]:
        return True
    else:
        return False
    '''
....This function takes the answer entered by the user and the correct answer from the given list
 .... and returns a value which is either true or fase
....'''
def replacement(level_ques,level_ans,count,answer):
    level_ques = level_ques.split()

        # index is used to store the index of the first blank in the question string

    index = level_ques.index('__' + str(count + 1) + '__')
    level_ques[index] = level_ques[index].replace('__' + str(count
            + 1) + '__', answer)
    level_ques = ' '.join(level_ques)
    #it returns the level_ques with the corrected answer
    return level_ques





levels()    
