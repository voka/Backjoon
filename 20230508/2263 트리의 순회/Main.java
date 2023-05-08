import java.io.*;

public class Main {
    // static int[] preOrder;
    static int[] inOrder;
    static int[] postOrder;
    static String answer = "";
    // static int idx = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String[] temp = br.readLine().split(" ");
        inOrder = new int[n];
        postOrder = new int[n];
        for (int i = 0; i < n; ++i) {
            inOrder[i] = Integer.parseInt(temp[i]);
        }
        temp = br.readLine().split(" ");
        for (int i = 0; i < n; ++i) {
            postOrder[i] = Integer.parseInt(temp[i]);
        }
        getPreOrder(0, n - 1, 0, n - 1);
        System.out.println(answer);
    }

    public static void getPreOrder(int inStart, int inEnd, int postStart, int postEnd) {// 분할 정복
        if (inStart > inEnd || postStart > postEnd)
            return;
        int root = postOrder[postEnd]; // 후위 순회 결과에서는 root 값을 알 수 있고
        int rootIdx = -1;
        for (int i = inStart; i <= inEnd; ++i) {
            if (inOrder[i] == root) {
                rootIdx = i;
                break;
            }
        }
        answer += root + " ";
        int leftSize = rootIdx - inStart; // 중위 순회 결과에서는 왼쪽 트리와 오른쪽 트리의 길이를 알 수 있을
        getPreOrder(inStart, rootIdx - 1, postStart, postStart + leftSize - 1);// left
        getPreOrder(rootIdx + 1, inEnd, postStart + leftSize, postEnd - 1);// right

    }
}