from eating import Cook, Dining
import sys

def main():
    while True:
        try:
            cook_or_dine = input("Cooking or Eating Out? ").lower().strip()
            if cook_or_dine == "cooking":
                cook = Cook()
                protein = cook.user_in()
                recipes = cook.recipes(protein)
                print(cook.pick(recipes))
            elif cook_or_dine == "eating out":
                dining = Dining()
                method = dining.user_in()
                restaurants = dining.restaurants(method)
                print(dining.pick(restaurants))
        except:
            pass
        else:
            done = input('Done? ')
            if done == 'y':
                sys.exit()
    
if __name__ == "__main__":
    main()