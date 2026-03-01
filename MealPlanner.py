#!/usr/bin/python
import csv

#Read meal data
with open('meal_data.csv', newline='') as csv_file:
    csv_reader = csv.reader(csv_file)
    line_count = 0

    meals = {}
    
    for row in csv_reader:
        if line_count == 0:
            header = row
            line_count += 1
        else:
            meals[row[0]] = row[1:]
            
    print(meals['Chinese Tofu'])

#1: Text Too small
#2: Struggling with the most basic syntax
#3: Struggling with the IDE
#4: Let's remember what we're trying to do
    #5: Might do maybe? Building a REST API with Python 3
