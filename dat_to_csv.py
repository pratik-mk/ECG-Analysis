# importing panda library 
import pandas as pd 
  
# readinag given csv file 
# and creating dataframe 
dataframe1 = pd.read_csv("ecg_data.dat") 
  
# storing this dataframe in a csv file 
dataframe1.to_csv('ecg-data.csv',  
                  index = None) 