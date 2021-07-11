# # find all sentence that have '.' '!' '?'
#
# letter = 0
# word = 0
# sentence = 0
#
# # formula
#
# L = (letter / word) * 100  # average the number of letter per 100 words
# S = (sentence / word) * 100  # average number of sentence per 100 words
# grade = round(0.0588 * L - 0.296 * S - 15.8) # for finding what grade can read in the pasted text

""" Example Sentence

    One flower. Two flower. Red flower. = (Before Grade 1)

    One flower. Two flower. Red flower. yellow flower =  (Grade 2)

    There are more things in Heaven and Earth, Horatio, than are dreamt of in your philosophy. = (Grade 9)

    There are more things in Heaven and Earth, Horatio than are dreamt of in your philosophy = (Grade 11)

    Will allow duplicate registration id’s for different users, so you are responsible for. = (Grade 14)

    Will allow duplicate registration_id’s for different users, so you are responsible for = (Grade 16+)

"""


def coleman_liau_index():
    text = str(input("Insert text here: "))

    letter = 0

    word = 0

    sentence = 0

    for words in text:

        if words.isalpha():

            letter += 1

        elif words == " ":

            word += 1

        elif words in [".", "!", "?"]:

            sentence += 1

    L = (letter / word) * 100

    S = (sentence / word) * 100

    grade = round(0.0588 * L - 0.296 * S - 15.8)

    if grade >= 16:

        print("grade 16+")

    elif grade < 1:

        print("grade 1")


    else:
        print(f"grade {grade}")


coleman_liau_index()
