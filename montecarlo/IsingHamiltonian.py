import numpy as np
from .BitString import *
import networkx as nx

class IsingHamiltonian:

    def __init__(self, G: nx.Graph):
        self.G = G
        self.mu = np.array([0 for i in range(G.number_of_nodes())])
        # self.mu: np.array = np.arra y([], dtype = float)
    
    def set_mu(self, mus: np.array):
        # self.mu = mus.copy()
        self.mu = mus.copy()
        return self

    def energy(self, bs: BitString):
        E = 0

        # print(G.edges.items())
    
        for e in self.G.edges:

            E += (-1 if bs.getBit(e[0]) != bs.getBit(e[1]) else 1) * self.G.edges[e]['weight'] 
            

        
        
        for i in range(bs.N):
            E += bs.getBit(i) * self.mu[i] * (-1 if bs.getBit(i) == 1 else 1)

        return E

    
    def compute_average_values(self, T: float):

        E  = 0.0
        M  = 0.0
        Z  = 0.0
        EE = 0.0
        MM = 0.0

        # Write your function here!

        k = 1 # 1.380649 * 10 ** (-23)
        beta = 1 / (k * T) 
        bs = BitString(self.G.number_of_nodes())

        # Find Z
        n = 2 ** bs.N
        for i in range(n):

            bs.set_integer_config(i)
            Z += np.exp(-beta * self.energy(bs))

        # Find P
        P: list[float] = []
        for i in range(n):
            bs.set_integer_config(i)
            P.append(np.exp(-beta * self.energy(bs)) / Z)

        # Find E
        for i in range(n):
            bs.set_integer_config(i)
            E += P[i] * self.energy(bs)
        
        # Find M
        for i in range(n):
            bs.set_integer_config(i)
            magnet = bs.on() - bs.off()

            M += P[i] * magnet

        # Find EE
        for i in range(n):
            bs.set_integer_config(i)
            EE += P[i] * self.energy(bs) ** 2
        
        # Find MM
        for i in range(n):
            bs.set_integer_config(i)
            magnet = bs.on() - bs.off()
            MM += P[i] * magnet ** 2

        # Find HC 
        HC = (EE - E ** 2) / (T ** 2)
        MS = (MM - M ** 2) / T
        
        return E, M, HC, MS
    