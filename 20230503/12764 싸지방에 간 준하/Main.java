import java.io.*;
import java.util.*;

public class Main {
    static class Comp implements Comparable<Comp> {
        int start;
        int end;

        public Comp(int s, int e) {
            this.start = s;
            this.end = e;
        }

        @Override
        public int compareTo(Comp target) {
            if(this.start!=target.start){
                return this.start - target.start;
            }
            else
                return this.end - target.end;
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
        seat.offer(new Comp(0, 0)); // idx, end_time
        List<Integer> answer = new ArrayList<>(); // count
        answer.add(0);
        while(!pq.isEmpty()){
            List<Integer> tt = new ArrayList<>();
            Comp c = pq.poll();
            while(true){
                Comp temp = seat.peek();
                if(seat.isEmpty() || temp.start > c.start ){
                    for(int t : tt){
                        seat.offer(new Comp(0,t));
                    }
                    break;
                }
                seat.remove();
                tt.add(temp.end);
            }
            Comp tmp = seat.peek();
            if(c.start < tmp.start){// 새로운 자리 만들기
                int size = seat.size();
                seat.offer(new Comp(c.end,size));
                answer.add(0);
                answer.set(size,answer.get(size) + 1);
            }
            else{// 기존 자리 바꾸기
                seat.remove();
                int idx = tmp.end;
                answer.set(idx, answer.get(idx) + 1);
                seat.offer(new Comp(c.end,idx));

            }
            //System.out.println(c + " " + tmp + " " + seat.peek());
        }
        System.out.println(seat.size());
        for(int i : answer){
            System.out.print(i + " ");
        }
    }

}