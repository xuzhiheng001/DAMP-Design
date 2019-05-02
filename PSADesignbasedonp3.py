import numpy
import random
import Tm
from parameters import *
import csv
import Pri3JU
import Comple


##name = input("What is data file name? ")
##
##f = open(name+".txt", 'r')
f=open ("PSASe.txt",'r')
Lcontent = f.read()
##Lcontent=list(content)
GCnumber=(Lcontent. count('G')+Lcontent. count('C'))/ len(Lcontent)

#length
#GC f1,r1 15-22; f2,r2 15-20; of,oor 15-20
#AT f1,r1 20-28; f2,r2 18-25; of,oor 20-28
#normal f1,r1 20-24; f2,r2 18-22; of,oor 18-25

if GCnumber>GCHigh:
    type="GC"
    f1,r1=range(GCLDF1[0],GCLDF1[1]+1),range(GCLDR1[0],GCLDR1[1]+1)
    f2,r2=range(GCLDF2[0],GCLDF2[1]+1),range(GCLDR2[0],GCLDR2[1]+1)
    of,oor=range(GCLDOF[0],GCLDOF[1]+1),range(GCLDOR[0],GCLDOR[1]+1)
elif GCnumber<GCLow:
    type="AT"
    f1,r1=range(ATLDF1[0],ATLDF1[1]+1),range(ATLDR1[0],ATLDR1[1]+1)
    f2,r2=range(ATLDF2[0],ATLDF2[1]+1),range(ATLDR2[0],ATLDR2[1]+1)
    of,oor=range(ATLDOF[0],ATLDOF[1]+1),range(ATLDOR[0],ATLDOR[1]+1)
else:
    type="normal"
    f1,r1=range(NOLDF1[0],NOLDF1[1]+1),range(NOLDR1[0],NOLDR1[1]+1)
    f2,r2=range(NOLDF2[0],NOLDF2[1]+1),range(NOLDR2[0],NOLDR2[1]+1)
    of,oor=range(NOLDOF[0],NOLDOF[1]+1),range(NOLDOR[0],NOLDOR[1]+1)
f.close()

f1list,r1list,f2list,r2list,oflist,oorlist=[],[],[],[],[],[]
f1listcho,r1listcho,f2listcho,r2listcho,oflistcho,oorlistcho=[],[],[],[],[],[]

for i in range(0,len(Lcontent)):
    for j in f1:
        if (i+j-1<len(Lcontent)):
            f1list.append([i,i+j-1])
            r1list.append([i,i+j-1])
        else:
            break
    for k in f2:
        if (i+k-1<len(Lcontent)):
            f2list.append([i,i+k-1])
            r2list.append([i,i+k-1])
        else:
            break
    for z in of:
        if (i+z-1<len(Lcontent)):
            oflist.append([i,i+z-1])
            oorlist.append([i,i+z-1])
        else:
            break
        
#Temperature
#GC f1,r1 64-68; f2,r2,of,or 59-63;
#AT f1,r1 60-63; f2,r2,of,or 55-58;
#normal f1,r1 64-66; f2,r2,of,or 59-61;
        
temperrange=[[GCF1R1Tem,GCFRTem],[ATF1R1Tem,ATFRTem],[NOF1R1Tem,NOFRTem]]

if type=="GC":
    tempchorange=temperrange[0]
elif type=="AT":
    tempchorange=temperrange[1]
else:
    tempchorange=temperrange[2]
        
for i in range(0,len(f1list)):
    testString=Lcontent[f1list[i][0]:f1list[i][1]]
    tmtem= Tm.tmcal(testString)[6]
    threetem=Tm.tmcal(testString)[1]
    fivetem=Tm.tmcal(testString)[0]
    HairSelfTem=Pri3JU.HairSelf(testString)
    if (tempchorange[0][0] <= tmtem <= tempchorange[0][1]) and threetem<=ThrSta and fivetem<=FiveSta and HairSelfTem==1:
        f1listcho.append(f1list[i])

for i in range(0,len(r1list)):
    testString=Lcontent[r1list[i][0]:r1list[i][1]]
    tmtem= Tm.tmcal(testString)[6]
    threetem=Tm.tmcal(testString)[1]
    fivetem=Tm.tmcal(testString)[0]
    HairSelfTem=Pri3JU.HairSelf(testString)
    if (tempchorange[0][0] <= tmtem <= tempchorange[0][1])and threetem<=ThrSta and fivetem<=FiveSta and HairSelfTem==1:
        r1listcho.append(r1list[i])

