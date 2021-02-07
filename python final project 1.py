# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 11:22:28 2020

@author: Sravanthi TC
"""

import pandas as pd
import numpy as np

#Q1-Create a dataframe “Camera_data” using Camera.csv
Camera_data=pd.read_csv("C:/Users/Sravanthi TC/Downloads/Project pyrth 1/Camera.csv")
Camera_data.head(10)
Camera_data.shape

#Q2-Find out the percentage of blank values in each column.

(Camera_data.isnull().sum()/len(Camera_data))*100

#Q3-View the statistical summary of the data

Camera_data.describe()

#Q4-Replace all the blank values with NaN.
Camera_data.replace(r'/s+' ,np.nan, inplace=True)

#Q5-Now replace all the Blank values with the column median.

Camera_data.fillna(Camera_data.median(),inplace=True)
Camera_data.isnull().sum()

#Q6- Add a new column “Discounted_Price” in which give a discount of 5% in the Price column.
Camera_data.columns
Camera_data["Discounted_Price"]=Camera_data["Price"]*.95
Camera_data

#Q7-Drop the columns Zoom Tele & Macro Focus range
Camera_data.drop(['Zoom tele (T)', 'Macro focus range'],axis=1,inplace=True)


#Q8: Replace the Model Name “Agfa ePhoto CL50” with “Agfa ePhoto CL250”
Camera_data['Model'].replace(["Agfa ePhoto CL50","Agfa ePhoto CL250"],inplace=True)


#Q9- Rename the column name from Release Date to Release Year.
Camera_data.rename(columns={"Release date":"Release Year"},inplace=True)
Camera_data

# Q10- Which is the most expensive Camera?
Camera_data[Camera_data['Price']==Camera_data['Price'].max()]['Model']

# Q11- Which camera have the least weight?
Camera_data[Camera_data['Weight (inc. batteries)']==Camera_data['Weight (inc. batteries)'].min()]['Model']

# Q12- Group the data on the basis of their release year.
Camera_data.groupby(by='Release Year')['Model'].count()

# Q13-Extract the Name, Storage Include, Price, Disounted_Price & Dimensions columns.
Camera_data=Camera_data[['Model','Storage included','Price','Discounted_Price','Dimensions']]
Camera_data

# Q14 - Extract the records for the cameras released in the year 2005 & 2006

Camera_data[Camera_data['Release Year'].isin(['2005','2006'])]
#[['Release Year','Model']]


# Q15-Find out 2007’s expensive & Cheapest Camera.
Camera_data[Camera_data['Price']==Camera_data['Price'].max()]['Model'][Camera_data["Release Year"]==2007]
Camera_data[Camera_data['Price']==Camera_data['Price'].min()]['Model'][Camera_data["Release Year"]==2007]

Camera_data[(Camera_data['Price']==Camera_data['Price'].max()) | (Camera_data['Price']==Camera_data['Price'].min())]


# Q16- Which Year maximum number of models is released?
Camera_data.groupby('Release Year')['Model'].count().tail(1)






