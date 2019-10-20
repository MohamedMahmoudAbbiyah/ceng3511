import sys

if len(sys.argv)!= 2:
	print("No File Name Given")
	sys.exit(1)
if sys.argv[1] != "graph.txt":
	print("Incorrect File Name")
	sys.exit(1)

file = open(sys.argv[1], 'r')
Graph = {}
for line in file.readlines():
	key = line[0]
	line = line.replace("\n","")
	line = line[3:-1]
	lists = []
	for i in line.split(", "):
		if int(i[2]) > 0:
			lists.append(i)
	Graph[key] = lists
file.close()
#print(Graph)

def make_sure(graph_to_search, start, end):
	if start not in graph_to_search:
		print("IT IS \"" + start + '\" Not Found In Graph !')
		sys.exit(1)
	if end not in graph_to_search:
		print("IT IS  \"" + end + '\" Not Found In Graph !')
		sys.exit(1)

def BFS(graph_to_search, start, end):
	queue = [[start]]
	visited = set()

	while queue:
		path = queue.pop(0)


		last = path[-1]

		# Checks if we have reached the end
		if last == end:
			return path
		# We check if the current node is already in the "visited nodes" set in order not to check it again.
		elif last not in visited:

			for current_neighbour in graph_to_search.get(last, []):
				new_path = list(path)
				new_path.append(current_neighbour[0])
				queue.append(new_path)
			# Marks the "last" as visited
			visited.add(last)
	return 0


def DFS (graph_to_search, start, goal):
	My_stack = [(start, [start])]
	visited = set()
	while My_stack:
		(vertex, path) = My_stack.pop()
		if vertex not in visited:
			if vertex == goal:
				return path
			visited.add(vertex)
			for neighbor in sorted(graph_to_search[vertex], reverse=True):
				My_stack.append((neighbor[0], path + [neighbor[0]]))
	return 0


def UCS(graph_to_search, start, end):
	My_queue = [(0,[start])]
	visited = set()
	while My_queue:
		path = My_queue.pop(0)
		vertex = path[1][-1]
		if vertex == end:
			return path[1]
		elif vertex not in visited:
			for current_neighbour in graph_to_search.get(vertex, []):
				new_path = list(path[1])
				new_path.append(current_neighbour[0])
				new_path = (path[0] + int(current_neighbour[2]), new_path)
				My_queue.append(new_path)
			My_queue.sort(key= lambda x:x[0])
			visited.add(vertex)
	return 0


start_state = input("Please give me your start state : ")
Goal_state = input("Please give me your goal state : ")

make_sure(Graph, start_state, Goal_state)
Result_of_BFS = BFS(Graph, start_state, Goal_state)
Result_of_Dfs = DFS(Graph, start_state, Goal_state)
Result_of_UCS = UCS(Graph, start_state, Goal_state)

print("BFS : ", end="")
if Result_of_BFS  == 0:
	print("There Is No Path Between Them")
else:
	print(*Result_of_BFS , sep=" - ")

print("DFS : ", end="")
if Result_of_Dfs == 0:
	print("There Is No Path Between Them")
else:
	print(*Result_of_Dfs, sep=" - ")

print("UCS : ", end="")
if Result_of_UCS == 0:
	print("There Is No Path Between Them")
else:
	print(*Result_of_UCS, sep=" - ")

sys.exit(0)