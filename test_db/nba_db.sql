###Note: Run the Homework_3_Final.py prior to this as that creates the database we use!!!!
use NBAInfo;

SET SQL_SAFE_UPDATES=0;
set foreign_key_checks=0;
/*
Explanation of Source:
I was getting an error that said I couldn't add to a table due to a foreign key
This source told me I could fix this error by adding the above line to my code.
*/

CREATE TABLE Person(
   personID VARCHAR(10) PRIMARY KEY,
   lastName VARCHAR(15) NOT NULL,
   firstName VARCHAR(15) NOT NULL
	);

CREATE TABLE Player(
   personID VARCHAR(10) PRIMARY KEY,
   playerNumber int, 
   position VARCHAR(15),
   foreign key f1(personID) references Person(personID)
   ON DELETE RESTRICT ON UPDATE CASCADE
	);
    
CREATE TABLE Coach(
   personID VARCHAR(10) PRIMARY KEY,
   winPercentage float,
   foreign key f1(personID) references Person(personID)
   ON DELETE RESTRICT ON UPDATE CASCADE
	);

CREATE TABLE Season(
   yearGroup VARCHAR(7) PRIMARY KEY
	);
    
CREATE TABLE Award(
   awardID VARCHAR(10) PRIMARY KEY,
   awardName VARCHAR(40),
   timesGiven INT
	);
    
CREATE TABLE AwardWinner(
	awardID VARCHAR(10),
	personID VARCHAR(10),
	yearGroup VARCHAR(7),
	PRIMARY KEY (awardID, personID, yearGroup),
	FOREIGN KEY f1(awardID) REFERENCES Award(awardID)
	ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY f2(personID) REFERENCES Person(personID)
	ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY f3(yearGroup) REFERENCES Season(yearGroup)
	ON DELETE RESTRICT ON UPDATE CASCADE
	);

CREATE TABLE Salary(
	personID VARCHAR(10),
	yearGroup VARCHAR(7),
	teamID VARCHAR(10),
	amountEarned INT,
	PRIMARY KEY (personID, yearGroup, teamID),
	FOREIGN KEY f1(personID) REFERENCES Person(personID)
	ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY f2(yearGroup) REFERENCES Season(yearGroup)
	ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY f3(teamID) REFERENCES Teams(teamID)
	ON DELETE RESTRICT ON UPDATE CASCADE
	);
    
CREATE TABLE PlayerSeasonStats(
	personID VARCHAR(10),
	yearGroup VARCHAR(7),
	pointsPerGame FLOAT,
	assistsPerGame FLOAT,
	fieldGoalPercentage FLOAT,
	threePointersPerGame FLOAT,
	threePointerPercentage FLOAT,
	freeThrowsPercentage FLOAT,
	offensiveReboundsPerGame FLOAT,
	defensiveReboundsPerGame FLOAT,
	turnoversPerGame FLOAT,
	blocksPerGame FLOAT,
	stealsPerGame FLOAT,
	PRIMARY KEY (personID, yearGroup),
	FOREIGN KEY f1(personID) REFERENCES Person(personID)
	ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY f2(yearGroup) REFERENCES Season(yearGroup)
	ON DELETE RESTRICT ON UPDATE CASCADE
	);
    
CREATE TABLE allStarEvents(
	eventID VARCHAR(10) PRIMARY KEY,
    eventName VARCHAR(25),
    maxRoundScore int
    );
    
CREATE TABLE eventWinner(
	eventID VARCHAR(10),
    yearGroup VARCHAR(7),
    personID VARCHAR(10),
    winnerScore int,
    winnerRounds int,
    PRIMARY KEY (eventID, yearGroup, personID),
	FOREIGN KEY f1(personID) REFERENCES Player(personID)
	ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY f2(yearGroup) REFERENCES Season(yearGroup)
	ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY f3(eventID) REFERENCES allStarEvents(eventID)
	ON DELETE RESTRICT ON UPDATE CASCADE
    );
    
CREATE TABLE leagueChamp(
	leagueID VARCHAR(10),
    teamID VARCHAR(10),
    yearGroup VARCHAR(7),
    PRIMARY KEY (leagueID, teamID, yearGroup),
    FOREIGN KEY f1(leagueID) REFERENCES League(leagueID)
    ON DELETE RESTRICT ON UPDATE CASCADE,
	FOREIGN KEY f2(teamID) REFERENCES Teams(teamID)
    ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY f3(yearGroup) REFERENCES Season(yearGroup)
    ON DELETE RESTRICT ON UPDATE CASCADE
	);


#Insert awards
INSERT INTO Award(awardID, awardName, timesGiven) VALUES ('NBAAWARD01', "Most Valuable Player", 64);
INSERT INTO Award(awardID, awardName, timesGiven) VALUES ('NBAAWARD02', "Rookie of the Year", 67);
INSERT INTO Award(awardID, awardName, timesGiven) VALUES ('NBAAWARD03', "Coach of the Year", 57);
INSERT INTO Award(awardID, awardName, timesGiven) VALUES ('NAAAWARD04', "G-League Most Valuable Player", 18);

#Insert Seasons
INSERT INTO Season(yearGroup) VALUES ("2018-19");
INSERT INTO Season(yearGroup) VALUES ("2017-18");

