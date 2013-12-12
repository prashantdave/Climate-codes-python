import csv

def csv_writer(filename, data):
   data = data.ravel();
   datawrite = open(filename+".csv", "a"); 
   writer = csv.writer(datawrite);
   writer.writerow(data.tolist());
   datawrite.close()
