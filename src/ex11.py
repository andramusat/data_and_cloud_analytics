import pandas as pd
from pandasql import sqldf

# Load the CSV files into pandas DataFrames
pizzas_df=pd.read_csv(r"D:\data_and_cloud_analytics\tables\pizzas.csv")
orders_df=pd.read_csv(r"D:\data_and_cloud_analytics\tables\orders.csv")
order_details_df=pd.read_csv(r"D:\data_and_cloud_analytics\tables\order_details.csv")

#converting the date column to datetime format
orders_df['date']=pd.to_datetime(orders_df['date'])

#define the SQL query to join the tables and filter transactions in 2015
query = """
        SELECT COALESCE(ROUND(SUM(od.quantity*p.price)), 0) AS total_revenue_2015
        FROM pizzas_df p
        LEFT JOIN order_details_df od ON p.pizza_id=od.pizza_id
        LEFT JOIN orders_df o ON od.order_id=o.order_id
        WHERE o.date LIKE '2015%'
        """

#execute the query using pandasql
result=sqldf(query, locals())

#print the total revenue generated in 2015
print("Total revenue generated in 2015:", result['total_revenue_2015'].values[0])
