

import json
import numpy
import datetime
import collections
from binance.client import Client
from binance import BinanceSocketManager

import config
import pandas as pd
import math
import numpy as np

class Trading:
    def __init__(self):
        #self.ticker = 'ethusd'+'t'
        #self.ticker = self.ticker.upper()
        self.client = Client(config.APIKEY,config.SECKEY)
        
    def get_price(self):
        bsm =  BinanceSocketManager(self.client)
        prices = self.client.get_all_tickers()
        df =  (pd.DataFrame.from_dict(prices))
        return df
    def strategy(self):
        g = Graph()
        df = self.get_price()
        df.price = df.price.astype(float)
        df.price = -1*np.log(df.price)
        for i in df.symbol:
            g.add_node(i)
        for j in df.price:
            g.weight.append((j))
        
        for m in range(len(df)-1):
            g.add_arc(df.symbol[m],df.symbol[m+1],df.price[m])
        for n in reversed(range(len(df)-1)):
            g.add_arc(df.symbol[n],df.symbol[n+1],df.price[n])
        
        dist, prec, bol = g.bellman_ford(g.weight,source=0)
        #####
        tot = 0
        for i in dist:
            tot += i
        profit = np.exp(-tot)-1
        if bol:
            print(f"Profit from the strategy is: {profit*100:.2g}%\n")
        return bol, profit

class Graph:
    def __init__(self):
        self.neighbors = []
        self.name2node = {}
        self.node2name = []
        self.weight = []
    
    def __len__(self):
        return len(self.node2name)
    def __getitem__(self,v):
        return self.neighbors[v]
    
    def add_node(self,name):
        assert name not in self.name2node
        self.name2node[name] = len(self.name2node)
        self.node2name.append(name)
        self.neighbors.append([]) 
        self.weight.append({})
        return self.name2node[name]
    
    def add_edge(self,name_u,name_v,weight_uv=None):
        self.add_arc(name_u, name_v, weight_uv) 
        self.add_arc(name_v, name_u, weight_uv)

    def add_arc(self,name_u,name_v,weight_uv=None):
        u = self.name2node[name_u]
        v = self.name2node[name_v] 
        self.neighbors[u].append(v)
        self.weight[u][v] = weight_uv

    def bellman_ford(self, weight, source=0):
        graph = self
        n = len(graph)
        dist = [float('inf')] * n
        prec = [None]*n
        dist[source] = 0
        for nb_iterations in range(n):
            changed = False
            for node in range(n):
                for neighbor in graph[node]:
                    alt = dist[node] + weight[node][neighbor]
                    if alt < dist[neighbor]:
                        dist[neighbor] = alt
                        prec[neighbor] = node
                        changed = True
                if not changed:
                    return dist,prec,False
        return dist, prec, True

#python3 arb.py
print(Trading().strategy())

