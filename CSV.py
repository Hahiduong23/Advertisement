import pandas as pd
import numpy as np

url = "https://raw.githubusercontent.com/selva86/datasets/master/Advertising.csv"
data = pd.read_csv(url)
column1 = data['TV']
column2 = data['Sales']

#Hiêp phương sai
covariance = np.cov(column1, column2)[0, 1]

#Phương sai từng cột
variance_col1 = np.var(column1, ddof=1) 
variance_col2 = np.var(column2, ddof=1)

#Hệ số tương quan 
pearson_corr = np.corrcoef(column1, column2)[0, 1]

#Góc
theta_radian = np.arccos(pearson_corr)  
theta_degree = np.degrees(theta_radian) 

#___________
print("Hiệp phương sai:", covariance)
print("Phương sai của cột 'TV':", variance_col1)
print("Phương sai của cột 'Sales':", variance_col2)
print("Hệ số tương quan Pearson:", pearson_corr)
print("Góc giữa hai cột (radian):", theta_radian)
print("Góc giữa hai cột (độ):", theta_degree)



