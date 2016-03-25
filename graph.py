from plotly.offline import plot
from plotly.graph_objs import Scatter,Layout,Figure

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1
length=file_len('streams')
lc=1
stream=[]
with open('streams') as f:
    while lc<=length:
        l=[]
        for i in f.readline().split():
            l.append(float(i))
        stream.append(l)
        lc+=1
hot=[]
cold=[]
for i in range(0,len(stream)):
    if stream[i][4]==0:
        cold.append(stream[i])
    else:
        hot.append(stream[i])
    
    
hottemps=[]
for i in range(0,len(hot)):
    hottemps.append(hot[i][0])
    hottemps.append(hot[i][1])
coldtemps=[]
for i in range(0,len(cold)):
    coldtemps.append(cold[i][0])
    coldtemps.append(cold[i][1])
hottemps.sort()
coldtemps.sort()

hotcomp=[]
for x in range(1,len(hottemps)):
    CP=0
    for i in range(0,len(hot)):
        if hot[i][1]<=hottemps[x-1] and hot[i][0]>=hottemps[x]:
            CP+=hot[i][3]
    hotcomp.append([CP,hottemps[x-1],hottemps[x]])
coldcomp=[]
for x in range(1,len(coldtemps)):
    CP=0
    for i in range(0,len(hot)):
        if cold[i][0]<=coldtemps[x-1] and cold[i][1]>=coldtemps[x]:
            CP+=cold[i][3]
    coldcomp.append([CP,coldtemps[x-1],coldtemps[x]])

#Graph Time!
h=[]
H=0
for i in range(0,len(hotcomp)):
    T=hotcomp[i][1]
    h.append([T,H])
    H+=(hotcomp[i][0]*(hotcomp[i][2]-hotcomp[i][1]))
    T=hotcomp[i][2]
    h.append([T,H])
hT=[]
hH=[]
for i in range(0,len(h)):
    hT.append(h[i][0])
    hH.append(h[i][1])

res=open('.qcmin')
c=[]
H=float(res.read())
for i in range(0,len(coldcomp)):
    T=coldcomp[i][1]
    c.append([T,H])
    H+=(coldcomp[i][0]*(coldcomp[i][2]-coldcomp[i][1]))
    T=coldcomp[i][2]
    c.append([T,H])
cT=[]
cH=[]
for i in range(0,len(c)):
    cT.append(c[i][0])
    cH.append(c[i][1])
trace0=Scatter(x=cH, y=cT, mode='lines+markers', name='Cold Composite Curve')
trace1=Scatter(x=hH, y=hT, mode='lines+markers', name='Hot Composite Curve')
layout=Layout(xaxis=dict(title='H (kW)'),yaxis=dict(title='T (oC)'))
fig=Figure(data=[trace0,trace1], layout=layout)
plot(fig)
