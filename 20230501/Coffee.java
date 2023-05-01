import java.io.*;
import java.util.*;

public class Coffee {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N, K;
        String[] input = br.readLine().split(" ");
        N = Integer.parseInt(input[0]);
        K = Integer.parseInt(input[1]);
        if (K == 0) {
            System.out.println(0);
            return;
        }
        int[] caffeines = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int[] dp = new int[K + 1]; // 카페인 i를 채우기 위해 마셔야 하는 커피 개수의 최솟갑 dp[i]
        Arrays.fill(dp, N + 1);
        for (int i = 0; i < N; ++i) {
            int caffeine = caffeines[i];
            if (caffeine == K) {
                dp[K] = 1;
                break;
            }
            for (int j = K; j >= caffeine; --j) {
                if (j == caffeine) { // 카페인 j를 채우기 위해 마셔야 하는 커피 개수는 무조건 1개
                    dp[j] = 1;
                } else { // min(dp[j], 현재 카페인을 제외하고 개수를 1증가시킨 것)
                    dp[j] = Math.min(dp[j - caffeine] + 1, dp[j]);
                }
            }
        }
        // for (int i = 1; i <= K; ++i) {
        // System.out.println(dp[i]);
        // }
        if (dp[K] == N + 1) {
            System.out.println(-1);
        } else {
            System.out.println(dp[K]);

        }
    }
}
// 1
// dp[j] = (dp[K-1] + 1, dp[j)]
// dp[]
