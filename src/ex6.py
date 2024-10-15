import pandas as pd

#load the CSV file into a pandas DataFrame
pizzas_df=pd.read_csv(r"D:\data_and_cloud_analytics\tables\pizzas.csv")

#group by pizza_type_id and size, then count the number of pizzas sold for each group
sales_summary=pizzas_df.groupby(['pizza_type_id', 'size']).size().reset_index(name='sold_quantity')

#display the sales summary DataFrame as a table
sales_summary
