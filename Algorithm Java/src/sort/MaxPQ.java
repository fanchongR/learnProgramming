//优先队列插入和删除（最大值）元素的复杂度都是O(log2n)

package sort;

public class MaxPQ {
	private int N;
	private int[] pq;
	
	private boolean less(int i ,int j){ return pq[i] < pq[j]; }
	private void exch(int i,int j){
		int temp = pq[i];
		pq[i] = pq[j];
		pq[j] = temp;
	}
	private void swim(int k){
		while( k > 1 && less(k/2,k) ){ 
			exch(k/2,k); 
			k = k/2;
			}
	}
	private void sink(int k){
		while(2*k <= N){
			int j = 2*k;
			if(j < N && less(j,j+1))j += 1;
			if( less(j,k) ) break;
			exch(j,k);
			k = j;
		}
	}
	
	public MaxPQ(int maxN) {
		pq = new int[maxN+1];
	}
	public boolean isEmpty(){
		return N==0;
	}
	public int size(){
		return N;
	}
	public void insert(int num){
		N += 1;
		pq[N] = num;
		swim(N);
	}
	public int delMax(){
		int temp = pq[1];
		pq[1] = pq[N];
//		pq[N] = null;
		N -= 1;
		sink(1);
		return temp;
	}
}
