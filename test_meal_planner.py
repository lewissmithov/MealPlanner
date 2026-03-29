#!/opt/homebrew/bin/python3
import pytest
from MealPlanner import hello_world, read_meal_data


def test_hello_world():
    assert hello_world() == "Hello World"

def test_one_equals_one():
    assert 1 == 1


def test_return_meals_with_keto_and_gf_potential():
    results = read_meal_data(0, 1, 1)

    ids = [row[0] for row in results]
    assert set(ids) == {2, 5}
    # Assert ids 2 and 5 are returned

#TODO: Return meals with a healthscore > x
#TODO: Return meals with keto potential
#TODO: Add a new meal 
#TODO: Add filtering on healthscore, ketopotential and gf potential
