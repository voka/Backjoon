# input ["P 300 6", "P 500 3", "S 1000 4", "P 600 2", "S 1200 1"]
# output  [1500, 2400]
# input ["P 300 6", "P 500 3", "S 1000 4", "P 600 1", "S 1200 2"]
# output  	[1800, 2700]
# input ["P 100 4", "P 300 9", "S 1000 7", "P 1000 8", "S 700 7", "S 700 3"]
# output  [7100, 10700]


class mybag():
    def __init__(self):
        self.stack_answer = 0
        self.queue_answer = 0
        self.stack = []
        self.queue = []
    
    def cal_stack(self,num):
        temp = 0
        total_sell = num
        
        pre = total_sell
        while total_sell > 0:
            qty, price = self.stack[0]
            total_sell = total_sell - qty
            if(total_sell >= 0):
                temp += qty*price
                del self.stack[0]
            else:
                temp += pre*price
                self.stack[0][0] = qty - pre
            pre = total_sell
            
        self.stack_answer += temp
            
    def cal_queue(self,num):
        temp = 0
        total_sell = num
        
        pre = total_sell
        while total_sell > 0:
            qty, price = self.queue[-1]
            total_sell = total_sell - qty
            if(total_sell >= 0):
                temp += qty*price
                del self.queue[-1]
            else:
                temp += pre*price
                self.queue[-1][0] = qty - pre
            pre = total_sell
            
        self.queue_answer += temp
            
    
def solution(record):
    a = mybag()
    for i in record:
        act, price, qty = i.split(" ")
        if act == "P":
            a.stack.append([int(qty), int(price)])
            a.queue.append([int(qty), int(price)])
        elif act == "S":
            a.cal_stack(int(qty))
            a.cal_queue(int(qty))
        else :
            pass
        
    
    return [a.stack_answer,a.queue_answer]