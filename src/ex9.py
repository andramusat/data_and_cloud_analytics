import pandas as pd

#read the pizzas CSV file into a DataFrame
pizzas_df = pd.read_csv(r"D:\data_and_cloud_analytics\tables\pizzas.csv")

#define a function to categorize the sizes
def categorize_size(size):
    if 's' in size.lower():
        return 'Small'
    elif 'm' in size.lower():
        return 'Medium'
    elif 'l' in size.lower():
        return 'Large'
    else:
        return 'Unknown'

#apply the function to create a new column 'size_category'
pizzas_df['size_category']=pizzas_df['size'].apply(categorize_size)

#group the pizzas by 'size_category' and calculate summary statistics for 'price'
summary_statistics=pizzas_df.groupby('size_category')['price'].agg(['mean', 'min', 'max'])

#display the summary statistics table
summary_statistics
