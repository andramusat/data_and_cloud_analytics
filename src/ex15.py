import pandas as pd
import matplotlib.pyplot as plt

#load the orders CSV into a pandas DataFrame
orders_df=pd.read_csv(r"D:\data_and_cloud_analytics\tables\orders.csv")

#convert the 'date' column to datetime format
orders_df['date']=pd.to_datetime(orders_df['date'])

#extract the day of the week from the 'date' column
orders_df['day_of_week']=orders_df['date'].dt.day_name()

#group the orders by the day of the week and count the number of orders for each day
orders_by_day=orders_df.groupby('day_of_week').size()

#plot the order frequency for each day of the week
plt.figure(figsize=(10, 6))
orders_by_day.plot(kind='bar', color='purple')
plt.title('Order Frequency by Day of the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Number of Orders')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()
