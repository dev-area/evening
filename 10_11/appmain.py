import requests
import table
import tablelist
import tools.strtools as stl




ls = tablelist.TableList()


r = requests.get("https://raw.githubusercontent.com/dev-area/DS/master/tips.csv")

g = r.iter_lines()
next(g)

for i in g:
    st = i.decode()
    flds = st.split(',')
    t = table.Table(float(flds[0]),float(flds[1]),flds[2],flds[3],flds[4],flds[5],int(flds[6]))
    ls.add(t)
    
print(stl.revstr("hello"))
a = ls.getbigtips()

print(ls.getmaxtip())


