import sqlite3


class PointAnalysis:
    def __init__(self):
        self.average = 0
        self.max = 0

    def open(self):
        self.bd = sqlite3.connect("baza_dan.db")
        self.cur = self.bd.cursor()

    def max_score(self):
        req = 'SELECT MAX(points) FROM all_point'
        result = self.bd.execute(req)
        return result.fetchone()[0]

    def min_score(self):
        req = 'SELECT MIN(points) FROM all_point'
        result = self.bd.execute(req)
        return result.fetchone()[0]

    def averages_score(self):
        req = 'select avg(points) from all_point'
        result = self.bd.execute(req)
        return result.fetchone()[0]

    def recording_score(self, points):
        req = f"""INSERT INTO all_point(points) VALUES({points})"""
        self.bd.execute(req)

    def close(self):
        self.bd.commit()
        self.bd.close()