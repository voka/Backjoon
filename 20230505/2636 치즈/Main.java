import java.util.*;
import java.io.*;

public class Main {
    static int N, M;
    static int[][] maps;

    static class Pair {
        int x;
        int y;

        public Pair(int x, int y) {
            this.x = x;
            this.y = y;
        }

        public int getx() {
            return this.x;
        }

        public int gety() {
            return this.y;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] temp = br.readLine().split(" ");
        N = Integer.parseInt(temp[0]);
        M = Integer.parseInt(temp[1]);
        int count = 0;
        int last = 0;
        maps = new int[N][M];
        for (int i = 0; i < N; ++i) {
            temp = br.readLine().split(" ");
            for (int j = 0; j < M; ++j) {
                maps[i][j] = Integer.parseInt(temp[j]);
            }
        }
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < M; ++j) {
                if (maps[i][j] != 0) {
                    last = BFS();
                    count++;
                }
            }
        }
        System.out.println(count);
        System.out.println(last);
    }

    public static int BFS() {
        Queue<Pair> q = new LinkedList<>();
        int[][] visited = new int[N][M];
        int[] dx = { 1, -1, 0, 0 };
        int[] dy = { 0, 0, 1, -1 };
        visited[0][0] = 1;
        q.add(new Pair(0, 0));
        int count = 0;
        while (!q.isEmpty()) {
            Pair c = q.poll();
            for (int i = 0; i < 4; ++i) {
                int nx = c.getx() + dx[i];
                int ny = c.gety() + dy[i];
                if ((0 <= nx && nx < M) && (0 <= ny && ny < N) && visited[ny][nx] == 0) {
                    visited[ny][nx] = 1;
                    if (maps[ny][nx] == 1) {
                        maps[ny][nx] = 0;
                        count++;
                        continue;
                    }
                    q.add(new Pair(nx, ny));
                }
            }
        }
        return count;

    }
}
