import java.io.*;
import java.util.*;

// 시작시간 비교용 우선순위 큐 1개
// 자리별 끝나는 시간 비교용 우선순위 큐 1개
// 인덱스 비교용 우선순위 큐 1개 (빈 자리중 가장 작은 인덱스를 가진 자리를 먼저 사용해야함)
// 사용횟수 기록용 배열은 100001 크기로 미리 선언 
// i 번째 시작시간과 1 ~ i-1 번째 중 가장 빨리 종료 시키는 시간 비교 
// 출력은 StringBuilder를 이용해 빠르게 하기
//

public class Main {
    static StringBuilder sb = new StringBuilder();
    static class Comp implements Comparable<Comp> {
        int start;
        int end;

        public Comp(int s, int e) {
            this.start = s;
            this.end = e;
        }

        @Override
        public int compareTo(Comp target) {
            return this.start - target.start;
        }

        @Override
        public String toString() {
            return "Comp{" +
                    "start=" + start +
                    ", end=" + end +
                    '}';
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        PriorityQueue<Comp> pq = new PriorityQueue<>();
        for(int i=0;i<N;++i){
            String[] s = br.readLine().split(" ");
            int p = Integer.parseInt(s[0]);
            int q = Integer.parseInt(s[1]);
            pq.offer(new Comp(p,q));
        }
        PriorityQueue<Comp> seat = new PriorityQueue<>();
        PriorityQueue<Integer> nextSeat = new PriorityQueue<>();
        nextSeat.add(0); // idx
        int [] answer = new int[100001]; // count
        while(!pq.isEmpty()){
            Comp c = pq.poll();
            while(!seat.isEmpty() && seat.peek().start < c.start){ // 초기화
                nextSeat.add(seat.poll().end);
            }
            if(nextSeat.isEmpty()){ // 새로운 자리 만들기
                int size = seat.size();
                seat.offer(new Comp(c.end,size));
                answer[size]++;
            }
            else{// 기존 자리 바꾸기
                int idx = nextSeat.poll();
                answer[idx]++;
                seat.offer(new Comp(c.end,idx));
            }
            //System.out.println(c + " " + seat.peek() + " " + nextSeat.size());
        }

        int count = seat.size() + nextSeat.size();
        sb.append(count+"\n");
        for(int i = 0; i<count;++i){
            sb.append(answer[i] + " ");
        }
        System.out.println(sb.toString());
    }

}