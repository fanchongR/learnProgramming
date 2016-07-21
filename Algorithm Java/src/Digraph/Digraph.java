package Digraph;

public abstract class Digraph {
	private final int V;
	private int E;
	private Bag<Integer>[] adj;
	
	public Digraph(int V)
	{
		this.V = V;
		this.E = 0;
		adj = (Bag<Integer>()) new Bag[V];
		for(int v=0;v<V;v++)
		{
			adj[v] = Bag<Integer>();
		}
	}
	public int E(){return E;}
	public int V(){return V;}
	public void addEdge(int v, int w )
	{
		adj[v].add(w);
		E++;
	}
	
	public Iterable<Integer> adj(int v){return adj[v];}
	
	public Digraph reverse()
	{
		Digraph R = new Digraph(V);
		for(int v=0;v<V;v++)
		{
			for(int w:adj(v)){R.addEdge(w,v);}
			
		}
		return R;
	}
}
