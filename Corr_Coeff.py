import numpy as np

def corr_coeff(data):
    Corr_Coeff=np.zeros([len(data),len(data)]) 
    for i in range(len(data)):
       for j in range(len(data)):
           Corr_Coeff[i,j]= np.corrcoef(data[i],data[j])[0][1]
    return Corr_Coeff       
