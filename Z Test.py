import scipy.stats as st
import numpy as np

s_x=90 #mean of sample data
p_u=82 #mean of population data
p_std=20 #sd of population data
n=81 #no of samples
ap=0.05 #value of alpha

#calculating z_value
z_table=st.norm.ppf(1-ap)

#z_calculation
z_cal=(s_x-p_u)/(p_std/np.sqrt(n))
print(z_cal)


#drawing our conclusion
if (z_table < z_cal):
    print("ha is right")
else :
    print("h0 is right")    