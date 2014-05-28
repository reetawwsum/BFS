#Breadth First Search with Shortest Path and distance from the initial vertex.

g = {}
explored = {} #0: Unexplored, 1: Explored
queue = []
distance = {} #For calculating shortest distance
predecessor = {} #For calculating shortest path

def bfs(g, s):
	#print s,
	explored[s] = 1
	distance[s] = 0
	predecessor[s] = None
	queue.append(s)
	while len(queue) > 0:
		v = queue.pop(0)
		for w in g[v]:
			if not explored[w]:
				explored[w] = 1
				distance[w] = distance[v] + 1
				predecessor[w] = v
				queue.append(w)
				#print w,

def printPath(g, s, v):
	if v == s:
		print s,
	elif predecessor[v] == None:
		print "Path Doesn't exit"
	else:
		printPath(g, s, predecessor[v])
		print v,

with open('input.txt', 'r') as graphInput:
	for line in graphInput:
		ints = [int(x) for x in line.split()]
		g[ints[0]] = ints[1:]
		explored[ints[0]] = 0

bfs(g, 1)
printPath(g, 1, 10)