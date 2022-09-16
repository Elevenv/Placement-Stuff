import java.util.Arrays;

public class MedianSortedArrays {
    public static void main(String args[]){
        int arr1[] = {1,2};
        int arr2[] = {3,4};
        int arr3[] = new int[arr1.length+arr2.length];
        int arr1Length = arr1.length;
        int arr2Length = arr2.length;
        for(int i=0;i<arr1Length;i++){
            arr3[i] = arr1[i];
        }
        for(int i=0;i<arr2Length;i++){
            arr3[arr1Length + i] = arr2[i];
        }
        int n = arr3.length;
        Arrays.sort(arr3);
        if(n%2!=0)
            System.out.println(arr3[n/2]);
        else{
            System.out.println((double)(arr3[(n - 1) / 2] + arr3[n / 2]) / 2.0);
        }
    }
}
