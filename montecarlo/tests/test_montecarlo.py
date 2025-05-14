"""
Unit and regression test for the montecarlo package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest
import networkx as nx
import montecarlo
import numpy as np

# Setting up for testing
h = montecarlo.BitString(10)
h.set_integer_config(45)
g = montecarlo.BitString(10)
g.set_integer_config(45)

G = nx.Graph()
G.add_nodes_from([i for i in range(10)])
G.add_edges_from([(i,(i+1)% G.number_of_nodes() ) for i in range(10)])
G.add_edge(2,5)
G.add_edge(4,8)
G.add_edge(4,0)
for e in G.edges:
    G.edges[e]['weight'] = 1.0


def test_montecarlo_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "montecarlo" in sys.modules

def testBitString():

    assert(h.integer() == 45)

    h.flip_site(9)

    assert(h.integer() == 44)

    rep = h.__repr__()

    assert(rep == "0000101100")

    assert(h != g)

    g.set_integer_config(44)
    
    assert(h == g)

    assert(len(h) == 10)

    assert(g.on() == 3)
    assert(g.off() == 7)

    assert(h.getBit(4) == 1)
    assert(h.getBit(0) == 0)

def testIsingHamiltonian():
    ih = montecarlo.IsingHamiltonian(G)

    ih = montecarlo.IsingHamiltonian(G).set_mu([.1 for i in range(10)])

    assert(np.isclose(ih.energy(g), 0.7))

    E, M, HC, MS = ih.compute_average_values(1)
    # print(E, M, HC, MS)

    assert(np.isclose(E, -8.769087662392312))
    assert(np.isclose(M, 0.10167706213939312))
    assert(np.isclose(HC, 1.9346155866375625))
    assert(np.isclose(MS, 2.031868730865069))



if __name__ == "__main__":
    testBitString()
    test_montecarlo_imported()
    testIsingHamiltonian()