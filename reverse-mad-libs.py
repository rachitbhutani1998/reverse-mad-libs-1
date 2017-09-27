# Question for first_level 
first_level = """__1__ is a performing art form consisting of purposefully selected sequences of __2__ movement.
 This movement has aesthetic and symbolic __3__, and is acknowledged as dance by performers and observers within a particular culture.
  Dance can be categorized and described by its __4__,
 by its repertoire of movements, or by its historical period or __5__ of origin."""



 def first_level_1(blank):
    print """dance is a performing art form consisting of purposefully selected sequences of __2__ movement.
 This movement has aesthetic and symbolic __3__, and is acknowledged as dance by performers and observers within a particular culture.
  Dance can be categorized and described by its __4__,
 by its repertoire of movements, or by its historical period or __5__ of origin."""
 def first_level_2(blank):
    print """dance is a performing art form consisting of purposefully selected sequences of value movement.
 This movement has aesthetic and symbolic __3__, and is acknowledged as dance by performers and observers within a particular culture.
  Dance can be categorized and described by its __4__,
 by its repertoire of movements, or by its historical period or __5__ of origin."""
 def first_level_3(blank):
    print """dance is a performing art form consisting of purposefully selected sequences of value movement.
 This movement has aesthetic and symbolic human, and is acknowledged as dance by performers and observers within a particular culture.
  Dance can be categorized and described by its __4__,
 by its repertoire of movements, or by its historical period or __5__ of origin."""
 def first_level_4(blank):
    print """dance is a performing art form consisting of purposefully selected sequences of value movement.
 This movement has aesthetic and symbolic human, and is acknowledged as dance by performers and observers within a particular culture.
  Dance can be categorized and described by its choreography,
 by its repertoire of movements, or by its historical period or __5__ of origin."""
 def first_level_5(blank):
    print """dance is a performing art form consisting of purposefully selected sequences of value movement.
 This movement has aesthetic and symbolic human, and is acknowledged as dance by performers and observers within a particular culture.
  Dance can be categorized and described by its choreography,
 by its repertoire of movements, or by its historical period or place of origin."""
    

# Answer for first_level
first_level_answers = ['dance', 'value', 'human', 'choreography', 'place']


# Question for second_level
second_level ="""__1__ shopping is a form of electronic commerce which allows __2__ to directly buy goods or services from a seller over the Internet using a web browser. 
Consumers find a product of interest by visiting the __3__ of the retailer directly or by searching among alternative vendors using a shopping search engine,
 which displays the same product's availability.
 As of 2016, customers can __4__ online using a __5__ of different computers and devices, including desktop computers, laptops, tablet computers and smartphones."""




def second_level_1(blank)
   print  """online shopping is a form of electronic commerce which allows __2__ to directly buy goods or services from a seller over the Internet using a web browser. 
Consumers find a product of interest by visiting the __3__ of the retailer directly or by searching among alternative vendors using a shopping search engine,
 which displays the same product's availability.
 As of 2016, customers can __4__ online using a __5__ of different computers and devices, including desktop computers, laptops, tablet computers and smartphones."""
def second_level_2(blank)
   print  """online shopping is a form of electronic commerce which allows consumers to directly buy goods or services from a seller over the Internet using a web browser. 
Consumers find a product of interest by visiting the __3__ of the retailer directly or by searching among alternative vendors using a shopping search engine, 
which displays the same product's availability.
 As of 2016, customers can __4__ online using a __5__ of different computers and devices, including desktop computers, laptops, tablet computers and smartphones."""
def second_level_3(blank)
   print  """online shopping is a form of electronic commerce which allows value to directly buy goods or services from a seller over the Internet using a web browser. 
Consumers find a product of interest by visiting the website of the retailer directly or by searching among alternative vendors using a shopping search engine, 
which displays the same product's availability.
 As of 2016, customers can __4__ online using a __5__ of different computers and devices, including desktop computers, laptops, tablet computers and smartphones."""
def second_level_4(blank)
   print  """online shopping is a form of electronic commerce which allows value to directly buy goods or services from a seller over the Internet using a web browser. 
Consumers find a product of interest by visiting the website of the retailer directly or by searching among alternative vendors using a shopping search engine, 
which displays the same product's availability.
 As of 2016, customers can shop online using a __5__ of different computers and devices, including desktop computers, laptops, tablet computers and smartphones."""
def second_level_5(blank)
   print  """online shopping is a form of electronic commerce which allows value to directly buy goods or services from a seller over the Internet using a web browser. 
Consumers find a product of interest by visiting the website of the retailer directly or by searching among alternative vendors using a shopping search engine, 
which displays the same product's availability.
 As of 2016, customers can shop online using a range of different computers and devices, including desktop computers, laptops, tablet computers and smartphones."""

# Answer for second_level 
second_level_answers = ['online', 'consumers', 'website', 'shop', 'range']



# Question string for third_level 
level_3 ="""A 100 gram serving of milk __1__ supplies 540 __2__.
 It is 59% carbohydrates , 30% fat and 8% protein .Approximately 65% of the __3__ in milk chocolate is saturated,
  composed mainly of palmitic __4__ and stearic acid, while the predominant unsaturated fat is __5__ acid."""



def third_level_1(blank)
    print="""A 100 gram serving of milk chocolate supplies 540 __2__.
 It is 59% carbohydrates , 30% fat and 8% protein .Approximately 65% of the __3__ in milk chocolate is saturated,
  composed mainly of palmitic __4__ and stearic acid, while the predominant unsaturated fat is __5__ acid."""
  def third_level_2(blank)
    print="""A 100 gram serving of milk chocolate supplies 540 calories.
 It is 59% carbohydrates , 30% fat and 8% protein .Approximately 65% of the __3__ in milk chocolate is saturated,
  composed mainly of palmitic __4__ and stearic acid, while the predominant unsaturated fat is __5__ acid."""
def third_level_3(blank)
    print="""A 100 gram serving of milk chocolate supplies 540 calories.
 It is 59% carbohydrates , 30% fat and 8% protein .Approximately 65% of the fat in milk chocolate is saturated,
  composed mainly of palmitic __4__ and stearic acid, while the predominant unsaturated fat is __5__ acid."""
def third_level_4(blank)
    print="""A 100 gram serving of milk chocolate supplies 540 calories.
 It is 59% carbohydrates , 30% fat and 8% protein .Approximately 65% of the fat in milk chocolate is saturated,
  composed mainly of palmitic acid and stearic acid, while the predominant unsaturated fat is __5__ acid."""
def third_level_5(blank)
    print="""A 100 gram serving of milk chocolate supplies 540 calories.
 It is 59% carbohydrates , 30% fat and 8% protein .Approximately 65% of the fat in milk chocolate is saturated,
  composed mainly of palmitic acid and stearic acid, while the predominant unsaturated fat is oleic acid."""

# Answer for third_level 
third_level_answers = ['chocolate', 'calories', 'fat', 'acid', 'oleic']





def levels():
    '''
The function has no input .This function asks the user for hardness of the level and then returns the level asked by user.
'''

    level = raw_input('''Enter easy for first_level medium for second_level hard for third_level''')
    if level == 'easy':
        print first_level
        start_game(first_level, first_level_answers)
    else:
        if level == 'medium':
         print _second_level
        start_game(second_level, second_level_answers)
    else:
      if level == 'hard':
        print str(third_level)
        start_game(third_level, third_level_answers)
    else:
        print 'You entered a wrong choice\n'
        levels()



def game_play(questions, answers):
    '''This function takes two input parameters,one for the questions and other for the answers'''


levels()







