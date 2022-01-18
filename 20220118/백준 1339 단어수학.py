from sys import stdin 
N = int(stdin.readline())
vokas = []
mydict = {}
for i in range(N):
    vokas.append(stdin.readline().strip())
    len_j = len(vokas[i])-1
    for j in range(len(vokas[i])):
        if vokas[i][j] not in mydict:
            mydict[vokas[i][j]] = pow(10,len_j-j)
        else:
            mydict[vokas[i][j]] += pow(10,len_j-j)
# 영향이 큰 알파벳 순으로 정렬 
MDS = sorted(mydict.items(), key = lambda x : (-x[1],x[0]))
#print(vokas,mydict,MDS)
# 알파벳을 0 ~ 9 사이 값으로 변경
for i in range(len(MDS)):
    chi = 9 - i 
    mydict[MDS[i][0]] = chi
#print(mydict,MDS)
answer = 0
# 알파벳 계산
for i in range(len(vokas)):
    for a,b in mydict.items():
        vokas[i] = vokas[i].replace(a,str(b))
    # 정답 구하기 
    answer += int(vokas[i])
print(answer)
    
 