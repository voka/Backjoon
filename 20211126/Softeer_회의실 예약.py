class meeting_room():
    def __init__(self, name):
        self.name = name
        self.time = [9,10,11,12,13,14,15,16,17]
        self.time_num = 1
        self.available_time = []
    
    def cal_time(self):
        tlen = len(self.time)
        if(tlen) == 0: 
            self.time_num = 0
            return
        mytime = 0
        time_start = self.time[0]
        pre = self.time[0]
        for t in range(1,tlen):
            #print(pre,self.time[t])
            if(self.time[t] - pre != 1 or t == tlen-1):
                if(t == tlen-1) : time_end = self.time[t] + 1
                else : time_end = pre + 1
                if(len(str(time_start)) == 1):
                    time_start = "0" + str(time_start)
                if(len(str(time_end)) == 1):
                    time_end = "0" + str(time_end)
                self.available_time.append([time_start,time_end])
                time_start = self.time[t]
                mytime += 1
            
            pre = self.time[t]
        self.time_num = mytime
    
    def del_time(self, start_time, end_time):
        for i in range(start_time,end_time):
            self.time.remove(i)
    
    def display_available_time(self):
        print("Room {}:".format(self.name))
        if self.time_num == 0:
            print("Not available")
        else:
            print("{} available:".format(self.time_num))
            for i in self.available_time:
                print("{0}-{1}".format(i[0],i[1]))

N,M = map(int,input().split())
#print(N,M)
Meeting_names = []
Meeting_dict = {}


for i in range(N):
    Mname = input()
    Meeting_names.append(Mname)
    a = meeting_room(Mname)
    Meeting_dict[Mname] = a

Meeting_names = sorted(Meeting_names)


for i in range(M):
    Mname, s, e = input().split()
    start_time = int(s)
    end_time = int(e)
    Meeting_dict[Mname].del_time(start_time,end_time)


enum = 0
for i in Meeting_names:
    enum += 1 
    #print(i, Meeting_dict[i].time)
    Meeting_dict[i].cal_time()
    Meeting_dict[i].display_available_time()
    if(enum != N):
        print("-----")