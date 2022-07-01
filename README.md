# Crypto-Arbitrage with Bellman-Ford Algorithm written in Python
The purpose of this repository is to provide strategy for Multi-Currency Arbitrage. Some definitions:
> Triangular arbitrage is the result of a discrepancy between three foreign currencies that occurs when the currency's exchange rates do not exactly match up. These opportunities are rare and traders who take advantage of them usually have advanced computer equipment and/or programs to automate the process.[^1]

Graph:
> A graph is a combinatorial object composed of a set of vertices V (also known as nodes) and a set of edges E. The edges correspond to pairs of vertices, which are generally distinct, and without a notion of order in the sense where (u,v) and (v,u) denote the same edge.
At times, we consider a variant, the directed graph, where the edges have an ori- entation. In this case, the edges are usually known as arcs. The arc (u,v) has origin u and destination v. Most of the algorithms described in this book operate on directed graphs but can be applied to non-directed graphs by replacing each edge (u,v) by two arcs (u,v) and (v,u).
Graphs can contain additional information, such as weights or letters, in the form of labels on the vertices or the edges.


Our goal is to develop a systematic method for detecting arbitrage opportunities by framing the problem in the language of graphs. 
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
