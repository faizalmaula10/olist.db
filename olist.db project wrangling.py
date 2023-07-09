
# Imports

import sqlite3 as sq3
import pandas.io.sql as pds
import pandas as pd

# Import libraries
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns, numpy as np
     

# Create a variable, `path`, containing the path to the `baseball.db` contained in `sample_data/`
path = 'F:\exercise pacmann\sql\olist.db'



# Create a connection, `con`, that is connected to database at `path`
con = sq3.Connection(path)

con


# Create a variable, `query`, containing a SQL query which reads in all data from the `` table

query = """
SELECT *
FROM olist_products_dataset;
"""
olist_products_dataset = pd.read_sql(query, con)
olist_products_dataset = pd.read_sql(query,con)
print(olist_products_dataset)

query = """
SELECT *
FROM olist_order_payments_dataset;
"""
olist_order_payments_dataset = pd.read_sql(query, con)
olist_order_payments_dataset = pd.read_sql(query,con)
print(olist_order_payments_dataset)


query = """
SELECT *
FROM olist_order_reviews_dataset;
"""
olist_order_reviews_dataset = pd.read_sql(query, con)
olist_order_reviews_dataset = pd.read_sql(query,con)
print(olist_order_reviews_dataset)

query = """
SELECT *
FROM olist_order_dataset;
"""
olist_orders_dataset = pd.read_sql(query, con)
olist_orders_dataset = pd.read_sql(query,con)
print(olist_orders_dataset)

query = """
SELECT *
FROM olist_order_items_dataset;
"""
olist_order_item_dataset = pd.read_sql(query, con)
olist_order_item_dataset = pd.read_sql(query,con)
print(olist_order_item_dataset)

query = """
SELECT *
FROM olist_sellers_dataset;
"""
olist_sellers_dataset= pd.read_sql(query, con)
olist_sellers_dataset= pd.read_sql(query,con)
print(olist_sellers_dataset)


query = """
SELECT *
FROM olist_order_customer_dataset;
"""
olist_order_customer_dataset= pd.read_sql(query, con)
olist_order_customer_dataset= pd.read_sql(query,con)
print(olist_order_customer_dataset)


query = """
SELECT *
FROM olist_geolocation_dataset;
"""
olist_geolocation_dataset= pd.read_sql(query, con)
olist_geolocation_dataset= pd.read_sql(query,con)
print(olist_geolocation_dataset)


merge1=pd.merge(olist_order_item_dataset,olist_sellers_dataset,on="seller_id") #join table


merge1

merge2=pd.merge(olist_order_item_dataset,olist_products_dataset,on="product_id") #join table
merge2


merge3=pd.merge(merge1,merge2,on="order_id") #join table pertama dan kedua

merge3


x=merge3['product_length_cm']
y=merge3['product_width_cm']
plt.scatter(x,y)
plt.show() #analisis setelah penggabungan tabel


persentase_ongkir=(merge3['freight_value_x']/merge3['price_x']).round(2)
avg=np.mean(persentase_ongkir)
print("rata-rata ongkir adalah :", avg)
sd=np.std(persentase_ongkir)
print("std deviasi dari ongkir adalah :",sd) #analisis mean dan std.deviasi ongkir

persentase_ongkir


x=merge3['price_x']
y=merge3['freight_value_x']
plt.scatter(x,y)
plt.show()
pearsons_coefficient = np.corrcoef(x, y)
print("The pearson's coeffient of the x and y inputs are: \n" ,pearsons_coefficient) #scatterplot harga dan ongkirnya , korelasinya kecil


x=merge3['freight_value_x']
y=merge3['product_weight_g']
plt.scatter(x,y)
plt.show()
pearsons_coefficient = np.corrcoef(x, y)
print("The pearson's coeffient of the x and y inputs are: \n" ,pearsons_coefficient) #scatter plot ongkir vs berat barang

plt.boxplot(persentase_ongkir) #boxplot persentase ongkir


persentase_ongkir=pd.Series(persentase_ongkir*100).round(2)
persentase_ongkir #convert to series


merge3 = pd.concat([merge3,persentase_ongkir.rename('persentase_ongkir')], axis=1)
merge3 #add to dataframe using concat


sns.displot(data=merge3,x='persentase_ongkir', kind="kde", fill=True) #plot desnitas


elements = np.array(merge3['persentase_ongkir'])

mean = np.mean(elements, axis=0)
sd = np.std(elements, axis=0)

final_list = [x for x in merge3['persentase_ongkir'] if (x > mean - 2 * sd)]
final_list = [x for x in final_list if (x < mean + 2 * sd)]
print(final_list) #membuang outlier


plt.boxplot(final_list) #plot setelah membuang outlier


mean = np.mean(final_list, axis=0)
sd = np.std(final_list, axis=0)
print("mean baru: ",mean)
print("std deviasi  baru: ",sd)


plt.hist(final_list) #histogram setelah membuat outlier


plt.hist(persentase_ongkir) #histogram sebelum membuang outlier

