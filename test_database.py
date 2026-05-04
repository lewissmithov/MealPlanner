#!/opt/homebrew/bin/python3
import pytest
from database import DBHandler 


def test_return_meals_with_keto_and_gf_potential():
    results = DBHandler.read_meal_data(0, 1, 1)

    ids = [row[0] for row in results]
    assert set(ids) == {2, 5}
    # Assert ids 2 and 5 are returned


def test_return_meals_with_healthscore_more_than_three():
    results = DBHandler.read_meal_data(3)

    ids = [row[0] for row in results]
    assert set(ids) == {2, 5}


def test_return_meals_with_keto_potential():
    results = DBHandler.read_meal_data(keto_potential=1)
    ids = [row[0] for row in results]
    assert set(ids) == {2, 5}


def test_return_all_meals():
    results = DBHandler.read_meal_data()
    ids = [row[0] for row in results]
    assert set(ids) == {1, 2, 3, 4, 5}


def test_assert_wrong_number_of_parameters():
    with pytest.raises(TypeError):
        results = DBHandler.read_meal_data(1,2,3,4)
        



#DONE: Return meals with keto potential
#TODO: further pytest learning
#TODO: Write MVP for this project, timebound it
#TODO: Add a new meal 
#TODO: Add filtering on healthscore, ketopotential and gf potential
