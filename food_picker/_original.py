import sys
import random
import pandas as pd

# Goals
"""
Create GUI for program
    -Use beyond the terminal
    -Consider Web App or App
Create Class(es) to clean up program - DONE

Features to Add:
    Create Running Grocery List
        -Prompt User if recipe / dinner should be based on what is available to User
            -If so, take into account what is in the fridge/pantry
            -If not, randomize as normal, assume user will shop for groceries
                -in this case allow user to input groceries to be added/removed from running list / csv file
    

"""

def cook():
    # create google sheets links
    google_sheets = True
    if google_sheets:
        recipes_sheet_id = "14ORhyWYRBDYt5nDCLTnLAZJ_mDeA3N0SFN9hJBxDbjI"

        chicken_id = "chicken"
        beef_id = "beef"
        pork_id = "pork"
        other_id = "other"

        chicken_sheet = f"https://docs.google.com/spreadsheets/d/{recipes_sheet_id}/gviz/tq?tqx=out:csv&sheet={chicken_id}"
        beef_sheet = f"https://docs.google.com/spreadsheets/d/{recipes_sheet_id}/gviz/tq?tqx=out:csv&sheet={beef_id}"
        pork_sheet = f"https://docs.google.com/spreadsheets/d/{recipes_sheet_id}/gviz/tq?tqx=out:csv&sheet={pork_id}"
        other_sheet = f"https://docs.google.com/spreadsheets/d/{recipes_sheet_id}/gviz/tq?tqx=out:csv&sheet={other_id}"

        chicken_df = pd.read_csv(chicken_sheet, usecols=["Recipes"])
        beef_df = pd.read_csv(beef_sheet, usecols=["Recipes"])
        pork_df = pd.read_csv(pork_sheet, usecols=["Recipes"])
        other_df = pd.read_csv(other_sheet, usecols=["Recipes"])

        chicken_recipes = chicken_df["Recipes"].tolist()
        beef_recipes = beef_df["Recipes"].tolist()
        pork_recipes = pork_df["Recipes"].tolist()
        other_recipes = other_df["Recipes"].tolist()

    else:  # create using lists in file folder
        chicken_recipes = open("recipes/chicken_recipes.txt").readlines()
        beef_recipes = open("recipes/beef_recipes.txt").readlines()
        pork_recipes = open("recipes/pork_recipes.txt").readlines()
        other_recipes = open("recipes/other_recipes.txt").readlines()

    # list out proteins
    protein_list = ["chicken", "beef", "pork", "other"]

    # ask user which protein they want
    while True:
        try:
            user_input = (
                input(f"What protein would you like?\n {protein_list}\n")
                .lower()
                .strip()
            )

        except user_input != any(protein for protein in protein_list):
            pass

        if user_input == "chicken":
            randomize = input("Randomize? y/n ").lower().strip()
            if randomize == "y":
                return print("- " + "\n- ".join(random.sample(chicken_recipes, 3)))
            else:
                for recipe in chicken_recipes:
                    print(f"- {recipe}")
                return
        elif user_input == "beef":
            randomize = input("Randomize? y/n ").lower().strip()
            if randomize == "y":
                return print("- " + "\n- ".join(random.sample(beef_recipes, 3)))
            else:
                for recipe in beef_recipes:
                    print(f"- {recipe}")
                return
        elif user_input == "pork":
            randomize = input("Randomize? y/n ").lower().strip()
            if randomize == "y":
                return print("- " + "\n- ".join(random.sample(pork_recipes, 3)))
            else:
                for recipe in pork_recipes:
                    print(f"- {recipe}")
                return
        elif user_input == "other":
            randomize = input("Randomize? y/n ").lower().strip()
            if randomize == "y":
                return print("- " + "\n- ".join(random.sample(other_recipes, 3)))
            else:
                for recipe in other_recipes:
                    print(f"- {recipe}")
                return

def eat_out():
    google_sheets = True
    if google_sheets:
        food_sheet_id = "14ORhyWYRBDYt5nDCLTnLAZJ_mDeA3N0SFN9hJBxDbjI"

        sit_down_id = "sit-down"
        fast_food_id = "fast-food"
        fancy_id = "fancy"

        sit_down_sheet = f"https://docs.google.com/spreadsheets/d/{food_sheet_id}/gviz/tq?tqx=out:csv&sheet={sit_down_id}"
        fast_food_sheet = f"https://docs.google.com/spreadsheets/d/{food_sheet_id}/gviz/tq?tqx=out:csv&sheet={fast_food_id}"
        fancy_sheet = f"https://docs.google.com/spreadsheets/d/{food_sheet_id}/gviz/tq?tqx=out:csv&sheet={fancy_id}"

        sit_down_df = pd.read_csv(sit_down_sheet, usecols=["Restaurants"])
        fast_food_df = pd.read_csv(fast_food_sheet, usecols=["Restaurants"])
        fancy_df = pd.read_csv(fancy_sheet, usecols=["Restaurants"])
        # in brackets is the column name
        sit_down_restaurants = sit_down_df["Restaurants"].tolist()
        fast_food_restaurants = fast_food_df["Restaurants"].tolist()
        fancy_restaurants = fancy_df["Restaurants"].tolist()
    else:
        return

    eat_out_list = ["sit down", "fast food", "fancy"]
    while True:
        try:
            user_input = input(f"Where to?\n{eat_out_list}\n").lower().strip()
        except:
            pass
        if user_input == "sit down":
            randomize = input("Randomize? y/n ").lower().strip()
            if randomize == "y":
                # the string below functions as separator
                return print("- " + "\n- ".join(random.sample(sit_down_restaurants, 3)))
            else:
                for restaurant in sit_down_restaurants:
                    print(f"- {restaurant}")
                return
        elif user_input == "fast food":
            randomize = input("Randomize? y/n ").lower().strip()
            if randomize == "y":
                return print(
                    "- " + "\n- ".join(random.sample(fast_food_restaurants, 3))
                )
            else:
                for restaurant in fast_food_restaurants:
                    print(f"- {restaurant}")
                return
        elif user_input == "fancy":
            randomize = input("Randomize? y/n ").lower().strip()
            if randomize == "y":
                return print("- " + "\n- ".join(random.sample(fancy_restaurants, 3)))
            else:
                for restaurant in fancy_restaurants:
                    print(f"- {restaurant}")
                return

def done():
    done = input('Done? ')
    if done == 'y':
        sys.exit()
    else:
        return

def main():
    while True:
        try:
            cook_eatout = (
                int(input("Cooking or Eating Out?\nChoose 1 or 2: ").lower().strip())
            )
            if cook_eatout == 1:
                cook()
            elif cook_eatout == 2:
                eat_out()
        except:
            pass
        else:
            done()
        
if __name__ == "__main__":
    main()