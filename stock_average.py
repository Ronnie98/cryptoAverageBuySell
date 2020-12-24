
#initialised lists used for buy
BoughtQuantity = []
BuyPrices = []
BoughtMultiple = []
#BuyFees = []

#initialised lists used for sell
SoldQuantity = []
SellPrices = []
SoldMultiple = []
#SellFees = []



#get input regarding coin name, save it in variable
CoinName = input("Name of coin: ")
#Contiunally go until quued to stop

	
	
	

while True:

	BuySell = input("Buy or Sell?, input b or s: ")
	
	if BuySell == 'done':
		break
	elif BuySell != 'b' and BuySell !='s':
		print("not valid")
		continue
	
	
	#try / except to see make sure value is numeric
	StrQuantity = input("Num of coins: ")
	try:
		#save value of num of coins
		Quantity = float(StrQuantity)
	except ValueError:
		print("Not a valid number.")
		continue
	if Quantity < 0:
		print ("Must be a positive amount.") 
	elif Quantity == 0 or bool(StrQuantity) == False:
		break
	
	try:	
		Price = float(input("Price of coins: "))
	except ValueError:
		print("Not a valid number")
		continue
		
	if Price < 0:
		print("Must be a positive amount.") 
		continue

	
	if BuySell == 'b':
		#append to the list new number of coins purchased
		BoughtQuantity.append(Quantity)
		#Fees.append(fee)
		
		BuyPrices.append(Price)
		#init price x quant to buy Bmultiple variable
		multiple = Price * Quantity
		#add this to buy - multiple list
		BoughtMultiple.append(multiple)

		#TotalBuyFees = sum(Fees)
		TotalBoughtCoins = sum(BoughtQuantity)
		TotalBuyCost = sum(BoughtMultiple)
		BuyAverage = TotalBuyCost / TotalBoughtCoins

	else:
		pass
		SoldQuantity.append(Quantity)
		SellPrices.append(Price)
		multiple = Price * Quantity
		SoldMultiple.append(multiple)
		#Fees.append(fee)

		#TotalSellFees = sum(Fees)
		TotalSoldCoins = sum(SoldQuantity)
		TotalSellCost = sum(SoldMultiple)
		SellAverage = TotalSellCost / TotalSoldCoins

	


print(f"You purchased {round(TotalBoughtCoins,3)} units of {CoinName} for an average cost of {round(BuyAverage,3)}")
print(f"You sold {round(TotalSoldCoins, 3 )} units of {CoinName} for an average cost of {round(SellAverage,3)}")
print("If trading on binance, you could factor in that there is a fee of 0.1%")





