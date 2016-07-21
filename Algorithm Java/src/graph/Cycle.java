package graph;

import practise.Graph;
import practise.graph;
##bug
public class Cycle {
	private boolean[] mark;	
	private boolean hasCycle;
	
	public Cycle(graph g){
		mark = new boolean[g.V()];
		for(int v=0;v<g.V();v++){
			if(hasCycle == false){
				mark[v] = true;
				dfs(g,v);
			}
		}
	}

	dfs(Graph g,int v){
		for(int i:g.adj(v)){
			if(mark[i]==false){
				mark[i] = true;
				dfs(g,i);
			}else{
				hasCycle = true;
			}
		}
	}
	
}
