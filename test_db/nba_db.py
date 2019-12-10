import requests
import bs4
from bs4 import BeautifulSoup
from mysql.connector import connect

def get_league_htmls():
    url1 = "https://en.wikipedia.org/wiki/National_Basketball_Association"
    url2 = "https://en.wikipedia.org/wiki/NBA_G_League"
    responseList = []
    response1 = requests.get(url1)
    response2 = requests.get(url2)
    responseList.append(response1.text)
    responseList.append(response2.text)
    return responseList

def get_stadium_htmls():
    url1 = "https://en.wikipedia.org/wiki/Chase_Center"
    url2 = "https://en.wikipedia.org/wiki/Toyota_Center"
    url3 = "https://en.wikipedia.org/wiki/Wells_Fargo_Center_(Philadelphia)"
    url4 = "https://en.wikipedia.org/wiki/Scotiabank_Arena"
    url5 = "https://en.wikipedia.org/wiki/Fiserv_Forum"
    url6 = "https://en.wikipedia.org/wiki/American_Airlines_Center"
    url7 = "https://en.wikipedia.org/wiki/Chesapeake_Energy_Arena"
    url8 = "https://en.wikipedia.org/wiki/Vivint_Smart_Home_Arena"
    url9 = "https://en.wikipedia.org/wiki/Barclays_Center"
    url10 = "https://en.wikipedia.org/wiki/Talking_Stick_Resort_Arena"
    url11 = "https://en.wikipedia.org/wiki/Paramount_Fine_Foods_Centre"
    responseList = []
    response1 = requests.get(url1)
    response2 = requests.get(url2)
    response3 = requests.get(url3)
    response4 = requests.get(url4)
    response5 = requests.get(url5)
    response6 = requests.get(url6)
    response7 = requests.get(url7)
    response8 = requests.get(url8)
    response9 = requests.get(url9)
    response10 = requests.get(url10)
    response11 = requests.get(url11)
    responseList.append(response1.text)
    responseList.append(response2.text)
    responseList.append(response3.text)
    responseList.append(response4.text)
    responseList.append(response5.text)
    responseList.append(response6.text)
    responseList.append(response7.text)
    responseList.append(response8.text)
    responseList.append(response9.text)
    responseList.append(response10.text)
    responseList.append(response11.text)
    return responseList

def get_html():
    url1 = "https://www.basketball-reference.com/teams/"
    url2 = "https://www.basketball-reference.com/gleague/teams/"
    responseList = []
    response1 = requests.get(url1)
    response2 = requests.get(url2)
    responseList.append(response1.text)
    responseList.append(response2.text)
    return responseList

def get_team(htmls):
    cnt = 0
    relevant_teams = list()
    for html in htmls:
        soup = BeautifulSoup(html, 'html.parser')
        all_teams = soup
        if cnt == 0:
            all_teams = soup.find(id = "teams_active").find("tbody").findAll("tr", class_= "full_table")
        else:
            all_teams = soup.find(id = "active").find("tbody").findAll("tr", class_= "full_table")
        for team in all_teams:
            team_name = team.a.getText()
            if cnt == 0 and (team_name == "Golden State Warriors" or team_name == "Houston Rockets" or team_name == "Philadelphia 76ers" or
                team_name == "Toronto Raptors" or team_name == "Milwaukee Bucks" or team_name == "Dallas Mavericks"
               or team_name == "Oklahoma City Thunder" or team_name == "Utah Jazz" or team_name == "Brooklyn Nets"
                or team_name == "Phoenix Suns"):
                relevant_teams.append(team)
            elif (team_name == "Raptors 905" or team_name == "Austin Spurs" or team_name == "Rio Grande Valley Vipers"):
                relevant_teams.append(team)
        cnt += 1
    """
    Richardson, Leonard. .Beautiful Soup Documentation.. Beautiful Soup Documentation -
    Beautiful Soup 4.4.0 Documentation, Crummy, 2015, www.crummy.com/software/BeautifulSoup/bs4/doc/.
    Explanation of Source: I did not know how to use Beautiful Soup to get a particular html/xml element like <a>
    this told me how to do this. Additionally, this source informed me of how to use a Beautiful Soup findAll
    call with two parameters.
    """

    """We only want a small number of teams for our database for simplification purposes so we will only
    include teams who have won the NBA championship in the last two season or teams who have
    had a player win MVP or Rookie of the Year in the last two seasons"""
    return relevant_teams

