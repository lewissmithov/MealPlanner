#!/opt/homebrew/bin/python3
import csv


def hello_world():
    return "Hello World"


def read_meal_data():
    """
    Docstring: This is a method to read the meal data from a csv
    
    Returns: 
        dict: meals
    """
    meals = {}

    with open('meal_data.csv', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file) #Todo: Change to dict reader
        line_count = 0

        
        for row in csv_reader:
            if line_count == 0:
                header = row
                line_count += 1
            else:
                meals[row[0]] = row[1:]

    return meals


def main():
    data = read_meal_data()
    print(data)


if __name__ == "__main__":
    main()