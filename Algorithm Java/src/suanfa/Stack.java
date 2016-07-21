package suanfa;

import java.util.Iterator;
public class Stack<Item> {
	private int N;
	private class Node{
		Item item = null;
		Node next = null;
	}
	private Node first;
	
	public int size(){return N;}
	public boolean isEmpty(){return N == 0;}
	public void push(Item item){
		Node oldfirst = first;
		first = new Node();
		first.item = item;
		first.next = oldfirst;
		N += 1;
	}
	public Item pop(){
		Item temp = first.item;
		first = first.next;
		N -= 1;
		return temp;
	}
	

}
