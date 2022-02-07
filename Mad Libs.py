from tkinter import *
import tkinter as tk


def madLibsRules():
    print("Have you ever played Mad Libs? If not, here's how to play!")
    print("I have a story that's missing some words. It's your job to give me the words to fill in the blanks, however,")
    print("I can't show you the story until we are done.")
    print("I will ask you for a person, place, or thing. Give me a word you think can fit in to the story.")
def madLibsBeg():
    reply = input("Are you ready? ")
    if reply in 'YESYesyes':
        print("Great! Let's get started!")
    elif reply in 'NONono':
        print("Let's go over the rules again, then!")
        madLibsRules()
        madLibsBeg()
    else:
        print("Sorry, say yes or no.")
        madLibsBeg()
def madLibsAsk():
    global wordOne, wordTwo, wordThree, wordFour, wordFive
    wordOne = input("Give me an animal: ")
    wordTwo = input("Awesome!, I love those! Now, give me a name: ")
    wordThree = input("Great name! Now, I need a color: ")
    wordFour = input("That's my favorite color! I need a past tense verb: ")
    wordFive = input("That sounds like fun! Finally, I need a boy's name: ")
def madLibsFinal():
    print("Awesome! I have all the words I need!")
    reply = input("Are you happy with your words and ready to read our story? ")
    if reply in "YESYesyes":
        print("Okay! Here it is:")
    else:
        print("I'm sorry! We can try again!")
        madLibsAsk()
def madLibsStory():
    print(f"""There was a kid named {wordFive}. He wanted nothing more than a {wordOne}.
One year, his parents decided to give him a {wordThree} {wordOne} for his birthday!
He named his pet {wordTwo}, and wanted to bring it to the local {wordOne} park.
He hoped it'd play nice, but it {wordFour} all the others away!""")
## actually calling the functions
def main():
    ask = input("Do you want to play Mad Libs? ")
    if ask in "YESyes":
        print("Awesome! Let's get started!")
        madLibsRules()
        madLibsBeg()
        madLibsAsk()
        madLibsFinal()
        madLibsStory()
    elif ask in "NOno":
        print("That's okay. See you later!")
    else:
        print("Sorry, say yes or no.")
        main()
if __name__ == "__main__":
    main()


## fuck you lol