import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv("Food_wastage_data.csv")
meal_prepared=data["Meal Prepared"]
food_wasted=data["Food Wasted (kg)"]
plt.figure()
plt.bar(meal_prepared,food_wasted)
plt.xlabel("Meal")
plt.xticks(rotation=45, fontsize=10)
plt.ylabel("Food Wasted [kg]")
plt.show()

cuisine_waste = data.groupby("Type of Cuisine")["Food Wasted (kg)"].sum()
plt.figure()
plt.pie(cuisine_waste,labels=cuisine_waste.index,autopct="%3.2f%%")
plt.title("Food Wastage by Type of Cuisine")
plt.axis()
plt.show()

column_name = "Food Wasted (kg)" 
meal_waste = data.groupby("Meal Type")[column_name].sum().reset_index()

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection="3d")

x_pos = np.arange(len(meal_waste))
y_pos = np.zeros(len(meal_waste)) 
z_pos = np.zeros(len(meal_waste)) 

dx = np.ones(len(meal_waste)) * 0.5  
dy = np.ones(len(meal_waste)) * 0.5 
dz = meal_waste[column_name]  

colors = ["red", "blue", "green"] 

ax.bar3d(x_pos, y_pos, z_pos, dx, dy, dz, color=colors, alpha=0.8)

ax.set_xlabel("Meal Type")
ax.set_ylabel(" ")
ax.set_zlabel("Food Wasted (kg)")
ax.set_title("Food Wastage by Meal Category")
ax.set_xticks(x_pos)
ax.set_xticklabels(meal_waste["Meal Type"])
plt.show()