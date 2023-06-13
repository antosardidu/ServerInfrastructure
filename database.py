import mysql.connector

# Create a connection to the database
connection = mysql.connector.connect(
  host='localhost',
  user='root', #ganti ke local account
  password='JohnCarlos1234', #ganti ke local account
  database='mydatabase'
)

# Create a cursor object
cursor = connection.cursor(buffered=True)

# Create a table
cursor.execute('''
CREATE TABLE USER (
  userID INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(255) NOT NULL,
  password VARCHAR(255) NOT NULL,
  memberLevel VARCHAR(255) NOT NULL,
  balance LONG
);

''')

cursor.execute('''
  CREATE TABLE TRANSACTION (
  transactionID INT AUTO_INCREMENT PRIMARY KEY,
  userID INT NOT NULL,
  amount LONG,
  type VARCHAR(255),
  FOREIGN KEY(userID) REFERENCES USER(userID)
);

''')

cursor.execute('''
  CREATE TABLE GAME(
  gameID INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255)
);

''')

cursor.execute('''
CREATE TABLE GAME_REPORT(
  gameID INT NOT NULL,
  userID INT NOT NULL,
  FOREIGN KEY (gameID) REFERENCES GAME(gameID),
  FOREIGN KEY (userID) REFERENCES USER(userID),
  winner boolean
);
''')

# Insert a row into the table
cursor.execute('''INSERT INTO USER (username, password, memberLevel, balance) VALUES ('john', '1234', 'common', 123456);''')
cursor.execute('''INSERT INTO USER (username, password, memberLevel, balance) VALUES ('viel', '5678', 'admin', 12344567);''')

cursor.execute('''INSERT INTO GAME (name) VALUES ('SLOT');''')
cursor.execute('''INSERT INTO GAME (name) VALUES ('BLACKJACK');''')
cursor.execute('''INSERT INTO GAME (name) VALUES ('POKER');''')

cursor.execute('''INSERT INTO TRANSACTION (userID, amount, type) VALUES (1, 10000, 'INCOMING');''')
cursor.execute('''INSERT INTO TRANSACTION (userID, amount, type) VALUES (2, 20000, 'OUTGOING');''')

cursor.execute('''INSERT INTO GAME_REPORT (gameID, userID, winner) VALUES (1, 2, true);''')
cursor.execute('''INSERT INTO GAME_REPORT (gameID, userID, winner) VALUES (1, 1, false);''')


# Commit the changes to the database
connection.commit()

# Close the connection to the database
connection.close()
