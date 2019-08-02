import matplotlib

##Output Number
printNumber=50

#None which is output by the original sequence N
#Dimer which is output by the Dimer type D
#Random which sequence is random R
#F25'position which sequence is sequnced by the F2 5' F
#Easy the Dimer and Harpin E ?????

OutputType="DS"

ParametersR=10

##GC range Default 0.4,0.65
GCLow=0.4
GCHigh=0.65

##length Default
#GC F1,R1 15-22; F2,R2 15-20; OF,OR 15-20
#AT F1,R1 20-28; F2,R2 18-25; OF,OR 20-28
#normal F1,R1 20-24; F2,R2 18-22; OF,OR 18-25

#GC

GCLDF1=[15,22]
GCLDR1=[15,22]
GCLDF2=[15,20]
GCLDR2=[15,20]
GCLDOF=[15,20]
GCLDOR=[15,20]

#AT

ATLDF1=[20,28]
ATLDR1=[20,28]
ATLDF2=[18,25]
ATLDR2=[18,25]
ATLDOF=[20,28]
ATLDOR=[20,28]

#Normal

NOLDF1=[20,24]
NOLDR1=[20,24]
NOLDF2=[18,22]
NOLDR2=[18,22]
NOLDOF=[18,25]
NOLDOR=[18,25]

##Temperature Control
#GC f1,r1 64-68; f2,r2,of,or 59-63;
#AT f1,r1 60-63; f2,r2,of,or 55-58;
#normal f1,r1 64-66; f2,r2,of,or 59-61;


GCF1R1Tem=[64,68]
GCFRTem=[59,63]

ATF1R1Tem=[60,63]
ATFRTem=[55,58]

NOF1R1Tem=[64,66]
NOFRTem=[59,61]

##Distance

ATF3TF2H=40
ATF2HF1H=[18,40]
ATF1TR1H=100
ATR1TR2T=[18,40]
ATR2TR3H=40

NOF3TF2H=40
NOF2HF1H=[18,40]
NOF1TR1H=100
NOR1TR2T=[18,40]
NOR2TR3H=40

GCF3TF2H=40
GCF2HF1H=[15,40]
GCF1TR1H=100
GCR1TR2T=[15,40]
GCR2TR3H=40

#GC,AT,Normal

##dG threshold

#Harpin and Dimer Check 
SelfDimerDeltaG=6
HeteroDimerDeltaG=5
HarpinDeltaG=0.5

#5'stability-5-5
FiveSta=-4
#3' stability
ThrSta=-4
