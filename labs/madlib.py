# Brittany Sandoval-Rivera (bs6sxv)
# Alisha Agrawal (aa3se)
"""
This program is a madlib.
"""


# prints madlib
def madlib(answer1, answer2, answer3, answer4, answer5, answer6, answer7, answer8, answer9):
    print("Once upon a time, there was a person named", answer1, "who lived in a", answer2+". They grew up loving",
          answer3+". But, their love,", answer4, "hated", answer3+".", answer3, "made", answer4, "start", answer5+".\n",
          answer1+': "Why do you hate', answer3+'?"\n', answer4+': "They are', answer6+'."\n', answer1+': "Your a(n)',
          answer7+". You work with", answer8+'. How is it any different?"\n', answer4+': "',
          answer8, "isn't the same as", answer3+". Maybe if you love", answer3,
          """as much as you love me, it wouldn't be such a problem."\n""",
          answer1+': "True. Sorry boo. Sounds like a personal problem', answer3,
          'treats me better than you ever did."\n',
          answer4+': "How can you say that?! You said you would', answer9, 'for me."\n',
          answer1+': "Goodbye,', answer4+'."')


# prompts user for answers
person1 = input("Your name: ")
place1 = input("A place you hate: ")
thing1 = input("Your favorite childhood toy: ")
person2 = input("Your favorite TV show character: ")
verb2 = input("Random exercise (-ing): ")
adj2 = input("Adjective to describe your mom: ")
prof2 = input("Your dream job: ")
thing2 = input("Your fear (a noun): ")
verb3 = input("An action you hate to do: ")


madlib(person1, place1, thing1, person2, verb2, adj2, prof2, thing2, verb3)
