import numpy as np
def find_reachable(g, r, i, ind):
	for j in range(n):
		if g[i, j] == 1:
			r[ind, j] = 1
			find_reachable(g, r, j, ind)
	return r

print("Enter number of nodes")
n = int(input())
graph = np.zeros((n,n))

print("Enter number of links")
l = int(input())
print("Enter all edges one by one as a, b: src, dest")
for i in range(l):
	a,b = map(int, input().split())
	a -= 1
	b -=1
	graph[a,b] = 1

reachable = np.zeros((n,n))
for i in range(n):
	reachable = find_reachable(graph, reachable, i, i)

for i in range(n):
	print("Ancestors of", i+1)
	for k in range(n):
		if reachable[k, i] == 1:
			print(k+1, end = " ")
	print()
	print("Descendants of", i+1)
	for k in range(n):
		if reachable[i, k] == 1:
			print(k+1, end = " ")
	print()



'''
Sample input:

Enter number of nodes
5
Enter number of links
4
Enter all edges one by one as a, b: src, dest
1 2
1 3
3 4
3 5

Sample output:
Ancestors of 1

Descendants of 1
2 3 4 5 
Ancestors of 2
1 
Descendants of 2

Ancestors of 3
1 
Descendants of 3
4 5 
Ancestors of 4
1 3 
Descendants of 4

Ancestors of 5
1 3 
Descendants of 5

'''
