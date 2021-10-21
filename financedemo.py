import yfinance as yahooFinance
import cryptocompare
import datetime


#Passing the argument FB to get the company's information
GetFacebookInformation =  yahooFinance.Ticker("FB")

#print(GetFacebookInformation.info)

print("Company Sector : ", GetFacebookInformation.info['sector'])

print("Company Address : ", GetFacebookInformation.info['address1'])

print("Fifty Two Week High : ", GetFacebookInformation.info['fiftyTwoWeekHigh'])

print(GetFacebookInformation.history(period="5d")) #getting the maximum number of daily FB Prices
#to get other periods, use 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 3y, 5y, 10y and ytd

#liberty to pick the start and end dates
startDate = datetime.datetime(2017, 8, 15)

endDate = datetime.datetime(2017, 8, 25)

print(GetFacebookInformation.history(start=startDate, end=endDate))

#extracting cryptocurrency data after installing the "Cryptocompare" library
GetBitcoinInformation =  yahooFinance.Ticker("BTC-USD")

startDate = datetime.datetime(2021, 9, 2)

endDate = datetime.datetime(2021, 9, 30)

print(GetBitcoinInformation.history(start=startDate, end=endDate))

#print(GetBitcoinInformation.info)

#print(GetBitcoinInformation.history(period="5d"))

#price = cryptocompare.get_price('BTC', 'USD')

#print(price)


