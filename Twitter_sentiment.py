from nltk.corpus import stopwords
from itertools import chain
from nltk.corpus import wordnet
from collections import defaultdict
import pip
import csv

#combined_dataset_verbose has all the news article.
f = open('combined_dataset_verbose.csv')
csv_f = csv.reader(f)
next(csv_f)

#data.txt has all POMS word.
fp=open("data.txt")
red=fp.read()
lis=[]
lis.append(red)
x=lis[0]
x=x.split("\n")

#final wordlist dictionary with each key having list of synonyms.
wordlist={}

#Loop through all words in x and get synonyms
for i in x:
    synonyms = wordnet.synsets(i)
    lemmas = set(chain.from_iterable([word.lemma_names() for word in synonyms]))
    lists = [x.encode('UTF8') for x in lemmas]
    lists.append(i)
    wordlist[i]=lists

#get set of all stop words
stop = set(stopwords.words('english'))

#Creating output csv file with header publish_date,Date,Tension,Depression,Anger,Fatigue,Confusion,Vigour,Class
fieldnames = ['publish_date','Date','Tension','Depression','Anger','Fatigue','Confusion','Vigour','Class']
fp=open('final.csv', 'w')
writer = csv.DictWriter(fp, fieldnames=fieldnames)
writer.writeheader()

#loop through all article and get sentiment score.
for row in csv_f:
    count={}
    total=0
    broken=[i for i in row[4].lower().split() if i not in stop]

    #get count for each word
    for key in wordlist.iterkeys():
        count[key]=len(set(wordlist[key])&set(broken))+1
        total+=count[key]

    #Calculating the probability
    for key in wordlist.iterkeys():
        count[key]=1.0*count[key]/total

    score={}
    if row[5] > row[8]:
        label = 0
    else:
        label = 1

    #Calculating the score
    score["Tension"]=count["Tense"]+count["Shaky"]+count["On Edge"]+count["Panicky"]+count["Relaxed"]+count["Uneasy"]+ \
                     count["Restless"] + count["Nervous"] + count["Anxious"]
    score["Depression"]=count["Unhappy"]+count["Sorry for things done"]+count["Sad"]+count["Blue"]+count["Hopeless"]+count["Unworthy"]+ \
                     count["Discouraged"] + count["Lonely"] + count["Miserable"]+ count["Gloomy"] + count["Desperate"] + count["Helpless"]+ \
                        count["Worthless"] + count["Terrified"] + count["Guilty"]
    score["Anger"]=count["Angry"]+count["Peeved"]+count["Grouchy"]+count["Spiteful"]+count["Annoyed"]+count["Resentful"]+ \
                     count["Bitter"] + count["Ready to Fight"] + count["Rebellious"]+count["Deceived"] + count["Furious"] + count["Bad Tempered"]

    score["Fatigue"] = count["Worn Out"] + count["Listless"] + count["Fatigued"] + count["Exhausted"] + count["Sluggish"] + count["Weary"] + \
                       count["Bushed"]

    score["Confusion"]=count["Confused"]+count["Unable to Concentrate"]+count["Muddled"]+count["Bewildered"]+count["Efficient"]+count["Forgetful"]+ \
                     count["Uncertain about things"]
    score["Vigour"] = count["Lively"] + count["Active"] + count["Energetic"] + count["Cheerful"] + \
                         count["Alert"] + count["Full of Pep"] + \
                         count["Carefree"]+count["Vigorous"]
    final={}

    '''final["Happy"]=
    final["Alert"]=
    final["Kind"]=
    final["Calm"]=
    '''

    #writting sentiment score to output file.
    writer.writerow( {'publish_date': row[1], 'Date': row[2], 'Tension': score["Tension"], 'Depression': score["Depression"],\
         'Anger': score["Anger"], 'Fatigue': score["Fatigue"], 'Confusion': score["Confusion"], 'Vigour': score["Vigour"], 'Class': label})











