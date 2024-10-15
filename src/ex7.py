import pandas as pd

#load the order details CSV file into a pandas DataFrame
order_details_df=pd.read_csv(r"D:\data_and_cloud_analytics\tables\order_details.csv")

#group by pizza_id and sum the quantities to get the total quantity of each pizza ordered
pizza_orders=order_details_df.groupby('pizza_id')['quantity'].sum().reset_index()

#sort the pizzas by total quantity in descending order and select the top 5
top_5_pizzas=pizza_orders.sort_values(by='quantity', ascending=False).head(5)

#display the top 5 most ordered pizzas as a table
top_5_pizzas
