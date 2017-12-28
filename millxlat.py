#! python3
# - save text in your clipboard and run this program. It will send the translated result back into the clipboard.

import re, pyperclip

import nltk
# Because nltk data was downloaded in the D drive.
nltk.data.path.append('/media/dhanush/DATA/PyCharm_Projects_Ddrive/nltk_data')
from nltk.corpus import state_union # State of the union addresses by various US presidents
from nltk.tokenize import PunktSentenceTokenizer
from nltk.corpus import wordnet 
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

my_phrases = [['boyfriend', 'bae'],
     ['totally', 'totes'],
     ['friends', 'woes'],
     ['proof', 'receipts'],
     ['no patience', 'zero chill'],
     ['greatest', 'GOAT'],
     ['talk trash', 'throw shade'],
     ['cute', 'smol'],
     ['knows', 'keeps it 100'],
     ['drunk', 'turnt'],
     [' very ', ' V '],
     ['watch', 'binge watch'],
     ['watched', 'binged'],
     ['group', 'squad'],
     [' avoid ', ' curve '],
     ['support', 'ship'],
     ['don''t care', 'DGAF'],
     ['were good', 'were lit AF'],
     ['was good', 'was lit AF'],
     ['dumb', 'dumb AF'],
     ['do well', 'slay'],
     ['real ', 'real AF '],
     ['unfair.', 'unfair. Literally can''t even.'],
     ['annoying.', 'annoying. I can''t even.'],
     ['disapprove', 'disapprove, SMH'],
     ['injustice', 'injustice, SMH'],
     ['excited', 'excited, YASSS'],
     ['thrilled', 'thrilled, YASSS'],
     ['girlfriend', 'bae'],
     ['on point', 'on fleek'],
     ['perfect', 'on fleek'],
     ['problem.', 'problem. The struggle is real.'],
     ['intoxicated', 'turnt'],
     ['crazy', 'cray cray'],
     ['great.', 'great AF.'],
     ['multitask', 'phub'],
     ['multitasking', 'phubbing'],
     ['hundred percent', 'hundo P. '],
     ['emotional', 'emosh'],
     ['impossible', 'imposh'],
     ['on a date', 'to Netflix and Chill']]

# INPUT TEXT  
text = """
I cant believe that your cute boyfriend is totally in love with her every time.
My friends and I even have proof that he was drunk! I hear they are going on a date. Of course he is cute but has no patience.
I dont mean to talk trash and everything but this event will be the greatest! Its very sad.
I seriously dissaprove. But im so excited! And I think its very unfair. And I dont care about it.
I think we should watch sex in the city tonight, its great. Dont get all emotional on me.
"""
text = text.replace('\n'," ")  # get rid of newlines

# get text from clipboard
#text=pyperclip.paste()

print("\nOriginal input:\n")
print(text)
print('\n')

#display all phrases im going to look for
#for i in range(len(a)):
#    print (my_phrases[i][0])

print("\nProcessing...\n")

tokens = nltk.word_tokenize(text)
#print(tokens)

tagged = nltk.pos_tag(tokens)
#print(tagged)

#build the patterns list
candidates = ""
for i in range(len(my_phrases)-1):
   candidates = candidates + str(my_phrases[i][0])+"|"
   
candidates = candidates + str(my_phrases[i+1][0])
allRegex=re.compile(candidates)
#print(allRegex)


#build indivudual compiles for each phrase in a two dim array 
myRegex = [['foo' for i in range(2)] for j in range(len(my_phrases))]
for i in range(len(my_phrases)):
   myRegex[i]=re.compile(my_phrases[i][0])
   
#print(myRegex[3])
#print(myRegex)

#start search
mo = allRegex.findall(text)

#loop thru each of my_phrases
for i in range(len(my_phrases)):
        mex = myRegex[i]
        #print(mex)
        
        mypat = my_phrases[i][0]
        #print(mypat)
        #print(i)

        if mypat in text:
            myInput=my_phrases[i][1]
            #print(myInput)

            text=mex.sub(myInput.upper(),text,count=0)
            #print(text)
            
    
print(text)

pyperclip.copy(text)