for i in range(0,len(f2list)):
    testString=Lcontent[f2list[i][0]:f2list[i][1]]
    tmtem= Tm.tmcal(testString)[6]
    threetem=Tm.tmcal(testString)[1]
    HairSelfTem=Pri3JU.HairSelf(testString)
    if (tempchorange[1][0] <= tmtem <= tempchorange[1][1])and threetem<=ThrSta and HairSelfTem==1:
        f2listcho.append(f2list[i])

for i in range(0,len(r2list)):
    testString=Lcontent[r2list[i][0]:r2list[i][1]]
    tmtem= Tm.tmcal(testString)[6]
    threetem=Tm.tmcal(testString)[1]
    HairSelfTem=Pri3JU.HairSelf(testString)
    if (tempchorange[1][0] <= tmtem <= tempchorange[1][1])and threetem<=ThrSta and HairSelfTem==1:
        r2listcho.append(r2list[i])

for i in range(0,len(oflist)):
    testString=Lcontent[oflist[i][0]:oflist[i][1]]
    tmtem= Tm.tmcal(testString)[6]
    threetem=Tm.tmcal(testString)[1]
    fivetem=Tm.tmcal(testString)[0]
    HairSelfTem=Pri3JU.HairSelf(testString)
    if (tempchorange[1][0] <= tmtem <= tempchorange[1][1])and threetem<=ThrSta and fivetem<=FiveSta and HairSelfTem==1:
        oflistcho.append(oflist[i])

for i in range(0,len(oorlist)):
    testString=Lcontent[oorlist[i][0]:oorlist[i][1]]
    tmtem= Tm.tmcal(testString)[6]
    threetem=Tm.tmcal(testString)[1]
    fivetem=Tm.tmcal(testString)[0]
    HairSelfTem=Pri3JU.HairSelf(testString)
    if (tempchorange[1][0] <= tmtem <= tempchorange[1][1])and threetem<=ThrSta and fivetem<=FiveSta and HairSelfTem==1:
        oorlistcho.append(oorlist[i])

f1r1list,f1r1f2list,f1r1f2r2list,f1r1f2r2list,f1r1f2r2oflist,finlist=[],[],[],[],[],[]

off2list=[]

if (type=="AT"):
    F3TF2H=ATF3TF2H
    F2HF1H=ATF2HF1H
    F1TR1H=ATF1TR1H
    R1TR2T=ATR1TR2T
    R2TR3H=ATR2TR3H
    F3TF2H=ATF3TF2H
elif (type=="GC"):
    F3TF2H=GCF3TF2H
    F2HF1H=GCF2HF1H
    F1TR1H=GCF1TR1H
    R1TR2T=GCR1TR2T
    R2TR3H=GCR2TR3H
    F3TF2H=GCF3TF2H
elif (type=="normal"):
    F3TF2H=NOF3TF2H
    F2HF1H=NOF2HF1H
    F1TR1H=NOF1TR1H
    R1TR2T=NOR1TR2T
    R2TR3H=NOR2TR3H
    F3TF2H=NOF3TF2H

for i in range(0,len(oflistcho)):
    oftem=oflistcho[i]
    for j in range(0,len(f2listcho)):
        if f2listcho[j][0]>oftem[1] and f2listcho[j][0]<=oftem[1]+F3TF2H:
            off2list.append([oflistcho[i],f2listcho[j]])


off2f1list=[]

for i in range(0,len(off2list)):
    off2tem=off2list[i]
    for j in range(0,len(f1listcho)):
        if f1listcho[j][0]>off2tem[-1][-1] and off2tem[-1][0]+F2HF1H[0]<=f1listcho[j][0]<=off2tem[-1][0]+F2HF1H[1]:
            off2f1tem=off2tem+[f1listcho[j]]
            off2f1list.append(off2f1tem)

off2f1r1list=[]

for i in range(0,len(off2f1list)):
    off2f1tem=off2f1list[i]
    for j in range(0,len(r1listcho)):
        if r1listcho[j][0]>off2f1tem[-1][-1]and r1listcho[j][0]<=off2f1tem[-1][-1]+F1TR1H:
            off2f1r1tem=off2f1tem+[r1listcho[j]]
            off2f1r1list.append(off2f1r1tem)

