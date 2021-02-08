import sys

# Artificial and Computational Intelligence Assignment 4
#Identify the correct uninformed search strategy for the given Assignment.
#Things to follow
	#1. Use appropriate data structures to represent the graph and the path using python libraries
	#2. Provide proper documentation
	#3. Find the path and print it
#Coding begins here
#1. Define the agent environment in the following block
	#PEAS environment, Initial data structures to define the graph and variable declarations

class UninformedSearch:
	def __init__(self):
		self.graph,self.cost = [[] for i in range(7)],{}  
		self.nodes = {
			0: "A",
			1: "B",
			2: "C",
			3: "D",
			4: "E",
			5: "F",
			6: "G"
		}
		self.min_cost_visited = []
		self.nodes_visited = []
		self.start = 0
		self.goal = {}

		# build edges
		self.graph[self.getNodePosition("A")].append(self.getNodePosition("B")) # A <-> B
		self.graph[self.getNodePosition("B")].append(self.getNodePosition("A"))
		self.graph[self.getNodePosition("A")].append(self.getNodePosition("C")) # A <-> C
		self.graph[self.getNodePosition("C")].append(self.getNodePosition("A"))
		self.graph[self.getNodePosition("B")].append(self.getNodePosition("D")) # B <-> D
		self.graph[self.getNodePosition("D")].append(self.getNodePosition("B"))
		self.graph[self.getNodePosition("B")].append(self.getNodePosition("G")) # B <-> G
		self.graph[self.getNodePosition("G")].append(self.getNodePosition("B"))
		self.graph[self.getNodePosition("C")].append(self.getNodePosition("E")) # C <-> E
		self.graph[self.getNodePosition("E")].append(self.getNodePosition("C"))
		self.graph[self.getNodePosition("C")].append(self.getNodePosition("G")) # C <-> G  
		self.graph[self.getNodePosition("G")].append(self.getNodePosition("C"))
		self.graph[self.getNodePosition("D")].append(self.getNodePosition("F")) # D <-> F
		self.graph[self.getNodePosition("F")].append(self.getNodePosition("D"))
		self.graph[self.getNodePosition("D")].append(self.getNodePosition("G")) # D <-> G  
		self.graph[self.getNodePosition("G")].append(self.getNodePosition("D"))
		self.graph[self.getNodePosition("E")].append(self.getNodePosition("F")) # E <-> F
		self.graph[self.getNodePosition("F")].append(self.getNodePosition("E"))
		self.graph[self.getNodePosition("E")].append(self.getNodePosition("G")) # E <-> G  
		self.graph[self.getNodePosition("G")].append(self.getNodePosition("E"))
		self.graph[self.getNodePosition("F")].append(self.getNodePosition("G")) # F <-> G
		self.graph[self.getNodePosition("G")].append(self.getNodePosition("F"))
		# add costs
		self.cost[self.getNodePosition("A"), self.getNodePosition("B")] = 110
		self.cost[self.getNodePosition("B"), self.getNodePosition("A")] = 110
		self.cost[self.getNodePosition("A"), self.getNodePosition("C")] = 132
		self.cost[self.getNodePosition("C"), self.getNodePosition("A")] = 132
		self.cost[self.getNodePosition("B"), self.getNodePosition("D")] = 159
		self.cost[self.getNodePosition("D"), self.getNodePosition("B")] = 159
		self.cost[self.getNodePosition("B"), self.getNodePosition("G")] = 59
		self.cost[self.getNodePosition("G"), self.getNodePosition("B")] = 59
		self.cost[self.getNodePosition("C"), self.getNodePosition("E")] = 89
		self.cost[self.getNodePosition("E"), self.getNodePosition("C")] = 89
		self.cost[self.getNodePosition("C"), self.getNodePosition("G")] = 120
		self.cost[self.getNodePosition("G"), self.getNodePosition("C")] = 120
		self.cost[self.getNodePosition("D"), self.getNodePosition("F")] = 98                            
		self.cost[self.getNodePosition("F"), self.getNodePosition("D")] = 98        
		self.cost[self.getNodePosition("D"), self.getNodePosition("G")] = 108
		self.cost[self.getNodePosition("G"), self.getNodePosition("D")] = 108        
		self.cost[self.getNodePosition("E"), self.getNodePosition("F")] = 68
		self.cost[self.getNodePosition("F"), self.getNodePosition("E")] = 68        
		self.cost[self.getNodePosition("E"), self.getNodePosition("G")] = 102
		self.cost[self.getNodePosition("G"), self.getNodePosition("E")] = 102        
		self.cost[self.getNodePosition("F"), self.getNodePosition("G")] = 92
		self.cost[self.getNodePosition("G"), self.getNodePosition("F")] = 92
	   
	def getNodePosition(self, node):
		if node in self.nodes.values():
			return list(self.nodes.values()).index(node)
		else:
			raise Exception("Invalid Node")
		   
	def getNode(self, position):
		if position in self.nodes.keys():
			return self.nodes[position]
		else:
			raise Exception("Invalid node position")        
	def setStartPosition(self, pos):
		self.start = pos

	def setGoals(self, goals):
		self.goals = goals  
