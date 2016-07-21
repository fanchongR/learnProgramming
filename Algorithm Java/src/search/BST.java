//支持高效的插入操作，需要链式结构。但单链无法支持二分查找，因为没有下标索引，要找到中间元素
//只能遍历链表。这时候结合二分查找的效率和链表的灵活性，需要二叉查找树
//rank select delete操作也很高效
//二叉查找树的性能依赖于插入键的顺序是否足够随机，但这取决于实际应用情况，不可控

package search;

public class BST<Key extends Comparable <Key>,Value> {
	private class Node{
		Node left;
		Node right;
		Key key;
		Value val;
		int N;
		public Node(Key key, Value val, int N){ this.key=key;this.val=val;this.N=N; }
	}
	
	private Node root;
	public int size(){ return size(root); }
	private int size(Node x){ 
		if(x==null)return 0;
		else return x.N; 
		}
	
	public Value get(Key key){
		return get(key,root);
	}
	private Value get(Key key, Node x){
		if(x == null) return null;
		int cmp = key.compareTo(x.key);
		if( cmp > 0 )return get(key,x.right);
		else if( cmp < 0 ) return get(key,x.left);
		else return x.val;
	}
	public void put(Key key, Value val){          //PS
		root = put(key,val,root);
	}
	private Node put(Key key, Value val, Node x){
		if(x==null)return new Node(key,val,1);
		int cmp = key.compareTo(x.key);
		if(cmp > 0)x.right = put(key,val,x.right);
		else if (cmp < 0)x.left = put(key,val,x.left);
		else x.val = val;
		x.N = size(x.left) + size(x.right) + 1;
		return x;
	}
	
	public Key min(){
		return min(root).key;
	}
	private Node min(Node x){
		if(x.left!=null)return min(x.left);
		else return x;
	}
	
	public Key floor(Key key){
		Node x = floor(key,root);
		if(x==null)return null;
		else return x.key;
	}
	private Node floor(Key key, Node x){
		if(x==null)return null;
		int cmp = key.compareTo(x.key);
		if(cmp==0)return x;
		if(cmp < 0){return floor(key,x.left);}
		else{
			Node t = floor(key,x.right);
			if(t==null)return x;
			else return t;
		}
	}
	
	public Key select (int k){
		return select(k,root).key;
	}
	private Node select(int k ,Node x){
		if(x==null)return null;
		int t = size(x.left);
		if( t>k )return select(k,x.left);
		else if( t<k )return select(k-t-1,x.right);
		else return x;
	}
	
	public int rank(Key key){
		return rank(key,root);
	}
	private int rank(Key key, Node x){
		if(x==null)return 0;
		int cmp = key.compareTo(x.key);
		if(cmp<0)return rank(key,x.left);
		else if (cmp>0)return size(x.left) + 1 + rank(key,x.right);
		else return size(x.left);
	}
	
	public void deleteMin(){
		root = deleteMin(root);
	}
	private Node deleteMin(Node x){
		if(x.left==null)return x.right;
		x.left = deleteMin(x.left);
		x.N = size(x.left) + size(x.right) + 1;
		return x;
	}
	
	public void delete(Key key){
		root = delete(key,root);
	}
	private Node delete(Key key, Node x){
		if(x==null) return null;
		int cmp = key.compareTo(x.key);
		if(cmp < 0)x.left = delete(key,x.left);
		else if (cmp > 0)x.right = delete(key,x.right);
		else{
			if(x.left==null)return x.right;
			else if(x.right==null)return x.left;
			else{
				x.val = min(x.right).val;
				x.right = deleteMin(x.right);       //这里不return x 要更新size
			}
		}
		x.N = size(x.right)+size(x.left)+1;
		return x;
	}
	
	public Iterable<Key> Keys(){
		return keys(min(),max());
	}
	public Iterable<Key> Keys(Key lo,Key hi){
		Queue<Key> queue = new Queue<Key>();
		keys(root,queue,lo,hi);
		return queue;
	}
	private void keys(Node x,Queue<Key> queue,Key lo,Key hi){
		if(x==null)return ;
		int cmplo = lo.compareTo(x.key);
		int cmphi = hi.compareTo(x.key);
		if(cmplo<0)keys(x.left,queue,lo,hi);
		if(cmplo<=0 && cmphi>=0)queue.enqueue(x.key);
		if(cmphi>0)keys(x.right,queue,lo,hi);
	}
}
