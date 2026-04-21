#!/opt/homebrew/bin/python3
import csv
import sqlite3
import logging


def hello_world():
    return "Hello World"


class DBHandler():
        
    def read_meal_data(healh_score=None, keto_potential=None, gf_potential=None):
        """
        Docstring: This is a method to read the meal data from
        the sqlite db and store it in a dict

        Returns in scope meals as dict or meal class
        """
        conditions = []

        if healh_score is not None:
            conditions.append(f"healthScore > {healh_score} ")
        if keto_potential is not None:
            conditions.append(f"ketoPotential = {keto_potential} ")
        if gf_potential is not None:
            conditions.append(f"gfPotential = {gf_potential} ")
        
        where_clause = " and ".join(conditions) if conditions else "1=1"
        query = f"select * from meals where {where_clause}"

        logging.debug(query)

        con = sqlite3.connect("meals.db")
        cur = con.cursor()
        cur.execute(query)

        return cur.fetchall()


class RecipeBook():
    None

    

def main():
    logging.basicConfig(level=logging.INFO)

    data = DBHandler.read_meal_data(1,2,3,4)
    print(data)


if __name__ == "__main__":
    main()
