import java.util.HashMap;

public class MostFrequentInArr {
    public static void main(String[] args) {
        // NOTE: The following input values are used for testing your solution.

        // mostFrequent(array1) should return 1.
        int[] array1 = {1, 3, 1, 3, 2, 1};
        System.out.println(mostFrequent(array1));
        // mostFrequent(array2) should return 3.
        int[] array2 = {3, 3, 1, 3, 2, 1};
        System.out.println(mostFrequent(array2));
        // mostFrequent(array3) should return null.
        int[] array3 = {};
        System.out.println(mostFrequent(array3));
        // mostFrequent(array4) should return 0.
        int[] array4 = {0};
        System.out.println(mostFrequent(array4));
        // mostFrequent(array5) should return -1.
        int[] array5 = {0, -1, 10, 10, -1, 10, -1, -1, -1, 1};
        System.out.println(mostFrequent(array5));
    }

    // Implement your solution below.
    public static Integer mostFrequent(int[] givenArray) {
        if (givenArray.length == 0) {
            return null;
        } else if (givenArray.length == 1) {
            return givenArray[0];
        }
        HashMap<Integer, Integer> hm = new HashMap<Integer, Integer>();
        for (int i: givenArray) {
            if (hm.containsKey(i)) {
                int toPut = hm.get(i);
                hm.remove(i);
                hm.put(i, toPut+1);
            } else {
                hm.put(i, 1);
            }
        }
        int maxKey = -1;
        int maxVal = 0;
        for (int i: hm.keySet()) {
            if (hm.get(i) > maxVal) {
                maxVal = hm.get(i);
                maxKey = i;
            }
        }
        return maxKey;
    }
}

