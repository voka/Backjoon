#include<iostream>
#include<math.h>
using namespace std;

struct circle{
    double x;
    double y;
    double r;
    bool operator==(circle A){
        if(x == A.x && y == A.y && r == A.r) return true;
        return false;
    }
};
double distance(circle A, circle B){
    return sqrt(pow(A.x-B.x,2) + pow(A.y-B.y,2));
}
int main(void){
    int T;
    cin>>T;
    while(T--){
        circle A,B;
        cin>>A.x>>A.y>>A.r>>B.x>>B.y>>B.r;
        if(A == B){
            cout<<"-1\n";
        }
        else{
            double D = distance(A,B);
            double D_r = fabs(A.r-B.r);
            double D_s = A.r + B.r;
            if(D == D_r || D == D_s){
                cout<<"1\n";
            }
            else if(D > D_r && D < D_s){
                cout<<"2\n";
            }
            else{
                cout<<"0\n";
            }
        }
    }
    return 0;
}