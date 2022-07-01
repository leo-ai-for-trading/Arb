# Crypto-Arbitrage with Bellman-Ford Algorithm written in Python
## Definitions
> Triangular arbitrage is the result of a discrepancy between three foreign currencies that occurs when the currency's exchange rates do not exactly match up. These opportunities are rare and traders who take advantage of them usually have advanced computer equipment and/or programs to automate the process.[^1]

###### Graph:
> A graph is a combinatorial object composed of a set of vertices V (also known as nodes) and a set of edges E. The edges correspond to pairs of vertices, which are generally distinct, and without a notion of order in the sense where (u,v) and (v,u) denote the same edge.
At times, we consider a variant, the directed graph, where the edges have an ori- entation. In this case, the edges are usually known as arcs. The arc (u,v) has origin u and destination v. Most of the algorithms described in this book operate on directed graphs but can be applied to non-directed graphs by replacing each edge (u,v) by two arcs (u,v) and (v,u).
Graphs can contain additional information, such as weights or letters, in the form of labels on the vertices or the edges.
![](https://github.com/leo-ai-for-trading/Crypto-Arb/blob/main/clip/Schermata%202022-07-01%20alle%2013.56.37.png)

###### Bellman-Ford algorithm:
> The Bellman-Ford algorithm finds the minimum weight path from a single source vertex to all other vertices on a weighted directed graph.

Our goal is to develop a systematic method for detecting arbitrage opportunities by framing the problem in the language of graphs. 

## Approach
We will assign currencies to different vertices, and let the edge weight represent the exchange rate.
find a cycle in the graph such that multiplying all the edge weights along that cycle results in a value greater than 1. In fact we have already described an algorithm that can find such a path – the problem is equivalent to finding a negative-weight cycle, provided we do some preprocessing on the edges.

Firstly, we note that Bellman-Ford computes the path weight by adding the individual edge weights. To make this work for exchange rates, which are multiplicative, an elegant fix is to first take the logs of all the edge weights. Thus when we sum edge weights along a path we are actually multiplying exchange rates – we can recover the multiplied quantity by exponentiating the sum. Secondly, Bellman-Ford attempts to find minimum weight paths and negative edge cycles, whereas our arbitrage problem is about maximising the amoun t of currency received. Thus as a simple modification, we must also make our log weights negative.
With these two tricks in hand, we are able to apply Bellman-Ford. The minimal weight between two currency vertices corresponds to the optimal exchange rate, the value of which can be found by by exponentiating the negative sum of weights along the path. As a corollary, we have the wonderful insight that: a negative-weight cycle on the negative-log graph corresponds to an arbitrage opportunity.

## Code
This functions of `Trading` class. 
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
