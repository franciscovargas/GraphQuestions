import java.lang.Math.*;

public class Heap<T extends Comparable<T>>{

    private T[] arr; // dynamic heap array
    
    public int heap_size = 0; // number of non leave nodes

    Heap(T[] arr2){

        //times 2 for dynamic array, implemented as vector
        arr =(T[]) new Comparable[2*arr2.length ];

        // instantiating heap with array
        for(int i=0; i < arr2.length; i++)
            insert(arr2[i], i);

    }

    private void dynamicArrayResize(int size){
        T[] tmp = arr;
        this.arr =(T[]) new Comparable[size];
        for(int i =0 ; i < arr.length; i++)
            arr[i] = tmp[i];
    }

    public void insert(T elem, int e){
        int v =  heap_size;
        int parent = (int) Math.floor((v-1)/2);

        while(v != 0 && elem.compareTo(arr[parent]) < 0){
            arr[v] = arr[parent];
            v = parent;
            parent = (int) Math.floor((v-1)/2);
        }
        arr[v] = elem;
        heap_size ++;
        if (heap_size == arr.length)
            dynamicArrayResize(2*heap_size);
    }

    public void heapify(int v){
        int tmp = v;
        int l =  (2*(v) + 1);
        int r =  (2*(v) + 2);
        if (l < heap_size &&
            arr[l].compareTo(arr[v]) < 0){
            tmp = l;
        }
        if (r < heap_size &&
            arr[r].compareTo(arr[tmp]) < 0){
            tmp = r;
        }
        if(tmp != v){
            T it = arr[tmp];
            arr[tmp] = arr[v];
            arr[v] = it;
            heapify(tmp);
        }       
    }

    public void removeMin(){
        System.out.println("Heapop!: " + arr[0]);
        arr[0] = arr[heap_size-1];
        arr[heap_size] = null;
        heap_size--;
        heapify(0);
        if ( arr.length > 3*heap_size + 1 )
            dynamicArrayResize(2*heap_size);
    }

    public static void main(String[] args){
        Integer[] arr =  {3, 5, 1, 4 ,2};
        Heap heap = new Heap(arr);
        for(int i=0; i < arr.length; i++)
            heap.removeMin();
    
        System.out.println("Finished running heap 1 \n");

        Character[] arr2 = {'c', 'e', 'a', 'd', 'b'};

        Heap heap2 = new Heap(arr2);
        for(int i=0; i < arr2.length; i++)
            heap2.removeMin();

        System.out.println("Finished running heap 2");
    }

}
