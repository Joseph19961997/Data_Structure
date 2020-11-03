# -*- coding: utf-8 -*-
"""https://www.geeksforgeeks.org/topological-sorting/
"""

from collections import defaultdict 


#Djisktra algorithm 
#This code might not be handling self loops- Need to verify

import sys
class Graph():
    def __init__(self,v):
        self.graph={} #Abstraction of the grpah in a dictionary
        self.path=[] #shortest distance from source to all vertices -doesn't calculate path information
        self.c=0 #keep track of the current cost
        self.V=v #total number of vertices in the graph
        self.A_node=[] #self.A_node=['A','B','C','D','E','F']
        self.A_node_i={} #self.A_node_i={0:'A',1:'B',2:'C',3:'D',4:'E',5:'F'} #from int to node
        self.A_node_j={} #self.A_node_j={'A':0,'B':1,'C':2,'D':3,'E':4,'F':5} #from node to int
        
    def Data_format(self):
        #1- Store all nodes in a list
        for i, j in enumerate(self.graph):
            self.A_node.append(j) 
            self.A_node_i[i]=j 
            self.A_node_j[j]=i 
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
    def Djisktra(self,node):
        dist = [sys.maxsize] * len(self.A_node) #list containing the distance of each node (initially infinity)
        return self.Djisktra_helper(node,dist) #return the shortance distance from source to all vertices
     
        
    def Djisktra_helper(self,node,dist):
        self.path.append(node) 
        if(len(self.path)==self.V): #once we have all nodes in the path- return the path
            return self.path
        
        
        for j in self.graph[node]: #loop through every neighbour of the node 
            if(j not in self.path): #that is not already in the path
                n_cost=self.graph[node][j]+self.c# compute new cost
                o_cost=dist[self.A_node_j[j]] #old cost
                #if the new cost is smaller than the old cost/dist, update dist otherwise, keep the current cost/dist
                dist[self.A_node_j[j]]=self.graph[node][j]+self.c  if n_cost<dist[self.A_node_j[j]] else o_cost #update the new cost
        
        n_node=self.shortest_path(dist) #Now, choose the shortest path
        return self.Djisktra_helper(n_node,dist) #repeat with next node
            
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
"""
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
G.Data_format()


print(G.Djisktra('A'))     



        
 
