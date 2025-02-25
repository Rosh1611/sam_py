from multipledispatch import dispatch

@dispatch(str,float,float,int,float)
#To Print The Row With Prices
def pretty_print(s1,f2,f3,i4,f5):
    print(f"|{s1:^20}|{f"{f2:05.2f}":^20}|{f"{f3:09.2f}":^20}|{f"{i4:03d}":^20}|{f"{f5:0.2f}":^20}|")
    #print(('|'+'{}'.center(15)+'|'+'{:04.2f}'.center(20)+'|'+'{:08.2f}'.center(20)+'|'+'{:06.2f}'.center(20)+'|'+'{:.2f}'.center(20)+'|').format(s1,f2,f3,f4,f5))
@dispatch(str,str,str,str,str)
def pretty_print(s1,s2,s3,s4,s5):
#To Print The Heading
    print(f"|{s1:^20}|{s2:^20}|{s3:^20}|{s4:^20}|{s5:^20}|")

#Land [in acres]
total_land=80
tomato_land=potato_land=cabbage_land=sunflower_land=sugarcane_land=total_land/5

#Production Rate [Tonnes per Acre]
tomato_production_rate=round((30/100*10)+(70/100*12),2)
potato_production_rate=10.0
cabbage_production_rate=14.0
sunflower_production_rate=0.7
sugarcane_production_rate=45.0

#Tonnes
tomato_yield=tomato_production_rate*tomato_land
potato_yield=potato_production_rate*potato_land
cabbage_yield=cabbage_production_rate*cabbage_land
sunflower_yield=sunflower_production_rate*sunflower_land
sugarcane_yield=sugarcane_production_rate*sugarcane_land

#To kilograms 
tomato_yield*=1000
potato_yield*=1000
cabbage_yield*=1000
sunflower_yield*=1000
sugarcane_yield*=1000

#Selling Price [Rs per kg]
tomato_price=7
potato_price=20
cabbage_price=24
sunflower_price=200
sugarcane_price=4000//1000 #Converting Rs/ton to Rs/kg

#Sales
tomato_sales=tomato_price*tomato_yield
potato_sales=potato_price*potato_yield
cabbage_sales=cabbage_price*cabbage_yield
sunflower_sales=sunflower_price*sunflower_yield
sugarcane_sales=sugarcane_price*sugarcane_yield
overall_sales=tomato_sales+potato_sales+cabbage_sales+sunflower_sales+sugarcane_sales

#Output As A Table
print()
print("The Farmer's Land".center(105))
print(('+'+"-"*20)*5+'+')
pretty_print("Crop","Production Rate","Yields","Selling Price","Sales")
pretty_print('',"[Tonnes per acre]","[kg]","[Rs per kg]","[Rs]")
print(('+'+"-"*20)*5+'+')
pretty_print("Tomato",tomato_production_rate,tomato_yield,tomato_price,tomato_sales)
pretty_print("Potato",potato_production_rate,potato_yield,potato_price,potato_sales)
pretty_print("Cabbage",cabbage_production_rate,cabbage_yield,cabbage_price,cabbage_sales)
pretty_print("Sunflower",sunflower_production_rate,sunflower_yield,sunflower_price,sunflower_sales)
pretty_print("Sugarcane",sugarcane_production_rate,sugarcane_yield,sugarcane_price,sugarcane_sales)
print(('+'+"-"*20)*5+'+')
print("\nThe Overall Sales = %0.2f"%overall_sales)


