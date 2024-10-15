import pandas as pd

#load the CSV file specifying the encoding(specifying the encoding parameter
#when reading the CSV file helps Pandas interpret the file's contents correctly, 
#especially when dealing with characters that fall outside the standard ASCII range.)
df=pd.read_csv(r"D:\data_and_cloud_analytics\tables\pizza_types.csv", encoding='latin1')

#initialize a dictionary to count ingredient occurrences
ingredient_counts={}

#iterate over each row in the DataFrame and parse the ingredients
for ingredients_str in df['ingredients']:
    ingredients=ingredients_str.split(", ")
    for ingredient in ingredients:
        if ingredient in ingredient_counts:
            ingredient_counts[ingredient]+=1
        else:
            ingredient_counts[ingredient]=1

#find the ingredient with the highest occurrence count
most_used_ingredient=max(ingredient_counts, key=ingredient_counts.get)
frequency_of_most_used_ingredient=ingredient_counts[most_used_ingredient]

print("The most used ingredient is:", most_used_ingredient)
print("It appears", frequency_of_most_used_ingredient, "times.")
