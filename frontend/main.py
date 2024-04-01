import streamlit as st
import sqlite3

conn = sqlite3.connect('data.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS texts
             (id INTEGER PRIMARY KEY,
              rating VARCHAR(30),
              summary VARCHAR(100),
              text TEXT)''')
conn.commit()
conn.close()


def main():
    pass

if __name__ == "__main__":
    pass