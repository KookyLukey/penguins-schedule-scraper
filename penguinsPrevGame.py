import urllib2
from bs4 import BeautifulSoup
import re
from datetime import datetime

# specify the url
pens_page = 'https://www.hockey-reference.com/teams/PIT/2018_games.html'
page = urllib2.urlopen(pens_page)
soup = BeautifulSoup(page, 'html.parser')

def findPrevGame():
    #Get tbody tags to find previous game scores and outcome
    bodyTags = soup.find('tbody')
    dateTag = bodyTags.findAll('td', attrs={'data-stat': 'date_game'})
    outcomeTag = bodyTags.findAll('td', attrs={'data-stat': 'game_outcome'})
    goalsForTag = bodyTags.findAll('td', attrs={'data-stat': 'goals'})
    goalsAgainstTag = bodyTags.findAll('td', attrs={'data-stat': 'opp_goals'})

    for idx, tag in enumerate(dateTag):
        tempGameDate = datetime.strptime(tag.text, '%Y-%m-%d')
        today = datetime.today()

        if tempGameDate < today:
            pass
        else:
            printGameDate = tempGameDate.strftime('%m/%d/%Y')
            print "Previous game: ", outcomeTag[idx-1].text, goalsForTag[idx-1].text, "-", goalsAgainstTag[idx-1].text
            break

findPrevGame()
