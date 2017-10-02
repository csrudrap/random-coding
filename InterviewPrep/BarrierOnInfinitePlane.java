import java.util.*;

/*Input : barriers[] = {{3 6 2}, {-7 4 3}
Output : 14
The barrier from 3 to 6 blocks 3, 4, 5, 6, 
so 4 persons blocked till now.
The barrier from -7 to 4 blocks -7,-6,-5,-4,-
3, -2, -1, 0, 1, 2, 3, 4. But, 3 and 4 have 
already been blocked.
So, total persons blocked is 14.
*/

public class BarrierOnInfinitePlane {
    public static int blockedPersons(Barrier[] barriers) {
        // Ex: {3,6,2}, {-7,4,3}
        // x1=3, x2=6, y=2
        // Get to know overlaps across arrays.
        Set<Integer> s = new HashSet<Integer>();
        for (Barrier b: barriers) {
        		for (int i = b.x1; i <= b.x2; i++) {
        			if (!s.contains(i)) {
        				s.add(i);
        			}
        		}
        }
        return s.size();
    }
    
    public static void main(String[] args) {
        Barrier b1 = new Barrier(3,6,2);
        Barrier b2 = new Barrier(-7,4,3);
        Barrier[] bArr = {b1, b2};
        int p = blockedPersons(bArr);
        System.out.println(p);
    }
}
class Barrier {
    int x1;
    int x2;
    int y;
    public Barrier(int x1, int x2, int y) {
        this.x1 = x1;
        this.x2 = x2;
        this.y = y;
    }
}



