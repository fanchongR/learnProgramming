package edgeweighteddigraph;

public class EdgeWeightedDigraph {
	private final int V;
	private int E;
	private Bag<DirectedEdge>[] adj;
	
	public EdgeWeightedDigraph(int V){
		this.V = V;
		this.E = 0;
		adj = (Bag<DirectedEdge>[]) new Bag[V];
		for(i=0;i<V;i++){
			adj[i] = new Bag<DirectedEdge>();
		}
	}
	
	public int V(){return V;}
	public int E(){return E;}
	public void addEdge(DirectedEdge e){
		adj[e.from()].add(e);
		E++;
	}
	public Iterable<Edge> adj(int v){return adj[v];}
	
	public Iterable<Edge> edges(){
		Bag<DirectedEdge> bag = new Bag<DirectedEdge>();
		for(v=0,v<V;v++){
			for(DirectedEdge e:adj[v])bag.add(e);
		}
		return bag;
	}
}
