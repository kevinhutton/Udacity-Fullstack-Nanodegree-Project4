-- Table definitions for the tournament project.

DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament ;
\c tournament
DROP TABLE  IF EXISTS players;
CREATE TABLE players (
	id SERIAL PRIMARY KEY,
	name text,
	wins INTEGER,
	matches INTEGER
);
DROP DATABASE IF EXISTS matches ;
CREATE TABLE matches (
	match_id SERIAL PRIMARY KEY,
	player_a_id INTEGER REFERENCES players(id),
	player_b_id INTEGER REFERENCES players(id),
	winner_id   INTEGER REFERENCES players(id)
);


