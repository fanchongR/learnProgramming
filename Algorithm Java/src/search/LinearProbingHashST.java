//线性探测法
//大小是M的数组 N个键 其中M>N
//利用率alpha=N/M 在1/8到1/2之间

package search;

public class LinearProbingHashST<Key,Value> {
	private int N;
	private int M=16;
	private Key[] keys;
	private Value[] vals;
	
	public LinearProbingHashST(int temp){
		M = temp;
		keys = (Key[]) new Object[M];
		vals = (Value[]) new Object[M];
	}
	
	private int hash(Key key){return (key.hashCode() & 0x7fffffff) % M;}
	private void resize(int cap){
		LinearProbingHashST<Key,Value> t;
		t = new LinearProbingHashST<Key,Value>(cap);
		for(int i;i<M;i++){
			if(keys[i]!=null)t.put(keys[i], vals[i]);
		}
		keys = t.keys;
		vals = t.vals;
		M = t.M;
	}
	
	public void put(Key key,Value val){
		if(N>=M/2)resize(2*M);
		int i;
		for(i = hash(key);keys[i]!=null;i=(i+1)%M) if(keys[i].equals(key)){ vals[i]=val;return; }
		keys[i] = key;
		vals[i] = val;
		N++;
	}
	public Value get(Key key){
		for(int i = hash(key);keys[i]!=null;i=(i+1)%M) if(keys[i].equals(key)){ return vals[i]; }
		return null;
	}
	public void delete(Key key){
		if(!contains(key))return;
		int i = hash(key);
		while(!keys[i].equals(key)){
			i = (i+1)%M;
		}
		keys[i] = null;
		vals[i] = null;
		i = (i+1)%M;
		while(keys[i]!=null){
			Key keyredo = keys[i];
			Value valredo = vals[i];
			keys[i] = null;
			vals[i] = null;
			N--;
			put(keyredo,valredo);
			i = (i+1)%M;
		}
		N--;
		if(N > 0 && N <= M/8)resize(M/2);
	}
	
}
