package suanfa;

public class FixedCapacityStackOfStrings<Item> {
	private int N;
	private Item[] a;
	public FixedCapacityStackOfStrings(int cap){
		N = 0;
		a = (Item[]) new Object[cap];
	}
	public void push(Item item){
		a[N++] = item;
	}
	public Item pop(){
		return a[--N];
	}
	public int size(){
		return N;
	}
	public boolean isEmpty(){
		return N==0;
	}
	
	
	
	public static void main(String argv[]){
		
	}

}
