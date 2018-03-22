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

    for tag in dateTag:
        #Match against date in row
        match = re.search('csk="\d{4}-\d{2}-\d{2}', str(tag))

        #trim excess info off date
        gameDate = match.group(0)
        gameDate = gameDate[5:]
        tempGameDate = datetime.strptime(gameDate, '%Y-%m-%d')
        today = datetime.today()

        if tempGameDate < today:
            print "game has already been played"
        else:
            print "Next game is: ", str(tempGameDate)
            break

findNextGame()


#modTag = nextGame_box.find('div', attrs={"class": "mod-container mod-no-footer mod-game current"})

#dateTime = modTag.find('h4')
#dateTime = str(dateTime)
#match = re.search('\w{3}, \w{3} \d{1,2}', dateTime)

#print nextGame_box
#print record_box[0].text.strip()
#print record_box[1].text.strip()
#print nextGame_box
