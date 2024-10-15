import pandas as pd
import matplotlib.pyplot as plt

#load the orders CSV into a pandas DataFrame
orders_df=pd.read_csv(r"D:\data_and_cloud_analytics\tables\orders.csv")

#convert the 'time' column to datetime with specified format
orders_df['time']=pd.to_datetime(orders_df['time'], format='%H:%M:%S')


#extract the hour, minute, and second components from the 'time' column
orders_df['hour']=orders_df['time'].dt.hour
orders_df['minute']=orders_df['time'].dt.minute
orders_df['second']=orders_df['time'].dt.second

#group the orders by hour, minute, and second and count the number of orders for each timestamp
order_frequency=orders_df.groupby(['hour', 'minute', 'second']).size()

#plot the order frequency over time
plt.figure(figsize=(12, 6))
order_frequency.plot(kind='line', color='purple')
plt.title('Order Frequency Over Time')
plt.xlabel('Time')
plt.ylabel('Number of Orders')
plt.grid(True)
plt.show()
