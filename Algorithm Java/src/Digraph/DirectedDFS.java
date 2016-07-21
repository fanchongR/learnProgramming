package Digraph;

public class DirectedDFS {
	private boolean[] marked;
	
	public DirectedDFS(Digraph G, int s){
		marked = new boolean[G.V()];
		dfs(G,s);
	}
	public DirectedDFS(Digraph G,Iterable<Integer> sources){
		marked = new boolean[G.V()];
		for(int s:sources){
			if(!marked[s])dfs(G,s);
		}
	}
	
	private void dfs(Digraph G, int s){
		marked[s] = true;
		for(int w:G.adj(s)){
			if(!marked[w]){
				dfs(G,w);
			}
		}
	}
	
	public boolean marked(int v){
		return marked[v];
	}
}
