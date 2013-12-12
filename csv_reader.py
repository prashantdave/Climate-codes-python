import csv
from numpy import array
def csv_read(file_path):
    file = csv.reader(open(file_path,"rb"))
    data = []
    for row in file:
        data.append(map(float,row))
    data = array(data)    
    return data    

def file_list(file_list_path):
    f = open(file_list_path)
    data_all=[]
    for line in f.readlines():
        data_all.append(csv_read(line[:-1]))
    return array(data_all)
    f.close()
## Variables from 01 file
#    Evap_rate = csv_read('/home/prashant/syno/Prashant_Data/2001/01/csv_files_lat_increased/all_files/0609/evap.csv')
#    u =  csv_read('/home/prashant/syno/Prashant_Data/2001/01/csv_files_lat_increased/dv2uv/0609/u.csv')
#    v = csv_read('/home/prashant/syno/Prashant_Data/2001/01/csv_files_lat_increased/dv2uv/0609/v.csv')
#    SH = csv_read('/home/prashant/syno/Prashant_Data/2001/01/csv_files_lat_increased/all_files/0609/q.csv')
#    Stability = csv_read('/home/prashant/syno/Prashant_Data/2001/01/csv_files_lat_increased/all_files/0609/st.csv')
#    aprc = csv_read('/home/prashant/syno/Prashant_Data/2001/01/csv_files_lat_increased/all_files/0609/aprc.csv')
#    aprl = csv_read('/home/prashant/syno/Prashant_Data/2001/01/csv_files_lat_increased/all_files/0609/aprl.csv')
#    Latent_heat = csv_read('/home/prashant/syno/Prashant_Data/2001/01/csv_files_lat_increased/all_files/0609/ahfl.csv')
#
## Variables from activ file
#    CDNC = csv_read('/home/prashant/syno/Prashant_Data/2001/activ/csv_files_lat_increased/0609/CDNC.csv')
#    ICNC = csv_read('/home/prashant/syno/Prashant_Data/2001/activ/csv_files_lat_increased/0609/ICNC.csv')
#    ICNC_BURDEN = csv_read('/home/prashant/syno/Prashant_Data/2001/activ/csv_files_lat_increased/0609/ICNC_BURDEN.csv')
#    W = csv_read('/home/prashant/syno/Prashant_Data/2001/activ/csv_files_lat_increased/0609/W_LARGE.csv')
#    CDER = csv_read('/home/prashant/syno/Prashant_Data/2001/activ/csv_files_lat_increased/0609/REFFL.csv')
# 
## Variables from forcing
#    Sur_Diret_MAM = csv_read('/home/prashant/syno/Prashant_Data/2001/forcing/csv_files_lat_increased/0305/FSW_CLEAR_SUR.csv')
#    Sur_Direct_JJAS = csv_read('/home/prashant/syno/Prashant_Data/2001/forcing/csv_files_lat_increased/0609/FSW_CLEAR_SUR.csv')
#    Sur_Indirect_JJAS = csv_read('/home/prashant/syno/Prashant_Data/2001/forcing/csv_files_lat_increased/0609/FSW_TOTAL_SUR.csv')
#        
## Variables from RADM
#    AOD_MAM = csv_read('/home/prashant/syno/Prashant_Data/2001/radm/csv_files_lat_increased/0305/TAU_2D.csv')
#    AOD_JJAS = csv_read('/home/prashant/syno/Prashant_Data/2001/radm/csv_files_lat_increased/0609/TAU_2D.csv')
#    BC_AOD_JJAS = csv_read('/home/prashant/syno/Prashant_Data/2001/radm/csv_files_lat_increased/0605/TAU_COMP_BC.csv')
#    DU_AOD_JJAS = csv_read('/home/prashant/syno/Prashant_Data/2001/radm/csv_files_lat_increased/0605/TAU_COMP_DU.csv')
 

