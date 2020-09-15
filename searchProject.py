import requests

def recipe_search(ingredient):
    app_id = 'de09872f'
    app_key = 'f9b77497acd1fd26cbf5ad7801e47cc4'
    url = 'https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, app_id, app_key)
    result = requests.get(url)
    data = result.json()
    return data["hits"]
def run():
    ingredient = input("Enter an ingredient or multiple ingredients you would like: ")
    calories = input("Would you like to know how many calories are in the recipe? yes/no:  ") #user has the option to see calories for each recipe
    results = recipe_search(ingredient)
    contents = "" #contents of the recipe list file
    calories_list = [] #creating a list for the calories of each recipe to go into
    label_list = [] #creating a list for all the labels of recipes

    with open('recipe.txt', 'w+') as recipe_file: #saves the results of the recipes found
        for response in results:
            recipe = response['recipe']
            label = recipe['label']

            if label not in label_list: #to get rid of any duplicate labels/recipes
                label_list.append(recipe['label'])
                print(label)
                print(recipe['url'])
                print("Weight: " + str(int(recipe['totalWeight'])) + 'g')  # displays the weight of recipe in grams
                calories_list.append(int(recipe['calories'])) # adding the calorie of each recipe to the list

                if calories == 'yes':
                    print("Calories: " + str(int(recipe['calories'])) + ' kcal' + '\n')
                    contents = contents + recipe['label'] + "\n" + recipe['url'] + '\n' + (
                                str(int(recipe['totalWeight'])) + 'g') + '\n' + (
                                           str(int(recipe['calories'])) + ' kcal') + '\n'
                else:
                    print("")
                    contents = contents + recipe['label'] + "\n" + recipe['url'] + '\n' + (
                                str(int(recipe['totalWeight'])) + 'g') + '\n'

        if calories == 'yes':
            print("The sorted list of all the calories from the recipe list: {}".format(sorted(calories_list)))  # printing the list

        recipe_file.write(contents)
run()
