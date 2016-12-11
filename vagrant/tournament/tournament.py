#!/usr/bin/env python
# tournament.py -- implementation of a Swiss-system tournament
# Kevin Hutton

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""

    try:
        print "Clearing matches records from matches database"
        dbConnection = connect()
        dbCursor = dbConnection.cursor()
        dbCursor.execute(""" TRUNCATE "matches" CASCADE """)
        dbConnection.commit()
        print "Successfully cleared matches database"
        return 0

    except Exception as error:
        print "Unable to clear matches database :\n %s" % (error)
        exit(1)


def deletePlayers():
    """Remove all the player records from the database."""

    try:
        print "Clearing player records from players database"
        dbConnection = connect()
        dbCursor = dbConnection.cursor()
        dbCursor.execute(""" TRUNCATE "players" CASCADE """)
        dbConnection.commit()
        print "Successfully cleared players database"
        return 0

    except Exception as error:
        print "Unable to clear players database :\n %s" % (error)
        exit(1)


def countPlayers():
    """Returns the number of players currently registered."""
    try:
        print "Counting players"
        dbConnection = connect()
        dbCursor = dbConnection.cursor()
        dbCursor.execute(""" select count(*) as count FROM "players" """)
        output = dbCursor.fetchone()
        return int(output[0]) or 0

    except Exception as error:
        print "Unable to count players in database :\n %s" % (error)
        exit(1)


def registerPlayer(name):
    """Adds a player to the tournament database.

    A unique ID will be assigned to the player during insertion

    Args:
      name: the player's full name (need not be unique).
    """

    try:
        print "Register Player"
        dbConnection = connect()
        dbCursor = dbConnection.cursor()
        dbCursor.execute("""INSERT INTO "players" (name) VALUES (%s) """,
                         (name,))
        dbConnection.commit()
        print "Successfully inserted %s into players database" % (name)

    except Exception as error:
        print "Unable to insert player into database :\n %s" % (error)
        exit(1)


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """

    try:
        print "Calculating player standings"
        dbConnection = connect()
        dbCursor = dbConnection.cursor()
        query = """select * from player_standings;"""
        dbCursor.execute(query)
        output = dbCursor.fetchall()
        return output

    except Exception as error:
        print "Unable to count players in database :\n %s" % (error)
        exit(1)


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """

    try:
        print "Report Match"
        dbConnection = connect()
        dbCursor = dbConnection.cursor()
        dbCursor.execute("""INSERT INTO "matches" (winner_id,loser_id) VALUES (%s,%s) """,
                         (winner,loser))
        dbConnection.commit()

    except Exception as error:
        print "Unable to report match :\n %s" % (error)
        exit(1)


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    list_of_players = playerStandings()

    # For this project , we assume that the number of players is even
    if (len(list_of_players) % 2 != 0):
        print "Odd number of players ! Exiting !"
        exit(1)
    # Iterate through list of players
    # Select pairs with equal or nearly-equal win record
    pairing_list = []
    my_itr = iter(list_of_players)
    for player in my_itr:
        try:
            next_player = my_itr.next()
            match = (player[0], player[1], next_player[0], next_player[1])
        except:
            match = (player[0], player[1], 'NA', 'NA')
        pairing_list.append(match)
    return pairing_list
