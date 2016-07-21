//如果所有的键都是小整数，可以用一个数组来实现无序符号表
//散列表是算法在时间和空间上权衡的经典例子
//散列函数    一致性  高效性 均匀性
//拉链法  线性探测法
//M条链表 N个键   未命中查找和插入的比较次数为 ~N/M
//拉链法是无序符号表，查找某个范围的键，查找最大最小的键都不合适，是线性的

package search;

public class SeparateChainingHashST {
	private int N;
	private int M;
	private SequentialSearchST<Key,Value>[] st;
	
	public SeparateChainingHashST(){this(997);}
	public SeparateChainingHashST(int M){
		this.M = M;
		st = (SequentialSearchST<Key,Value>[]) new SequentialSearchST[M];
		for(int i=0;i<M;i++){
			st[i] = new SequentialSearchST();
		}
	}
	
	private int hash(Key key){return (key.hashCode() & 0x7fffffff) % M;}
	
	public Value get(Key key){ return (Value) st[hash(key)].get(key); }
	public void put(Key key){ st[hash(key)].put(key,val); }
}

