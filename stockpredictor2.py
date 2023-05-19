import yfinance as yf

userWalletUSD = 5000

msft = yf.Ticker("^gspc")
hist = msft.history(period="12mo")

print(hist)