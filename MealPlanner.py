#!/opt/homebrew/bin/python3
import csv
import sqlite3
import logging


def hello_world():
    return "Hello World"


def read_meal_data(healh_score=0, keto_potential=0, gf_potential=0):
    """
    Docstring: This is a method to read the meal data from
    the sqlite db and store it in a dict

    Returns in scope meals as dict or meal class
    """
    meals = {}

    query = (
        f"select * from meals " \
        f"where healthScore > {healh_score} " \
        f"and ketoPotential = {keto_potential} " \
        f"and gfPotential = {gf_potential} "
    )

    logging.debug(query)

    con = sqlite3.connect("meals.db")
    cur = con.cursor()
    cur.execute(query)

    return cur.fetchall()
    
    return meals


def main():
    logging.basicConfig(level=logging.INFO)

    data = read_meal_data(gf_potential=1)
    print(data)


if __name__ == "__main__":
    main()