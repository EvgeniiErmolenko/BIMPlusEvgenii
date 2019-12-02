N,n=int(input('inter the number of polygon points: ')),0
SumAx,SumAx1,SumAx2,SumSx,SumSy,SumIx,SumIy,SumIxy=0,0,0,0,0,0,0,0
Xs=[]
Ys=[]
CD=''
Coordinates=''
print('Enter x and y coordinates for polygon points:')
while n<=N:
    if n<N:
        x,y=[float(i) for i in input().split()]
        Xs+=[x]
        Ys+=[y]
        if n==N-1:
            Xs+=[Xs[0]]
            Ys+=[Ys[0]]
        Coordinates=str(Xs[n])+'   '+ str(Ys[n])
        CD+='   '+str(n+1)+'      '+Coordinates+'\n'
    if n>0:
        #SumAx+=(Xs[n]+Xs[n-1])*(Ys[n]-Ys[n-1])
        SumAx1+=Ys[n]*Xs[n-1]
        SumAx2+=Xs[n]*Ys[n-1]
        SumSx+=(Xs[n]-Xs[n-1])*(Ys[n]**2+Ys[n-1]*Ys[n]+Ys[n-1]**2)
        SumSy+=(Ys[n]-Ys[n-1])*(Xs[n]**2+Xs[n-1]*Xs[n]+Xs[n-1]**2)
        SumIx+=(Xs[n]-Xs[n-1])*(Ys[n]**3+Ys[n]**2*Ys[n-1]+Ys[n]*Ys[n-1]**2+Ys[n-1]**3)
        SumIy+=(Ys[n]-Ys[n-1])*(Xs[n]**3+Xs[n]**2*Xs[n-1]+Xs[n]*Xs[n-1]**2+Xs[n-1]**3)
        SumIxy+=(Ys[n]-Ys[n-1])*(Ys[n]*(3*Xs[n]**2+2*Xs[n]*Xs[n-1]+Xs[n-1]**2)+Ys[n-1]*(3*Xs[n-1]**2+2*Xs[n]*Xs[n-1]+Xs[n]**2))
    n+=1
Ax=(SumAx1-SumAx2)/2
Sx=SumSx/(-6)
Sy=SumSy/6
Ix=SumIx/(-12)
Iy=SumIy/12
Ixy=SumIxy/(-24)
Xt=Sy/Ax
Yt=Sx/Ax
Ixt=Ix-Yt**2*Ax
Iyt=Iy-Xt**2*Ax
Ixyt=Ixy+Xt*Yt*Ax
print('\n'+'Coordinates')
print(f"{'Point №'}   {'X':>3}   {'Y':>3}")
print('-'*20)
print(CD)
print('\n'+'Geometric characteristics:')
print(f"{'Ax:':10} {Ax:5.2f}")
print(f"{'Sx:':10} {Sx:5.2f}")
print(f"{'Sy:':10} {Sy:5.2f}")
print(f"{'Ix:':10} {Ix:5.2f}")
print(f"{'Iy:':10} {Iy:5.2f}")
print(f"{'Ixy:':10} {Ixy:5.2f}")
print(f"{'Xt:':10} {Xt:5.2f}")
print(f"{'Yt:':10} {Yt:5.2f}")
print(f"{'Ixt:':10} {Ixt:5.2f}")
print(f"{'Iyt:':10} {Iyt:5.2f}")
print(f"{'Ixyt:':10} {Ixyt:5.2f}")
