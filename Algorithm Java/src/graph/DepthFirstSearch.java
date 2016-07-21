package graph;

public class DepthFirstSearch {
	private boolean[] marked;
	private int count;
	
	public DepthFirstSearch(Graph G, int s)   //G是图 s是深度搜索起点
	{
		marked = new boolean[G.V()];
		dfs(G,s);
	}
	private void dfs(Graph G, int s)
	{
		marked[s] = true;
		count++;
		for(int w:G.adj(s))
		{
			if(marked[w] == false){dfs(G,w);}
		}
	}
	
	public boolean marked(int w){return marked[w];}
	public int count(){return count;}
	
	
}
