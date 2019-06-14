# Series of Imports
from geograpy import places
import geograpy
import articleDateExtractor
#import datetime
from datetime import datetime
from newspaper import Article
from test_sample import Person_Score,Publisher_Score
# Scrapping the article and loading the article - extract the keywords
url4 = "https://www.bbc.com/news/av/uk-england-manchester-48344930/manchester-city-fans-cheer-on-heroes-after-treble-triumph"

def mention_position(PlaceList):
    list = pc.city_mentions
    sum = 0
    i = 1
    count = 1
    for each in PlaceList:
        temp = i
        for index in range(len(list)):
            if list[index][0] == each:
                count = list[index][1]
                break
        if count>1:
            temp = i*1.1
        sum+= temp
        i=i-0.1
    print "mention_position score is: ", sum
    return sum

def time_score(url):

    d = articleDateExtractor.extractArticlePublishedDate(url)
    currentDT = (datetime.now())
    temp= 0.001
    print d
    print currentDT
    if d.year == currentDT.year:
        if d.month == currentDT.month:
            if d.day == currentDT.day:
                temp = 0.4
            elif abs(d.day - currentDT.day) == 1:
                temp = 0.3
            elif abs(d.day - currentDT.day) == 2:
                temp = 0.2
            elif abs(d.day - currentDT.day) == 3:
                temp = 0.1
            elif abs(d.day - currentDT.day) == 4:
                temp = 0.05
            else:
                temp = 0.01
    print "Time score is: ", temp
    return temp
toi_article = Article(url4, language="en")
toi_article.download()
toi_article.parse()
toi_article.nlp()
#print(toi_article.title)
list = toi_article.keywords
for i in range(len(list)):
    tmep = str(list[i])
    list[i] = tmep.capitalize()

"""
This part is used to extract all the places that are mentioned in the article which belong to any place on any continent around the world
But we print only those that belong to the UK
"""
pc = geograpy.get_place_context(url=url4)
pc.set_countries()
pc.set_regions()
pc.set_cities()

L1 = pc.country_cities.get("United Kingdom")

"""
Extracting Date and fetching score on article provided how old the news is
"""

"""
This part is used to extract all the places that are mentioned in the article which belong to any place on any continent around the world -- but from the keywords spotted in the article 
But we print only those that belong to the UK
"""
pc = places.PlaceContext(list)
pc.set_countries()
pc.set_regions()
pc.set_cities()
L2 = pc.country_cities.get("United Kingdom")
PlaceList = []
for each in L1:
    PlaceList.append(str(each))
for each in L2:
    if each not in PlaceList:
        PlaceList.append(str(each))


"""
Score based on Document calculation based distance
"""
score = mention_position(PlaceList)
score *= Publisher_Score("Watford",PlaceList)
score *= Person_Score("Oval",PlaceList)
score *= time_score(url4)

print "Final Calc score is:- ",score