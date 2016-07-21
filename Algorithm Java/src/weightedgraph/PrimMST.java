package weightedgraph;

public class PrimMST {
	private double[] distTo;
	private Edge[] edgeTo;
	private boolean[] marked;
	private IndexMinPQ<Double> pq;
	
	public PrimMST(EdgeWeightedGraph G){
		distTo = new double[G.V()];
		edgeTo = new Edge[G.V()]
		marked = new boolean[G.V()];
		for(int v=0;v<G.V();v++){
			distTo[v] = DOUBLE.POSITIVE_INFINITY;
		}
		pq = new IndexMinPQ<Double>(G.V());
		
		distTo[0] = 0.0;
		pq.insert(0,0.0)
		while(!pq.isEmpty()){
			visit(G,pq.delMin());
		}
		
	private void visit(EdgeWeightedGraph G, int v){
		marked[v] = true;
		for(Edge e:G.adj(v)){
			int w = e.other(v);
			if(marked[w])continue;
			if(e.weight() < distTo[w]){
				edgeTo[w] = e;
				distTo[w] = e.weight();
				if(pq.contains(w))pq.change(w,distTo(w));
				else pq.insert(w,distTo[w]);
			}
		}
	}
	
	public Iterable<Edge> edges(){return mst;}
	public double weight()
}
