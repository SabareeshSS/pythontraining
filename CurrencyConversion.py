'''
Created on 03-Jun-2016

@author: BALASUBRAMANIAM
'''
def USDTOINR(fromAmt):
    return 68.5*fromAmt

def EURTOINR(fromAmt):
    return 88.5*fromAmt

def sumAllCurrencies(currArray):
    sumcurr = 0
    for _ in currArray:
        sumcurr+=_
    return sumcurr


def sumAllCurrencies(currArray,tax):
    sumcurr = 0
    for _ in currArray:
        sumcurr+=_
    return sumcurr-tax

if __name__ == "__main__":
    print("currency conversion.py is being run directly")
else:
    print("currency conversion.py  is being imported into another module")
