from graphviz import Digraph

g = Digraph('cyclic graph', filename='cycle.gv')

g.edge('Elias', 'Babis')
g.edge('Babis', 'George')
g.edge('Vangelis', 'George')
g.edge('Vangelis', 'Vangelis')
g.edge('Elias', 'Vangelis')
g.edge('George', 'Elias')

g.edge('Alice', 'Bob')
g.edge('Bob', 'Alice')

g.view()
