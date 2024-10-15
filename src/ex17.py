import pandas as pd
from pandasql import sqldf

#load the CSV files into pandas DataFrames
pizzas_df=pd.read_csv(r"D:\data_and_cloud_analytics\tables\pizzas.csv")
orders_df=pd.read_csv(r"D:\data_and_cloud_analytics\tables\orders.csv")
order_details_df=pd.read_csv(r"D:\data_and_cloud_analytics\tables\order_details.csv")

#convert the 'date' column to datetime
orders_df['date']=pd.to_datetime(orders_df['date'], format='%m/%d/%Y')

#create a DataFrame with a full range of dates in 2015
full_date_range=pd.date_range(start='2015-01-01', end='2015-12-31')
full_date_df=pd.DataFrame(full_date_range, columns=['date'])

#define the SQL queries to join the tables and calculate daily revenue
query="""
        SELECT fd.date, COALESCE(SUM(od.quantity*p.price), 0) AS daily_revenue
        FROM full_date_df fd
        LEFT JOIN orders_df o ON fd.date=o.date
        LEFT JOIN order_details_df od ON o.order_id=od.order_id
        LEFT JOIN pizzas_df p ON od.pizza_id=p.pizza_id
        GROUP BY fd.date
        """

#execute the query using pandasql
full_revenue_df=sqldf(query, globals())

#identify the dates with no sales (daily_revenue is 0)
no_sales_dates=full_revenue_df[full_revenue_df['daily_revenue']==0]

#display the periods with no pizza sales 
print("Periods with no pizza sales:")
no_sales_dates


