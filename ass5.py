def Getorder_():
    AvailableMoneyFunc= int(input("How much is your money?: "))
    QualityOfAppleYouWantFunc= int(input("How much is the apple: "))
    return AvailableMoneyFunc, QualityOfAppleYouWantFunc

def GetQuantityYouCanBuy_(TotalAmountOfMoneyYouCanSpendF, TotalQualityOfAppleYouWantToPurchase):
    GetQuantityYouCanBuyFunc= TotalAmountOfMoneyYouCanSpendF // TotalQualityOfAppleYouWantToPurchase
    return GetQuantityYouCanBuyFunc


def GetTotalChange(TotalAmountOfMoneyYouCanSpend, TotalQuantityOfAppleYouWantToPurchase):
    GetTotalChangeFunc= TotalAmountOfMoneyYouCanSpend % TotalQuantityOfAppleYouWantToPurchase
    return GetTotalChangeFunc


def DisplayOutPut(GetQuantityYouCanBuyF, GetTotalChangeF):
    print(f"You can buy {GetQuantityYouCanBuyF} apples and your change is {GetTotalChangeF}. ")

TotalAmountOfMoneyYouCanSpend,TotalQuantityOfAppleYouWantToPurchase= Getorder_()

YouCanBuy = GetQuantityYouCanBuy_(TotalQuantityOfAppleYouWantToPurchase,TotalQuantityOfAppleYouWantToPurchase)
YourChangeIs = GetTotalChange(TotalAmountOfMoneyYouCanSpend, TotalQuantityOfAppleYouWantToPurchase)

DisplayOutPut(YouCanBuy,YourChangeIs)
