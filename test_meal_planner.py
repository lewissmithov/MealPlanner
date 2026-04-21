#!/opt/homebrew/bin/python3
import pytest
from MealPlanner import hello_world, read_meal_data


def test_return_meals_with_keto_and_gf_potential():
    results = read_meal_data(0, 1, 1)

    ids = [row[0] for row in results]
    assert set(ids) == {2, 5}
    # Assert ids 2 and 5 are returned


def test_return_meals_with_healthscore_more_than_three():
    results = read_meal_data(3)

    ids = [row[0] for row in results]
    assert set(ids) == {2, 5}


#TODO: Return meals with a healthscore > x
#TODO: pytest learning
#TODO: Return meals with keto potential
#TODO: Add a new meal 
#TODO: Add filtering on healthscore, ketopotential and gf potential
