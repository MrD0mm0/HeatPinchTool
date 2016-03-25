# Stream format [Supply Temp (Ts), Target Temp (Tt), DH, CP, Cold(0)/Hot(1) {, Ts shift, Tt shift}]
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

Tshift=[]
DTmin=float(input('DTmin - Minimum approach temperature= '))
n=len(stream) # Number of streams
for i in range(0,n):
    if stream[i][4]==0:
        stream[i].append(stream[i][0]+(DTmin/2))
        stream[i].append(stream[i][1]+(DTmin/2))
        Tshift.append(stream[i][0]+(DTmin/2))
        Tshift.append(stream[i][1]+(DTmin/2))
    else:
        stream[i].append(stream[i][0]-(DTmin/2))
        stream[i].append(stream[i][1]-(DTmin/2)) 
        Tshift.append(stream[i][0]-(DTmin/2))
        Tshift.append(stream[i][1]-(DTmin/2)) 
Tshift.sort()

streamshift=[]
for x in range(1,len(Tshift)):
    CP=0
    for i in range(0,n):
        if stream[i][4]==0:
            if stream[i][5]<=Tshift[x-1] and stream[i][6]>=Tshift[x]:
                    CP+=stream[i][3]
        else:
            if stream[i][6]<=Tshift[x-1] and stream[i][5]>=Tshift[x]:
                    CP-=stream[i][3]
    streamshift.append([CP*(Tshift[x]-Tshift[x-1]),Tshift[x-1]])
streamshift.reverse()
heatflow=[]
heat=0
for i in range(0,len(streamshift)):
    heat-=streamshift[i][0]
    heatflow.append([heat,streamshift[i][1]])
lowest=heatflow[0][0]
pinch=heatflow[0][1]
for i in range(0,len(heatflow)):
    if heatflow[i][0]<lowest:
        lowest=heatflow[i][0]
        pinch=heatflow[i][1]
        
res=open('.qcmin','w')
phot= pinch+DTmin/2
pcold=pinch-DTmin/2
qhmin=-lowest
qcmin=heatflow[len(heatflow)-1][0]-lowest
print('Pinch shifted T=', pinch,'oC')
print('Pinch for Hot streams=',phot,'oC')
print('Pinch for Cold streams=', pcold,'oC')
print('QHmin=',qhmin,'kW')
print('QCmin=',qcmin,'kW')
res.write(str(qcmin))
