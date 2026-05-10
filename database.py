#!/opt/homebrew/bin/python3
"""
Database module for MealPlanner.

Handles all database operations including reading meal data
with various filtering options.
"""

import sqlite3
import logging

from models import Meal

class DBHandler():
        
    def read_meals(healh_score=None, keto_potential=None, gf_potential=None):
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


    def read_all_meals() -> list[Meal]:
        """
        Docstring: This is a method to read all meal data from
        the sqlite db and return it as a list of Meal objects.
        """
        query = "select * from meals"

        con = sqlite3.connect("meals.db")
        cur = con.cursor()
        cur.execute(query)
        
        meals = []
        
        results = cur.fetchall() #list of tuples
        for meal in results:
            meals.append(Meal(*meal))

        
        return meals