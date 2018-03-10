#! /usr/bin/python3

import json
import string
import random
import re
from urllib.request import urlopen




                #Global declarations
dictionary = open("dictionary.txt","r")
guessedLetters = []




                #Starting the game by calling API
def startGame():

    global guessedLetters
    guessedLetters = []
 # specify URL to connect to JSON API  url = 
    jsonObj = urlopen(url).read()
    data = json.loads(jsonObj.decode('utf-8'))
    token = data['token']
    while (data['status'] != "DEAD"):
        print("You have "+str(data['remaining_guesses'])+" chances left")

                #Choose letter to guess
        char = chooseNew(data['state'])
        guessedLetters.append(char)                #Stores the guessed character to prevent repeating guesses
        data = makeGuess(token,char)
        print("Character to be guessed is "+char)
        print(data['state'])
        
                #Prisoner is Freed and next round is started
        if (data['status'] == "FREE"):
            print("FREE")
            startGame()
            
                #Prisoner is Dead and next round is started      
    print("DEAD")
    startGame()           
        
            



                #Makes a guess with character stored in a
def makeGuess(code,alpha):
   # specify URL to connect to JSON API url = 
    jsonObj =  urlopen(url).read()
    newData = json.loads(jsonObj.decode('utf-8'))
    return newData
    

                #decide on which character to guess next
def chooseNew(state):
    words = state.split()           #Retrieving individual words from state
    hashMap={}



    for word in words:
        tempVar = word
        if word.find("_") != -1:
            word = word.replace("_", "[a-z]")           #Building regular expression for each word
            word+="$"
            word = "^" + word
            for newLine in dictionary:                     
                if len(newLine) == len(tempVar)+1:         
                    match=re.search(word, newLine, re.IGNORECASE)     #If length of RE matches with length of dictionary entry, searches for match.
                    if match is not None:
                        i=0
                        for c in tempVar:
                            if tempVar[i] == '_':
                                newChar = match.group(0)[i].lower()      #Retrieves 'i'th character from the match
                                if newChar in hashMap:
                                    hashMap[newChar] = hashMap[newChar]+1           #Creates a Hash map of the characters and their frequency from each match.
                                else:
                                    hashMap[newChar] = 1
                            i+=1
            dictionary.seek(0)              #Resets Dictionary for next word 

    maxChar = str(max(hashMap, key=hashMap.get))         #Retrieves most frequent character from Hash map
    while maxChar.lower() in guessedLetters:
        del hashMap[maxChar]                                 #If chosen character has already been used, use next.
        maxChar = str(max(hashMap, key=hashMap.get))
    guess = maxChar
    return guess
    
		
    



startGame()
    
