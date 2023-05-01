import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        int D, P;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stk = new StringTokenizer(br.readLine());
        D = Integer.parseInt(stk.nextToken());
        P = Integer.parseInt(stk.nextToken());
        int[][] _list = new int[P][2];
        for (int i = 0; i < P; ++i) {
            String[] input = br.readLine().split(" ");
            _list[i][0] = Integer.parseInt(input[0]);
            _list[i][1] = Integer.parseInt(input[1]);
        }
        int[] dp = new int[D + 1]; // 길이가 i 일때 최대 용량 dp[i]
        dp[0] = Integer.MAX_VALUE;

        for (int i = 0; i < P; ++i) {
            int curL = _list[i][0];
            int curC = _list[i][1];
            for (int j = D; j >= curL; --j) {// 최대 길이 D만 맞추면 된다. + 중복 불가
                dp[j] = Math.max(Math.min(dp[j - curL], curC), dp[j]);
                // 수도관의 용량은 수도관을 이으면 이떄의 최소값이 되기 때문에 중간에 연결하는 파이프의 용령 중 최소값을 찾아야 한다.
                // min(dp[j-L])
                // 그리고 그 최소값과 현재 저장되어 있는 값 중 최대값을 선택하면 된다.
            }
        }
        System.out.println(dp[D]);

    }
}
