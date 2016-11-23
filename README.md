# Udacity Fullstack Nanodegree Project 4 - Game Tournament

The purpose of this project was to create a Python module that uses  PostgreSQL to keep track of players and matches in a game tournament.

This application demonstrates the following tools/technologies:

  1. python
  2. postgres-sql
 
This project was done as part of the Udacity Fullstack Nanodegree program

###How to Run Project

1. Retrieve workspace: <br> ``` git clone https://github.com/kevinhutton/Udacity-Fullstack-Nanodegree-Project4.git ```
2. Navigate to "vagrant" folder: <br> ``` cd Udacity-Fullstack-Nanodegree-Project4/vagrant ```
3. Start vagrant VM: <br> ``` vagrant up ```
4. Log onto VM: <br> ``` vagrant ssh ```
5. Navigate to "tournament" folder: <br> ``` vagrant@vagrant-ubuntu-trusty-32:~$ cd /vagrant/tournament/ ```
6. Create database and tables: <br> ``` vagrant@vagrant-ubuntu-trusty-32:/vagrant/tournament$ psql -f tournament.sql ```
7. Launch tournament test suite: <br> ``` vagrant@vagrant-ubuntu-trusty-32:/vagrant/tournament$ python tournament_test.py ```


At the conclusion of step #7 , you should see the output ```Success!  All tests pass!```

