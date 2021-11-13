def GetTotalTransaction_():
    TotalBoughtApple_= int(input("How many apples would you like to purchase: "))
    TotalBoughtOrange_= int(input("How many orange would you like to purchase: "))
    return TotalBoughtApple_, TotalBoughtOrange_

def GetComputation_(TotalBoughtApple_,TotalBouightOrange_,ApplePriceF,OrangePriceF):
    AmountOfPurchaceFunc= (TotalBoughtApple_*ApplePriceF) + (TotalBouightOrange_ * OrangePriceF)
    return AmountOfPurchaceFunc

def GetDisplayOutput_(AmountOfPurchaseFunc):
    print(f"The total amount is {AmountOfPurchaseFunc}.")

print("The price of apple is 20 pesos")
print("The price of orange is 25 pesos")

ApplePrice = 20
OrangePrice = 25

TotalBoughtApple_, TotalBoughtOrange_ = GetTotalTransaction_()
AmountOfPurchaseFunc = GetComputation_ (ApplePrice, OrangePrice, TotalBoughtApple_, TotalBoughtOrange_)
GetDisplayOutput_(AmountOfPurchaseFunc)