####Insert into player and playerseasonstats tables.
INSERT INTO Person(personID, lastName, firstName) VALUES ("NBAMILGA34", "Antetokounmpo", "Giannas");
INSERT INTO Player(personID, playerNumber, position) VALUES ("NBAMILGA34",34,"PF");
INSERT INTO PlayerSeasonStats(personID, yearGroup, pointsPerGame, assistsPerGame, fieldGoalPercentage, threePointersPerGame, threePointerPercentage, freeThrowsPercentage, offensiveReboundsPerGame, defensiveReboundsPerGame, turnoversPerGame, blocksPerGame, stealsPerGame)
VALUES ("NBAMILGA34", "2018-19", 27.7, 5.9, 57.8, 0.7, 25.6, 72.9, 2.2, 10.3, 12.5, 1.5, 1.3);
INSERT INTO PlayerSeasonStats(personID, yearGroup, pointsPerGame, assistsPerGame, fieldGoalPercentage, threePointersPerGame, threePointerPercentage, freeThrowsPercentage, offensiveReboundsPerGame, defensiveReboundsPerGame, turnoversPerGame, blocksPerGame, stealsPerGame)
VALUES ("NBAMILGA34", "2017-18", 26.9, 4.8, 52.9, 0.6, 30.7, 76.0, 2.1, 8.0, 10.0, 1.4, 1.5);
INSERT INTO Person(personID, lastName, firstName) VALUES("NBADALLD77", "Doncic", "Luka");
INSERT INTO Player(personID, playerNumber, position) VALUES("NBADALLD77", 77, "SG") ;
INSERT INTO PlayerSeasonStats(personID, yearGroup, pointsPerGame, assistsPerGame, fieldGoalPercentage, threePointersPerGame, threePointerPercentage, freeThrowsPercentage, offensiveReboundsPerGame, defensiveReboundsPerGame, turnoversPerGame, blocksPerGame, stealsPerGame)
VALUES ("NBADALLD77", "2018-19", 21.2, 6.0, 42.7, 2.3, 32.7, 71.3, 1.2, 6.6, 3.4, 0.3, 1.1);
INSERT INTO Person(personID, lastName, firstName) VALUES('NBAPHIBS25', 'Simmons', 'Ben');
INSERT INTO Player(personID, playerNumber, position) VALUES('NBAPHIBS25', 25, 'PG') ;
INSERT INTO PlayerSeasonStats(personID,yearGroup, pointsPerGame, assistsPerGame, fieldGoalPercentage, threePointersPerGame, threePointerPercentage, freeThrowsPercentage, offensiveReboundsPerGame, defensiveReboundsPerGame, turnoversPerGame, blocksPerGame, stealsPerGame)
VALUES ('NBAPHIBS25', '2017-18', 15.8, 8.2, 56.3, 0, 0, 56.0, 1.8, 6.3, 3.4, 0.9, 1.7);
INSERT INTO PlayerSeasonStats(personID,yearGroup, pointsPerGame, assistsPerGame, fieldGoalPercentage, threePointersPerGame, threePointerPercentage, freeThrowsPercentage, offensiveReboundsPerGame, defensiveReboundsPerGame, turnoversPerGame, blocksPerGame, stealsPerGame)
VALUES ('NBAPHIBS25', '2018-19', 16.9, 7.7, 54.5, 0, 0, 60.0, 2.2, 6.6, 3.5, .8, 1.4);
INSERT INTO Person(personID, lastName, firstName) VALUES('NBAHOUJH13', 'Harden', 'James');
INSERT INTO Player(personID, playerNumber, position) VALUES('NBAHOUJH13', 13, 'PG') ;
INSERT INTO PlayerSeasonStats(personID,yearGroup, pointsPerGame, assistsPerGame, fieldGoalPercentage, threePointersPerGame, threePointerPercentage, freeThrowsPercentage, offensiveReboundsPerGame, defensiveReboundsPerGame, turnoversPerGame, blocksPerGame, stealsPerGame)
VALUES ('NBAHOUJH13', '2018-19', 36.1, 7.5, 44.2, 4.8, 36.8, 87.9, 0.8, 5.8, 5.0, .7, 2);
INSERT INTO PlayerSeasonStats(personID,yearGroup, pointsPerGame, assistsPerGame, fieldGoalPercentage, threePointersPerGame, threePointerPercentage, freeThrowsPercentage, offensiveReboundsPerGame, defensiveReboundsPerGame, turnoversPerGame, blocksPerGame, stealsPerGame)
VALUES ('NBAHOUJH13', '2017-18', 30.4, 8.8, 44.9, 3.7, 36.7, 85.8, 0.6, 4.8, 4.4, .7, 1.8);
INSERT INTO Person(personID, lastName, firstName) VALUES('NBAGSWKT11', 'Thompson', 'Klay');
INSERT INTO Player(personID, playerNumber, position) VALUES('NBAGSWKT11', 11, 'SG');
INSERT INTO PlayerSeasonStats(personID,yearGroup, pointsPerGame, assistsPerGame, fieldGoalPercentage, threePointersPerGame, threePointerPercentage, freeThrowsPercentage, offensiveReboundsPerGame, defensiveReboundsPerGame, turnoversPerGame, blocksPerGame, stealsPerGame)
VALUES ('NBAGSWKT11', '2018-19', 21.5, 2.4, 46.7, 3.1, 40.2, 81.6, .5, 3.41,.5, .6, 1.1);
INSERT INTO PlayerSeasonStats(personID,yearGroup, pointsPerGame, assistsPerGame, fieldGoalPercentage, threePointersPerGame, threePointerPercentage, freeThrowsPercentage, offensiveReboundsPerGame, defensiveReboundsPerGame, turnoversPerGame, blocksPerGame, stealsPerGame)
VALUES ('NBAGSWKT11', '2017-18', 20, 2.5, 48.8, 3.1, 44.0, 83.7, .4, 3.4, 1.8, .5, .8);
INSERT INTO Person(personID, lastName, firstName) VALUES('NBATORDW55', 'Wright', 'Delon');
INSERT INTO Player(personID, playerNumber, position) VALUES('NBATORDW55', 55, 'PG');
INSERT INTO PlayerSeasonStats(personID,yearGroup, pointsPerGame, assistsPerGame, fieldGoalPercentage, threePointersPerGame, threePointerPercentage, freeThrowsPercentage, offensiveReboundsPerGame, defensiveReboundsPerGame, turnoversPerGame, blocksPerGame, stealsPerGame)
VALUES ('NBATORDW55', '2018-19', 8.7, 3.5, 43.4, .7, 29.8, 79.3, .9, 2.6, 1, .4, 1.2);
INSERT INTO PlayerSeasonStats(personID,yearGroup, pointsPerGame, assistsPerGame, fieldGoalPercentage, threePointersPerGame, threePointerPercentage, freeThrowsPercentage, offensiveReboundsPerGame, defensiveReboundsPerGame, turnoversPerGame, blocksPerGame, stealsPerGame)
VALUES ('NBATORDW55', '2017-18', 8.0, 2.9, 46.5, .8, 36.6, 82.9, .7, 2.2, 1.1, .5, 1);
INSERT INTO Person(personID, lastName, firstName) VALUES('NBAOKCHD06', 'Diallo', 'Hamidou');
INSERT INTO Player(personID, playerNumber, position) VALUES('NBAOKCHD06', 6, 'SF');
INSERT INTO PlayerSeasonStats(personID,yearGroup, pointsPerGame, assistsPerGame, fieldGoalPercentage, threePointersPerGame, threePointerPercentage, freeThrowsPercentage, offensiveReboundsPerGame, defensiveReboundsPerGame, turnoversPerGame, blocksPerGame, stealsPerGame)
VALUES ('NBAOKCHD06', '2018-19', 3.7, 0.3, 45.5, .1, 16.7, 61.0, 0.7, 1.2, 0.5, 0.2, 0.4);
INSERT INTO Person(personID, lastName, firstName) VALUES('NBAUTADM45', 'Mitchell', 'Donovan');
INSERT INTO Player(personID, playerNumber, position) VALUES('NBAUTADM45', 45, 'SG');
INSERT INTO PlayerSeasonStats(personID,yearGroup, pointsPerGame, assistsPerGame, fieldGoalPercentage, threePointersPerGame, threePointerPercentage, freeThrowsPercentage, offensiveReboundsPerGame, defensiveReboundsPerGame, turnoversPerGame, blocksPerGame, stealsPerGame)
VALUES ('NBAUTADM45', '2018-19', 23.8, 4.2, 43.2, 2.4, 36.2, 80.6, 0.8, 3.3, 2.8, 0.4, 1.4);
INSERT INTO PlayerSeasonStats(personID,yearGroup, pointsPerGame, assistsPerGame, fieldGoalPercentage, threePointersPerGame, threePointerPercentage, freeThrowsPercentage, offensiveReboundsPerGame, defensiveReboundsPerGame, turnoversPerGame, blocksPerGame, stealsPerGame)
VALUES ('NBAUTADM45', '2017-18', 20.5, 3.7, 43.7, 2.4, 34.0, 80.5, 0.7, 3.1, 2.7, 0.3, 1.5);
INSERT INTO Person(personID, lastName, firstName) VALUES('NBABRKJH12', 'Harris', 'Joe');
INSERT INTO Player(personID, playerNumber, position) VALUES('NBABRKJH12', 12, 'SG');
INSERT INTO PlayerSeasonStats(personID,yearGroup, pointsPerGame, assistsPerGame, fieldGoalPercentage, threePointersPerGame, threePointerPercentage, freeThrowsPercentage, offensiveReboundsPerGame, defensiveReboundsPerGame, turnoversPerGame, blocksPerGame, stealsPerGame)
VALUES ('NBABRKJH12', '2018-19', 13.7, 0.5, 50.0, 2.4, 47.4, 82.7, 0.7, 3.1, 1.6, 0.2, 0.5);
INSERT INTO PlayerSeasonStats(personID,yearGroup, pointsPerGame, assistsPerGame, fieldGoalPercentage, threePointersPerGame, threePointerPercentage, freeThrowsPercentage, offensiveReboundsPerGame, defensiveReboundsPerGame, turnoversPerGame, blocksPerGame, stealsPerGame)
VALUES ('NBABRKJH12', '2017-18', 10.8, 0.4, 49.1, 1.9, 41.9, 82.7, 0.7, 2.7, 1.2, 0.3, 0.4);
INSERT INTO Person(personID, lastName, firstName) VALUES('NBAPHODB01', 'Booker', 'Devin');
INSERT INTO Player(personID, playerNumber, position) VALUES('NBAPHODB01', 1, 'SG');
INSERT INTO PlayerSeasonStats(personID,yearGroup, pointsPerGame, assistsPerGame, fieldGoalPercentage, threePointersPerGame, threePointerPercentage, freeThrowsPercentage, offensiveReboundsPerGame, defensiveReboundsPerGame, turnoversPerGame, blocksPerGame, stealsPerGame)
VALUES ('NBAPHODB01', '2018-19', 26.6, 6.8, 46.7, 2.1, 32.6, 86.6, 0.6, 3.5, 4.1, 0.2, 0.9);
INSERT INTO PlayerSeasonStats(personID,yearGroup, pointsPerGame, assistsPerGame, fieldGoalPercentage, threePointersPerGame, threePointerPercentage, freeThrowsPercentage, offensiveReboundsPerGame, defensiveReboundsPerGame, turnoversPerGame, blocksPerGame, stealsPerGame)
VALUES ('NBAPHODB01', '2017-18', 24.9, 4.7, 43.2, 2.7, 38.3, 87.8, 0.5, 4.0, 3.6, 0.3, 0.9);
INSERT INTO Person(personID, lastName, firstName) VALUES('NBARAPCB25', 'Boucher', 'Chris');
INSERT INTO Player(personID, playerNumber, position) VALUES('NBARAPCB25', 25, 'PF');
INSERT INTO PlayerSeasonStats(personID,yearGroup, pointsPerGame, assistsPerGame, fieldGoalPercentage, threePointersPerGame, threePointerPercentage, freeThrowsPercentage, offensiveReboundsPerGame, defensiveReboundsPerGame, turnoversPerGame, blocksPerGame, stealsPerGame)
VALUES ('NBARAPCB25', '2018-19', 27.2, 1.1, 50.9, 2.2, 32.0, 76.2, 3.0, 8.5, 2.1, 4.1, 1.3);
INSERT INTO PlayerSeasonStats(personID,yearGroup, pointsPerGame, assistsPerGame, fieldGoalPercentage, threePointersPerGame, threePointerPercentage, freeThrowsPercentage, offensiveReboundsPerGame, defensiveReboundsPerGame, turnoversPerGame, blocksPerGame, stealsPerGame)
VALUES ('NBARAPCB25', '2017-18', 11.8, 0.8, 46.9, 0.6, 22.0, 61.8, 2.8, 4.7, 0.9, 2.2, 0.5);
INSERT INTO Person(personID, lastName, firstName) VALUES('NBARAPLB04', 'Brown', 'Lorenzo');
INSERT INTO Player(personID, playerNumber, position) VALUES('NBARAPLB04', 4, 'PG');
INSERT INTO PlayerSeasonStats(personID,yearGroup, pointsPerGame, assistsPerGame, fieldGoalPercentage, threePointersPerGame, threePointerPercentage, freeThrowsPercentage, offensiveReboundsPerGame, defensiveReboundsPerGame, turnoversPerGame, blocksPerGame, stealsPerGame)
VALUES ('NBARAPLB04', '2017-18', 18.8, 8.8, 46.8, 1.1, 33.0, 79.2, 0.5, 4.7, 3.7, 0.3, 1.8);
INSERT INTO Person(personID, lastName, firstName) VALUES('NBAMILMB00', 'Budenholzer', 'Mike');
INSERT INTO Coach(personID, winPercentage) VALUES('NBAMILMB00', 73.2);
INSERT INTO Person(personID, lastName, firstName) VALUES('NBATORDC00', 'Casey', 'Dwayne');
INSERT INTO Coach(personID, winPercentage) VALUES('NBATORDC00', 72.0);


