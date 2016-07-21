//get是logN put是N put还是太慢了。查找是很快，但是如果要同时支持查找和插入（还有删除）的混合操作，
//二分查找还是太慢了

package search;

public class BinarySearchST <Key extends Comparable<Key>,Value>{
	private Key keys[];
	private Value vals[];
	private int N;
	
	public BinarySearchST (int num){
		keys = (Key[]) new Object[num];
		vals = (Value[]) new Object[num];
	}
	public int size(){ return N; }
	
	public int rank(Key key){
		int lo = 0;
		int hi = N-1;
		while(lo <= hi){
			int mid = (lo+hi)/2;
			int cmp = key.compareTo( keys[mid] );
			if(cmp < 0)hi = mid - 1;
			else if(cmp > 0) lo = mid + 1;
			else return mid;
		}
		return lo;
	}
	public Value get(Key key){
		if(N==0)return null;
		int i = rank(key);
		if(i < N && keys[i].compareTo(key)==0)return vals[i];
		else return null;
	}
	public void put(Key key, Value val){
		int i = rank(key);
		if(i < N && keys[i].compareTo(key)==0){
			vals[i] = val;
		}
		else{
			for(int j = N-1;j>i;j--){
				keys[j] = keys[j-1];
				vals[j] = vals[j-1];
			}
			keys[i] = key;
			vals[i] = val;
			N++;
		}
	}
	public void delete(Key key){
		
	}

}
