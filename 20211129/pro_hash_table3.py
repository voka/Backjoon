def solution(genres, plays):
    mymusic = {} # genres, "횟수 , 고유번호"
    musicpopulur = {} # 장르 횟수
    for i in range(len(genres)):
        if genres[i] in mymusic:
            mymusic[genres[i]].append([plays[i],i])
        else:
            mymusic[genres[i]] = []
            mymusic[genres[i]].append([plays[i],i])
        if genres[i] in musicpopulur:
            musicpopulur[genres[i]] += plays[i]
        else:
            musicpopulur[genres[i]] = plays[i]
    ss = sorted(musicpopulur.items(), key = lambda item : item[1] ,reverse=True ) # 딕셔너리 정렬해서 튜플리스트로 만드는 것도 외워둘 것 !
    
    answer = []
    for i in ss:
        mymusic[i[0]].sort(key=lambda x : (x[0],-x[1]), reverse=True) # 요런식으로 정렬함수 사용하면 n 차원도 정렬할 수 있을거 같다. 유용 !!!
        answer.append(mymusic[i[0]][0][1])
        if(len(mymusic[i[0]]) > 1) : answer.append(mymusic[i[0]][1][1])
        
    return answer