# -*- coding: utf-8 -*-

#https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/



#Djisktra algorithm 
#This code might not be handling self loops- Need to verify

import sys
class Graph():
    def __init__(self,v):
        self.graph={} #Abstraction of the grpah in a dictionary
        self.path=[] #shortest distance  -doesn't calculate path information
        self.c=0 #keep track of the current cost
        self.V=v #total number of vertices in the graph
        self.A_node=[] #self.A_node=['A','B','C','D','E','F']
        self.A_node_i={} #self.A_node_i={0:'A',1:'B',2:'C',3:'D',4:'E',5:'F'} #from int to node
        self.A_node_j={} #self.A_node_j={'A':0,'B':1,'C':2,'D':3,'E':4,'F':5} #from node to int
        self.parent={}
        self.source=0
        #self.source
        
    def Data_format(self):
        #1- Store all nodes in a list
        for i, j in enumerate(self.graph):
            self.A_node.append(j) 
            self.A_node_i[i]=j 
            self.A_node_j[j]=i 
            self.P=[] #this list contains the shortest path from source to destination
            
    def append(self,source,dest,cost):
        #A_node=[] #garther all the nodes 
        if source in self.graph: #if the node already exists
            self.graph[source].update({dest:cost}) #append new neighbor with corresponding cost
        else:
            self.graph[source]={dest:cost} #create the node
            
        if dest in self.graph: #do the same for the destination because the graph is undirected
            self.graph[dest].update({source:cost}) #just remove this graph for directed graph
        else:
            self.graph[dest]={source:cost}
    def Djisktra(self,node,destination):
        self.source=node
        #p={}
        dist = [sys.maxsize] * len(self.A_node) #list containing the distance of each node (initially infinity)
        self.Djisktra_helper(node,dist,destination) #return the shortance distance from source to all vertices
        

        return self.S_path(destination)
        
    def Djisktra_helper(self,node,dist,destination):
        self.path.append(node) 
        if(destination in self.path): #once we have all nodes in the path- return the path
            #return (self.c,self.path)
            return self.parent
        
        
        for j in self.graph[node]: #loop through every neighbour of the node 
            if(j not in self.path): #that is not already in the path
                n_cost=self.graph[node][j]+self.c# compute new cost
                o_cost=dist[self.A_node_j[j]] #old cost
                #if the new cost is smaller than the old cost/dist, update dist otherwise, keep the current cost/dist
                if n_cost<dist[self.A_node_j[j]]:
                    dist[self.A_node_j[j]]=self.graph[node][j]+self.c 
                    self.parent[j]=node #parent node
                    #p=self.parent.copy()
                else : 
                    dist[self.A_node_j[j]]=o_cost
                
        
        n_node=self.shortest_path(dist) #Now, choose the shortest path
        return self.Djisktra_helper(n_node,dist,destination) #repeat with next node
    def S_path(self,destination):
            self.P.append(destination) #return the actual shortest path from node i to node J
            if(destination==self.source):
                return 
            
            else:
                self.S_path(self.parent[destination]) #recursive call 
            return self.c,self.P  
            
            
            
    def shortest_path(self,dist):
        
        min_cost=sys.maxsize #helper to chose the min cost
         
        for i,j in enumerate(dist):
            if (j<min_cost): #if the cost of the path to that node is the smallest and not already in the path
                Id=i #index of the node with the smallest cost
                self.c=j #keep track of the new cost
                min_cost=j
                n_node=self.A_node_i[i] #next node
       
        dist[Id]=sys.maxsize #Set the cost of that node very high so that it won't be used in future iterations
        return n_node #return the next node
          
   
                
 
G=Graph(6)
"""
G.append('A','B',2)
G.append('A','C',4)
G.append('B','C',1)
G.append('B','E',2)
G.append('B','D',3)
G.append('B','F',7)
G.append('C','E',2)
G.append('D','E',3)
G.append('D','F',5)
G.append('E','F',1) 
"""  
#G.Print()

G.append('A','B',2)
G.append('A','C',1)
G.append('A','D',5)
G.append('B','C',2)
G.append('B','D',3)
G.append('C','E',1)
G.append('C','D',3)
G.append('D','E',1)
G.append('D','F',5)
G.append('E','F',2)

"""
Exam
G.append('A','B',1)
G.append('A','D',3)
G.append('A','F',8)
G.append('B','D',1)
G.append('B','E',4)
G.append('B','C',2)
G.append('D','C',2)
G.append('D','E',2)
G.append('C','E',2)
G.append('C','F',4)
G.append('E','F',2)
"""
G.Data_format()

Cost, Path=G.Djisktra('F','B')

print("The shortest path is ",Path[::-1]," with a cost of ",Cost)

   
#print(sys.maxsize)

#print(sorted(dic))


        
 
