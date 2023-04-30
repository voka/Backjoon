import java.util.*;
import java.io.*;

public class Main {
    static int[] _list;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stk = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(stk.nextToken());
        int M = Integer.parseInt(stk.nextToken());

        _list = new int[M];

        for (int i = 0; i < M; i++) {
            _list[i] = Integer.parseInt(br.readLine());
        }
        int start = 1, mid = 0;
        int end = (int) Math.pow(10, 9);
        while (start <= end) {
            mid = (start + end) / 2;
            if (solve(N, mid)) {
                end = mid - 1;
            } else {
                start = mid + 1;
            }
        }
        System.out.println(start);
    }

    static boolean solve(int n, int mid) {
        int cnt = 0;
        for (int i = 0; i < _list.length; ++i) {
            if (_list[i] % mid != 0) {
                cnt += (_list[i] / mid) + 1;
            } else {
                cnt += (_list[i] / mid);
            }
        }
        if (cnt <= n) {
            return true;
        } else {
            return false;
        }
    }
}