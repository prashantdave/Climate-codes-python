from numpy import trapz
#from csv_reader import csv_read
execfile('/home/prashant/PhD/codes/python_codes/csv_reader.py')

# Variables from 01 file
Evap_rate = csv_read('/home/prashant/syno/Prashant_Data/2001/01/csv_files_lat_increased/all_files/0609/evap.csv')
u =  csv_read('/home/prashant/syno/Prashant_Data/2001/01/csv_files_lat_increased/dv2uv/0609/u.csv')
v = csv_read('/home/prashant/syno/Prashant_Data/2001/01/csv_files_lat_increased/dv2uv/0609/v.csv')
SH = csv_read('/home/prashant/syno/Prashant_Data/2001/01/csv_files_lat_increased/all_files/0609/q.csv')
Stability = csv_read('/home/prashant/syno/Prashant_Data/2001/01/csv_files_lat_increased/all_files/0609/st.csv')
aprc = csv_read('/home/prashant/syno/Prashant_Data/2001/01/csv_files_lat_increased/all_files/0609/aprc.csv')
aprl = csv_read('/home/prashant/syno/Prashant_Data/2001/01/csv_files_lat_increased/all_files/0609/aprl.csv')
Latent_heat = csv_read('/home/prashant/syno/Prashant_Data/2001/01/csv_files_lat_increased/all_files/0609/ahfl.csv')

# Variables from activ file
CDNC = csv_read('/home/prashant/syno/Prashant_Data/2001/activ/csv_files_lat_increased/0609/CDNC.csv')
ICNC = csv_read('/home/prashant/syno/Prashant_Data/2001/activ/csv_files_lat_increased/0609/ICNC.csv')
ICNC_BURDEN = csv_read('/home/prashant/syno/Prashant_Data/2001/activ/csv_files_lat_increased/0609/ICNC_BURDEN.csv')
W = csv_read('/home/prashant/syno/Prashant_Data/2001/activ/csv_files_lat_increased/0609/W_LARGE.csv')
CDER = csv_read('/home/prashant/syno/Prashant_Data/2001/activ/csv_files_lat_increased/0609/REFFL.csv')
CDER_mean = CDER.mean(0)
# Variables from forcing
Sur_Direct_MAM = csv_read('/home/prashant/syno/Prashant_Data/2001/forcing/csv_files_lat_increased/0305/FSW_CLEAR_SUR.csv')
Sur_Direct_JJAS = csv_read('/home/prashant/syno/Prashant_Data/2001/forcing/csv_files_lat_increased/0609/FSW_CLEAR_SUR.csv')
Sur_Indirect_JJAS = csv_read('/home/prashant/syno/Prashant_Data/2001/forcing/csv_files_lat_increased/0609/FSW_TOTAL_SUR.csv')
                                         
# Variables from RADM
AOD_MAM = csv_read('/home/prashant/syno/Prashant_Data/2001/radm/csv_files_lat_increased/0305/TAU_2D.csv')
AOD_JJAS = csv_read('/home/prashant/syno/Prashant_Data/2001/radm/csv_files_lat_increased/0609/TAU_2D.csv')
BC_AOD_JJAS = csv_read('/home/prashant/syno/Prashant_Data/2001/radm/csv_files_lat_increased/0609/TAU_COMP_BC.csv')
DU_AOD_JJAS = csv_read('/home/prashant/syno/Prashant_Data/2001/radm/csv_files_lat_increased/0609/TAU_COMP_DU.csv')

u850 = u[25,:]
v850 = v[25,:]
uv850 = u850 + v850
W_int = trapz(W,axis=0)
SH_int = trapz(SH,axis=0)

CDNC_mean = CDNC[11:].mean(0) 
ICNC_mean = ICNC[3:].mean(0) 
CD_IC_NC = CDNC_mean + ICNC_mean

LTS = Stability[21,:]*(1009/725)**0.286-Stability[30,:]
precp = aprc + aprl

Data_Matrix_Direct =[AOD_JJAS, -1*Sur_Direct_JJAS, -1*Sur_Indirect_JJAS, LTS, SH_int, W_int, AOD_MAM, -1*Sur_Direct_MAM, uv850, Evap_rate, precp] 
Data_Matrix_Indirect = [AOD_JJAS, BC_AOD_JJAS, SH_int, W_int, ICNC_BURDEN, Latent_heat, CD_IC_NC, CDER_mean, -1*Sur_Indirect_JJAS,LTS,precp, aprc]

from Corr_Coeff import corr_coeff
import csv
#Correlation_Matrix = corr_coeff(Data_Matrix_Direct) # For Direct Forcing
Correlation_Matrix = corr_coeff(Data_Matrix_Indirect)  # For Indirect Forcing 

datawrite = open("Corr_Mat.txt", "w")
writer = csv.writer(datawrite)
for i in Correlation_Matrix:
    writer.writerow(i.round(2))
#    writer.writerow(map(int,i))

datawrite.close()

