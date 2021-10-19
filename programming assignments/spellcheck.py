# Alisha Agrawal (aa3se)
"""
examines user-entered text for misspelled words
"""
import urllib.request

url = 'http://cs1110.cs.virginia.edu/files/words.txt'
file = urllib.request.urlopen(url)
file_read = file.readlines()
w_list = []  # stores list of words from url
u_list = []  # stores list of words from user
isitblank = False  # true if user enters blank space

for line in file_read:  # stores every line in file into a w_list
    file = line.decode('utf-8').strip(".?!,()'\"").split()
    w_list.append(file[0].lower())

print("Type text; enter a blank line to end.")

while not isitblank:
    inp = input('')
    if inp == '':  # exit out of while loop
        isitblank = True
    else:
        u_list = inp.split()  # stores every word by blank space into u_list
        for word in u_list:
            word = word.strip(".?!,()\"'")  # strips off leading/trailing punctuation
            if word.lower() not in w_list:  # checks if word is in list of words from file
                print("  MISSPELLED:", word)
