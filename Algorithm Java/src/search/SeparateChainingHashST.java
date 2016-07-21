//������еļ�����С������������һ��������ʵ��������ű�
//ɢ�б����㷨��ʱ��Ϳռ���Ȩ��ľ�������
//ɢ�к���    һ����  ��Ч�� ������
//������  ����̽�ⷨ
//M������ N����   δ���в��ҺͲ���ıȽϴ���Ϊ ~N/M
//��������������ű�����ĳ����Χ�ļ������������С�ļ��������ʣ������Ե�

package search;

public class SeparateChainingHashST {
	private int N;
	private int M;
	private SequentialSearchST<Key,Value>[] st;
	
	public SeparateChainingHashST(){this(997);}
	public SeparateChainingHashST(int M){
		this.M = M;
		st = (SequentialSearchST<Key,Value>[]) new SequentialSearchST[M];
		for(int i=0;i<M;i++){
			st[i] = new SequentialSearchST();
		}
	}
	
	private int hash(Key key){return (key.hashCode() & 0x7fffffff) % M;}
	
	public Value get(Key key){ return (Value) st[hash(key)].get(key); }
	public void put(Key key){ st[hash(key)].put(key,val); }
}