###Insert Award Winners
INSERT INTO AwardWinner(awardID, personID, yearGroup) VALUES ('NBAAWARD01', "NBAMILGA34", "2018-19");
INSERT INTO AwardWinner(awardID, personID, yearGroup) VALUES ('NBAAWARD02', "NBADALLD77", "2018-19");
INSERT INTO AwardWinner(awardID, personID, yearGroup) VALUES ('NBAAWARD03', 'NBAMILMB00', "2018-19");
INSERT INTO AwardWinner(awardID, personID, yearGroup) VALUES ('NBAAWARD04', 'NBARAPCB25', "2018-19");
INSERT INTO AwardWinner(awardID, personID, yearGroup) VALUES ('NBAAWARD01', 'NBAHOUJH13', "2017-18");
INSERT INTO AwardWinner(awardID, personID, yearGroup) VALUES ('NBAAWARD02', 'NBAPHIBS25', "2017-18");
INSERT INTO AwardWinner(awardID, personID, yearGroup) VALUES ('NBAAWARD03', 'NBATORDC00', "2017-18");
INSERT INTO AwardWinner(awardID, personID, yearGroup) VALUES ('NBAAWARD04', 'NBARAPLB04', "2017-18");


###Insert Salary Information
INSERT INTO Salary(personID, yearGroup, teamID, amountEarned) VALUES ("NBADALLD77", "2018-19", "NBADAL0001", 6560640);
INSERT INTO Salary(personID, yearGroup, teamID, amountEarned) VALUES ("NBAMILGA34", "2018-19", "NBAMIL0004", 22471910);
INSERT INTO Salary(personID, yearGroup, teamID, amountEarned) VALUES ("NBAMILGA34", "2017-18", "NBAMIL0004", 24157304);
INSERT INTO Salary(personID, yearGroup, teamID, amountEarned) VALUES ('NBAHOUJH13', "2018-19", "NBAHOU0003", 30421854);
INSERT INTO Salary(personID, yearGroup, teamID, amountEarned) VALUES ('NBAHOUJH13', "2017-18", "NBAHOU0003", 28299399);
INSERT INTO Salary(personID, yearGroup, teamID, amountEarned) VALUES ('NBAPHIBS25', "2018-19", "NBAPHI0006", 6434520);
INSERT INTO Salary(personID, yearGroup, teamID, amountEarned) VALUES ('NBAPHIBS25', "2017-18", "NBAPHI0006", 6168840);
INSERT INTO Salary(personID, yearGroup, teamID, amountEarned) VALUES ('NBATORDW55', "2017-18", "NBATOR0008", 1645200);
INSERT INTO Salary(personID, yearGroup, teamID, amountEarned) VALUES ('NBAGSWKT11', "2017-18", "NBAGSW0002", 17826150);
INSERT INTO Salary(personID, yearGroup, teamID, amountEarned) VALUES ('NBAGSWKT11', "2018-19", "NBAGSW0002", 18988725);
INSERT INTO Salary(personID, yearGroup, teamID, amountEarned) VALUES ('NBATORDC00', "2017-18", "NBATOR0008", 6000000);
INSERT INTO Salary(personID, yearGroup, teamID, amountEarned) VALUES ('NBATORDC00', "2018-19", "NBATOR0008", 6000000);
INSERT INTO Salary(personID, yearGroup, teamID, amountEarned) VALUES ('NBAMILMB00', "2017-18", "NBAMIL0004", 2000000);
INSERT INTO Salary(personID, yearGroup, teamID, amountEarned) VALUES ('NBAMILMB00', "2018-19", "NBAMIL0004", 2000000);
INSERT INTO Salary(personID, yearGroup, teamID, amountEarned) VALUES ('NBARAPCB25', "2017-18", 'NBARAP0011', 1022825);
INSERT INTO Salary(personID, yearGroup, teamID, amountEarned) VALUES ('NBARAPCB25', "2018-19", 'NBARAP0011', 1022825);
INSERT INTO Salary(personID, yearGroup, teamID, amountEarned) VALUES ('NBARAPLB04', "2017-18", 'NBARAP0011', 1621415);
INSERT INTO Salary(personID, yearGroup, teamID, amountEarned) VALUES ('NBAPHODB01', "2017-18", 'NBAPHO0007', 2319360);
INSERT INTO Salary(personID, yearGroup, teamID, amountEarned) VALUES ('NBAPHODB01', "2018-19", 'NBAPHO0007', 3314365);
INSERT INTO Salary(personID, yearGroup, teamID, amountEarned) VALUES ('NBABRKJH12', "2017-18", 'NBANJN0000', 1524305);
INSERT INTO Salary(personID, yearGroup, teamID, amountEarned) VALUES ('NBABRKJH12', "2018-19", 'NBANJN0000', 8333333);
INSERT INTO Salary(personID, yearGroup, teamID, amountEarned) VALUES ('NBAUTADM45', "2017-18", 'NBAUTA0009', 2621280);
INSERT INTO Salary(personID, yearGroup, teamID, amountEarned) VALUES ('NBAUTADM45', "2018-19", 'NBAUTA0009', 3111480);
INSERT INTO Salary(personID, yearGroup, teamID, amountEarned) VALUES ('NBAOKCHD06', "2018-19", 'NBAOKC0005', 838464);

