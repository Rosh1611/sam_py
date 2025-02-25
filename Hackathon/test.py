import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data=pd.read_csv("Food_wastage_data.csv")
meal_prepared=data["Meal Prepared"]
food_wasted=data["Food Wasted (kg)"]
meal_category=data["Meal Type"]
food_wastage_percentage=["Percentage Wasted (%)"]
"""
plt.figure()
plt.bar(meal_prepared,food_wasted)
plt.xlabel("Meal")
plt.xticks(rotation=45, fontsize=10)
plt.ylabel("Food Wasted [kg]")
plt.show()
"""
"""
grouped_data = data.groupby("Meal Type")["Food Wasted (kg)"].sum()
plt.figure()
plt.pie(grouped_data,labels=grouped_data.index,autopct="%3.2f%%")
plt.axis()
plt.show()
"""
cuisine_waste = data.groupby("Type of Cuisine")["Food Wasted (kg)"].sum().reset_index()


cuisine_waste_pivot = cuisine_waste.set_index("Type of Cuisine")


plt.figure(figsize=(10, 6))
sns.heatmap(cuisine_waste_pivot, annot=True, cmap="Reds", linewidths=0.5)


plt.title("Heatmap of Food Wastage by Type of Cuisine")
plt.ylabel("Type of Cuisine")
plt.yticks( fontsize=8)
plt.show()