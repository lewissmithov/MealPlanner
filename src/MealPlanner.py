#!/opt/homebrew/bin/python3
'''
For containing main business logic; not data models
'''
import logging
from models import Meal
from database import DBHandler


def main():
    logging.basicConfig(level=logging.INFO)

    meals = DBHandler.read_all_meals()
    for meal in meals:
        print(f"Meal: {meal}")

    #Add meal
    chatt = Meal(6, 'Sweetcorn Chatt', 4, 1, 1)
    DBHandler.add_meal(chatt)


if __name__ == "__main__":
    main()