# Insert League Champs
INSERT INTO leagueChamp(leagueID, teamID, yearGroup) VALUES ("NBALeague1", "NBATOR0008", "2018-19");
INSERT INTO leagueChamp(leagueID, teamID, yearGroup) VALUES ("NBALeague2", "NBARIO0012", "2018-19");
INSERT INTO leagueChamp(leagueID, teamID, yearGroup) VALUES ("NBALeague1", "NBAGSW0002", "2017-18");
INSERT INTO leagueChamp(leagueID, teamID, yearGroup) VALUES ("NBALeague2", "NBAAUS0010", "2017-18");

#Insert All-Star Events
INSERT INTO allStarEvents(eventID, eventName, maxRoundScore) VALUES("STAREVENT1", "Slam Dunk Contest", 50);
INSERT INTO allStarEvents(eventID, eventName, maxRoundScore) VALUES("STAREVENT2", "Three Point Contest", 34);

#Insert All-Star Event Winners
INSERT INTO eventWinner(eventID, yearGroup, personID, winnerScore, winnerRounds) VALUES("STAREVENT2", "2018-19", 'NBABRKJH12', 26, 1);
INSERT INTO eventWinner(eventID, yearGroup, personID, winnerScore, winnerRounds) VALUES("STAREVENT2", "2017-18", 'NBAPHODB01', 28, 1);
INSERT INTO eventWinner(eventID, yearGroup, personID, winnerScore, winnerRounds) VALUES("STAREVENT1", "2018-19", 'NBAOKCHD06', 88, 2);
INSERT INTO eventWinner(eventID, yearGroup, personID, winnerScore, winnerRounds) VALUES("STAREVENT1", "2017-18", 'NBAUTADM45', 98, 2);


