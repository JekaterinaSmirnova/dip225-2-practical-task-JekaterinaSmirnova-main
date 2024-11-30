import pandas

fails = pandas.read_excel("description.xlsx", sheet_name="LookupAREA") # if no pages are specified, then the last one saved is open
info_list = fails.values.tolist()

get_info=input('Kāds reģions? ')  #input information from terminal

reg_id=0
for row in info_list:
    if row[1]==get_info:
        reg_id=row[0]
        break    
if reg_id==0:
    print('Reģions nav atrasts')
    exit()

CleanData=[]
csv=open('data.csv','r')
for line in csv:
    CleanData.append(line.rstrip().split(','))

geo_count=[]
for line in CleanData:
    if line[1]==reg_id:
        geo_count.append(int(line[3]))

sum(geo_count)
print ("Dati par reģionu:", get_info, " ID:",  reg_id, " reģionu summa:", sum(geo_count))