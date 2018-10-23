# Relational DB and Foreign Keys

### Learning Objectives
***Students will be able to...***

* Diagram out an ERD of a Relational Database (Review)
* Use Foreign Keys to connect multiple tables in SQLite
* Build a database with a one to one relationship
* Build a database with a one to many relationship
* Query a database
* Make a Join Table SQL query (Luxury Goal)

---

### Context

* We've done CRUD with a single table database. That's all great but as our data becomes bigger we are going to need more tables for organization.

---

### Lessons

##### Part 1 - ERDs / Relationships Review

* What are some examples of a one to one relationship? How about a one to many relationship?
  * One to One
    * A person has one SSN
    * A person has one passport
  * One to Many
    * A person has one birthday / A birthday has many people
    * A person has one gym / A gym has many members
    * A pet has one owner / A person has many pets

***One to One***

* A row in a table has a relationship with another row in another table. 
* This relationship works both ways between the two tables. Each row can have a connection only with one other row from another table. 

***One to Many***

* A row in one table can have a connection with multiple rows in another table
* In reverse, multiple rows in a table can be connected to the same row in another table

***Five Min Exercise***

* Take the examples above and draw out an ERD of them. 
* We'll be using the ERD diagram website: [http://ondras.zarovi.cz/sql/demo/](http://ondras.zarovi.cz/sql/demo/)

***Hints***

* Which table takes precedent over the other in a relational database?
* Is there a parent table and a child table?

  
##### Part 2 - SQL Foriegn Keys

* Foreign Keys allow us to reference one table to another.
* A Foreign Key is an extra `colomn` in a table
* This column will be located/entered in the `child table` and will `reference` the parent

***Example Code Along***

***This can be a code along, or a pair program where you drive and they take notes. There's a create.db file for reference***

* Let's build out the gym example above inside a create.db file
* We'll have two tables
* Only one table will have a `Foreign Key` column

```
CREATE TABLE gyms (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT,
  city TEXT,
  rate INTEGER
);

CREATE TABLE members(
  member_id INTEGER PRIMARY KEY AUTOINCREMENT,
  gym_id INTEGER,
  first_name TEXT,
  last_name TEXT,
  age INTEGER,
  FOREIGN KEY(gym_id) REFERENCES gyms(id)
);
```
* Add the following gyms and members

```
GYMS = [
  ["Golds Gym", "Los Angeles", 40],
  ["Equinox", "New York", 150],
  ["Planet Fitness", "New Jersey", 15],
  ["Blink", "New York", 20],
]

MEMBERS = [
  [2, "Wade", "Wilson", 50],
  [2, "James", "Howlett", 324],
  [4, "Peter", "Parker", 21],
  [1, "Steve", "Rogers", 87],
  [3, "Scott", "Summers", 35],
  [1, "Jean", "Grey", 30],
  [4, "Kitty", "Pride", 20],
  [3, "Natasha", "Romenov", 38],
  [2, "Maria", "Hill", 32],
]
```
* Lets make sure we got everything right here

```
SELECT * FROM members;
```
* Now let's use the foreign key to grab us some items

```
SELECT members.first_name FROM members, gyms WHERE gyms.id=2;
```
* Woah why did we get all the first names in the members table? 
* Is our foreign key not working? 
* Or maybe SQL isn't doing this search how you think it is. We have to specify the relationship in the query as well. 

***Challenge Question***

* Let's say we're at the point in our Python code where we've got the name of a gym stored in a variable, like below:
```
name = 'Equinox'
```
* And from here, I want to find the members who belong to that Gym.
* I would probably do a two step process. 

***First Step***

* I would query gyms to find the ID of the gym:

```
gym_id = "SELECT id FROM gyms WHERE name = 'Equinox';"
```
* And based on our current database the `gym_id` variable has now been `assigned` a `value` of 2

***Second Step***

* I would query the members table, and find all members who have `2` in their `gym_id` column, as shown below:

```
members_of_gym = "SELECT * FROM members WHERE gym_id=gym_id;"
```
* And this would return to me all members who belong to the gym called `Equiniox`. 
* My problem with this is that it's two steps. 
* **First** we query the gym table, and **second** we query the members table. Is there a way to do this in one step? All I could think of was this:

```
members_of_gym = SELECT * FROM members WHERE gym_id=(SELECT id FROM gyms WHERE name = 'Equinox');
```
***Spoiler alert! Solution below!***

* The **solution** is to use an `AND` SQL statement:

```
members_of_gym = '''
  SELECT *
  FROM member, gyms
  WHERE members.gym_id=gyms.id AND gyms.name='Equinox';
'''
```


#### Resources

* [SQL Schema Designer](http://ondras.zarovi.cz/sql/demo/)
* [SQLite tutorial](http://zetcode.com/db/sqlite/)
* [Best practices for database design. There are more good things on this site](http://www.sqlwatchmen.com/blogs/jim/2011/03/28/best-practices-for-database-schema-design/)
* [10 common database design mistakes](https://www.simple-talk.com/sql/database-administration/ten-common-database-design-mistakes/)
* [An article about null values. The important part of this is that emptiness and null are not the same. You don't have to agree with what he says.](http://www.bennadel.com/blog/85-why-null-values-should-not-be-used-in-a-database-unless-required.htm)
* [High Scalability - A blog on scaling databases](http://highscalability.com/)
* [SQL Course](http://www.sqlcourse.com/)
* [SQL Course 2](http://www.sqlcourse2.com/)