###Comment Out Users after creation
/*create user eventCoordinator identified by "Coordinator";
create user GM identified by "GM";
create user MasterOfCeremonies identified by "MoC";
create user TeamOwner identified by "Owner";
create user LeagueCommissioner identified by "Commissioner";
create user Anyone identified by "Anyone";*/


DELIMITER $$
CREATE PROCEDURE enterPlayer( 
    pID CHAR(10),
    pLastName CHAR(15),
    pFirstName CHAR(15),
    pNumber int,
    pPosition char(15)
) 
BEGIN
    insert into Person(personID, lastName, firstName)
    values(pID, pLastName, pFirstName)
    on duplicate key update
    personID = pID, 
    lastName = pLastName, 
    firstName = pFirstName;
    insert into Player(personID, playerNumber, position)
    values(pID, pNumber, pPosition)
    on duplicate key update
    personID = pID, 
    playerNumber = pNumber, 
    position = pPosition;
END $$

CREATE PROCEDURE updatePlayer( 
    pID CHAR(10),
    pLastName CHAR(15),
    pFirstName CHAR(15),
    pNumber int,
    pPosition char(15)
) 
BEGIN
    update Person
    set lastName = pLastName, 
    firstName = pFirstName
    where personID = pID;
    update Player
    set playerNumber = pNumber, 
    position = pPosition
    where personID = pID;
END $$

CREATE PROCEDURE enterCoach( 
    pID CHAR(10),
    pLastName CHAR(15),
    pFirstName CHAR(15),
    pWinPercentage float
) 
BEGIN
    insert into Person(personID, lastName, firstName)
    values(pID, pLastName, pFirstName)
    on duplicate key update
    personID = pID,
    lastName = pLastName,
    firstName = pFirstName;
    insert into Coach(personID, winPercentage)
    values(pID, pWinPercentage)
    on duplicate key update
    personID = pID,
    winPercentage = pWinPercentage;
END $$

CREATE PROCEDURE updateCoach( 
    pID CHAR(10),
    pLastName CHAR(15),
    pFirstName CHAR(15),
    pWinPercentage float
) 
BEGIN
    update Person
    set lastName = pLastName, 
    firstName = pFirstName
    where personID = pID;
    update Coach
    set winPercentage = pWinPercentage
    where personID = pID;
END $$

CREATE PROCEDURE enterAwardInformation( 
    pID varCHAR(10),
    pAwardName varCHAR(40),
    pTimesGiven int
) 
BEGIN
    insert into Award(awardID, awardName, timesGiven)
    values(pID, pAwardName, pTimesGiven)
    on duplicate key update
    awardID = pID, 
    awardName = pAwardName,
    timesGiven = pTimesGiven;
END $$

CREATE PROCEDURE enterEvent( 
    pID varCHAR(10),
    pEventName varCHAR(40),
    pMaxRoundScore int
) 
BEGIN
    insert into allStarEvents(eventID, eventName, maxRoundScore)
    values(pID, pEventName, pMaxRoundScore)
    on duplicate key update
    eventID = pID, 
    eventName = pEventName,
    maxRoundScore = pMaxRoundScore;
END $$

CREATE PROCEDURE enterTeam( 
    pID varCHAR(10),
    pTeamName varCHAR(35),
    pYearsInLeague int,
    pPlayoffs int,
    pStadiumID varCHAR(10),
    pLocationID varCHAR(10)
) 
BEGIN
    insert into Teams(teamID, teamName, yearsInLeague, playoffs, stadiumID, locationID)
    values(pID, pTeamName, pYearsInLeague, pPlayoffs, pStadiumID, pLocationID)
    on duplicate key update
    teamID = pID, 
    teamName = pTeamName,
    yearsInLeague = pYearsInLeague, 
    playoffs = pPlayoffs,
    stadiumID = pStadiumID,
    locationID = pLocationID;
END $$

CREATE PROCEDURE updateTeam( 
    pID varCHAR(10),
    pTeamName varCHAR(35),
    pYearsInLeague int,
    pPlayoffs int,
    pStadiumID varCHAR(10),
    pLocationID varCHAR(10)
) 
BEGIN
    update Teams
    set teamName = pTeamName, 
    yearsInLeague = pYearsInLeague, 
    playoffs = pPlayoffs,
    stadiumID = pStadiumID,
    locationID = pLocationID
    where teamID = pID;
END $$

CREATE PROCEDURE enterLeague( 
    pLeagueID varCHAR(10),
    pLeagueName varCHAR(40),
    pLeaguePresident varchar(30)
) 
BEGIN
    insert into Leagues(leagueID, leagueName, leaguePresident)
    values(pLeagueID, pLeagueName, pLeaguePresident)
    on duplicate key update
    leagueID = pLeagueID,
    leagueName = pLeagueName,
    leaguePresident = pLeaguePresident;
