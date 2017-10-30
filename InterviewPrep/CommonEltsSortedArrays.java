// Given 2 arrays, return an array of all the common elements.
// Hint: Similar approach to merge of mergesort. 
import java.util.*;

class CommonEltsSortedArrays {
    public static void main(String[] args) {
        int[] A1 = {1,3,4,6,7,9};
        int[] B1 = {1,2,4,5,9,10};
        printList(commonElements(A1, B1));
    
        int[] A2 = {1,4,5,11,15,18,22,23,27,30};
        int[] B2 = {2,3,5,6,7,9,11,13,14,16,19,22,26,28,30,38};
        printList(commonElements(A2, B2));
    }
    
    public static void printList(Integer[] arr) {
        for (Integer i: arr) {
            System.out.print(i.intValue() + "\t");
        }
        System.out.println("\n");
    }

    public static Integer[] commonElements(int[] A, int[] B) {
        List<Integer> commonList = new ArrayList<Integer>();
        int i = 0;
        int j = 0;
        while (i < A.length && j < B.length) {
            if (A[i] == B[j]) {
                commonList.add(A[i]);
                i++;
                j++;
            } else if (A[i] < B[j]) {
                i++;
            } else {
                j++;
            }
        }
        Integer[] commonArr = new Integer[commonList.size()];
        commonArr = commonList.toArray(commonArr);
        return commonArr;
    }
}

