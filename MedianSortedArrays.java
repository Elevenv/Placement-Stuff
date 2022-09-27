import java.util.Arrays;

public class MedianSortedArrays{
    public static void main(String args[]){
        int[] nums1 = {1,3};
        int[] nums2 = {2,7};
        float res = 0;
        int n;
        int[] nums3 = new int[nums1.length+nums2.length];
        int n1Len = nums1.length;
        int n2Len = nums2.length;
        for(int i=0;i<n1Len;i++)
            nums3[i] = nums1[i];
        for(int i=0;i<n2Len;i++)
            nums3[n1Len+i] = nums2[i];
        Arrays.sort(nums3);
        n = nums3.length;
        if(n%2!=0)
            System.out.println(nums3[n/2]);
        else
            res = nums3[(n-1)/2]+nums3[n/2];
            System.out.println(res/2);
    }
}
