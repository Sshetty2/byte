"""

Problem 2 Database Schema

* Using either a visual SQL schema designer or a CREATE TABLE statement, design a database of states, cities, and parks as follows:

* There are many states, there are many cities, there are many parks.

* Cities have names and population. Every city is in one state.

* Parks have names. Every park is in at least one state, but a park can occupy more than one state. (For instance, Yellowstone is in Wyoming, Idaho, and Montana)

* States have names and population.


states
pk
name varchar
population int

city
pk
fk state
name varchar
population integer 

parks
pk
names

park_coverage_map
pk
fk state
fk park
"""
states_table = """CREATE TABLE states(
    pk INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR,
    population INTEGER;"""

cities_table = """CREATE TABLE cities(
    pk INTEGER PRIMARY KEY AUTOINCREMENT,
    state INTEGER,
    name VARCHAR,
    population INTEGER,
    FOREIGN KEY(state) REFERENCES states(pk);
    """

parks_table = """CREATE TABLE parks(
    pk INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR;"""

park_coverage_map = """CREATE TABLE park_coverage_map(
    pk INTEGER PRIMARY KEY AUTOINCREMENT,
    state VARCHAR,
    park VARCHAR,
    FOREIGN KEY(state) REFERENCES states(pk),
    FOREIGN KEY(park) REFERENCES parks(pk);"""

