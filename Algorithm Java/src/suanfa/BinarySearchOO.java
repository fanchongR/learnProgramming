package suanfa;

import java.util.Arrays;
public class BinarySearchOO{
	private int[] numbers;
	public BinarySearchOO(int[] a){
		numbers = new int[a.length];
		for(int i=0;i<a.length;i++){
			numbers[i]=a[i];
		}
		Arrays.sort(numbers);
	}
	public int contains(int key){
		return rank(key);
	}
	public int rank(int key){
		int start=0;
		int end=numbers.length-1;
		while(start<=end){
			int mid = (start+end)/2;
			if(numbers[mid]>key)end=mid-1;
			else if(numbers[mid]<key)start=mid+1;
			else return mid;
		}
		return -1;
	}
	
	
	public static void main(String args[]){
		int[] a = {1,2,4,5,7,9,10};
		BinarySearchOO aa = new BinarySearchOO(a);
		System.out.println(aa.rank(10));
	}
}




