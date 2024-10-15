import pandas as pd
import matplotlib.pyplot as plt
from pandasql import sqldf

#load the CSV files into pandas DataFrames
pizzas_df=pd.read_csv(r"D:\data_and_cloud_analytics\tables\pizzas.csv")
orders_df=pd.read_csv(r"D:\data_and_cloud_analytics\tables\orders.csv")
order_details_df=pd.read_csv(r"D:\data_and_cloud_analytics\tables\order_details.csv")

#converting the date column to datetime format
orders_df['date']=pd.to_datetime(orders_df['date'])

#define the SQL query to join the tables and filter transactions in 2015, grouped by month
query = """
      SELECT SUBSTR(o.date, INSTR(o.date, '/')+1) AS month,
            COALESCE(SUM(od.quantity*p.price), 0) AS revenue
      FROM pizzas_df p
      LEFT JOIN order_details_df od ON p.pizza_id=od.pizza_id
      LEFT JOIN orders_df o ON od.order_id=o.order_id
      WHERE o.date LIKE '2015%'
      GROUP BY month
      """

#execute the query using pandasql
result=sqldf(query, locals())

#plot the revenue for each month
plt.figure(figsize=(10, 6))
plt.bar(result['month'], result['revenue'], color='purple')
plt.xlabel('Month')
plt.ylabel('Revenue')
plt.title('Revenue Generated Each Month in 2015')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()