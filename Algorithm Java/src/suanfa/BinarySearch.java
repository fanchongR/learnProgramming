package suanfa;

import java.util.Arrays;
public class BinarySearch{
	public static int rank(int key,int[] a){
		int lo = 0;
		int hi = a.length -1;
		while(lo<=hi){
			int mid = lo + (hi-lo)/2;
			if(key>a[mid])lo = mid;
			else if(key<a[mid])hi = mid;
			else return mid;
		}
		return -1;
	}
	
	public static void main(String[] args){
		int[] a = {1,2,4,6,7,9};
		int temp = rank(2,a);
		System.out.println(temp);
	}
	
}