off2f1r1r2list=[]

for i in range(0,len(off2f1r1list)):
    off2f1r1tem=off2f1r1list[i]
    for j in range(0,len(r2listcho)):
        if r2listcho[j][0]>off2f1r1tem[-1][-1] and off2f1r1tem[-1][-1]+R1TR2T[0]<=r2listcho[j][1]<=off2f1r1tem[-1][-1]+R1TR2T[1]:
            off2f1r1r2tem=off2f1r1tem+[r2listcho[j]]
            off2f1r1r2list.append(off2f1r1r2tem) 

off2f1r1r2oorlist=[]

for i in range(0,len(off2f1r1r2list)):
    off2f1r1r2tem=off2f1r1r2list[i]
    for j in range(0,len(oorlistcho)):
        if oorlistcho[j][0]>off2f1r1r2tem[-1][-1] and oorlistcho[j][0]<=off2f1r1r2tem[-1][-1]+R2TR3H:
            off2f1r1r2oortem=off2f1r1r2tem+[oorlistcho[j]]
            off2f1r1r2oorlist.append(off2f1r1r2oortem)

if (len(off2f1r1r2oorlist)>0):    

    if (len(off2f1r1r2oorlist)<printNumber or printNumber==0):
        print('All the possiblities have been in the output.')
        printLength=len(off2f1r1r2oorlist)
    else:
        printLength=printNumber

    if OutputType=='N'or OutputType=='R'or OutputType=='F':
        if OutputType=='N':
            printRange=range(0,printLength)
        elif OutputType=='R':
            printRange=random.sample(set(range(0,len(off2f1r1r2oorlist))), printLength)
        elif OutputType=='F':
            off2f1r1r2oorlist=sorted(off2f1r1r2oorlist,key=lambda x:x[1][0])
            printRange=range(0,printLength)

        with open('primerDesign.csv', 'w', newline='') as csvfile:
            fieldnames = ['Number','FO', 'FI','FC','RC','RI','RO']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            count=1
            for i in printRange:
                oftem=''.join(Lcontent[off2f1r1r2oorlist[i][0][0]:off2f1r1r2oorlist[i][0][1]])     
                f2tem=''.join(Lcontent[off2f1r1r2oorlist[i][1][0]:off2f1r1r2oorlist[i][1][1]])
                f1tem=''.join(Lcontent[off2f1r1r2oorlist[i][2][0]:off2f1r1r2oorlist[i][2][1]])
                r1tem=''.join(Lcontent[off2f1r1r2oorlist[i][3][0]:off2f1r1r2oorlist[i][3][1]])
                r2tem=''.join(Lcontent[off2f1r1r2oorlist[i][4][0]:off2f1r1r2oorlist[i][4][1]])
                oortem=''.join(Lcontent[off2f1r1r2oorlist[i][5][0]:off2f1r1r2oorlist[i][5][1]])

                FItem=Comple.MakeComplement(f1tem,1)+'TTTT'+f2tem
                FCtem=Comple.MakeComplement(f1tem,1)

                RItem=r1tem+'TTTT'+Comple.MakeComplement(r2tem,1)
                ROtem=Comple.MakeComplement(oortem,1)
                writer.writerow({'Number':count,'FO': oftem, 'FI': FItem,'FC':FCtem,'RC':r1tem,'RI':RItem,'RO':ROtem})
                count=count+1

        print (len(off2f1r1r2oorlist))

        print ("Done. Check the CSV file")
    elif OutputType=='DS':
        print ('DS model')
        NResults=[]
        for i in range(0,len(off2f1r1r2oorlist)):
            oftem=''.join(Lcontent[off2f1r1r2oorlist[i][0][0]:off2f1r1r2oorlist[i][0][1]])     
            f2tem=''.join(Lcontent[off2f1r1r2oorlist[i][1][0]:off2f1r1r2oorlist[i][1][1]])
            f1tem=''.join(Lcontent[off2f1r1r2oorlist[i][2][0]:off2f1r1r2oorlist[i][2][1]])
            r1tem=''.join(Lcontent[off2f1r1r2oorlist[i][3][0]:off2f1r1r2oorlist[i][3][1]])
            r2tem=''.join(Lcontent[off2f1r1r2oorlist[i][4][0]:off2f1r1r2oorlist[i][4][1]])
            oortem=''.join(Lcontent[off2f1r1r2oorlist[i][5][0]:off2f1r1r2oorlist[i][5][1]])

            FOtem=oftem
            FItem=Comple.MakeComplement(f1tem,1)+'TTTT'+f2tem
            FCtem=Comple.MakeComplement(f1tem,1)

            R1tem=r1tem
            RItem=r1tem+'TTTT'+Comple.MakeComplement(r2tem,1)
            ROtem=Comple.MakeComplement(oortem,1)
            NResultTem=[FOtem,FItem,FCtem,R1tem,RItem,ROtem]
            NResults.append(NResultTem)

        DeltaG=[]
