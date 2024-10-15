import pandas as pd

#load the CSV file into a DataFrame
df=pd.read_csv(r"D:\data_and_cloud_analytics\tables\pizza_types.csv", encoding='latin1')

#initialize a set to store unique types of cheese
cheese_types=set()

#function to split ingredients by both commas and semicolons
def split_ingredients(ingredients_str):
    return [item.strip() for item in ingredients_str.replace(';', ',').split(',')]

#iterate over each row in the DataFrame and parse the ingredients
for ingredients_str in df['ingredients']:
    ingredients=split_ingredients(ingredients_str)
    for ingredient in ingredients:
        if "cheese" in ingredient.lower():  #check if the word 'cheese' is in the ingredient
            cheese_types.add(ingredient.strip())

#convert the set of unique cheeses to a sorted list
unique_cheeses=sorted(cheese_types)

# Print the results
print(f"The restaurant uses {len(unique_cheeses)} types of cheese.")
print("\nThe types of cheese used are:")
for cheese in unique_cheeses:
    print(cheese)

#create a DataFrame with an ID column and a Cheese column
cheese_df=pd.DataFrame({'ID': range(1, len(unique_cheeses)+1), 'Cheese': unique_cheeses})

#print the DataFrame with a title
print("\nList of cheese types used by the restaurant Luigi’s Pizza")
cheese_df