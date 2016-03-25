streamno=1
stream=[]
while True:
    print('Stream', streamno,'(Leave unknown blank)')
    Ts=input("Ts - Supply Temp (oC)= ")
    Tt=input('Tt - Target Temp (oC)= ')
    CP=input('CP - Heat capacity flowrate (kW/oC)= ')
    if Ts=='':
        H=input('dH - Required heat transfer duty (kW)= ')
        Ts=float(Tt)-(float(H)/float(CP))
    if Tt=='':
        H=input('dH - Required heat transfer duty (kW)= ')
        Tt=(float(H)/float(CP))+float(Ts)
    if CP=='':
        H=input('dH - Required heat transfer duty (kW)= ')
        CP=float(H)/(float(Tt)-float(Ts))
    else:
        H=float(CP)*(float(Tt)-float(Ts))
    ch=0
    if float(Tt)-float(Ts)<0:
        ch=1
    stream.append([float(Ts),float(Tt),float(H),float(CP),ch])
    final=str(input('Final Stream? (y/N): '))
    if final=='y':
        break
    else:
        streamno+=1
f=open('streams','w')
for i in range(0,len(stream)):
    for x in stream[i]:
        f.write(str(x))
        f.write(' ')
    f.write('\n')
