-- Table definitions for the tournament project.

DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament ;
\c tournament
CREATE TABLE players (
	id SERIAL PRIMARY KEY,
	name text
);
CREATE TABLE matches (
	id SERIAL PRIMARY KEY,
	winner_id INTEGER REFERENCES players(id),
    loser_id INTEGER REFERENCES players(id)
);
CREATE VIEW player_wins AS
SELECT players.id,players.name , count(matches.winner_id)
as number_of_wins from players left join matches on
players.id = matches.winner_id
group by players.id order by number_of_wins DESC ;

CREATE VIEW player_matches AS
SELECT players.id,players.name , count(matches.id) as number_of_matches from players
left join matches on players.id = matches.winner_id or players.id = matches.loser_id
group by players.id order by number_of_matches DESC ;

CREATE VIEW player_standings AS
select player_wins.id,player_wins.name,player_wins.number_of_wins,
player_matches.number_of_matches from
player_wins,player_matches where player_wins.id = player_matches.id
order by player_wins.number_of_wins DESC;



