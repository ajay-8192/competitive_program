#include <bits/stdc++.h>
using namespace std;
#define NUM_V 4

bool helper(list<int> *graph, int u, bool *visited, bool *recStack) {
	visited[u] = true;
	recStack[u] = true;
	
	for(auto i : graph[u]) {
		if(recStack[i])
			return true;
		else if(u == i)
			return true;
		else if(!visited[i]){
			if(helper(graph, i, visited, recStack))
				return true;
		}
	}
	
	recStack[u] = false;
	return false;
}

bool isCyclic(list<int> *graph, int V) {
	bool visited[V];
	bool recStack[V];
	
	for(int i = 0; i < V; i++)
		visited[i] = false,recStack[i] = false;
	
	for (int u = 0;u < V; u++){
		if(!visited[u]){
			if(helper(graph, u, visited, recStack))
				return true;
		}
	}
	return false;
}

int main() {
	list<int> *graph = new list<int> [NUM_V];
	graph[0].push_back(1);
	graph[0].push_back(2);
	graph[1].push_back(2);
	graph[2].push_back(0);
	graph[2].push_back(3);
	graph[3].push_back(3);
	cout << isCyclic(graph, NUM_V) << endl;
	return 0;
}