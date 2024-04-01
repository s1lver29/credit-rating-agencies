import sqlite3

def create_new_entry(text: str):
    conn = sqlite3.connect('data.db')

    summary = text[:100]
    rating = "Загрузка"

    c = conn.cursor()
    c.execute("INSERT INTO texts (rating, summary, text) VALUES (?, ?, ?)", (rating, summary, text))
    conn.commit()
    conn.close()

def get_list_press_releases():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("SELECT id, summary, rating FROM texts")
    res = c.fetchall()
    conn.close()
    ids = []
    summaries = []
    ratings = []
    for row in res:
        ids.append(row[0])
        summaries.append(row[1])
        ratings.append(row[2])

    res = {
        "ids": ids,
        "summaries": summaries,
        "ratings": ratings
    }

    return res

def get_press_release(id: int):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute("SELECT summary, text FROM texts WHERE id = (?)", id)
    res = c.fetchone()
    conn.close()

    return res