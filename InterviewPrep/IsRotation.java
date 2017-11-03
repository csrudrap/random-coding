import java.util.*;
public class IsRotation {
    public static void main(String[] args) {
        // NOTE: The following input values will be used for testing your solution.
        int[] array1 = {1, 2, 3, 4, 5, 6, 7};
        int[] array2a = {4, 5, 6, 7, 8, 1, 2, 3};
        System.out.println(isRotation(array1, array2a)); // should return false.
        int[] array2b = {4, 5, 6, 7, 1, 2, 3};
        System.out.println(isRotation(array1, array2b)); //should return true.
        int[] array2c = {4, 5, 6, 9, 1, 2, 3};
        // isRotation(array1, array2c) should return false.
        int[] array2d = {4, 6, 5, 7, 1, 2, 3};
        // isRotation(array1, array2d) should return false.
        int[] array2e = {4, 5, 6, 7, 0, 2, 3};
        // isRotation(array1, array2e) should return false.
        int[] array2f = {1, 2, 3, 4, 5, 6, 7};
        // isRotation(array1, array2f) should return true.
    }

    // Implement your solution below.
    public static Boolean isRotation(int[] array1, int[] array2) {
        if (array1.length != array2.length) {
            return false;
        }
        if (array1.length == 0 || array1.length == 1) {
            return true;
        }
        ArrayList<Integer> arr2Indices = new ArrayList<Integer>();
        for (int i = 0; i < array2.length; i++) {
            if (array2[i] == array1[0]) {
                arr2Indices.add(i);
            }
        }
        int count = 0;
        for (int index: arr2Indices) {
            count = 0;
            int diff = index; // index - 0, because the index we're looking at in arr1 is 0.
            for (int j = 0; j < array1.length; j++) {
                if (array1[j] != array2[(j + diff) % array1.length]) {
                    break;
                }
                count++;
            }
            if (count == array1.length) {
                return true;
            }
        }
        return false;
    }
}

