package suanfa;

public class FixedCapacityStack<Item> {
	private Item[] a;
	private int N;
	public FixedCapacityStack(int cap){
		a = (Item[]) new Object[cap];
	}
	public boolean isEmpty(){
		return N==0;
	}
	public int size(){
		return N;
	}
	
	public void resize(int max){
		Item[] temp = (Item[]) new Object[max];
		for(int i=0;i<N;i++){
			temp[i] = a[i];
		}
		a = temp;
	}
	public void push(Item item){
		if(N == a.length)resize(2*a.length);
		a[N++] = item;
	}
	public Item pop(){
		Item item =  a[--N];
		if(N>0 && N == a.length/4)resize(a.length/2);
		return item;
	}
}
