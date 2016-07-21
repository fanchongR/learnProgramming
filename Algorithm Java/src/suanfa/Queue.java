package suanfa;

import java.util.Iterator;
public class Queue<Item> implements Iterable<Item>{
	private class Node{
		Item item;
		Node next;
	}
	private int N;
	private Node first;
	private Node last;
	
	public int size(){return N;}
	public boolean isEmpty(){ return N==0;}
	public void enqueue(Item item){
		Node oldlast = last;
		last = new Node();
		last.item = item;
		last.next = null;
		if(N==0)first = last;
		else oldlast.next = last;
		N += 1;
	}
	public Item dequeue(){
		Item temp = first.item;
		first = first.next;
		N -= 1;
		if(N==0)last = null;
		return temp;
	}
	
	
	public Iterator<Item> iterator(){
		return new ListIterator();
	}
	private class ListIterator implements Iterator<Item>{
		private Node current = first;
		public boolean hasNext(){ return current!=null; }
		public void remove(){}
		public Item next(){
			Item item = current.item;
			current = current.next;
			return item;
		}
		
	}
	
	
	
	
	
	public static void main(String argv[]){
		Queue a = new Queue();
		a.enqueue(4);
		a.enqueue(7);
		System.out.println(a.dequeue());
		System.out.println(a.dequeue());
	}
}
