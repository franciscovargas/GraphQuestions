import java.io.*;
import java.util.*;

public class Bubble {
    
    public static void swap(int[] a, int i, int j){
        int tmp = a[i];
        a[i] = a[j];
        a[j] = tmp;
    }
    
    public static int bubbleSort(int[] arr){
        boolean isSorted = false;
        int lastSorted = arr.length -1;
        int numSwap = 0;
        while(!isSorted){
            isSorted = true;
            for(int i=0; i < lastSorted;i++){
                if(arr[i] > arr[i+1]){
                    swap(arr, i, i+1);
                    numSwap++;
                    isSorted = false;
                }
            }
            lastSorted--;
        }
        return numSwap;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int a[] = new int[n];
        for(int a_i=0; a_i < n; a_i++){
            a[a_i] = in.nextInt();
        }
        int numSwap = bubbleSort(a);
        System.out.println("Array is sorted in " + numSwap + " swaps.");
        System.out.println("First Element: " + a[0]);
        System.out.println("Last Element: "+ a[n-1]);
    }
}