END $$

CREATE PROCEDURE updateLeague( 
    pLeagueID varCHAR(10),
    pLeagueName varCHAR(40),
    pLeaguePresident varchar(30)
) 
BEGIN
    update Leagues
    set leagueName = pLeagueName, 
    leaguePresident = pLeaguePresident
    where leagueID = pLeagueID;
END $$

CREATE PROCEDURE enterStadiums( 
    pStadiumID varCHAR(10),
    pStadiumName varCHAR(35),
    pCapacity varchar(10),
    pLocationID varChar(10),
    pStreetAddress varCHAR(60),
    pCity varCHAR(25),
    pState varCHar(25)
) 
BEGIN
    insert into Locations(locationID, streetAddress, city, state)
    values(pLocationID, pStreetAddress, pCity, pState)
    on duplicate key update
    locationID = pLocationID,
    streetAddress = pStreetAddress,
    city = pCity,
    locationID = pLocationID;
    insert into Stadiums(stadiumID, stadiumName, capacity, locationID)
    values(pStadiumID, pStadiumName, pCapacity, pLocationID)
    on duplicate key update
    stadiumID = pStadiumID,
    stadiumName = pStadiumName,
    capacity = pCapacity,
    locationID = pLocationID;
END $$

CREATE PROCEDURE updateStadiums( 
    pStadiumID varCHAR(10),
    pStadiumName varCHAR(35),
    pCapacity varchar(10),
    pLocationID varChar(10),
    pStreetAddress varCHAR(60),
    pCity varCHAR(25),
    pState varCHar(25)
) 
BEGIN
    update Locations
    set streetAddress = pStreetAddress,
    city = pCity,
    state = pState
    where locationID = pLocationID;
    update Stadiums
    set stadiumName = pStadiumName,
    capacity = pCapacity,
    locationID = pLocationID
    where stadiumID = pStadiumID;
END $$

CREATE PROCEDURE enterSalary( 
    pPlayerID varCHAR(10),
    pSeasonID varCHAR(7),
    pTeamID varchar(10),
    pAmountEarned int
) 
BEGIN
    insert into Salary(personID, yearGroup, teamID, amountEarned)
    values(pPlayerID, pSeasonID, pTeamID, pAmountEarned)
    on duplicate key update
    personID = pPlayerID,
    yearGroup = pSeasonID, 
    teamID = pTeamID, 
    amountEarned = pAmountEarned;
END $$

CREATE PROCEDURE enterSeason( 
    pYearGroup varCHAR(7)
) 
BEGIN
    insert into Season(yearGroup)
    values(pYearGroup)
    on duplicate key update
    yearGroup = pYearGroup;
END $$

CREATE PROCEDURE enterAwardWinner( 
    pAwardID varCHAR(10),
    pPlayerID varCHAR(10),
    pYearGroup varchar(7)
) 
BEGIN
    insert into AwardWinner(awardID, personID, yearGroup)
    values(pAwardID, pPlayerID, pYearGroup)
    on duplicate key update
    awardID = pAwardID,
    personID = pPlayerID,
    yearGroup = pYearGroup;
END $$

CREATE PROCEDURE enterEventWinner( 
    pEventID varCHAR(10),
    pYearGroup varchar(7),
    pPersonID varchar(10),
    pwinnerScore int,
    pwinnerRounds int
) 
BEGIN
    insert into eventWinner(eventID, yearGroup, personID, winnerScore, winnerRounds)
    values(pEventID, pYearGroup, pPersonID, pWinnerScore, pWinnerRounds)
    on duplicate key update
    eventID = pEventID,
    yearGroup = pYearGroup,
    personID = pPersonID,
    winnerScore = pWinnerScore,
    winnerRounds = pWinnerRounds;
END $$

CREATE PROCEDURE enterPlayerStatistics( 
    pPlayerID varCHAR(10),
    pYearGroup varchar(7),
    pPointsPerGame float,
    pAssistsPerGame float,
    pFieldGoalPercentage float,
    pThreePointersPerGame float,
    pThreePointerPercentage float,
    pFreeThrowsPercentage float,
    pOffensiveReboundsPerGame float,
    pDefensiveReboundsPerGame float,
    pTurnoversPerGame float,
    pBlocksPerGame float,
    pStealsPerGame float
) 
BEGIN
    insert into PlayerSeasonStats(personID, yearGroup, pointsPerGame, assistsPerGame, fieldGoalPercentage, threePointersPerGame, threePointerPercentage, freeThrowsPercentage, offensiveReboundsPerGame, defensiveReboundsPerGame, turnoversPerGame, blocksPerGame, stealsPerGame)
    values(pPlayerID, pYearGroup, pPointsPerGame, pAssistsPerGame, pFieldGoalPercentage, pThreePointersPerGame, pThreePointerPercentage, pFreeThrowsPercentage, pOffensiveReboundsPerGame, pDefensiveReboundsPerGame, pTurnoversPerGame, pBlocksPerGame, pStealsPerGame)
    on duplicate key update
    personID = pPlayerID,
    yearGroup = pYearGroup,
    pointsPerGame = pPointsPerGame,
    assistsPerGame = pAssistsPerGame,
    fieldGoalPercentage = pFieldGoalPercentage,
    threePointersPerGame = pThreePointersPerGame,
    threePointerPercentage = pThreePointerPercentage,
    freeThrowsPercentage = pFreeThrowsPercentage,
    offensiveReboundsPerGame = pOffensiveReboundsPerGame,
    defensiveReboundsPerGame = pDefensiveReboundsPerGame,
    turnoversPerGame = pTurnoversPerGame,
    blocksPerGame = pBlocksPerGame,
    stealsPerGame = pStealsPerGame;
END $$


CREATE PROCEDURE viewAwardWinnerBySeason ( 
    pYearGroup varCHAR(7)
) 
BEGIN
    SELECT p.lastName, p.firstName, a.awardName
    FROM Person AS p
    JOIN AwardWinner AS w ON p.personID = w.personID
    join Award as a on w.awardID = a.awardID
    WHERE w.yearGroup = pYearGroup
    order by w.yearGroup desc;
END $$

