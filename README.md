# Crypto-Arbitrage with Bellman-Ford Algorith written in Python
The purpose of this repository is to provide strategy for Multi-Currency Arbitrage. What is Triangular Arbitrage.
> Triangular arbitrage is the result of a discrepancy between three foreign currencies that occurs when the currency's exchange rates do not exactly match up. These opportunities are rare and traders who take advantage of them usually have advanced computer equipment and/or programs to automate the process.[^1]

I decided to go further than Triangular Arbitrage by using all the tickers available through the **API** from **python-binance** library, with 
```
client.get_all_tickers()
```
This functions was included in the class `Trading`. 
> List of functions:
```
Trading.get_price()
```
- get last price from *binance API* and put together into a dataframe by using pandas
```
Trading.strategy()
```
- recall the `Graph` class[^2] and the `Graph.bellman_ford()` to perform the strategy and print the  *boolean* variable `bol` (`True` if negative cycles were detected, `False` otherwise) and the **profit**  expressed as %



[^1]:[Investopedia: Triangular Arbitrage](https://www.investopedia.com/terms/t/triangulararbitrage.asp)
[^2]: The code to implement it has been taken from this [book](https://amzn.to/3bBI8tP)
