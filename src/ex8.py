import pandas as pd
from pandasql import sqldf

#reading data from CSV files
order_details_df=pd.read_csv(r"D:\data_and_cloud_analytics\tables\order_details.csv")
orders_df=pd.read_csv(r"D:\data_and_cloud_analytics\tables\orders.csv")
pizzas_df=pd.read_csv(r"D:\data_and_cloud_analytics\tables\pizzas.csv")

#converting the date column to datetime format
orders_df['date']=pd.to_datetime(orders_df['date'])

#defining the SQL query for LEFT JOIN
right_join_query="""
                  SELECT DISTINCT p.pizza_id
                  FROM pizzas_df p
                  LEFT JOIN order_details_df od ON p.pizza_id=od.pizza_id
                  LEFT JOIN orders_df o ON od.order_id=o.order_id
                  WHERE o.date NOT LIKE '2015%'
                    OR o.date IS NULL
                  """

#executing the query
right_result=sqldf(right_join_query, locals())

#displaying the result as a DataFrame
right_result
