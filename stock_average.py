
#initialised lists used for buy
BoughtQuantity = []
#list to be used to track quantity bought
BuyPrices = []
#list to be used to track prices for bought quantity
BoughtMultiple = []
#list to be used to store the total values (price*quantity) of buys

#initialised lists used for sell
SoldQuantity = []
#list to be used to track quantity sold
SellPrices = []
#list to be used to track prices for sold quantity
SoldMultiple = []
#list to be used to store the total values (price*quantity) of sales



#get input regarding coin name, save it in variable
CoinName = input("Name of coin: ")

#start while loop, set continually to True
while True:
#understand whether user wants to input buy or sell call	
	BuySell = input("Buy or Sell?, input b or s: ")
	#if user types 'done', break and move on
	if BuySell == 'done':
		break
		#error handling
	elif BuySell != 'b' and BuySell !='s':
		print("not valid")
		continue
	
	
	#try / except to see make sure value is positive numeric value
	StrQuantity = input("Num of coins: ")
	try:
		#save value of num of coins
		Quantity = float(StrQuantity)
	except ValueError:
		print("Not a valid number.")
		continue
	if Quantity < 0:
		print ("Must be a positive amount.") 
		#second way to break while loop
	elif Quantity == 0 or bool(StrQuantity) == False:
		break

	#error handling, to make sure price is a positive numeric value
	try:	
		Price = float(input("Price of coins: "))
	except ValueError:
		print("Not a valid number")
		continue
		
	if Price < 0:
		print("Must be a positive amount.") 
		continue


	#steps to take if user is inputing a buy order.
	if BuySell == 'b':
		#append to the list new number of coins purchased
		BoughtQuantity.append(Quantity)
		
		
		BuyPrices.append(Price)
		#init price x quant to buy Bmultiple variable
		multiple = Price * Quantity
		#add this to buy - multiple list
		BoughtMultiple.append(multiple)

		
		TotalBoughtCoins = sum(BoughtQuantity)
		TotalBuyCost = sum(BoughtMultiple)
		BuyAverage = TotalBuyCost / TotalBoughtCoins

	#steps to take is user is inputting a sell order.
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





