import urllib2
from bs4 import BeautifulSoup
import re
from datetime import datetime
#record = record_box.text.strip()

# specify the url
pens_page = 'https://www.hockey-reference.com/teams/PIT/2018_games.html'
page = urllib2.urlopen(pens_page)
soup = BeautifulSoup(page, 'html.parser')

def findNextGame():
    #Get tbody tags to find date of games
    bodyTags = soup.find('tbody')
    dateTag = bodyTags.findAll('td', attrs={'data-stat': 'date_game'})
    oppTag = bodyTags.findAll('td', attrs={'data-stat': 'opp_name'})
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
            print "Next game: ", str(printGameDate), "vs", str(oppTag[idx].text)
            break

findNextGame()