CREATE PROCEDURE viewAwardWinnerBySeasonAndTeam ( 
    pYearGroup varCHAR(7),
    pTeamID varchar(10)
) 
BEGIN
    SELECT p.lastName, p.firstName, a.awardName, t.teamName
    FROM Teams AS t
    JOIN Salary AS s ON t.teamID = s.teamID
    join Person as p on s.personID = p.personID
    join AwardWinner as w on p.personID = w.personID
    join Award as a on w.awardID = a.awardID
    WHERE s.yearGroup = pYearGroup and t.teamID = pTeamID
    order by w.yearGroup desc, t.teamName;
END $$

CREATE PROCEDURE viewAwardWinnerByLeague (
    pLeagueID varchar(10)
) 
BEGIN
    SELECT p.personID, p.lastName, p.firstName, a.awardName, a.awardID, l.leagueID, l.leagueName
    FROM Leagues AS l
    JOIN Teams AS t ON t.leagueID = l.leagueID
    JOIN Salary AS s ON t.teamID = s.teamID
    join Person as p on s.personID = p.personID
    join AwardWinner as w on p.personID = w.personID
    join Award as a on w.awardID = a.awardID
    WHERE l.leagueID = pLeagueID
    AND w.yearGroup = s.yearGroup
    order by l.leagueID;
END $$

CREATE PROCEDURE viewPlayerStatsBySeason ( 
    pYearGroup varCHAR(7)
) 
BEGIN
    SELECT 
    p.lastName, p.firstName, n.yearGroup,
    s.pointsPerGame, s.assistsPerGame, 
    s.fieldGoalPercentage, s. threePointersPerGame, 
    s.threePointerPercentage, s.freeThrowsPercentage, 
    s.offensiveReboundsPerGame, s.defensiveReboundsPerGame, 
    s.turnoversPerGame, s.blocksPerGame, s.stealsPerGame
    FROM PlayerSeasonStats AS s
    JOIN Person AS p ON p.personID = s.personID
    join Season as n on s.yearGroup = n.yearGroup
    WHERE n.yearGroup = pYearGroup
    order by n.yearGroup desc;
END $$

CREATE PROCEDURE viewPlayerStatsByPlayer ( 
    pPlayerID varCHAR(10)
) 
BEGIN
    SELECT 
    p.lastName, p.firstName, n.yearGroup,
    s.pointsPerGame, s.assistsPerGame, 
    s.fieldGoalPercentage, s. threePointersPerGame, 
    s.threePointerPercentage, s.freeThrowsPercentage, 
    s.offensiveReboundsPerGame, s.defensiveReboundsPerGame, 
    s.turnoversPerGame, s.blocksPerGame, s.stealsPerGame
    FROM PlayerSeasonStats AS s
    JOIN Person AS p ON p.personID = s.personID
    join Season as n on s.yearGroup = n.yearGroup
    WHERE p.personID = pPlayerID
    order by p.personID;
END $$

CREATE PROCEDURE viewSalaryBySeason ( 
    pYearGroup varCHAR(7)
) 
BEGIN
    SELECT p.lastName, p.firstName, s.amountEarned, t.yearGroup
    FROM Salary as s
    JOIN Person AS p ON s.personID = p.personID
    join PlayerSeasonStats as t on p.personID = t.personID
    WHERE s.yearGroup = pYearGroup
    order by t.yearGroup desc;
END $$

CREATE PROCEDURE viewSalaryByPerson ( 
    pPersonID varCHAR(10)
) 
BEGIN
    SELECT p.lastName, p.firstName, s.amountEarned, s.yearGroup
    FROM Person as p
    JOIN Salary AS s ON s.personID = p.personID
    WHERE p.personID = pPersonID;
END $$

CREATE PROCEDURE viewLeagueChampionBySeason ( 
    pYearGroup varCHAR(7)
) 
BEGIN
    SELECT t.teamName, g.leagueName, l.yearGroup
    FROM Teams as t
    JOIN leagueChamp AS l ON l.teamID = t.teamID
    JOIN Leagues AS g ON g.leagueID = l.leagueID
    WHERE l.yearGroup = pYearGroup;
END $$

CREATE PROCEDURE viewStadiumByTeam ( 
    pTeamID varCHAR(10)
) 
BEGIN
    SELECT t.teamID, s.stadiumName, s.capacity, l.streetAddress, l.city, l.state
    FROM Teams as t
    JOIN Stadiums AS s ON s.stadiumID = t.stadiumID
    JOIN Locations as l on l.locationID = s.locationID
    WHERE t.teamID = pTeamID;
END $$

CREATE PROCEDURE viewEventWinnerBySeason ( 
    pEventID varCHAR(10)
) 
BEGIN
    SELECT p.PersonID, p.firstName, p.lastName, e.eventID, a.eventName, e.yearGroup
    FROM eventWinner as e
    JOIN Person AS p ON p.PersonID = e.PersonID
    Join allStarEvents as a on a.eventID = e.eventID
    WHERE e.eventID = pEventID;
END $$

CREATE PROCEDURE viewEventWinnerBySeasonandTeam ( 
    pEventID varCHAR(10)
) 
BEGIN
    SELECT p.PersonID, p.firstName, p.lastName, e.eventID, a.eventName, e.yearGroup
    FROM eventWinner as e
    JOIN Person AS p ON p.PersonID = e.PersonID
    Join allStarEvents as a on a.eventID = e.eventID
    JOIN Salary as s on s.PersonID = p.PersonID
    JOIN Teams AS t ON t.teamID = s.teamID 
    WHERE e.eventID = pEventID;
END $$

CREATE PROCEDURE viewCoachesBySeasonandTeam ( 
    pPersonID varCHAR(10)
) 
BEGIN
    SELECT p.PersonID, p.firstName, p.lastName, t.teamID, t.teamName, s.yearGroup
    FROM Coach as c
    JOIN Person AS p ON p.PersonID = c.PersonID
    JOIN Salary as s on s.PersonID = p.PersonID
    JOIN Teams AS t ON t.teamID = s.teamID 
    WHERE c.personID = pPersonID;
END $$

DELIMITER ;

