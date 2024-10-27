# test_script.py
import sys
import sqlite3
from fuzzywuzzy import fuzz

recipes_db_file = 'db.sqlite3'
# Simulate reading an ingredient passed as an argument (like a POST parameter)
ingredient = sys.argv[1]
ingredient = ingredient.strip()



def find_best_match(ingredient, database):
    best_match = None
    highest_ratio = 0
    for db_ingredient in database:
        ratio = fuzz.ratio(ingredient.lower(), db_ingredient.lower())
        if ratio > highest_ratio:
            highest_ratio = ratio
            best_match = db_ingredient
    return best_match, highest_ratio

conn = sqlite3.connect(recipes_db_file)
cursor = conn.cursor()

# Read the ingredient database
cursor.execute("SELECT Ingredient FROM ingredient_database")
existing_ingredients = [row[0] for row in cursor.fetchall()]

if ingredient:
    best_match, match_ratio = find_best_match(ingredient, existing_ingredients)


cursor.execute(
    "SELECT Alternative1, Alternative2, Alternative3, Alternative4, Alternative5 FROM ingredient_database WHERE Ingredient = ?",
    (best_match,)
)
ingredients = cursor.fetchall()


for alternative in ingredients[0]:
    print(alternative)
conn.close()