import sqlite3

db = sqlite3.connect('fitness.db')

cursor = db.cursor()

cursor.execute('''
  CREATE TABLE gyms (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    city TEXT,
    rate INTEGER
  );
''')

cursor.execute('''
  CREATE TABLE members(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    gym_id INTEGER,
    first_name TEXT,
    last_name TEXT,
    age INTEGER,
    FOREIGN KEY(gym_id) REFERENCES gyms(id)
  );
''')


db.commit()
# db.close()

print("Your tables have been made!")

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
  [2, "Maria", "Hill", 32]
]

print("Destroying old data")
cursor.execute("DELETE FROM gyms")
cursor.execute("DELETE FROM members")

for gym in GYMS:
  cursor.execute(
    """
    INSERT INTO gyms ("name", "city", "rate") 
    VALUES (?, ?, ?);
    """,(gym[0], gym[1], gym[2])
  )

db.commit()

for member in MEMBERS:
  cursor.execute(
    """
    INSERT INTO members ("gym_id", "first_name", "last_name", "age")
    VALUES (?, ?, ?, ?);
    """, (member[0], member[1], member[2], member[3])
  )

db.commit()
cursor.close()





