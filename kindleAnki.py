import sqlite3
path = r"C:\Users\deone\OneDrive\Documents\KindleAnki1.db"
con = sqlite3.connect(path)
cur = con.cursor()


myList = cur.execute("SELECT word FROM WORDS WHERE lang = 'fr' ").fetchall()

for i in range(len(myList)):
    print(myList[i]) 





