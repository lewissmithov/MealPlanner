#!/opt/homebrew/bin/python3
'''
For containing main business logic; not data models
'''
import logging
from models import Meal
from database import DBHandler


def main():
    logging.basicConfig(level=logging.INFO)

    data = DBHandler.read_meal_data(1,2,3)
    print(data)


if __name__ == "__main__":
    main()
