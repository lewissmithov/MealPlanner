# Mark down file for my meal planner
cuetsmakedinner.com

You can have the week schedule where meals are dragged and dropped in to the slots (i.e. Monday lunch). Can use Warp for this.

Output would produce a list of ingredients required for the shop.

Actions List:
    DONE: Containerize app using Podman
    DONE: Create a Meal class that maps to your database records (this gives a clean python representation of my data model)
    TODO: Add a test for DBHandler.read_all_meals()
    TODO: modify DBHandler.read_meals() to return Meal objects instead of raw tuples
    TOOD: Create a Function to add meals to the catelog. 