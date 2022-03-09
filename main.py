# Ebrahim Asadi
# Student No: 9973731248
# Last Updated: 1400/11/07

from scheduling_graph import *

myGraph = SchedulingGraph()
myGraph.add_node('v0', NOP)
myGraph.add_node('v1', Multiplier)
myGraph.add_node('v2', Multiplier)
myGraph.add_node('v3', Multiplier)
myGraph.add_node('v4', ALU)
myGraph.add_node('v5', ALU)
myGraph.add_node('v6', Multiplier)
myGraph.add_node('v7', Multiplier)
myGraph.add_node('v8', Multiplier)
myGraph.add_node('v9', ALU)
myGraph.add_node('v10', ALU)
myGraph.add_node('v11', ALU)
myGraph.add_node('vn', NOP)

myGraph.add_edge('v0', 'v1')
myGraph.add_edge('v0', 'v2')
myGraph.add_edge('v0', 'v6')
myGraph.add_edge('v0', 'v8')
myGraph.add_edge('v0', 'v10')
myGraph.add_edge('v1', 'v3')
myGraph.add_edge('v2', 'v3')
myGraph.add_edge('v6', 'v7')
myGraph.add_edge('v8', 'v9')
myGraph.add_edge('v10', 'v11')
myGraph.add_edge('v3', 'v4')
myGraph.add_edge('v4', 'v5')
myGraph.add_edge('v7', 'v5')
myGraph.add_edge('v5', 'vn')
myGraph.add_edge('v9', 'vn')
myGraph.add_edge('v11', 'vn')

myGraph.list_scheduling()
print("")
myGraph.print_predecessors('vn')
print("")
myGraph.print_predecessors('v9')
print("")
myGraph.print_successors('v0')
print("")
myGraph.print_successors('v7')

print("")
myGraph.ASAP()
myGraph.ALAP(6)

