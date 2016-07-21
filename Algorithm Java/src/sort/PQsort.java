package sort;

public class PQsort {
	public static void exch(int[] a,int i, int j){
		int temp = a[i];
		a[i] = a[j];
		a[j] = temp;
	}
	public static boolean less(int[] a,int i,int j){
		return a[i] < a[j];
	}
	public static void sink(int[] a,int i,int N){
		while(2*i <= N){
			int temp = 2*i;
			if(temp < N && less(a,temp,temp+1))temp += 1;
			if(less(a,temp,i))break;
			exch(a,i,temp);
			i = temp;
		}
	}
	public static void pqsort(int[] a){
		int N = a.length-1;
		for(int i=N/2;i>0;i--) sink(a,i,N);
		
		for(int i = N;i>1;i--){
			exch(a,1,N--);
			sink(a,1,N);
		}
		
	}
	
	
	public static void main(String argv[]){
		int[] a ={100,8,5,1,3,30,8,6,3,10,2};
		pqsort(a);
		for(int i=0;i<a.length;i++){
			System.out.println(a[i]);
		}
	}
}
