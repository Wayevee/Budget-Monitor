import os


from deta import Deta
from dotenv import load_dotenv


DETA_KEY = "a06ltofuwbp_TaQN3gSrSALx9CEfDzvgtREA236bLXWH"


deta = Deta(DETA_KEY)

db = deta.Base("monthly_reports")
db2 = deta.Base("users_db")


def insert_period (period, incomes, expenses, comment):
    """Returns the report on a successful creation, otherwise raises an error"""
    return db.put ({"key": period, "incomes": incomes, "expenses": expenses, "comment": comment})


def fetch_all_periods():
    """Returns a dict of all periods"""
    res = db.fetch()
    return res.items


def get_period(period):
        """if not found the function will return home"""
        return db.get(period)

def insert_user(username,name,password):
    """ Retruns the user on a successful ser creation, otherwise raises an errror"""
    return db2.put({"key": username, "name": name, "password": password})