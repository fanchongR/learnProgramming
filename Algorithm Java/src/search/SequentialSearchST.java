package search;

public class SequentialSearchST <Key,Value>{
	private class Node{
		Key key;
		Value value;
		Node next;
	}
	private int N;
	private Node first;
	
	public Value get(Key key){
		for(Node i = first; i != null;i=i.next ){
			if( key.equals(i.key) )return i.value;
		}
		return null;
	}
	public void put(Key key, Value value){
		for(Node i = first; i != null; i=i.next){
			if(key.equals(i.key)){
				i.value = value;
				return ;
			}
		}
		Node oldfirst = first;
		first = new Node();
		first.key = key;			
		first.value = value;
		first.next = oldfirst;
		N += 1;		
	}
	
	public int size(){ return N; }
	public void delete(Key key){
		if(N==0)return;
		if(first.key == key){first = first.next;N--;}
		else{
			for(Node i =first; i.next != null;i=i.next ){
				if(i.next.key == key ){
					i.next = i.next.next;
					N--;
					return;
					}
			}
		}
	}
	
	
//	public keys()	

}
