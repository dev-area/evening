import table


class TableList(object):
    def __init__(self):
        self.__tlist = []
        
    def add(self,table):
        self.__tlist.append(table)
        
    def showall(self):
        for t in self.__tlist:
            t.show()
            
    def getbigtips(self):
        for t in self.__tlist:
            if t.getTip() > 5:
                yield t

    def getmaxtip(self):
        mx = 0
        for t in self.__tlist:
              mx = max(mx,t.tip)
        return mx

if __name__ == '__main__':

    tls = TableList()
    
    t1 = table.Table(130,25,'Female')
    tls.add(t1)
    
    tls.showall()
    