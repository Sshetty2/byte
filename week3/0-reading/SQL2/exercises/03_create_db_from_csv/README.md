# Create a Database from CSV data

##### Description

* For this exercise you will be importing data from the provided `employees.csv` file into a sqlite3 database
* CSV stands for Comma Seperated Values
* Each row is a new person (think similar to an excel spreadsheet but instead of columns all the values are seperated by commas)
* Each person has a name, cellphone, homephone, workphone, email, country

##### Objective 1

* Plan out your tables. 
	* You will have a users table and a phone numbers table.
	* A user has many phone numbers
* Use the [SQL Schema Designer](http://ondras.zarovi.cz/sql/demo/) to plan out your ERDS
	* Push up your ERD's to this folder`(in your own branch)` so I can view them

***If the Schema Designer is giving you problems make a drawing of your ERD. Take a picture of it with your phone and then save it and send it to GITHUB***

##### Objective 2

* Make your python files to create this database and the two tables
* Test your new database by running queries inside the sqlite3 terminal
	* Find all the people who live in Grenada
	* Find all the people who live in Korea
	* Find all the people who's full name contains the name Cindy
		* How can you search a partial string in sqlite? Google time!

##### Resources

* Pythons SQL [documentation](https://docs.python.org/3.4/library/sqlite3.html)
* Pythons CSV Library  [documentation](https://docs.python.org/3.4/library/csv.html)
