import pandas as pd 
import numpy as np
import os

cat_lookup = pd.read_csv('key.csv', header=0)
cat_lookup.replace(to_replace = np.nan, value ="Unknown")
cat_lookup.replace(to_replace = float, value ="Unknown")
cat_lookup['Category'] = cat_lookup['Category'].str.upper() 
cat_lookup['Description'] = cat_lookup['Description'].str.upper() 

files = os.listdir('./data')

for file in files:
	print(file)
	if os.path.isfile('data/' + file):
		dat = pd.read_csv('data/' + file, header=0)

		dat.replace(to_replace = np.nan, value ="Unknown")
		dat.replace(to_replace = float, value ="Unknown")
		dat['Description'] = dat['Description'].str.upper() 

		for iterkey, krow in cat_lookup.iterrows():
			dat.loc[dat['Description'].str.contains(krow["Description"], na=False), 'Category'] = krow["Category"]
			dat.loc[dat['Description'].str.contains(krow["Description"], na=False), 'Key'] = krow["Description"]

			# dat.loc[dat['Key'].str.contains("VENMO", na=False) & ((dat["Amount"] == -395) | (dat["Amount"] == -1100) | (dat["Amount"] == -2200)), 'Category'] = "RENT"
			dat.loc[dat['Key'].str.contains("VENMO", na=False) & ((dat["Amount"] == "-395") | (dat["Amount"] == "-1100") | (dat["Amount"] == "-2200")), 'Category'] = "RENT"


		dat.to_csv('data/' + file, index=False) 