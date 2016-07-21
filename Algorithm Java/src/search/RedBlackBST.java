//查找和插入都是对数级别，删除也是
//最复杂的代码仅限于put和delete，BST中的查找最大最小键，select,rank,floor,ceiling和范围查找
//不做任何改动就能用。因为红黑树也是二叉查找树而这些操作不涉及颜色。
//除开范围查找，其他操作都是对数级别

package search;


public class RedBlackBST<Key extends Comparable <Key>,Value> {
	private final boolean RED = true;
	private final boolean BLACK = false;
	private Node root;
	
	
	private class Node{
		Key key;
		Value val;
		Node left;
		Node right;
		boolean color;
		int N;
		Node(Key key,Value val,int N,boolean color){
			this.key = key;
			this.val = val;
			this.N = N;
			this.color = color;
		}
	}
	
	private boolean isRed(Node x){
		if(x==null)return false;
		return x.color==RED;
	}
	
	Node rotateLeft(Node h){
		Node x = h.right;
		h.right = x.left;
		x.left = h;
		x.color = h.color;
		h.color = RED;
		x.N = h.N;
		h.N = size(h.left) + size(h.right) + 1;
		return x;
	}
	Node rotateRight(Node h){
		Node x = h.left;
		h.left = x.right;
		x.right = h;
		x.color = h.color;
		h.color = RED;
		x.N = h.N;
		h.N = size(h.left) + size(h.right) + 1;
		return x;
	}
	void flipColors(Node h){
		h.left.color = BLACK;
		h.right.color = BLACK;
		h.color = RED;
	}
	
	public int size(){ return size(root); }
	private int size(Node x){ 
		if(x==null)return 0;
		else return x.N; 
	}
	
	public void put(Key key, Value val){
		root = put(root,key,val);
		root.color = BLACK;
	}
	private Node put(Node h,Key key,Value val){
		if(h==null)return new Node(key,val,1,RED);
		int cmp = key.compareTo(h.key);
		if(cmp<0)h.left = put(h.left,key,val);
		else if (cmp>0)h.right = put(h.right,key,val);
		else h.val = val;
		
		if( isRed(h.right) && !isRed(h.left) ) h = rotateLeft(h);
		if( isRed(h.left) && isRed(h.left.left) ) h = rotateRight(h);
		if( isRed(h.left) && isRed(h.right) ) flipColors(h);
		h.N = size(h.left) + size(h.right) + 1;
		return h;
	}
	
}
