package weightedgraph;

public class EdgeWeightedGragh {
	private final int V;
	private int E;
	private Bag<Edge>[] = adj;
	
	public EdgeWeightedGragh(int V){
		this.V = V;
		this.E = 0;
		adj = (Bag<Edge>[]) new Bag[V];
		for(int i=0;i<V;i++){
			adj[i] = new Bag<Edge>[];
		}
	}
	
	public void addEdge(Edge e){
		int first = e.either();
		int second = e.other(first);
		adj[first].add(e);
		adj[second].add(e);
		E++;
	}
	
	public int V(){return V;}
	public int E(){return E;}
	public Iterable<Edge> adj(int v){return adj[v];}
	public Iterable<Edge> edges(){
		
	}
}
