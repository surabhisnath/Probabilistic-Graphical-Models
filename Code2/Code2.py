import numpy as np

import numpy as np
import sys

sys.setrecursionlimit(10**6) 

#---------------------------------


# Code borrowed from GeeksforGeeks
from collections import defaultdict 
   

class Graph: 
   
    def __init__(self,vertices): 
        #No. of vertices 
        self.V= vertices
        
        # default dictionary to store graph 
        self.graph = defaultdict(list)  
   
    # function to add an edge to graph 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
   
    '''A recursive function to print all paths from 'u' to 'd'. 
    visited[] keeps track of vertices in current path. 
    path[] stores actual vertices and path_index is current 
    index in path[]'''
    def printAllPathsUtil(self, u, d, visited, path): 
  
        # Mark the current node as visited and store in path 
        visited[u]= True
        path.append(u) 
  
        # If current vertex is same as destination, then print 
        # current path[] 
        if u == d:
            # print(path)
            arr.append(path.copy())

        else: 
            # If current vertex is not destination 
            #Recur for all the vertices adjacent to this vertex 
            for i in self.graph[u]: 
                if visited[i]==False: 
                    self.printAllPathsUtil(i, d, visited, path) 
                      
        # Remove current vertex from path[] and mark it as unvisited 
        path.pop() 
        visited[u]= False
        
   
   
    # Prints all paths from 's' to 'd' 
    def printAllPaths(self,s, d): 
  
        # Mark all the vertices as not visited 
        visited =[False]*(self.V) 
  
        # Create an array to store paths 
        path = [] 
  
        # Call the recursive helper function to print all paths 
        self.printAllPathsUtil(s, d,visited, path)



#----------------------------------


def find_reachable(g, r, i, ind):
	for j in range(a):
		if g[i, j] == 1:
			r[ind, j] = 1
			find_reachable(g, r, j, ind)
	return r

s = input()
a,b,c = map(int, s.split())

gdir = np.zeros((a,a))
gundir = np.zeros((a,a))
g = Graph(a)

for i in range(b):
	line = input()
	src, dest = map(int, line.split())
	gdir[src-1, dest-1] = 1
	gundir[src-1, dest-1] = 1
	gundir[dest-1, src-1] = 1
	g.addEdge(src-1, dest-1)
	g.addEdge(dest-1, src-1)	 


# print(gundir)

reachable = np.zeros((a,a))
for i in range(a):
	reachable = find_reachable(gdir, reachable, i, i)

d = {}
# print("Finding nodes having V structure")
for n in range(a):
	if gdir[:,n].sum() >= 2:
		indices = [i for i, x in enumerate(gdir[:,n]) if x == 1]
		d[n] = indices
# print(d)


allpaths = [[0 for i in range(a)] for j in range(a)]

for i in range(a):
	for j in range(i+1,a):
		arr = []
		g.printAllPaths(i,j)
		
		allpaths[i][j] = arr
		allpaths[j][i] = arr

# allpaths[0][1] = [[0,1]]
# allpaths[1][0] = [[0,1]]
# allpaths[0][2] = [[0,1,2]]
# allpaths[2][0] = [[0,1,2]]
# allpaths[1][2] = [[1,2]]
# allpaths[2][1] = [[1,2]]

def check(src, dest):
	paths = allpaths[src][dest]
	for path in paths:
		cn = 0
		v = False
		prev = path[0]
		for elem in range(1, len(path)-1):
			if path[elem] in d:
				if prev in d[path[elem]] and path[elem+1] in d[path[elem]]:
					# print("There is a V structure")
					v = True
					
					if path[elem] in ob:
						print("False")
						return
					for k in range(a):
						if reachable[path[elem], k] == 1:
							if k in ob:
								print("False")
								return

		
		if v == False:
			for elem in range(0, len(path)):
				if path[elem] not in ob:
					cn += 1
			if cn == len(path):
				print("False")
				return
	
	print("True")
	return


for query in range(c):
	l = input()
	arr = l.split()
	src = int(arr[0]) - 1
	dest = int(arr[1]) - 1
	ob = []
	for k in range(3,len(arr)):
		if int(arr[k]) == 0:
			ob = []
		else:
			ob.append(int(arr[k]) - 1)
	
	check(src, dest)



			





