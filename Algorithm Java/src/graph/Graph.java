package graph;

public class Graph {
	private final int V;
	private int E;
	private Bag<Integer>[] adj;
	
	public Graph(int V){
		this.V = V; E = 0;
		for(int i=0;i < V;i++){
			adj[i] = Bag<Integer>[]; 
		}
	}
	
	public Graph(In in)
	{
		this(in.readInt());
		int E = in.readInt();
		for(int i=0; i<E; i++)
		{
			int v = in.readInt();
			int w = in.readInt();
			addEdge(v,w);
		}
	}
	public int V(){return V;}
	public int E(){return E;}
	
	public void addEdge(v,w)
	{
		adj[v].add(w);
		adj[w].add(v);
	}
	
	public Iterable<Integer> adj(int v){return adj[v];}
}
