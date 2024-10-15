import pandas as pd

#load the orders CSV into a pandas DataFrame
orders_df=pd.read_csv(r"D:\data_and_cloud_analytics\tables\orders.csv")

#extract the date component from the 'date' column
orders_df['date']=pd.to_datetime(orders_df['date'])

#group the orders by date and count the number of orders for each date
daily_orders=orders_df.groupby(orders_df['date'].dt.date).size()

#calculate the average number of orders per day
average_orders_per_day=round(daily_orders.mean())

print("Average orders per day:", average_orders_per_day)