grant execute on procedure enterPlayer to GM;
grant execute on procedure updatePlayer to GM;
grant execute on procedure enterCoach to GM;
grant execute on procedure updateCoach to GM;
grant execute on procedure enterAwardInformation to MasterOfCeremonies;
grant execute on procedure enterTeam to GM;
grant execute on procedure updateTeam to GM;
grant execute on procedure enterStadiums to TeamOwner;
grant execute on procedure updateStadiums to TeamOwner;
grant execute on procedure enterSalary to TeamOwner;
grant execute on procedure enterSeason to LeagueCommissioner;
grant execute on procedure enterLeague to LeagueCommissioner;
grant execute on procedure updateLeague to LeagueCommissioner;
grant execute on procedure enterAwardWinner to MasterOfCeremonies;
grant execute on procedure enterPlayerStatistics to GM;
grant execute on procedure enterEvent to eventCoordinator;
grant execute on procedure enterEventWinner to eventCoordinator;
-- below are the cases anyone can do. These procedures are not in yet.

grant execute on procedure viewAwardWinnerBySeason to GM;
grant execute on procedure viewAwardWinnerBySeason to TeamOwner;
grant execute on procedure viewAwardWinnerBySeason to LeagueCommissioner;
grant execute on procedure viewAwardWinnerBySeason to MasterOfCeremonies;
grant execute on procedure viewAwardWinnerBySeason to eventCoordinator;
grant execute on procedure viewAwardWinnerBySeason to Anyone;

grant execute on procedure viewAwardWinnerBySeasonAndTeam to GM;
grant execute on procedure viewAwardWinnerBySeasonAndTeam to TeamOwner;
grant execute on procedure viewAwardWinnerBySeasonAndTeam to LeagueCommissioner;
grant execute on procedure viewAwardWinnerBySeasonAndTeam to MasterOfCeremonies;
grant execute on procedure viewAwardWinnerBySeasonAndTeam to eventCoordinator;
grant execute on procedure viewAwardWinnerBySeasonAndTeam to Anyone;

grant execute on procedure viewAwardWinnerByLeague to GM;
grant execute on procedure viewAwardWinnerByLeague to TeamOwner;
grant execute on procedure viewAwardWinnerByLeague to LeagueCommissioner;
grant execute on procedure viewAwardWinnerByLeague to MasterOfCeremonies;
grant execute on procedure viewAwardWinnerByLeague to eventCoordinator;
grant execute on procedure viewAwardWinnerByLeague to Anyone;

grant execute on procedure viewPlayerStatsBySeason to GM;
grant execute on procedure viewPlayerStatsBySeason to TeamOwner;
grant execute on procedure viewPlayerStatsBySeason to LeagueCommissioner;
grant execute on procedure viewPlayerStatsBySeason to MasterOfCeremonies;
grant execute on procedure viewPlayerStatsBySeason to eventCoordinator;
grant execute on procedure viewPlayerStatsBySeason to Anyone;

grant execute on procedure viewPlayerStatsByPlayer to GM;
grant execute on procedure viewPlayerStatsByPlayer to TeamOwner;
grant execute on procedure viewPlayerStatsByPlayer to LeagueCommissioner;
grant execute on procedure viewPlayerStatsByPlayer to MasterOfCeremonies;
grant execute on procedure viewPlayerStatsByPlayer to eventCoordinator;
grant execute on procedure viewPlayerStatsByPlayer to Anyone;

grant execute on procedure viewSalaryBySeason to GM;
grant execute on procedure viewSalaryBySeason to TeamOwner;
grant execute on procedure viewSalaryBySeason to LeagueCommissioner;
grant execute on procedure viewSalaryBySeason to MasterOfCeremonies;
grant execute on procedure viewSalaryBySeason to eventCoordinator;
grant execute on procedure viewSalaryBySeason to Anyone;

grant execute on procedure viewSalaryByPerson to GM;
grant execute on procedure viewSalaryByPerson to TeamOwner;
grant execute on procedure viewSalaryByPerson to LeagueCommissioner;
grant execute on procedure viewSalaryByPerson to MasterOfCeremonies;
grant execute on procedure viewSalaryByPerson to eventCoordinator;
grant execute on procedure viewSalaryByPerson to Anyone;

grant execute on procedure viewLeagueChampionBySeason to GM;
grant execute on procedure viewLeagueChampionBySeason to TeamOwner;
grant execute on procedure viewLeagueChampionBySeason to LeagueCommissioner;
grant execute on procedure viewLeagueChampionBySeason to MasterOfCeremonies;
grant execute on procedure viewLeagueChampionBySeason to eventCoordinator;
grant execute on procedure viewLeagueChampionBySeason to Anyone;

grant execute on procedure viewStadiumByTeam to GM;
grant execute on procedure viewStadiumByTeam to TeamOwner;
grant execute on procedure viewStadiumByTeam to LeagueCommissioner;
grant execute on procedure viewStadiumByTeam to MasterOfCeremonies;
grant execute on procedure viewStadiumByTeam to eventCoordinator;
grant execute on procedure viewStadiumByTeam to Anyone;

grant execute on procedure viewEventWinnerBySeason to GM;
grant execute on procedure viewEventWinnerBySeason to TeamOwner;
grant execute on procedure viewEventWinnerBySeason to LeagueCommissioner;
grant execute on procedure viewEventWinnerBySeason to MasterOfCeremonies;
grant execute on procedure viewEventWinnerBySeason to eventCoordinator;
grant execute on procedure viewEventWinnerBySeason to Anyone;

grant execute on procedure viewEventWinnerBySeasonandTeam to GM;
grant execute on procedure viewEventWinnerBySeasonandTeam to TeamOwner;
grant execute on procedure viewEventWinnerBySeasonandTeam to LeagueCommissioner;
grant execute on procedure viewEventWinnerBySeasonandTeam to MasterOfCeremonies;
grant execute on procedure viewEventWinnerBySeasonandTeam to eventCoordinator;
grant execute on procedure viewEventWinnerBySeasonandTeam to Anyone;

grant execute on procedure viewCoachesBySeasonandTeam to GM;
grant execute on procedure viewCoachesBySeasonandTeam to TeamOwner;
grant execute on procedure viewCoachesBySeasonandTeam to LeagueCommissioner;
grant execute on procedure viewCoachesBySeasonandTeam to MasterOfCeremonies;
grant execute on procedure viewCoachesBySeasonandTeam to eventCoordinator;
grant execute on procedure viewCoachesBySeasonandTeam to Anyone;



