
#define _CRT_SECURE_NO_WARNINGS
#include <bits/stdc++.h>
using namespace std;

int N, M,num,arr[26],ans_num,answer[26],MAX;
vector<pair<int, int>> road[26];
vector<int> contain_a;
bool used[26]; 
stack<int> recent;
string ans, temp;
int main(void) {
   ifstream in("3.inp");
   ofstream out("out.out");
   in >> N >> M;
   int i, weight=0,iter=0,next_iter = 1;
   char c1, c2;
   bool pass=false;
   for (i = 0; i < M; i++) {
      in >> c1 >> c2 >> weight;
      road[c1 - 'a'].push_back(make_pair(c2-'a', weight));
      road[c2 - 'a'].push_back(make_pair(c1-'a', weight));
   }
   for (auto K : road[0]) contain_a.push_back(K.first);
   recent.push(0);
   arr[0] = 0;
   used[0] = true;
   int re=0;
   for (int i = 0; i < 26; i++) {
      if (road[i].empty()) continue;
      road[i].push_back(make_pair(26,0));
   }
   num = contain_a.size()-1;
   int time=0;

   bool next = true;
   weight = 0;
   int limit = contain_a.size();
   limit = round(limit / 2);

   while (1) {
      if (iter==-1) break;
      //if (iter == 0 && recent.top() > limit) break;
      pass = false;

      if (arr[next_iter] == 0 && !next) {
         re = 0;
      } 
      else { re = recent.top(); recent.pop();
      } 
      next = false;
      if (road[arr[iter]][re].first == 26) { 
         used[arr[iter]] = false;
         arr[next_iter] = 0;
         iter--; next_iter--; 
         if(!recent.empty()) weight -= road[arr[iter]][recent.top()-1].second;
         continue; 
      } 
      if (road[arr[iter]][re].first == 0) {
         if (weight + road[arr[iter]][re].second >= MAX) { 
            temp = "";
            for (int i = 0; i < next_iter; i++)
               temp.push_back((char)(arr[i]+'a'));
            if (weight + road[arr[iter]][re].second == MAX) {
               if (!ans.empty() && temp < ans) {
                  ans = temp;
                  ans_num = next_iter;
               }
            }
            else {
               MAX = weight + road[arr[iter]][re].second;
               ans = temp;
               ans_num = next_iter;
            }
         }
         recent.push(re + 1);  
         next = true;
         continue;
      }

      if (used[road[arr[iter]][re].first]) { 
         recent.push(re + 1);
         next = true;
         continue;
      }
      arr[next_iter] = road[arr[iter]][re].first; 
      weight += road[arr[iter]][re].second;        
      used[arr[next_iter]] = true;
      recent.push(re+1);

      if (iter > num) { 
         for (auto K : contain_a) {
            if (used[K] == 0) {
               pass = true;
               break;
            }
         }
      }
      else {
         pass = true;
      }
      if(!pass){
         used[arr[next_iter]] = false;
         weight -= road[arr[iter]][re].second;
         continue;
      }
      iter++; next_iter++;
      num++;
   }
   cout << MAX << endl;
   for (auto K : ans) {
      cout << K << " ";
   }
}