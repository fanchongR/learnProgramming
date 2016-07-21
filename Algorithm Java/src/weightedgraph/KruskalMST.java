package weightedgraph;

public class KruskalMST {
	private Queue<Edge> mst;
	
	public KruskalMST(EdgeWeightedGraph G){
		mst = new Queue<Edge>();
		MinPQ<Edge> pq = new MinPQ<Edge>(G.edges());
		UF uf = new UF(G.V());
		
		while(!pq.isEmpty() && mst.size() < G.V()-1){
			Edge e = pq.delMin();
			int v = e.either(); int w = e.other(v);
			if(uf.connected(v,w))continue;
			uf.union(v,w);
			mst.enqueue(e);
		}
	}
}
