
import java.util.*;
import java.io.*;

public class Main {
    static StringBuilder sb = new StringBuilder();

    static class DoubleI implements Comparable<DoubleI> {
        int abs;
        int val;

        public DoubleI(int a, int b) {
            this.abs = a;
            this.val = b;
        }

        @Override
        public int compareTo(DoubleI a) {
            if (this.abs != a.abs)
                return this.abs - a.abs;
            return this.val - a.val;
        }

    }

    public static void main(String[] args) throws IOException {
        PriorityQueue<DoubleI> pq = new PriorityQueue<>();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N; ++i) {
            int command = Integer.parseInt(br.readLine());
            if (command == 0) {
                if (pq.isEmpty()) {
                    sb.append("0\n");
                } else {
                    sb.append(pq.poll().val + "\n");
                }
            } else {
                if (command < 0)
                    pq.add(new DoubleI(command * -1, command));
                else
                    pq.add(new DoubleI(command, command));
            }
        }
        System.out.println(sb.toString());
    }
}
