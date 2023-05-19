class time:
    def __init__(self,h,m):
        self.h=h
        self.m=m
    def AddTime(t1,t2):
        t3=time(0,0)
        t3.h=t2.h+t1.h
        t3.m=t2.m+t1.m
        if t3.m>=60:
            t3.h+=1
            t3.m-=60
        return t3
    def display(self):
        print("Time is ",self.h," hours and ",self.m," minutes")
    def display_m(self):
        print("Time in mins: ", self.h*60+self.m)

t1=time(1,20)
t2=time(1,42)
t=time.AddTime(t1,t2)
t.display()
t.display_m()

Xn = (X - Xminimum) / ( Xmaximum - Xminimum)  
