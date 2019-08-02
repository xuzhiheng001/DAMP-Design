import numpy
import Tm
from parameters import *
import csv
import primer3
##import Pri3JU
##import Comple
import matplotlib

lines = [line.split() for line in open("excel.txt",'r')]
Name=['FO','FI','FC','RC','RI','RO']
DeltaG=[]

for i in range (1,7):
    for j in range(1,7):
        if (i!=j):
            if(i==2 or i==5):
                Tem1=primer3.calcHeterodimer(lines[0][i][:ParametersR],lines[0][j])
                DeltaGTem1=Tem1.dg/1000
                Tem2=primer3.calcHeterodimer(lines[0][i][-ParametersR:],lines[0][j])
                DeltaGTem2=Tem2.dg/1000
                DeltaG.append(DeltaGTem1)
                DeltaG.append(DeltaGTem2)
            else:
                Tem=primer3.calcHeterodimer(lines[0][i][-ParametersR:],lines[0][j])
                DeltaGTem=Tem.dg/1000
                DeltaG.append(DeltaGTem)
SumDeltaG=sum(DeltaG)
MaxDeltaG=min(DeltaG)
with open('primerDetail.csv', 'w', newline='') as csvfile:
    fieldnames = (['Name','Sequence', 'FdeltaG','TdeltaG','GCrate','Hsum',
                   'Ssum','Gsum','Tm'])
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in range(1,7):
        TemR=Tm.tmcal(lines[0][i])
        writer.writerow({'Name':Name[i-1],'Sequence':lines[0][i],
                         'FdeltaG':TemR[0],'TdeltaG':TemR[1],'GCrate':TemR[2],
                         'Hsum':TemR[3],'Ssum':TemR[4],'Gsum':TemR[5],
                         'Tm':TemR[6]})
    
    fieldnames=(['FO-FI','FO-FC', 'FO-RC','FO-RI','FO-RO',
                 'FIhead-FO','FItale-FO','FIhead-FC','FItale-FC',
                 'FIhead-RC','FItale-RC',
                 'FIhead-RI','FItale-RI','FIhead-RO','FItale-RO',
                 'FC-FO','FC-FI','FC-RC','FC-RI','FC-RO',
                 'RC-FO','RC-FI','RC-FC','RC-RI','RC-RO',
                 'RIhead-FO','RItale-FO','RIhead-FI','RItale-FI',
                 'RIhead-FC','RItale-FC',
                 'RIhead-RC','RItale-RC','RIhead-RO','RItale-RO',
                 'RO-FO','RO-FI','RO-FC','RO-RC','RO-RI','SumG','MaxG'])
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'FO-FI':DeltaG[0],'FO-FC':DeltaG[1], 'FO-RC':DeltaG[2],
                     'FO-RI':DeltaG[3],'FO-RO':DeltaG[4],'FIhead-FO':DeltaG[5],
                     'FItale-FO':DeltaG[6],'FIhead-FC':DeltaG[7],
                     'FItale-FC':DeltaG[8],'FIhead-RC':DeltaG[9],
                     'FItale-RC':DeltaG[10],'FIhead-RI':DeltaG[11],
                     'FItale-RI':DeltaG[12],'FIhead-RO':DeltaG[13],
                     'FItale-RO':DeltaG[14],'FC-FO':DeltaG[15],
                     'FC-FI':DeltaG[16],'FC-RC':DeltaG[17],'FC-RI':DeltaG[18],
                     'FC-RO':DeltaG[19],'RC-FO':DeltaG[20],'RC-FI':DeltaG[21],
                     'RC-FC':DeltaG[22],'RC-RI':DeltaG[23],'RC-RO':DeltaG[24],
                 'RIhead-FO':DeltaG[25],'RItale-FO':DeltaG[26],
                 'RIhead-FI':DeltaG[27],'RItale-FI':DeltaG[28],
                 'RIhead-FC':DeltaG[29],'RItale-FC':DeltaG[30],
                 'RIhead-RC':DeltaG[31],'RItale-RC':DeltaG[32],
                 'RIhead-RO':DeltaG[33],'RItale-RO':DeltaG[34],
                 'RO-FO':DeltaG[35],'RO-FI':DeltaG[36],'RO-FC':DeltaG[37],
                     'RO-RC':DeltaG[38],'RO-RI':DeltaG[39],'SumG':SumDeltaG,
                     'MaxG':MaxDeltaG})

