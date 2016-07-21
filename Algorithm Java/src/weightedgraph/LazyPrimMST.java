package weightedgraph;

public class LazyPrimMST {
	private boolean[] marked;
	private Queue<Edge> mst;
	private MinPQ<Edge> pq;
	
	public LazyPrimMST(EdgeWeightedGraph G){
		pg = new MinPQ<Edge>();
		marked = new boolean[G.V()];
		mst = Queue<Edge>();
		
		visit(G,0);
		while(!pg.isEmpty()){
			Edge e = pq.delMin();
			int v = e.either(); int w = e.other(v);
			if(marked[v] && marked[w])continue;
			mst.enqueue(e);
			if(!makred[v]) visit(G,v);
			if(!marked[w]) visit(G,w);
		}	
	}
	private void visit(EdgeWeightedGraph G, int v){
		marked[v] = true;
		for(Edge e:G.adj(v)){
			if(!marked[e.other(v)])pq.insert(e);
		}
	}
	
	public Iterable<Edge> edges(){return mst;}
	public double weight()
}
