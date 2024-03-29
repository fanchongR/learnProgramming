package edgeweighteddigraph;

public class DijkstraSP {
	private DirectedEdge[] edgeTo;
	private double[] distTo;
	private IndexMinPQ<Double> pq;
	
	public DijkstraSP(EdgeWeightedDigraph G, int s){
		edgeTo = new DirectedEdge[G.V()];
		distTO = new double[G.V()];
		pq = new IndexMinPQ<Double>(G.V());
		
		for(int v=0;v < G.V();v++){
			distTo[v] = Double.POSITIVE_INFINITY;
		distTo[s] = 0.0;
		pq.insert(s,0.0);
		while(!pq.isEmpty())relax(G,pq.delMin())
		}
	}
	
	private void relax(EdgeWeightedDigraph G,int v){
		for(DirectedEdge e:G.adj(v)){
			int w = e.to();
			if(distTo[w] > distTo[v] + e.weight()){
				distTo[w] = distTo[v] + e.weight();
				edgeTo[w] = e;
				if(pq.contains(w))pq.change(w,distTo[w]);
				else pq.insert(w.distTo[w]);
			}	
		}
	}
	
	
	
	
	
	
	public double distTo(int v){return distTo[v];}  //返回最短路径长度
	public boolean hasPathTo(int v){return distTo[v] < Double.POSITIVE_INFINITY;}
	public Iterable<DirectedEdge> pathTo(int v){
		if(!hasPathTo(v))return null;
		Stack<DirectedEdge> path = new Stack<DirectedEdge>();
		for(DirectedEdge e = edgeTo[v];e != null; e = edgeTo[e.from()]){
			path.push(e);
		}
		return path;
	}
	
}
