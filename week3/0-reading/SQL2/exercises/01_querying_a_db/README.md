## QUERY PRACTICE

##### Description

* Practice makes perfect
* You have been given a database file in this repo called `sitemetrics.db`
* All the work for this exercise will be done in the terminal. That's right, we're taking a break from python files. 

##### Objective

* Open the database file using the sqlite3 command in your terminal.
* For each question, enter the SQL Query you used and your answer
* Then push up your answers to YOUR OWN GITHUB BRANCH 

-------------
##### How many people are from California?  
SELECT COUNT(*) FROM users WHERE state = 'CA';

##### Who has the most page views? How many do they have, and where are they from?
SELECT * FROM users ORDER BY page_views DESC LIMIT 1;


##### Who has the least page views? How many do they have and where are they from?
SELECT name, page_views FROM users ORDER BY page_views LIMIT 1  OFFSET 1;
SELECT * FROM users WHERE name = 'Vivian Rosa';
or 
SELECT * FROM users WHERE name = (SELECT name FROM users ORDER BY page_views LIMIT 1  OFFSET 1);


##### Who are the most recent visitors to the site?(at least 3)
SELECT * FROM users ORDER BY last_visit DESC LIMIT 3;


##### Who was the first visitor?
SELECT * FROM users ORDER BY last_visit LIMIT 1;

##### Who has an email address with the domain 'horse.edu'?
SELECT * FROM users WHERE email LIKE "%horse.edu%";

##### How many people are from the city Graford?
SELECT * FROM users where city = 'Graford';


##### What are the names of all the cities that start with the letter V, in alphabetical order?
SELECT * FROM users where city LIKE "V%" ORDER BY city;

##### What are the names and home cities for people searched for the word "drain"?
SELECT id FROM search_terms WHERE word = "drain";
SELECT user_id FROM user_searches WHERE term_id = 201;

or 

SELECT user_id FROM user_searches WHERE term_id = (SELECT id FROM search_terms WHERE word = "drain");

then 

SELECT * FROM users WHERE id IN (76, 172, 216, 218);

OR simply 

SELECT * FROM users WHERE id IN (SELECT user_id FROM user_searches WHERE term_id = (SELECT id FROM search_terms WHERE word = "drain"));

 


##### How many times was "trousers" a search term?

SELECT COUNT(*) FROM user_searches WHERE term_id = (SELECT id FROM search_terms WHERE word = "trousers");


##### What were the search terms used by visitors who last visited on August 22 2014?

SELECT word FROM search_terms where id IN (SELECT term_id FROM user_searches WHERE user_id IN (SELECT id FROM users WHERE last_visit = "2014-08-22"));

SELECT search_terms.word FROM  users, search_terms, user_searches WHERE users.last_visit = '2014-08-22' AND users.id = user_searches.user_id AND user_searches.term_id = search_terms.id;
##### What was the most frequently used search term by people from Idaho?

SELECT id FROM users WHERE state = 'ID';
SELECT term_id FROM user_searches WHERE user_id IN (SELECT id FROM users WHERE state = 'ID');

SELECT word, COUNT(*) 
FROM users, search_terms, user_searches 
    users.state = 'ID' AND users.id = user_searches.user_id AND user_searches.term_id = search_terms.id 
GROUP BY word;


##### What is the name of user 391, and what are his search terms?

SELECT name FROM users where id = '391';
SELECT word FROM search_terms WHERE id IN (select term_id from user_searches where user_id = '391');

or

SELECT word FROM user_searches, search_terms WHERE user_searches.user_id = '391' AND search_terms.id = user_searches.term_id;