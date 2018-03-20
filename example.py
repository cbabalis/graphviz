from graphviz import Digraph

g = Digraph('19th of March meeting', filename='test.gv')

g.edge('Elias', 'Babis')
g.edge('Elias', 'George')
g.edge('Vangelis', 'George')
g.edge('Elias', 'Vangelis')

g.view()
