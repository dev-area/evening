

class Table(object):
    def __init__(self,total_bill=0.0,tip=0.0,gen='Female',smoker='No',day='Sun',time='Dinner',size=3):
        self.__total_bill = total_bill
        self.__tip = tip
        self.__gen = gen
        self.__smoker = smoker
        self.__day = day
        self.__time = time 
        self.__size = size
        
    def show(self):
        print("total bill:",self.__total_bill,"tip:",self.__tip)
        
    def getTotalBill(self):
        return self.__total_bill

    def getTip(self):
        return self.__tip
    
    def __getattr__(self,name):
        return self.__dict__['_Table__' + name]
    
    def __setattr__(self,name,v):
        if name in ['total_bill','tip','gen','smoker','day','time','size']:
            raise Exception("no!!!")
        else:
            super().__setattr__(name,v)
    
    def getfield(self,name):
        return self.__dict__['_Table__' + name]
    
    def getTipPercent(self):
        return round(self.__tip / self.__total_bill,3)
    
        
    


if __name__ == '__main__':
    print("my tests=========")
    t = Table(120,14)
#    t.show()

#    print(t.getTotalBill()*0.12)
    
#    print(t.getTipPercent())



