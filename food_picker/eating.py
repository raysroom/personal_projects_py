import random
import pandas as pd

class Cook:
    recipes_sheet_id = "14ORhyWYRBDYt5nDCLTnLAZJ_mDeA3N0SFN9hJBxDbjI"

    protein_list = ["chicken", "beef", "pork", "other"]
    def user_in(self):
        while True:
            try:
                protein = (
                    input(f"What protein would you like?\n {self.protein_list}\n")
                    .lower()
                    .strip()
                )
                if protein in self.protein_list:
                    return protein
            except protein != any(protein for protein in self.protein_list):
                pass

    def recipes(self,protein):

        if protein == "chicken":
            chicken_sheet = f"https://docs.google.com/spreadsheets/d/{self.recipes_sheet_id}/gviz/tq?tqx=out:csv&sheet={protein}"

            chicken_df = pd.read_csv(chicken_sheet, usecols=["Recipes"])

            chicken_recipes = chicken_df["Recipes"].tolist()

            return chicken_recipes
        elif protein == "beef":
            beef_sheet = f"https://docs.google.com/spreadsheets/d/{self.recipes_sheet_id}/gviz/tq?tqx=out:csv&sheet={protein}"

            beef_df = pd.read_csv(beef_sheet, usecols=["Recipes"])

            beef_recipes = beef_df["Recipes"].tolist()

            return beef_recipes
        elif protein == "pork":
            pork_sheet = f"https://docs.google.com/spreadsheets/d/{self.recipes_sheet_id}/gviz/tq?tqx=out:csv&sheet={protein}"

            pork_df = pd.read_csv(pork_sheet, usecols=["Recipes"])

            pork_recipes = pork_df["Recipes"].tolist()

            return pork_recipes
        elif protein == "other":
            other_sheet = f"https://docs.google.com/spreadsheets/d/{self.recipes_sheet_id}/gviz/tq?tqx=out:csv&sheet={protein}"

            other_df = pd.read_csv(other_sheet, usecols=["Recipes"])

            other_recipes = other_df["Recipes"].tolist()
            return other_recipes
    
    def pick(self, recipes):
        randomize = input("Randomize? y/n ").lower().strip()
        if randomize == "y":
            return ("- " + "\n- ".join(random.sample(recipes, 3)))
        else:
            for recipe in recipes:
                return (f"- {recipe}")
            
class Dining:
    dining_list = ["sit down", "fast food", "fancy"]
    food_sheet_id = "14ORhyWYRBDYt5nDCLTnLAZJ_mDeA3N0SFN9hJBxDbjI"

    def user_in(self):
        while True:
            try:
                dining = input(f"Where to?\n{self.dining_list}\n").lower().strip()
                if dining in self.dining_list:
                    return dining
            except:
                pass

    def restaurants(self, dining):
    
        if dining == "sit down":
            sit_down_sheet = f"https://docs.google.com/spreadsheets/d/{self.food_sheet_id}/gviz/tq?tqx=out:csv&sheet=sit-down"

            sit_down_df = pd.read_csv(sit_down_sheet, usecols=["Restaurants"])

            sit_down_restaurants = sit_down_df["Restaurants"].tolist()

            return sit_down_restaurants
        
        elif dining == "fast food":
            fast_food_sheet = f"https://docs.google.com/spreadsheets/d/{self.food_sheet_id}/gviz/tq?tqx=out:csv&sheet=fast-food"

            fast_food_df = pd.read_csv(fast_food_sheet, usecols=["Restaurants"])

            fast_food_restaurants = fast_food_df["Restaurants"].tolist()

            return fast_food_restaurants
        
        elif dining == "fancy":
            fancy_sheet = f"https://docs.google.com/spreadsheets/d/{self.food_sheet_id}/gviz/tq?tqx=out:csv&sheet={dining}"

            fancy_df = pd.read_csv(fancy_sheet, usecols=["Restaurants"])

            fancy_restaurants = fancy_df["Restaurants"].tolist()

            return fancy_restaurants

    def pick(self, restaurants):
        randomize = input("Randomize? y/n ").lower().strip()
        if randomize == "y":
            return ("- " + "\n- ".join(random.sample(restaurants, 3)))
        else:
            for restaurant in restaurants:
                return (f"- {restaurant}")