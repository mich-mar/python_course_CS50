nutritionFacts = {"Apple" : 130,
                  "Banana" : 110,
                  "Avocado" : 50,
                  "Cantaloupe" : 50,
                  "Grapefruit" : 60,
                  "Grapes" : 90,
                  "Honeydew Melon" : 50,
                  "Kiwifruit" : 90,
                  "Lemon" : 20,
                  "Lime" : 20,
                  "Nectarine" : 60,
                  "Orange" : 80,
                  "Peach" : 60,
                  "Pineapple" : 50,
                  "Plums" : 70,
                  "Strawberries" : 50,
                  "Sweet Cherries" : 100,
                  "Tangerine" : 50,
                  "Watermelon" : 80}

def main():
    fruit = input("Item: ")
    fruit = fruit.lower().title()
    
    if fruit in nutritionFacts:
        calories = nutritionFacts[fruit]
        print("Calories:", nutritionFacts[fruit])

main()