def main():
    cnx = connect(user='root', password='Thename55!@#')
    cursor = cnx.cursor()
    cursor.execute("DROP DATABASE IF EXISTS NBAInfo")
    cursor.execute("CREATE DATABASE NBAInfo DEFAULT CHARACTER SET 'utf8'")
    cursor.execute("USE NBAInfo")

    TABLE1 = """CREATE TABLE Locations (
        locationID VARCHAR(10) NOT NULL,
        streetAddress VARCHAR(60),
        city VARCHAR(25),
        state VARCHAR(25),
        PRIMARY KEY (locationID)
    );"""
    cursor.execute(TABLE1)

    TABLE2 = """CREATE TABLE Stadiums (
        stadiumID VARCHAR(10),
        stadiumName VARCHAR(35),
        capacity VARCHAR(10),
        locationID VARCHAR(10),
        PRIMARY KEY(stadiumID),
        FOREIGN KEY f1(locationID) REFERENCES Locations(locationID)
        ON DELETE RESTRICT ON UPDATE CASCADE
    );"""
    cursor.execute(TABLE2)

    TABLE3 = """CREATE TABLE Leagues (
        leagueID VARCHAR(10) NOT NULL,
        leagueName VARCHAR(40),
        leaguePresident VARCHAR(30),
        PRIMARY KEY (leagueID)
    );"""
    cursor.execute(TABLE3)

    TABLE4 = """CREATE TABLE Teams (
        teamID VARCHAR(10) NOT NULL,
        teamName VARCHAR(35) NOT NULL,
        yearsInLeague INT(2),
        playoffs INT(2),
        stadiumID VARCHAR(10),
        leagueID VARCHAR(10),
        PRIMARY KEY (teamID),
        FOREIGN KEY f1(stadiumID) REFERENCES Stadiums(stadiumID)
        ON DELETE RESTRICT ON UPDATE CASCADE,
        FOREIGN KEY f2 (leagueID) REFERENCES Leagues(leagueID)
        ON DELETE RESTRICT ON UPDATE CASCADE
    );"""
    cursor.execute(TABLE4)

    _ROW1 ="""INSERT INTO Locations (
        locationID,
        streetAddress,
        city,
        state
    ) VALUES (
        %(locationID)s,
        %(streetAddress)s,
        %(city)s,
        %(state)s
    );"""

    _ROW2 ="""INSERT INTO Stadiums (
        stadiumID,
        stadiumName,
        capacity,
        locationID
    ) VALUES (
        %(stadiumID)s,
        %(stadiumName)s,
        %(capacity)s,
        %(locationID)s
    );"""

    _ROW3 ="""INSERT INTO Leagues (
        leagueID,
        leagueName,
        leaguePresident
    ) VALUES (
        %(leagueID)s,
        %(leagueName)s,
        %(leaguePresident)s
    );"""

    _ROW4 = """INSERT INTO Teams (
        teamID,
        teamName,
        yearsInLeague,
        playoffs,
        stadiumID,
        leagueID
    ) VALUES (
        %(teamID)s,
        %(teamName)s,
        %(yearsInLeague)s,
        %(playoffs)s,
        %(stadiumID)s,
        %(leagueID)s
    );"""
    
    leagueHTMLS = get_league_htmls()
    leagueNum = 1
    for league in leagueHTMLS:
        leagueDict = {}
        soup = BeautifulSoup(league, 'html.parser')
        leagueDict["leagueID"] = "NBALeague" + str(leagueNum)
        leagueDict["leagueName"] = soup.body.h1.getText()
        pres1 = soup.body.find(class_ = "infobox").find("a", {"title": "Adam Silver"})
        pres2 = soup.body.find(class_ = "infobox").find("a", {"title": "Shareef Abdur-Rahim"})
        if (pres1 == None):
            leagueDict["leaguePresident"] = pres2.getText()
        else:
            leagueDict["leaguePresident"] = pres1.getText()
        leagueNum += 1
        cursor.execute(_ROW3, leagueDict)
        
    """
    Beautiful Soup Find First Whose Title Attribute Equal a Certain String. Stack Overflow, Stack Overflow, 1 Sept,
    stackoverflow.com/questions/45307817/beautiful-soup-find-first-a-whose-title-attribute-equal-a-certain-string.
    Explanation of source;
    I wanted to know how to get the title portion of an html page in order to get the names of league presidents
    for my database. Using the information provided by this source, I wrote the above line adding the league presidents
    to the database.
    """
    
    stadiumHTMLS = get_stadium_htmls()
    cnt = 0
    for stadium in stadiumHTMLS:
        locationDict = {}
        stadiumDict = {}
        soup = BeautifulSoup(stadium, 'html.parser')
        if (cnt < 10):
            locationDict["locationID"] = "STADLOC" + "00" + str(cnt)
            stadiumDict["locationID"] = "STADLOC" + "00" + str(cnt)
        else:
            locationDict["locationID"] = "STADLOC" + "0" + str(cnt)
            stadiumDict["locationID"] = "STADLOC" + "0" + str(cnt)
        cnt += 1
        locInfo = soup.body.find(class_ = "infobox").findAll("td", {"class": "label"})
        """
        Getting the Nth Element Using BeautifulSoup.. Stack Overflow, 1 Feb,
        stackoverflow.com/questions/8724352/getting-the-nth-element-using-beautifulsoup.
        Explanation of Source:
        This source told me I could parse through pieces of beautiful soup findAll commands
        the same way I would a list. I used this to parse html data to get a stadium's capacity.
        """
        cityInfo = locInfo[1].getText().split(", ")
        locationDict["city"] = cityInfo[0]
        locationDict["state"] = cityInfo[1]
        locationDict["streetAddress"] = locInfo[0].getText()
        cursor.execute(_ROW1, locationDict)
        if (soup.body.find(class_ = "infobox").find("a", {"title":"National Basketball Association"}) != None):
            stadiumDict["stadiumID"] = "NBASTAD" + soup.body.find(class_ = "infobox").find("a", {"title":"National Basketball Association"}).previous_element.previous_element[0:3]
            if stadiumDict["stadiumID"] == "NBASTADNew":
                stadiumDict["stadiumID"] = "NBASTADOkl"
        else:
            stadiumDict["stadiumID"] = "NBASTAD" + soup.body.find(class_ = "infobox").find("a", {"title":"NBA G League"}).previous_element.previous_element[0:3]
        """
        Beautiful Soup- How Can We Get Elements before the  Element?. Stack Overflow, 1 Nov,
        stackoverflow.com/questions/52320843/beautiful-soup-how-can-we-get-elements-before-the-head-element.
        Explanation of Source:
        This source told me how to access the previus text element for a beautiful soup query.
        This allowed me to get the team names tha came before certain league identifiers
        """
        stadiumDict["stadiumName"] = soup.body.h1.getText()
        checknext = False
        capCnt = 0
        for option in soup.body.find(class_ = "infobox").findAll("td"):
            if(option.getText()[0:10] == "Basketball"):
                capList = option.getText().split(" ")[1][0:6].strip("H").split(",")
                stadiumDict["capacity"] = int(capList[0] + capList[1])
            elif (10 > len(option.getText()) > 2 and option.getText()[2] == ","):
                capList = option.getText().split("[")[0].split(",")
                stadiumDict["capacity"] = int(capList[0] + capList[1])
        cursor.execute(_ROW2, stadiumDict)



    team_htmls = get_html()
    league = get_team(team_htmls)
    tmCount = 0
    for team in league:
        teamDict = {}
        if tmCount < 10:
            teamDict["teamID"] = "NBA" + team.a.get('href')[7:10] + "000" + str(tmCount)
        else:
            teamDict["teamID"] = "NBA" + team.a.get('href')[15:18] + "00" + str(tmCount)
        if (team.a.getText() == "Austin Spurs" or team.a.getText() == "Rio Grande Valley Vipers"):
            teamDict["stadiumID"] = None
        else:
            teamDict["stadiumID"] = "NBASTAD" + team.a.getText()[0:3]
        teamDict["teamName"] = team.a.getText()
        """
        .r/Learnpython - Having Issues Finding Data-Tense with beautifulsoup4.. Reddit, 2018,
        www.reddit.com/r/learnpython/comments/87v813/having_issues_finding_datatense_with/.
        Explanation of Source: I got an error when I called team.find(data-stat=years). This
        site provided me with a way to call for this information without getting an error.
        """
        teamDict["yearsInLeague"] = team.find("td", {"data-stat":"years"}).getText()
        teamDict["playoffs"] = team.find("td", {"data-stat":"years_playoffs"}).getText()
        if (team.a.getText() == "Raptors 905" or team.a.getText() == "Austin Spurs" or team.a.getText() == "Rio Grande Valley Vipers"):
            teamDict["leagueID"] = "NBALeague2"
        else:
            teamDict["leagueID"] = "NBALeague1"
        cursor.execute(_ROW4, teamDict)
        tmCount += 1

    cnx.commit()

    cnx.close()

if __name__ == '__main__':
    main()

