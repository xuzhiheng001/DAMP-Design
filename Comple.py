import numpy as np
import matplotlib

def MakeComplement(theSequence,isDNA):
    returnString=""
    for i in range (0,len(theSequence)):
        temp=theSequence[i]
        if temp=="A":
            if(isDNA):
                temp="T"
            else:
                temp="U"
        elif temp=="T":
            temp="A"
        elif temp=="U":
            temp="A"
        elif temp=="G":
            temp="C"
        elif temp=="C":
            temp="G"
        elif temp=="M":
            temp="K"
        elif temp=="K":
            temp="M"
        elif temp=="R":
            temp="Y"
        elif temp=="Y":
            temp="R"
        elif temp=="W":
            temp="W"
        elif temp=="S":
            temp="S"
        elif temp=="V":
            temp="B"
        elif temp=="B":
            temp="V"
        elif temp=="H":
            temp="D"
        elif temp=="D":
            temp="H"
        returnString=returnString+temp
    returnString ="".join (reversed(returnString))
    return returnString
