
"""Assignment_Prasanna.ipynb"""

import pandas as pd
import numpy as np

df = pd.read_csv('/content/car_price_dataset.csv')
df

"""## 1. What is the average price of all cars in the dataset?"""

avg = df['Price'].mean()
print(f'The average price of all the cars in the dataset is $ {avg}  ')

"""# 2. Which car brand has the highest average price?

"""
avg_price_by_brand = df.groupby('Brand')['Price'].mean()
print(f"The car brand with the highest average price is: {highest_avg_price_brand}")

"""# 3. What is the most common fuel type in the dataset?"""

a = df['Fuel_Type'].mode()[0]
print(f'The most common fuel type is {a}')

"""# 4. How many cars have a mileage greater than 200,000?"""

n = len(df[df['Mileage'] > 200000])
print(f'the number of cars with mileage greater than 200,000 is : {n}  ')

"""# 5. What is the distribution of cars by transmission type?"""

transmission_counts = df.groupby('Transmission')['Transmission'].count()
print(transmission_counts)

"""# 6. Which car model has the highest price?"""

max_price = df['Price'].max()
car_with_max_price = df[df['Price'] == max_price]
car_model = car_with_max_price['Model'].values[0]
print(f"The car model with the highest price is: {car_model}")

"""# 7. What is the average price of cars by fuel type?

"""

avg_price_by_fuel_type = df.groupby('Fuel_Type')['Price'].mean()
print(avg_price_by_fuel_type)

"""# 8. How many cars are from the year 2020 or later?"""

n = df[df['Year']>=2020].shape[0]
print(f'The number of cars form year 2020 and later is {n}')

"""# 9. What is the average engine size for each brand?"""

avg_engine_size_by_brand = df.groupby('Brand')['Engine_Size'].mean()
print(avg_engine_size_by_brand)

"""# 10. Which car has the lowest mileage?"""

df[df["Mileage"] == df["Mileage"].min()]

"""# 11. What is the correlation between mileage and price?"""

correlation = df['Mileage'].corr(df['Price'])
print(f"The correlation between mileage and price is: {correlation}")

"""#12. How many cars have more than 2 owners?

"""

num_cars_more_than_2_owners = len(df[df['Owner_Count'] > 2])
print(f"The number of cars with more than 2 owners is: {num_cars_more_than_2_owners}")

"""# 13. What is the average price of cars by year?

"""

avg_price_by_year = df.groupby('Year')['Price'].mean()
print(avg_price_by_year)

"""#14. Which car has the highest number of doors?

"""

car_with_max_doors = df[df['Doors'] == df['Doors'].max()]
print(car_with_max_doors)

"""#15. What is the average mileage for each fuel type?

"""

avg_mileage_by_fuel_type = df.groupby('Fuel_Type')['Mileage'].mean()
print(avg_mileage_by_fuel_type)

"""#16. How many cars are from the brand 'Toyota'?"""

n =  len(df[df['Brand']=="Toyota"])
print(f'The number of cars from toyota is : {n}')

"""#17. What is the average price of cars with automatic transmission?

"""

automatic_cars = df[df['Transmission'] == 'Automatic']  # Filter for automatic cars
avg_price_automatic = automatic_cars['Price'].mean()     # Calculate average price
print(f"The average price of cars with automatic transmission is: ${avg_price_automatic:.2f}")

"""#18. Which car has the highest owner count?"""

# Assuming the column containing owner count is named 'Owner_Count'
car_with_max_owners = df[df['Owner_Count'] == df['Owner_Count'].max()]
print(car_with_max_owners)

"""#19. What is the average engine size for cars with diesel fuel type?

"""

diesel_cars = df[df['Fuel_Type'] == 'Diesel']
avg_engine_size_diesel = diesel_cars['Engine_Size'].mean()
print(f"The average engine size for cars with diesel fuel type is: {avg_engine_size_diesel:.2f} liters")

"""#20. How many cars have a price greater than $10,000?

"""

num_cars_over_10k = len(df[df['Price'] > 10000])
print(f"The number of cars with a price greater than $10,000 is: {num_cars_over_10k}")

