import requests
import pprint
pp = pprint.PrettyPrinter(indent=2)

def recipe_search(ingredient1):
    app_id = "331a1591"
    app_key = "4209e7a5dee1b6da8c8ee6ffdcfda65c"
    url1 = "https://api.edamam.com/search?q={}&app_id={}&app_key={}".format(ingredient1, app_id, app_key)
    response = requests.get(url1)
    data = response.json()
    return data['hits']

def create_sorted_list():
    ingredient1 = input("Enter an ingredient or multiple ingredients you would like: ")
    results = recipe_search(ingredient1)
    names_included = [results[0]['recipe']['label']]
    names_list = [] #the list for all three details
    all_cals = []

    for item in results:
        name = (item['recipe']['label']) # if its not already in there add it

        if name not in names_included: #only looking at names not already considered(gets rid of duplicates
            names_included.append(name) #then include the label
            url = (item['recipe']['url'])
            name = (item['recipe']['label'])
            cal = int((item['recipe']['calories']))
            payload = [cal, url]
            combined = [name, payload] #combining all three things
            names_list.append(combined) #adding the new combination for every iteration
            all_cals.append(cal) #adding to the list of all calories

    all_cals.sort() #sorted the list of calories

    sorted_recipes = [] #creates a list for sorted recipes to be stored in
    for cal_target in all_cals:
        for name in names_list:
            if cal_target == name[1][0]: #if the all cals list matches the first item in each list(calories), then add it to the sorted list
                sorted_recipes.append(name)#adds each combination in sorted list

    return sorted_recipes


x = create_sorted_list()
pp.pprint(x)

with open('recipes.txt', 'w+') as f:
    f.write(str(x))

