package graph;

public class BreadFirstPaths {
	private boolean[] marked;
	private int edgeTo[];
	private final int s;
	
	public BreadFirstPaths(Graph G, int s)
	{
		marked = new boolean[G.V()];
		edgeTo = new int[G.V()];
		this.s = s;
		bfs(G,s);
	}
	private void bfs(Graph G, int s)
	{
		Queue<Integer> queue = new Queue<Integer>();
		marked[s] = true;
		queue.enqueue(s);
		while(!queue.isEmpty())
		{
			int v = queue.dequeue();
			for(int w:G.adj(v))
			{
				if(!marked[v])
				{
					edgeTo[w] = v;
					marked[w] = true;
					queue.enqueue(w);
				}
			}
		}	
	}
	
	

}
