//有序线性表,当元素按递增次序排列,
//删除时间均为( 1 ),插入操作所需时间为(n).

package sort;

public class PQprimary {
	private class Node{
		int item;
		Node next;
	}
	private int N;
	private Node first;
	
	public int delMax(){
		int temp = first.item;
		first = first.next;
		N -= 1;
		return temp;		
	}
	public void insert(int item){
		if(N==0){
			first = new Node();
			first.item = item;
		}
		else if(first.item < item){
			Node oldfirst = first;
			Node first = new Node();
			first.item = item;
			first.next = oldfirst;
		}
		else{
			Node i = first;
			while( i.next != null && i.next.item >= item ){
				i = i.next;
			}
			Node j = i.next;
			Node temp = new Node();
			temp.item = item;
			i.next = temp;
			temp.next = j;
		}
		N += 1;
	}
	
	
	public static void main(String argv[]){
		PQprimary a = new PQprimary();
		int[] numbers = {4,5};
		for(int i=0;i<numbers.length;i++){
			a.insert(numbers[i]);
		}
		for(int i=0;i<numbers.length;i++){
			System.out.println(a.delMax());
		}
		
	}
	

}
