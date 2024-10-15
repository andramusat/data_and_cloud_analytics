import pandas as pd
import matplotlib.pyplot as plt

#load the pizzas CSV file into a pandas DataFrame
pizzas_df = pd.read_csv(r"D:\data_and_cloud_analytics\tables\pizzas.csv")

#plot the distribution of prices using a histogram
plt.figure(figsize=(10, 6))
plt.hist(pizzas_df['price'], bins=20, color='purple', edgecolor='black')
plt.title('Distribution of Pizza Prices')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
