from parameters import *
import primer3
import Comple
import matplotlib

def Hairpin(Sequence):
    TemResult=primer3.calcHairpin(Sequence)
##    print(TemResult.dg/1000)
    if TemResult.structure_found==1 and abs(TemResult.dg/1000)>HarpinDeltaG:
        return 0
    else:
        return 1

def HeteroDimer(Seq1,Seq2):
    TemResult=primer3.calcHeterodimer(Seq1,Seq2)
    if abs(TemResult.dg/1000)>HeteroDimerDeltaG:
        return 0
    else:
        return 1


def SelfDimer(Seq):
    TemResult=primer3.calcHeterodimer(Seq,Seq)
##    print (TemResult.dg/1000)
    if abs(TemResult.dg/1000)>SelfDimerDeltaG:
        return 0
    else:
        return 1

def HairSelf (Seq):
    if SelfDimer(Seq) ==1 and Hairpin(Seq)==1:
        return 1
    else:
        return 0


NResults=['CCCATGTTTTCAGCATTATCAGAA', 'GTCCCCCCACTGTGTTTAGCATTTTACCCCACAAGATTTAAACACC', 'GTCCCCCCACTGTGTTTAGCA', 'CCTGTTGCACCAGGCCAGAT', 'ATCTGGCCTGGTGCAACAGGTTTTCAAGGGGAAGTGACATAGCAG', 'TCCTGAAGGGTACTGGTAGT']
##Tlist=["A","B","C","D","E","F"]


def DeltaGsum(list):
    Gsum=0
    for i in range(0,len(list)):
        for j in range(0,len(list)):
            if (i!=j):
                if(i==1 or i==4):
                    Tem1=primer3.calcHeterodimer(list[i][:ParametersR],list[j])
                    DeltaGTem1=Tem1.dg
                    Tem2=primer3.calcHeterodimer(list[i][-ParametersR:],list[j])
                    DeltaGTem2=Tem2.dg
                    Gsum=DeltaGTem1+DeltaGTem2+Gsum
                else:
                    Tem=primer3.calcHeterodimer(list[i][-ParametersR:],list[j])
                    DeltaGTem=Tem.dg
                    Gsum=DeltaGTem+Gsum
    return (Gsum/1000)

def DeltaGmax(list):
    Gmax=[]
    for i in range(0,len(list)):
        for j in range(0,len(list)):
            if (i!=j):
                if(i==1 or i==4):
                    Tem1=primer3.calcHeterodimer(list[i][:ParametersR],list[j])
                    DeltaGTem1=Tem1.dg
                    Tem2=primer3.calcHeterodimer(list[i][-ParametersR:],list[j])
                    DeltaGTem2=Tem2.dg
                    Gmax.append(abs(DeltaGTem1))
                    Gmax.append(abs(DeltaGTem2))
                    
                else:
                    Tem=primer3.calcHeterodimer(list[i][-ParametersR:],list[j])
                    DeltaGTem=Tem.dg
                    Gmax.append(abs(DeltaGTem))
    return max(Gmax)/1000

tt=DeltaGmax(NResults)
        
##    NorList=[[1,1],[1,3],[1,4],[3,1],[3,3],[4,1]]
##    PreList=[[2,1],[2,3],[2,4],[5,1]]
##    PostList=[[1,2],[1,5],[3,2],[4,2]]
##    DoubleList=[[2,2]]
##    for i in range(0,len(list)):
##        for j in range(1,len(list)-i):
##            if ([i,j] in NorList):
##                Tem=primer3.calcHeterodimer(list[i],list[-j])
##                DeltaGTem=Tem.dg
##                Gsum=DeltaGTem+Gsum
##            if ([i,j] in PreList):
##                Tem1=primer3.calcHeterodimer(list[i][:ParametersR],list[-j])
##                Tem2=primer3.calcHeterodimer(list[i][-ParametersR:],list[-j])
##                DeltaGTem1=Tem1.dg
##                DeltaGTem2=Tem2.dg
##                Gsum=DeltaGTem1+DeltaGTem2+Gsum
##            if ([i,j] in PostList):
##                Tem1=primer3.calcHeterodimer(list[i],list[-j][:ParametersR])
##                Tem2=primer3.calcHeterodimer(list[i],list[-j][-ParametersR:])
##                DeltaGTem1=Tem1.dg
##                DeltaGTem2=Tem2.dg
##                Gsum=DeltaGTem1+DeltaGTem2+Gsum
##            if ([i,j] in DoubleList):
##                Tem1=primer3.calcHeterodimer(list[i][:ParametersR],list[-j][:ParametersR])
##                DeltaGTem1=Tem1.dg
##                Tem2=primer3.calcHeterodimer(list[i][:ParametersR],list[-j][-ParametersR:])
##                DeltaGTem2=Tem2.dg
##                Tem3=primer3.calcHeterodimer(list[i][-ParametersR:],list[-j][:ParametersR])
##                DeltaGTem3=Tem3.dg
##                Tem4=primer3.calcHeterodimer(list[i][-ParametersR:],list[-j][-ParametersR:])
##                DeltaGTem4=Tem4.dg
##                Gsum=DeltaGTem1+DeltaGTem2+DeltaGTem3+DeltaGTem4+Gsum

##tt=DeltaGsum(NResults)

##theFullSequence="AATTGGAAAAGGCCGGCCTTTTCCAATT"
##TT=Hairpin(theFullSequence)
##KK=HeteroDimer(theFullSequence,theFullSequence)
##ZZ=SelfDimer(theFullSequence)
##GG=HairSelf (theFullSequence)
