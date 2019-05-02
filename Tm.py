import numpy as np

def tmcal (Sequence):
    SequDic={
        "AA":[-8,-21.9,-1.2],
        "TT":[-8,-21.9,-1.2],
        "AT":[-5.6,-15.2,-0.9],
        "TA":[-6.6,-18.4,-0.9],
        "CA":[-8.2,-21,-1.7],
        "TG":[-8.2,-21,-1.7],
        "GT":[-6.6,-16.4,-1.5],
        "AC":[-6.6,-16.4,-1.5],
        "CT":[-8.8,-23.5,-1.5],
        "AG":[-8.8,-23.5,-1.5],
        "GA":[-9.4,-25.5,-1.5],
        "TC":[-9.4,-25.5,-1.5],
        "CG":[-11.8,-29,-2.8],
        "GC":[-10.5,-26.4,-2.3],
        "GG":[-10.9,-28.4,-2.1],
        "CC":[-10.9,-28.4,-2.1]
        }

    deltaHin=0.6
    deltaSin=-9
    deltaGin=3.4

    Hsum=deltaHin
    Ssum=deltaSin
    Gsum=deltaGin

    for i in range(0,len(Sequence)-1):    
        Hsum=Hsum+SequDic[Sequence[i:i+2]][0]
        Ssum=Ssum+SequDic[Sequence[i:i+2]][1]
        Gsum=Gsum+SequDic[Sequence[i:i+2]][2]

    C=0.000124585
    Na=0.05

    Tm=Hsum*1000/(Ssum+1.987*np.log(C/4))-273.15+16.6*np.log10 (Na)
    Lcontent=list(Sequence)
    GCrate=(Lcontent. count('G')+Lcontent. count('C'))/ len(Lcontent)

    FdeltaG=deltaGin
    TdeltaG=deltaGin

    for i in range(0,5):
        FdeltaG=FdeltaG+SequDic[Sequence[i:i+2]][2]
        
        if i!=4:
            TdeltaG=TdeltaG+SequDic[Sequence[-6+i:-4+i]][2]
        else:
            TdeltaG=TdeltaG+SequDic[Sequence[-6+i:]][2]

    return ([FdeltaG,TdeltaG,GCrate,Hsum,Ssum,Gsum,Tm,len(Sequence)])

##kk=tmcal('GCTGCTTGATGTCCCCCCACTTTTACCCCACAAGATTTAAACACC')
