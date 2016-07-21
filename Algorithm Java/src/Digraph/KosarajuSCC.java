package Digraph;

public class KosarajuSCC {
	private boolean[] marked;
	private int[] id;
	private int count;
	
	public KosarajuSCC(Digraph G){
		...
	}
	
	private void dfs(Digraph G,int v){
		marked[v] = true;
		id[v] = count;
		for(int w:G.adj(v)){
			if(!marked[w])dfs(G,w);
		}
	}
	
	public boolean stronglyConnected(int v, int w){
		return id[v]==id[w];
	}
}