##        testLength=20
        for j in range(0,len(NResults)):
##        for j in range(0,testLength):
            DeltaGTem=Pri3JU.DeltaGsum(NResults[j])
            DeltaG.append([j,abs(DeltaGTem)])
        ListNumber=sorted(DeltaG,key=lambda x: x[1])
        printRange=range(0,printLength)

        with open('primerDesign.csv', 'w', newline='') as csvfile:
            fieldnames = ['Number','FO', 'FI','FC','RC','RI','RO','SumDimmer']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            count=1
            for i in printRange:
                writer.writerow({'Number':count,'FO': NResults[ListNumber[i][0]][0], 'FI':NResults[ListNumber[i][0]][1],'FC':NResults[ListNumber[i][0]][2],'RC':NResults[ListNumber[i][0]][3],'RI':NResults[ListNumber[i][0]][4],'RO':NResults[ListNumber[i][0]][5],'SumDimmer':ListNumber[i][1]})
                count=count+1

        print ("Done. Check the CSV file")

    elif OutputType=='DM':
        print ('DM model')
        NResults=[]
        for i in range(0,len(off2f1r1r2oorlist)):
            oftem=''.join(Lcontent[off2f1r1r2oorlist[i][0][0]:off2f1r1r2oorlist[i][0][1]])     
            f2tem=''.join(Lcontent[off2f1r1r2oorlist[i][1][0]:off2f1r1r2oorlist[i][1][1]])
            f1tem=''.join(Lcontent[off2f1r1r2oorlist[i][2][0]:off2f1r1r2oorlist[i][2][1]])
            r1tem=''.join(Lcontent[off2f1r1r2oorlist[i][3][0]:off2f1r1r2oorlist[i][3][1]])
            r2tem=''.join(Lcontent[off2f1r1r2oorlist[i][4][0]:off2f1r1r2oorlist[i][4][1]])
            oortem=''.join(Lcontent[off2f1r1r2oorlist[i][5][0]:off2f1r1r2oorlist[i][5][1]])

            FOtem=oftem
            FItem=Comple.MakeComplement(f1tem,1)+'TTTT'+f2tem
            FCtem=Comple.MakeComplement(f1tem,1)

            R1tem=r1tem
            RItem=r1tem+'TTTT'+Comple.MakeComplement(r2tem,1)
            ROtem=Comple.MakeComplement(oortem,1)
            NResultTem=[FOtem,FItem,FCtem,R1tem,RItem,ROtem]
            NResults.append(NResultTem)

        DeltaG=[]
        for j in range(0,len(NResults)):
            DeltaGTem=Pri3JU.DeltaGmax(NResults[j])
            DeltaG.append([j,abs(DeltaGTem)])

        ListNumber=sorted(DeltaG,key=lambda x: x[1])
        printRange=range(0,printLength)

        with open('primerDesign.csv', 'w', newline='') as csvfile:
            fieldnames = ['Number','FO', 'FI','FC','RC','RI','RO','MaxDimmer']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            count=1
            for i in printRange:
                writer.writerow({'Number':count,'FO': NResults[ListNumber[i][0]][0], 'FI':NResults[ListNumber[i][0]][1],'FC':NResults[ListNumber[i][0]][2],'RC':NResults[ListNumber[i][0]][3],'RI':NResults[ListNumber[i][0]][4],'RO':NResults[ListNumber[i][0]][5],'MaxDimmer':ListNumber[i][1]})
                count=count+1

        print ("Done. Check the CSV file")
    else:
        print('Please choose the output module in the module list.')
else:
    print ("None is printed. Please try to change the parameters(most important parameters are SelfDimerDeltaG, HeteroDimerDeltaG, HarpinDeltaG)")
    
##
##OF F2 F1 R1 R2 OR Sequence





