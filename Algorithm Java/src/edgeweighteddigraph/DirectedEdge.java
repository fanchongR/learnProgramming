package edgeweighteddigraph;

public class DirectedEdge {
	private int v;
	private int w;
	private double weight;
	
	public DirectedEdge(int v,int w,double weight){
		this.v = v;
		this.w = w;
		this.weight = weight;
	}
	
	public double weight(){return this.weight;}
	public int from(){return this.v;}
	public int to(){return this.w;}
	
	public String toString(){
		return String.format("%d->%d %.2f",v,w,weight);
	}
}