#2. Define a formula that Checks for existence of path
	#Function for checking for the  path


#3. Implementation of search technique for finding the path
	# Uniform Cost Search    
	def UCS(self):
		answer = []
		queue = []
		for i in range(len(self.goals)):
			answer.append(10**8)
		queue.append([0, self.start,""])
		visited = {}
		count = 0
		while (len(queue) > 0):
			queue = sorted(queue)
			p = queue[-1]
			del queue[-1]
			p[0] *= -1
			
			if (p[1] in self.goals):
				
				index = self.goals.index(p[1])
				if (answer[index] == 10**8):
					count += 1
				if (answer[index] > p[0]):
					answer[index] = p[0]
				#print(queue)
				if queue:
					del queue[-1]
				queue = sorted(queue)
				if (count == len(self.goals)):
					self.min_cost_visited.append(answer[0])
					self.nodes_visited.append(self.goals[0])
					print("path is : "+str(p[2])+str(p[1]))
					return self.goals[0]

			print(visited)
			path = str(p[2]) + str(p[1])
			if (p[1] not in visited):
				for i in range(len(self.graph[p[1]])):
					#print(self.graph[p[1]])
					queue.append([(p[0] + self.cost[(p[1], self.graph[p[1]][i])])* -1, self.graph[p[1]][i],path])
			visited[p[1]] = 1
			#print(visited)
		   
		self.min_cost_visited.append(answer[0])
		self.nodes_visited.append(self.goals[0])
		return self.goals[0]

#4. Calling main function
	#Function call to the search technique
   
if __name__ == '__main__':
	uninformedSearch = UninformedSearch()
	startInput = input("Enter the starting point (from A, B, C, D, E, F, G) : ") 
	startPosition = uninformedSearch.getNodePosition(startInput)
	if (startPosition < 0):
		print("Invalid Start Input : ",startInput)
		sys.exit()
	   
	n = int(input("Enter number of Goals/Destination: "))
	glist = list(input("\nEnter the Goal Node: ").strip().split())[:n]
	try:
		goal_input_list = []          
		for goalInput in glist:
			goal_input_list.append(uninformedSearch.getNodePosition(goalInput))
	except:
		print("Invalid Goals Input : ", glist)
		sys.exit()

	goall = []
	for gi in goal_input_list:    
		goall.append(gi)    

	uninformedSearch.setStartPosition(startPosition)
	uninformedSearch.setGoals(goall)

	while goall:  
		#print("----------------")
		#print(goal)
		goal_reached_pos = uninformedSearch.UCS()
		goal_reached = uninformedSearch.getNode(goal_reached_pos)
		#print(goal_reached)
		uninformedSearch.setStartPosition(goal_reached_pos)
		goall.remove(goal_reached_pos)
		uninformedSearch.setGoals(goall)
	print("Vertices----")
	for n in uninformedSearch.nodes_visited:        
		print(uninformedSearch.getNode(n))
	print("Min Cost for each node")
	for mc in uninformedSearch.min_cost_visited:        
		print(mc)
		   


#5. The agent should provide the following output
	#5.1. Whether a path exists
	#Function to find the existence of path


	#5.2. The path that covers required vertices in the graph
	#Function that prints the path covering required vertices using appropriate uninformed search


	#5.3. Print the total number of vertices (areas) visited by the agent in finding the path
	#Execute code to print the number of vertices travelled to cover the path. (using appropriate uninformed search)

