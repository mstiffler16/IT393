from flask import Flask,render_template, request
import pymysql

app = Flask(__name__)

class Database:
	def __init__(self):
		host = "127.0.0.1"
		user = "root"
		password = "Thename55!@#"
		#db = "ballerLeagues"
		db = "NBAInfo"
		self.con = pymysql.connect(host=host, user=user, password=password, db=db,
		  cursorclass=pymysql.cursors.DictCursor)
		self.cur = self.con.cursor()
	def view_award_winners_by_season(self, yearGroup):
		self.cur.execute("Call viewAwardWinnerBySeason(%s)", yearGroup)
		result = self.cur.fetchall()
		return result
	def view_award_winners_by_season_and_team(self, yearGroup, teamID):
		self.cur.execute("Call viewAwardWinnerBySeasonAndTeam(%s, %s)", (yearGroup, teamID))
		result = self.cur.fetchall()
		return result
	def view_award_winners_by_league(self, leagueID):
                self.cur.execute("Call viewAwardWinnerByLeague(%s)", (leagueID))
                result = self.cur.fetchall()
                return result
	def view_player_stats_by_season(self, yearGroup):
                self.cur.execute("Call viewPlayerStatsBySeason(%s)", (yearGroup))
                result = self.cur.fetchall()
                return result
	def view_player_stats_by_player(self, playerID):
                self.cur.execute("Call viewPlayerStatsByPlayer(%s)", (playerID))
                result = self.cur.fetchall()
                return result
	def view_salary_by_season(self, yearGroup):
                self.cur.execute("Call viewSalaryBySeason(%s)", (yearGroup))
                result = self.cur.fetchall()
                return result
	def view_salary_by_person(self, playerID):
                self.cur.execute("Call viewSalaryByPerson(%s)", (playerID))
                result = self.cur.fetchall()
                return result
	def view_league_champion_by_season(self, yearGroup):
                self.cur.execute("Call viewLeagueChampionBySeason(%s)", (yearGroup))
                result = self.cur.fetchall()
                return result
	def view_stadium_by_team(self, teamID):
                self.cur.execute("Call viewStadiumByTeam(%s)", (teamID))
                result = self.cur.fetchall()
                return result
	def view_event_winner_by_season(self, eventWinner):
                self.cur.execute("Call viewEventWinnerBySeason(%s)", (eventWinner))
                result = self.cur.fetchall()
                return result
	def view_event_winner_by_season_and_team(self, eventWinner):
                self.cur.execute("Call viewEventWinnerBySeasonAndTeam(%s)", (eventWinner))
                result = self.cur.fetchall()
                return result
	def view_coaches_by_season_and_team(self, personID):
                self.cur.execute("Call viewCoachesBySeasonandTeam(%s)", (personID))
                result = self.cur.fetchall()
                return result
	def enter_season(self, yearGroup):
                self.cur.execute("Call enterSeason(%s)", (yearGroup))
                self.con.commit()
	def enter_league(self, leagueID, leagueName, leaguePresident):
                self.cur.execute("Call enterLeague(%s, %s, %s)", (leagueID, leagueName, leaguePresident))
                self.con.commit()
	def update_league(self, leagueID, leagueName, leaguePresident):
                self.cur.execute("Call updateLeague(%s, %s, %s)", (leagueID, leagueName, leaguePresident))
                self.con.commit()
	def enter_event(self, eventID, eventName, maxRoundScore):
                self.cur.execute("Call enterEvent(%s, %s, %s)", (eventID, eventName, maxRoundScore))
                self.con.commit()
	def enter_event_winner(self, eventID, yearGroup, personID, winnerScore, winnerRounds):
                self.cur.execute("Call enterEventWinner(%s, %s, %s, %s, %s)", (eventID, yearGroup, personID, winnerScore, winnerRounds))
                self.con.commit()
	def enter_player(self, personID, lastName, firstName, number, position):
                self.cur.execute("Call enterPlayer(%s, %s, %s, %s, %s)", (personID, lastName, firstName, number, position))
                self.con.commit()
	def update_player(self, personID, lastName, firstName, number, position):
                self.cur.execute("Call updatePlayer(%s, %s, %s, %s, %s)", (personID, lastName, firstName, number, position))
                self.con.commit()
	def enter_coach(self, personID, lastName, firstName, winPercentage):
                self.cur.execute("Call enterCoach(%s, %s, %s, %s)", (personID, lastName, firstName, winPercentage))
                self.con.commit()
	def update_coach(self, personID, lastName, firstName, winPercentage):
                self.cur.execute("Call updateCoach(%s, %s, %s, %s)", (personID, lastName, firstName, winPercentage))
                self.con.commit()
	def enter_team(self, teamID, teamName, yearsInLeague, playoffs, stadiumID, locationID):
                self.cur.execute("Call enterTeam(%s, %s, %s, %s, %s, %s)", (teamID, teamName, yearsInLeague, playoffs, stadiumID, locationID))
                self.con.commit()
	def update_team(self, teamID, teamName, yearsInLeague, playoffs, stadiumID, locationID):
                self.cur.execute("Call updateTeam(%s, %s, %s, %s, %s, %s)", (teamID, teamName, yearsInLeague, playoffs, stadiumID, locationID))
                self.con.commit()
	def enter_player_stats(self, personID, yearGroup, pointsPerGame, assistsPerGame, fieldGoalPercentage, threePointersPerGame, threePointerPercentage, freeThrowsPercentage, offensiveReboundsPerGame, defensiveReboundsPerGame, turnoversPerGame, blocksPerGame, stealsPerGame):
                self.cur.execute("Call enterPlayerStatistics(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (personID, yearGroup, pointsPerGame, assistsPerGame, fieldGoalPercentage, threePointersPerGame, threePointerPercentage, freeThrowsPercentage, offensiveReboundsPerGame, defensiveReboundsPerGame, turnoversPerGame, blocksPerGame, stealsPerGame))
                self.con.commit()
	def enter_award_information(self, awardID, awardName, timesGiven):
                self.cur.execute("Call enterAwardInformation(%s, %s, %s)", (awardID, awardName, timesGiven))
                self.con.commit()
	def enter_award_winner(self, awardID, playerID, yearGroup):
                self.cur.execute("Call enterAwardWinner(%s, %s, %s)", (awardID, playerID, yearGroup))
                self.con.commit()
	def enter_stadium(self, stadiumID, stadiumName, capacity, locationID, streetAddress, city, state):
                self.cur.execute("Call enterStadiums(%s, %s, %s, %s, %s, %s, %s)", (stadiumID, stadiumName, capacity, locationID, streetAddress, city, state))
                self.con.commit()
	def update_stadium(self, stadiumID, stadiumName, capacity, locationID, streetAddress, city, state):
                self.cur.execute("Call updateStadiums(%s, %s, %s, %s, %s, %s, %s)", (stadiumID, stadiumName, capacity, locationID, streetAddress, city, state)) 
                self.con.commit()
	def enter_salary(self, playerID, seasonID, teamID, amountEarned):
                self.cur.execute("Call enterSalary(%s, %s, %s, %s)", (playerID, seasonID, teamID, amountEarned))
                self.con.commit()

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/Any')
def any():
	return render_template('any.html')

@app.route('/Any/view_award_winner_by_season', methods=['GET','POST'])
def anyproc1():
	#Malviya, Aditya. .PYTHON . FLASK MYSQL CONNECTION.. Codementor, Codementor, 6 Feb. 2019,
	#www.codementor.io/adityamalviya/python-flask-mysql-connection-rxblpje73.
	#Explanation of Sourse:
	#I was unsure how to gather parameters inserted by users of the webpage into
	#my SQL statements this source gave showed me how to do this using the request
	#package and the "POST" method
	if request.method == "POST":
		details = request.form
		season = details["season"]
		db = Database()
		winners = db.view_award_winners_by_season(season)
		return render_template("view_award_winner_by_season.html", result=winners, content_type = 'application/json')
	else:
		return render_template("get_season.html")

@app.route('/Any/view_award_winner_by_season_and_team', methods = ['GET', 'POST'])
def anyproc2():
	if request.method == "POST":
		details = request.form
		season = details["season"]
		teamID = details["teamID"]
		db = Database()
		winners = db.view_award_winners_by_season_and_team(season, teamID)
		return render_template("view_award_winner_by_season_and_team.html", result=winners, content_type = 'application/json')
	else:
		return render_template("get_season_and_team.html")

@app.route('/Any/view_award_winner_by_league', methods = ['GET', 'POST'])
def anyproc3():
        if request.method == "POST":
                details = request.form
                league = details["leagueID"]
                db = Database()
                winners = db.view_award_winners_by_league(league)
                return render_template("view_award_winner_by_league.html", result=winners, content_type = 'application/json')
        else:
                return render_template("get_league.html")

@app.route('/Any/view_player_stats_by_season', methods = ['GET', 'POST'])
def anyproc4():
        if request.method == "POST":
                details = request.form
                yearGroup = details["season"]
                db = Database()
                winners = db.view_player_stats_by_season(yearGroup)
                return render_template("view_player_stats_by_season.html", result=winners, content_type = 'application/json')
        else:
                return render_template("get_season.html")

@app.route('/Any/view_player_stats_by_player', methods = ['GET', 'POST'])
def anyproc5():
        if request.method == "POST":
                details = request.form
                playerID = details["playerID"]
                db = Database()
                winners = db.view_player_stats_by_player(playerID)
                return render_template("view_player_stats_by_player.html", result=winners, content_type = 'application/json')
        else:
                return render_template("get_player.html")

@app.route('/Any/view_salary_by_season', methods = ['GET', 'POST'])
def anyproc6():
        if request.method == "POST":
                details = request.form
                yearGroup = details["season"]
                db = Database()
                winners = db.view_salary_by_season(yearGroup)
                return render_template("view_salary_by_season.html", result=winners, content_type = 'application/json')
        else:
                return render_template("get_season.html")

@app.route('/Any/view_salary_by_person', methods = ['GET', 'POST'])
def anyproc7():
        if request.method == "POST":
                details = request.form
                playerID = details["playerID"]
                db = Database()
                winners = db.view_salary_by_person(playerID)
                return render_template("view_salary_by_player.html", result=winners, content_type = 'application/json')
        else:
                return render_template("get_player.html")

@app.route('/Any/view_league_champ_by_season', methods = ['GET', 'POST'])
def anyproc8():
        if request.method == "POST":
                details = request.form
                yearGroup = details["season"]
                db = Database()
                winners = db.view_league_champion_by_season(yearGroup)
                return render_template("view_league_champion_by_season.html", result=winners, content_type = 'application/json')
        else:
                return render_template("get_season.html")

@app.route('/Any/view_stadium_by_team', methods = ['GET', 'POST'])
def anyproc9():
        if request.method == "POST":
                details = request.form
                teamID = details["teamID"]
                db = Database()
                winners = db.view_stadium_by_team(teamID)
                return render_template("view_stadium_by_team.html", result=winners, content_type = 'application/json')
        else:
                return render_template("get_team.html")

@app.route('/Any/view_event_winner_by_season', methods = ['GET', 'POST'])
def anyproc10():
        if request.method == "POST":
                details = request.form
                eventID = details["eventID"]
                db = Database()
                winners = db.view_event_winner_by_season(eventID)
                return render_template("view_event_winner_by_season.html", result=winners, content_type = 'application/json')
        else:
                return render_template("get_event.html")

@app.route('/Any/view_event_winner_by_season_and_team', methods = ['GET', 'POST'])
def anyproc11():
        if request.method == "POST":
                details = request.form
                eventID = details["eventID"]
                db = Database()
                winners = db.view_event_winner_by_season_and_team(eventID)
                return render_template("view_event_winner_by_season_and_team.html", result=winners, content_type = 'application/json')
        else:
                return render_template("get_event.html")

@app.route('/Any/view_coaches_by_season_and_team', methods = ['GET', 'POST'])
def anyproc12():
        if request.method == "POST":
                details = request.form
                coach = details["playerID"]
                db = Database()
                winners = db.view_coaches_by_season_and_team(coach)
                return render_template("view_coaches_by_season_and_team.html", result=winners, content_type = 'application/json')
        else:
                return render_template("get_player.html")


@app.route('/Comm')
def comm():
	return render_template('comm.html')


@app.route('/Comm/view_award_winner_by_season', methods=['GET','POST'])
def commproc1():
        if request.method == "POST":
                details = request.form
                season = details["season"]
                db = Database()
                winners = db.view_award_winners_by_season(season)
                return render_template("view_award_winner_by_season.html", result=winners, content_type = 'application/json')
        else:
                return render_template("get_season.html")

@app.route('/Comm/view_award_winner_by_season_and_team', methods = ['GET', 'POST'])
def commproc2():
        if request.method == "POST":
                details = request.form
                season = details["season"]
                teamID = details["teamID"]
                db = Database()
                winners = db.view_award_winners_by_season_and_team(season, teamID)
                return render_template("view_award_winner_by_season_and_team.html", result=winners, content_type = 'application/json')
        else:
                return render_template("get_season_and_team.html")

@app.route('/Comm/view_award_winner_by_league', methods = ['GET', 'POST'])
def commproc3():
        if request.method == "POST":
                details = request.form
                league = details["leagueID"]
                db = Database()
                winners = db.view_award_winners_by_league(league)
                return render_template("view_award_winner_by_league.html", result=winners, content_type = 'application/json')
        else:
                return render_template("get_league.html")

@app.route('/Comm/view_player_stats_by_season', methods = ['GET', 'POST'])
def commproc4():
        if request.method == "POST":
                details = request.form
                yearGroup = details["season"]
                db = Database()
                winners = db.view_player_stats_by_season(yearGroup)
                return render_template("view_player_stats_by_season.html", result=winners, content_type = 'application/json')
        else:
                return render_template("get_season.html")

@app.route('/Comm/view_player_stats_by_player', methods = ['GET', 'POST'])
def commproc5():
        if request.method == "POST":
                details = request.form
                playerID = details["playerID"]
                db = Database()
                winners = db.view_player_stats_by_player(playerID)
                return render_template("view_player_stats_by_player.html", result=winners, content_type = 'application/json')
        else:
                return render_template("get_player.html")

@app.route('/Comm/view_salary_by_season', methods = ['GET', 'POST'])
def commproc6():
        if request.method == "POST":
                details = request.form
                yearGroup = details["season"]
                db = Database()
                winners = db.view_salary_by_season(yearGroup)
                return render_template("view_salary_by_season.html", result=winners, content_type = 'application/json')
        else:
                return render_template("get_season.html")

@app.route('/Comm/view_salary_by_person', methods = ['GET', 'POST'])
def commproc7():
        if request.method == "POST":
                details = request.form
                playerID = details["playerID"]
                db = Database()
                winners = db.view_salary_by_person(playerID)
                return render_template("view_salary_by_player.html", result=winners, content_type = 'application/json')
        else:
                return render_template("get_player.html")

@app.route('/Comm/view_league_champ_by_season', methods = ['GET', 'POST'])
def commproc8():
        if request.method == "POST":
                details = request.form
                yearGroup = details["season"]
                db = Database()
                winners = db.view_league_champion_by_season(yearGroup)
                return render_template("view_league_champion_by_season.html", result=winners, content_type = 'application/json')
        else:
                return render_template("get_season.html")

@app.route('/Comm/view_stadium_by_team', methods = ['GET', 'POST'])
def commproc9():
        if request.method == "POST":
                details = request.form
                teamID = details["teamID"]
                db = Database()
                winners = db.view_stadium_by_team(teamID)
                return render_template("view_stadium_by_team.html", result=winners, content_type = 'application/json')
        else:
                return render_template("get_team.html")

@app.route('/Comm/view_event_winner_by_season', methods = ['GET', 'POST'])
def commproc10():
        if request.method == "POST":
                details = request.form
                eventID = details["eventID"]
                db = Database()
                winners = db.view_event_winner_by_season(eventID)
                return render_template("view_event_winner_by_season.html", result=winners, content_type = 'application/json')
        else:
                return render_template("get_event.html")

@app.route('/Comm/view_event_winner_by_season_and_team', methods = ['GET', 'POST'])
def commproc11():
        if request.method == "POST":
                details = request.form
                eventID = details["eventID"]
                db = Database()
                winners = db.view_event_winner_by_season_and_team(eventID)
                return render_template("view_event_winner_by_season_and_team.html", result=winners, content_type = 'application/json')
        else:
                return render_template("get_event.html")

@app.route('/Comm/view_coaches_by_season_and_team', methods = ['GET', 'POST'])
def commproc12():
        if request.method == "POST":
                details = request.form
                coach = details["playerID"]
                db = Database()
                winners = db.view_coaches_by_season_and_team(coach)
                return render_template("view_coaches_by_season_and_team.html", result=winners, content_type = 'application/json')
        else:
                return render_template("get_player.html")

@app.route('/Comm/enter_season', methods = ['GET', 'POST'])
def commproc13():
        if request.method == "POST":
                details = request.form
                season = details["season"]
                db = Database()
                winners = db.enter_season(season)
                return render_template("get_season.html")
        else:
                return render_template("get_season.html")

@app.route('/Comm/enter_league', methods = ['GET', 'POST'])
def commproc14():
        if request.method == "POST":
                details = request.form
                leagueID = details["leagueID"]
                leagueName = details["leagueName"]
                leaguePresident = details["leaguePresident"]
                db = Database()
                winners = db.enter_league(leagueID, leagueName, leaguePresident)
                return render_template("enter_league.html")
        else:
                return render_template("enter_league.html")

@app.route('/Comm/update_league', methods = ['GET', 'POST'])
def commproc15():
        if request.method == "POST":
                details = request.form
                leagueID = details["leagueID"]
                leagueName = details["leagueName"]
                leaguePresident = details["leaguePresident"]
                db = Database()
                winners = db.update_league(leagueID, leagueName, leaguePresident)
                return render_template("update_league.html")
        else:
                return render_template("update_league.html")

@app.route('/Coor')
def coor():
	return render_template('coor.html')

@app.route('/Coor/view_award_winner_by_season', methods=['GET','POST'])
def coorproc1():
        if request.method == "POST":
                details = request.form
                season = details["season"]
                db = Database()
                winners = db.view_award_winners_by_season(season)
                return render_template("view_award_winner_by_season.html", result=winners, content_type = 'application/json')
        else:
                return render_template("get_season.html")

@app.route('/Coor/view_award_winner_by_season_and_team', methods = ['GET', 'POST'])
def coorproc2():
        if request.method == "POST":
                details = request.form
                season = details["season"]
                teamID = details["teamID"]
                db = Database()
                winners = db.view_award_winners_by_season_and_team(season, teamID)
                return render_template("view_award_winner_by_season_and_team.html", result=winners, content_type = 'application/json')
        else:
                return render_template("get_season_and_team.html")

@app.route('/Coor/view_award_winner_by_league', methods = ['GET', 'POST'])
def coorproc3():
        if request.method == "POST":
                details = request.form
                league = details["leagueID"]
                db = Database()
                winners = db.view_award_winners_by_league(league)
                return render_template("view_award_winner_by_league.html", result=winners, content_type = 'application/json')
        else:
                return render_template("get_league.html")

@app.route('/Coor/view_player_stats_by_season', methods = ['GET', 'POST'])
def coorproc4():
        if request.method == "POST":
                details = request.form
                yearGroup = details["season"]
                db = Database()
                winners = db.view_player_stats_by_season(yearGroup)
                return render_template("view_player_stats_by_season.html", result=winners, content_type = 'application/json')
        else:
                return render_template("get_season.html")

@app.route('/Coor/view_player_stats_by_player', methods = ['GET', 'POST'])
def coorproc5():
        if request.method == "POST":
                details = request.form
                playerID = details["playerID"]
                db = Database()
                winners = db.view_player_stats_by_player(playerID)
                return render_template("view_player_stats_by_player.html", result=winners, content_type = 'application/json')
        else:
                return render_template("get_player.html")

@app.route('/Coor/view_salary_by_season', methods = ['GET', 'POST'])
def coorproc6():
        if request.method == "POST":
                details = request.form
                yearGroup = details["season"]
                db = Database()
                winners = db.view_salary_by_season(yearGroup)
                return render_template("view_salary_by_season.html", result=winners, content_type = 'application/json')
        else:
                return render_template("get_season.html")

@app.route('/Coor/view_salary_by_person', methods = ['GET', 'POST'])
def coorproc7():
        if request.method == "POST":
                details = request.form
                playerID = details["playerID"]
                db = Database()
                winners = db.view_salary_by_season(playerID)
                return render_template("view_salary_by_player.html", result=winners, content_type = 'application/json')
        else:
                return render_template("get_player.html")

@app.route('/Coor/view_league_champ_by_season', methods = ['GET', 'POST'])
def coorproc8():
        if request.method == "POST":
                details = request.form
                yearGroup = details["season"]
                db = Database()
                winners = db.view_league_champion_by_season(yearGroup)
                return render_template("view_league_champion_by_season.html", result=winners, content_type = 'application/json')
        else:
                return render_template("get_season.html")

@app.route('/Coor/view_stadium_by_team', methods = ['GET', 'POST'])
def coorproc9():
        if request.method == "POST":
                details = request.form
                teamID = details["teamID"]
                db = Database()
                winners = db.view_stadium_by_team(teamID)
                return render_template("view_stadium_by_team.html", result=winners, content_type = 'application/json')
        else:
                return render_template("get_team.html")

@app.route('/Coor/view_event_winner_by_season', methods = ['GET', 'POST'])
def coorproc10():
        if request.method == "POST":
                details = request.form
                eventID = details["eventID"]
                db = Database()
                winners = db.view_event_winner_by_season(eventID)
                return render_template("view_event_winner_by_season.html", result=winners, content_type = 'application/json')
        else:
                return render_template("get_event.html")

@app.route('/Coor/view_event_winner_by_season_and_team', methods = ['GET', 'POST'])
def coorproc11():
        if request.method == "POST":
                details = request.form
                eventID = details["eventID"]
                db = Database()
                winners = db.view_event_winner_by_season_and_team(eventID)
                return render_template("view_event_winner_by_season_and_team.html", result=winners, content_type = 'application/json')
        else:
                return render_template("get_event.html")

@app.route('/Coor/view_coaches_by_season_and_team', methods = ['GET', 'POST'])
def coorproc12():
        if request.method == "POST":
                details = request.form
                coach = details["playerID"]
                db = Database()
                winners = db.view_coaches_by_season_and_team(coach)
                return render_template("view_coaches_by_season_and_team.html", result=winners, content_type = 'application/json')
        else:
                return render_template("get_player.html")

@app.route('/Coor/enter_event', methods = ['GET', 'POST'])
def coorproc13():
        if request.method == "POST":
                details = request.form
                eventID = details["eventID"]
                eventName = details["eventName"]
                maxRoundScore = details["maxRoundScore"]
                db = Database()
                winners = db.enter_event(eventID, eventName, maxRoundScore)
                return render_template("enter_event.html", result=winners, content_type = 'application/json')
        else:
                return render_template("enter_event.html")

@app.route('/Coor/enter_event_winner', methods = ['GET', 'POST'])
def coorproc14():
        if request.method == "POST":
                details = request.form
                eventID = details["eventID"]
                yearGroup = details["yearGroup"]
                personID = details["personID"]
                winnerScore = details["winnerScore"]
                winnerRounds = details["winnerRounds"]
                db = Database()
                winners = db.enter_event_winner(eventID, yearGroup, personID, winnerScore, winnerRounds)
                return render_template("enter_event_winner.html", result=winners, content_type = 'application/json')
        else:
                return render_template("enter_event_winner.html")


@app.route('/GM')
def gm():
	return render_template('gm.html')

@app.route('/GM/view_award_winner_by_season', methods=['GET','POST'])
def gmproc1():
        if request.method == "POST":
                details = request.form
                season = details["season"]
                db = Database()
                winners = db.view_award_winners_by_season(season)
                return render_template("view_award_winner_by_season.html", result=winners, content_type = 'application/json')
        else:
                return render_template("get_season.html")

@app.route('/GM/view_award_winner_by_season_and_team', methods = ['GET', 'POST'])
def gmproc2():
        if request.method == "POST":
                details = request.form
                season = details["season"]
                teamID = details["teamID"]
                db = Database()
                winners = db.view_award_winners_by_season_and_team(season, teamID)
                return render_template("view_award_winner_by_season_and_team.html", result=winners, content_type = 'application/json')
        else:
                return render_template("get_season_and_team.html")

@app.route('/GM/view_award_winner_by_league', methods = ['GET', 'POST'])
def gmproc3():
        if request.method == "POST":
                details = request.form
                league = details["leagueID"]
                db = Database()
                winners = db.view_award_winners_by_league(league)
                return render_template("view_award_winner_by_league.html", result=winners, content_type = 'application/json')
        else:
                return render_template("get_league.html")

@app.route('/GM/view_player_stats_by_season', methods = ['GET', 'POST'])
def gmproc4():
        if request.method == "POST":
                details = request.form
                yearGroup = details["season"]
                db = Database()
                winners = db.view_player_stats_by_season(yearGroup)
                return render_template("view_player_stats_by_season.html", result=winners, content_type = 'application/json')
        else:
                return render_template("get_season.html")

@app.route('/GM/view_player_stats_by_player', methods = ['GET', 'POST'])
def gmproc5():
        if request.method == "POST":
                details = request.form
                playerID = details["playerID"]
                db = Database()
                winners = db.view_player_stats_by_player(playerID)
                return render_template("view_player_stats_by_player.html", result=winners, content_type = 'application/json')
        else:
                return render_template("get_player.html")

@app.route('/GM/view_salary_by_season', methods = ['GET', 'POST'])
def gmproc6():
        if request.method == "POST":
                details = request.form
                yearGroup = details["season"]
                db = Database()
                winners = db.view_salary_by_season(yearGroup)
                return render_template("view_salary_by_season.html", result=winners, content_type = 'application/json')
        else:
                return render_template("get_season.html")

@app.route('/GM/view_salary_by_person', methods = ['GET', 'POST'])
def gmproc7():
        if request.method == "POST":
                details = request.form
                playerID = details["playerID"]
                db = Database()
                winners = db.view_salary_by_person(playerID)
                return render_template("view_salary_by_player.html", result=winners, content_type = 'application/json')
        else:
                return render_template("get_player.html")

@app.route('/GM/view_league_champ_by_season', methods = ['GET', 'POST'])
def gmproc8():
        if request.method == "POST":
                details = request.form
                yearGroup = details["season"]
                db = Database()
                winners = db.view_league_champion_by_season(yearGroup)
                return render_template("view_league_champion_by_season.html", result=winners, content_type = 'application/json')
        else:
                return render_template("get_season.html")

@app.route('/GM/view_stadium_by_team', methods = ['GET', 'POST'])
def gmproc9():
        if request.method == "POST":
                details = request.form
                teamID = details["teamID"]
                db = Database()
                winners = db.view_stadium_by_team(teamID)
                return render_template("view_stadium_by_team.html", result=winners, content_type = 'application/json')
        else:
                return render_template("get_team.html")

@app.route('/GM/view_event_winner_by_season', methods = ['GET', 'POST'])
def gmproc10():
        if request.method == "POST":
                details = request.form
                eventID = details["eventID"]
                db = Database()
                winners = db.view_event_winner_by_season(eventID)
                return render_template("view_event_winner_by_season.html", result=winners, content_type = 'application/json')
        else:
                return render_template("get_event.html")

@app.route('/GM/view_event_winner_by_season_and_team', methods = ['GET', 'POST'])
def gmproc11():
        if request.method == "POST":
                details = request.form
                eventID = details["eventID"]
                db = Database()
                winners = db.view_event_winner_by_season_and_team(eventID)
                return render_template("view_event_winner_by_season_and_team.html", result=winners, content_type = 'application/json')
        else:
                return render_template("get_event.html")

@app.route('/GM/view_coaches_by_season_and_team', methods = ['GET', 'POST'])
def gmproc12():
        if request.method == "POST":
                details = request.form
                coach = details["playerID"]
                db = Database()
                winners = db.view_coaches_by_season_and_team(coach)
                return render_template("view_coaches_by_season_and_team.html", result=winners, content_type = 'application/json')
        else:
                return render_template("get_player.html")

@app.route('/GM/enter_player', methods = ['GET', 'POST'])
def gmproc13():
        if request.method == "POST":
                details = request.form
                personID = details["personID"]
                lastName = details["lastName"]
                firstName = details["firstName"]
                number = details["number"]
                position = details["position"]
                db = Database()
                winners = db.enter_player(personID, lastName, firstName, number, position)
                return render_template("enter_player.html")
        else:
                return render_template("enter_player.html")

@app.route('/GM/update_player', methods = ['GET', 'POST'])
def gmproc14():
        if request.method == "POST":
                details = request.form
                personID = details["personID"]
                lastName = details["lastName"]
                firstName = details["firstName"]
                number = details["number"]
                position = details["position"]
                db = Database()
                winners = db.update_player(personID, lastName, firstName, number, position)
                return render_template("update_player.html")
        else:
                return render_template("update_player.html")

@app.route('/GM/enter_coach', methods = ['GET', 'POST'])
def gmproc15():
        if request.method == "POST":
                details = request.form
                personID = details["personID"]
                lastName = details["lastName"]
                firstName = details["firstName"]
                winPercentage = details["winPercentage"]
                db = Database()
                winners = db.enter_coach(personID, lastName, firstName, winPercentage)
                return render_template("enter_coach.html")
        else:
                return render_template("enter_coach.html")

@app.route('/GM/update_coach', methods = ['GET', 'POST'])
def gmproc16():
        if request.method == "POST":
                details = request.form
                personID = details["personID"]
                lastName = details["lastName"]
                firstName = details["firstName"]
                winPercentage = details["winPercentage"]
                db = Database()
                winners = db.update_coach(personID, lastName, firstName, winPercentage)
                return render_template("update_coach.html")
        else:
                return render_template("update_coach.html")

@app.route('/GM/enter_team', methods = ['GET', 'POST'])
def gmproc17():
        if request.method == "POST":
                details = request.form
                teamID = details["teamID"]
                teamName = details["teamName"]
                yearsInLeague = details["yearsInLeague"]
                playoffs = details["Playoffs"]
                stadiumID = details["stadiumID"]
                locationID = details["locationID"]
                db = Database()
                winners = db.enter_team(teamID, teamName, yearsInLeague, playoffs, stadiumID, locationID)
                return render_template("enter_team.html")
        else:
                return render_template("enter_team.html")

@app.route('/GM/update_team', methods = ['GET', 'POST'])
def gmproc18():
        if request.method == "POST":
                details = request.form
                teamID = details["teamID"]
                teamName = details["teamName"]
                yearsInLeague = details["yearsInLeague"]
                playoffs = details["Playoffs"]
                stadiumID = details["stadiumID"]
                locationID = details["locationID"]
                db = Database()
                winners = db.update_team(teamID, teamName, yearsInLeague, playoffs, stadiumID, locationID)
                return render_template("update_team.html")
        else:
                return render_template("update_team.html")

@app.route('/GM/enter_player_statistics', methods = ['GET', 'POST'])
def gmproc19():
        if request.method == "POST":
                details = request.form
                playerID = details["playerID"]
                yearGroup = details["yearGroup"]
                pointsPerGame = details["pointsPerGame"]
                assistsPerGame = details["assistsPerGame"]
                fieldGoalPercentage = details["fieldGoalPercentage"]
                threePointersPerGame = details["threePointersPerGame"]
                threePointerPercentage = details["threePointerPercentage"]
                freeThrowsPercentage = details["freeThrowsPercentage"]
                offensiveReboundsPerGame = details["offensiveReboundsPerGame"]
                defensiveReboundsPerGame = details["defensiveReboundsPerGame"]
                turnoversPerGame = details["turnoversPerGame"]
                blocksPerGame = details["blocksPerGame"]
                stealsPerGame = details["stealsPerGame"]
                db = Database()
                winners = db.enter_player_stats(playerID, yearGroup, pointsPerGame, assistsPerGame, fieldGoalPercentage, threePointersPerGame, threePointerPercentage, freeThrowsPercentage, offensiveReboundsPerGame, defensiveReboundsPerGame, turnoversPerGame, blocksPerGame, stealsPerGame)
                return render_template("enter_player_stats.html")
        else:
                return render_template("enter_player_stats.html")


@app.route('/MOC')
def moc():
	return render_template('MoC.html')

@app.route('/MOC/view_award_winner_by_season', methods = ['GET', 'POST'])
def mocproc1():
        if request.method == "POST":
                details = request.form
                season = details["season"]
                db = Database()
                winners = db.view_award_winners_by_season(season)
                return render_template("view_award_winner_by_season.html", result=winners, content_type = 'application/json')
        else:
                return render_template("get_season.html")

@app.route('/MOC/view_award_winner_by_season_and_team', methods = ['GET', 'POST'])
def mocproc2():
        if request.method == "POST":
                details = request.form
                season = details["season"]
                teamID = details["teamID"]
                db = Database()
                winners = db.view_award_winners_by_season_and_team(season, teamID)
                return render_template("view_award_winner_by_season_and_team.html", result=winners, content_type = 'application/json')
        else:
                return render_template("get_season_and_team.html")

@app.route('/MOC/view_award_winner_by_league', methods = ['GET', 'POST'])
def mocproc3():
        if request.method == "POST":
                details = request.form
                league = details["leagueID"]
                db = Database()
                winners = db.view_award_winners_by_league(league)
                return render_template("view_award_winner_by_league.html", result=winners, content_type = 'application/json')
        else:
                return render_template("get_league.html")

@app.route('/MOC/view_player_stats_by_season', methods = ['GET', 'POST'])
def mocproc4():
        if request.method == "POST":
                details = request.form
                yearGroup = details["season"]
                db = Database()
                winners = db.view_player_stats_by_season(yearGroup)
                return render_template("view_player_stats_by_season.html", result=winners, content_type = 'application/json')
        else:
                return render_template("get_season.html")

@app.route('/MOC/view_player_stats_by_player', methods = ['GET', 'POST'])
def mocproc5():
        if request.method == "POST":
                details = request.form
                playerID = details["playerID"]
                db = Database()
                winners = db.view_player_stats_by_player(playerID)
                return render_template("view_player_stats_by_player.html", result=winners, content_type = 'application/json')
        else:
                return render_template("get_player.html")

@app.route('/MOC/view_salary_by_season', methods = ['GET', 'POST'])
def mocproc6():
        if request.method == "POST":
                details = request.form
                yearGroup = details["season"]
                db = Database()
                winners = db.view_salary_by_season(yearGroup)
                return render_template("view_salary_by_season.html", result=winners, content_type = 'application/json')
        else:
                return render_template("get_season.html")

@app.route('/MOC/view_salary_by_person', methods = ['GET', 'POST'])
def mocproc7():
        if request.method == "POST":
                details = request.form
                playerID = details["playerID"]
                db = Database()
                winners = db.view_salary_by_person(playerID)
                return render_template("view_salary_by_player.html", result=winners, content_type = 'application/json')
        else:
                return render_template("get_player.html")

@app.route('/MOC/view_league_champ_by_season', methods = ['GET', 'POST'])
def mocproc8():
        if request.method == "POST":
                details = request.form
                yearGroup = details["season"]
                db = Database()
                winners = db.view_league_champion_by_season(yearGroup)
                return render_template("view_league_champion_by_season.html", result=winners, content_type = 'application/json')
        else:
                return render_template("get_season.html")

@app.route('/MOC/view_stadium_by_team', methods = ['GET', 'POST'])
def mocproc9():
        if request.method == "POST":
                details = request.form
                teamID = details["teamID"]
                db = Database()
                winners = db.view_stadium_by_team(teamID)
                return render_template("view_stadium_by_team.html", result=winners, content_type = 'application/json')
        else:
                return render_template("get_team.html")

@app.route('/MOC/view_event_winner_by_season', methods = ['GET', 'POST'])
def mocproc10():
        if request.method == "POST":
                details = request.form
                eventID = details["eventID"]
                db = Database()
                winners = db.view_event_winner_by_season(eventID)
                return render_template("view_event_winner_by_season.html", result=winners, content_type = 'application/json')
        else:
                return render_template("get_event.html")

@app.route('/MOC/view_event_winner_by_season_and_team', methods = ['GET', 'POST'])
def mocproc11():
        if request.method == "POST":
                details = request.form
                eventID = details["eventID"]
                db = Database()
                winners = db.view_event_winner_by_season_and_team(eventID)
                return render_template("view_event_winner_by_season_and_team.html", result=winners, content_type = 'application/json')
        else:
                return render_template("get_event.html")

@app.route('/MOC/view_coaches_by_season_and_team', methods = ['GET', 'POST'])
def mocproc12():
        if request.method == "POST":
                details = request.form
                coach = details["playerID"]
                db = Database()
                winners = db.view_coaches_by_season_and_team(coach)
                return render_template("view_coaches_by_season_and_team.html", result=winners, content_type = 'application/json')
        else:
                return render_template("get_player.html")

@app.route('/MOC/enter_award_information', methods = ['GET', 'POST'])
def mocproc13():
        if request.method == "POST":
                details = request.form
                awardID = details["awardID"]
                awardName = details["awardName"]
                timesGiven = details["timesGiven"]
                db = Database()
                winners = db.enter_award_information(awardID, awardName, timesGiven)
                return render_template("enter_award_information.html")
        else:
                return render_template("enter_award_information.html")

@app.route('/MOC/enter_award_winner', methods = ['GET', 'POST'])
def mocproc14():
        if request.method == "POST":
                details = request.form
                awardID = details["awardID"]
                playerID = details["playerID"]
                yearGroup = details["yearGroup"]
                db = Database()
                winners = db.enter_award_winner(awardID, playerID, yearGroup)
                return render_template("enter_award_winner.html")
        else:
                return render_template("enter_award_winner.html")

@app.route('/Owner')
def owner():
	return render_template('owner.html')

@app.route('/Owner/view_award_winner_by_season', methods = ['GET', 'POST'])
def ownerproc1():
        if request.method == "POST":
                details = request.form
                season = details["season"]
                db = Database()
                winners = db.view_award_winners_by_season(season)
                return render_template("view_award_winner_by_season.html", result=winners, content_type = 'application/json')
        else:
                return render_template("get_season.html")

@app.route('/Owner/view_award_winner_by_season_and_team', methods = ['GET', 'POST'])
def ownerproc2():
        if request.method == "POST":
                details = request.form
                season = details["season"]
                teamID = details["teamID"]
                db = Database()
                winners = db.view_award_winners_by_season_and_team(season, teamID)
                return render_template("view_award_winner_by_season_and_team.html", result=winners, content_type = 'application/json')
        else:
                return render_template("get_season_and_team.html")

@app.route('/Owner/view_award_winner_by_league', methods = ['GET', 'POST'])
def ownerproc3():
        if request.method == "POST":
                details = request.form
                league = details["leagueID"]
                db = Database()
                winners = db.view_award_winners_by_league(league)
                return render_template("view_award_winner_by_league.html", result=winners, content_type = 'application/json')
        else:
                return render_template("get_league.html")

@app.route('/Owner/view_player_stats_by_season', methods = ['GET', 'POST'])
def ownerproc4():
        if request.method == "POST":
                details = request.form
                yearGroup = details["season"]
                db = Database()
                winners = db.view_player_stats_by_season(yearGroup)
                return render_template("view_player_stats_by_season.html", result=winners, content_type = 'application/json')
        else:
                return render_template("get_season.html")

@app.route('/Owner/view_player_stats_by_player', methods = ['GET', 'POST'])
def ownerproc5():
        if request.method == "POST":
                details = request.form
                playerID = details["playerID"]
                db = Database()
                winners = db.view_player_stats_by_player(playerID)
                return render_template("view_player_stats_by_player.html", result=winners, content_type = 'application/json')
        else:
                return render_template("get_player.html")

@app.route('/Owner/view_salary_by_season', methods = ['GET', 'POST'])
def ownerproc6():
        if request.method == "POST":
                details = request.form
                yearGroup = details["season"]
                db = Database()
                winners = db.view_salary_by_season(yearGroup)
                return render_template("view_salary_by_season.html", result=winners, content_type = 'application/json')
        else:
                return render_template("get_season.html")

@app.route('/Owner/view_salary_by_person', methods = ['GET', 'POST'])
def ownerproc7():
        if request.method == "POST":
                details = request.form
                playerID = details["playerID"]
                db = Database()
                winners = db.view_salary_by_person(playerID)
                return render_template("view_salary_by_player.html", result=winners, content_type = 'application/json')
        else:
                return render_template("get_player.html")

@app.route('/Owner/view_league_champ_by_season', methods = ['GET', 'POST'])
def ownerproc8():
        if request.method == "POST":
                details = request.form
                yearGroup = details["season"]
                db = Database()
                winners = db.view_league_champion_by_season(yearGroup)
                return render_template("view_league_champion_by_season.html", result=winners, content_type = 'application/json')
        else:
                return render_template("get_season.html")

@app.route('/Owner/view_stadium_by_team', methods = ['GET', 'POST'])
def ownerproc9():
        if request.method == "POST":
                details = request.form
                teamID = details["teamID"]
                db = Database()
                winners = db.view_stadium_by_team(teamID)
                return render_template("view_stadium_by_team.html", result=winners, content_type = 'application/json')
        else:
                return render_template("get_team.html")

@app.route('/Owner/view_event_winner_by_season', methods = ['GET', 'POST'])
def ownerproc10():
        if request.method == "POST":
                details = request.form
                eventID = details["eventID"]
                db = Database()
                winners = db.view_event_winner_by_season(eventID)
                return render_template("view_event_winner_by_season.html", result=winners, content_type = 'application/json')
        else:
                return render_template("get_event.html")

@app.route('/Owner/view_event_winner_by_season_and_team', methods = ['GET', 'POST'])
def ownerproc11():
        if request.method == "POST":
                details = request.form
                eventID = details["eventID"]
                db = Database()
                winners = db.view_event_winner_by_season_and_team(eventID)
                return render_template("view_event_winner_by_season_and_team.html", result=winners, content_type = 'application/json')
        else:
                return render_template("get_event.html")

@app.route('/Owner/view_coaches_by_season_and_team', methods = ['GET', 'POST'])
def ownerproc12():
        if request.method == "POST":
                details = request.form
                coach = details["playerID"]
                db = Database()
                winners = db.view_coaches_by_season_and_team(coach)
                return render_template("view_coaches_by_season_and_team.html", result=winners, content_type = 'application/json')
        else:
                return render_template("get_player.html")

@app.route('/Owner/enter_stadiums', methods = ['GET', 'POST'])
def ownerproc13():
        if request.method == "POST":
                details = request.form
                stadiumID = details["stadiumID"]
                stadiumName = details["stadiumName"]
                capacity = details["Capacity"]
                locationID = details["locationID"]
                streetAddress = details["streetAddress"]
                city = details["City"]
                state = details["State"]
                db = Database()
                winners = db.enter_stadium(stadiumID, stadiumName, capacity, locationID, streetAddress, city, state)
                return render_template("enter_stadium.html")
        else:
                return render_template("enter_stadium.html")

@app.route('/Owner/update_stadiums', methods = ['GET', 'POST'])
def ownerproc14():
        if request.method == "POST":
                details = request.form
                stadiumID = details["stadiumID"]
                stadiumName = details["stadiumName"]
                capacity = details["Capacity"]
                locationID = details["locationID"]
                streetAddress = details["streetAddress"]
                city = details["City"]
                state = details["State"]
                db = Database()
                winners = db.update_stadium(stadiumID, stadiumName, capacity, locationID, streetAddress, city, state)
                return render_template("update_stadium.html")
        else:
                return render_template("update_stadium.html")

@app.route('/Owner/enter_salary', methods = ['GET', 'POST'])
def ownerproc15():
        if request.method == "POST":
                details = request.form
                personID = details["playerID"]
                yearGroup = details["yearGroup"]
                teamID = details["teamID"]
                amountEarned = details["amountEarned"]
                db = Database()
                winners = db.enter_salary(personID, yearGroup, teamID, amountEarned)
                return render_template("enter_salary.html")
        else:
                return render_template("enter_salary.html")

