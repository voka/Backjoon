import java.util.*;
import java.io.*;

public class Main {
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        PriorityQueue<Integer> low = new PriorityQueue<>();
        PriorityQueue<Integer> high = new PriorityQueue<>();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        for (int i = 1; i <= N; ++i) {
            int command = Integer.parseInt(br.readLine());
            if (i == 1) {
                low.add(command * -1);
                sb.append(command + "\n");
                continue;
            }
            if (!low.isEmpty()) {
                if (low.peek() * -1 < command)
                    high.add(command);
                else
                    low.add(command * -1);
            }
            // System.out.println(low.size() + " " + high.size());
            // 개수 맞추기
            while (true) {
                if ((i % 2 == 0 && low.size() == high.size()) || (i % 2 == 1 && low.size() == high.size() + 1))
                    break;
                if (low.size() > high.size())
                    high.add(low.poll() * -1);
                else
                    low.add(high.poll() * -1);
            }
            sb.append(low.peek() * -1 + "\n");
        }
        System.out.println(sb.toString());
    }
}