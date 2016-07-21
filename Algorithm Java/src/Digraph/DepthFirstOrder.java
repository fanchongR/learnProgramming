package Digraph;

public class DepthFirstOrder {
	private boolean[] marked;
	private Queue<Integer> pre;
	private Queue<Integer> post;
	private Stack<Integer> reversePost;
	
	public DepthFirstOrder(Digraph G){
		marked = new boolean[G.V()];
		pre = new Queue<Integer>();
		post = new Queue<Integer>();
		reversePost = new Stack<Integer>();
		
		for(int i=0;i<G.V();i++){
			if(!marked[i])dfs(G,i);
		}
	}
	
	private void dfs(Digraph G, int v){
		marked[v] = true;
		pre.enqueue(v);
		for(int w:G.adj(v)){
			if(!marked[w]){
				dfs(G,w);
			}
		}
		post.enqueue(v);
		reversePose.push(v);
	}
	
	public Iterable<Integer> reversePost(){return reversePost;}
}
