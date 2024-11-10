def Distance(From,To):
    import pickle
    f1=open("DISTANCE.obj",'rb')
    R=pickle.load(f1)
    F=0
    for i in R:
            if(i[0]==From and i[1]==To):
                D=i[2]
                F=1
                break
    if F==0:
        D=int(input('Enter Distance Manually(in Km):'))
    f1.close()
    return(D)
def NewBus():
    print('ADDING A NEW BUS')
    import pickle
    f1=open('Bus_Details.obj','rb')
    L=pickle.load(f1)
    f1.close()
    f=open('Bus_Details.obj','wb')
    Busid=input('Enter Bus id:')
    Bname=input('Enter Bus Name:')
    From=input('Enter pickup Location:')
    To=input('Enter Destination:')
    d='y'
    Day=[]
    while d in 'yY':
        D=input('Enter Day of Bus:')
        Day.append(D)
        d=input('Want to enter more day(Y/N):')
    Dist=Distance(From,To)
    Time=input('Enter Time:')
    Seat=int(input('Enter Total Available Seats:'))
    T=20
    TF=T*Dist
    Rec=[Busid,Bname,From,To,Seat,Day,Dist,Time,T,TF]
    L.append(Rec)
    pickle.dump(L,f)
    f.close()
    print('NEW BUS ADDED SUCESSFULLY')
    print('.'*187)
    
def DeleteBus():
    print('REMOVING A BUS')
    import pickle
    f=open('Bus_Details.obj','rb')
    R=pickle.load(f)
    lst=[]
    Bid=input('Enter Bus id:')
    for i in R:
        if(i[0]!=Bid):
            lst.append(i)
    f.close()
    f=open('Bus_Details.obj','wb')
    pickle.dump(lst,f)
    f.close()
    print('BUS REMOVED SUCESSFULLY')
    print('.'*187)
def DisplayBus():
    import pickle
    f=open('Bus_Details.obj','rb')
    R=pickle.load(f)
    print('\nBusid\tBusname\tFrom\tTo\tTotal_Seats\tDay\tDistance\tTime\tTeriff\tFare')
    print('--------	-------------	-------	----         --------------                -----	------------	-------	-------	--------')
    for Rec in R:
        for i in Rec:
            print(i,end='\t')
        print()
    f.close()
    print('.'*187)
def AllBooking():
    import pickle
    f=open('Passenger_Details.obj','rb')
    R=pickle.load(f)
    print('\nBookingID | Date	     Seat_No.    Busname\tTime\tFare\tName\t\tPhone\t\tE-mail')
    print('---------------  ------	     ------------    -------------	-------	-------	--------		---------		---------')
    for i in R:
        print(f'{i[0]}\t  {i[1]}  {i[2]}\t   {i[4]}	{i[7]}\t{i[8]}\t{i[9]}\t{i[11]}\t{i[12]}\t')
    f.close()
    print('.'*187)
        

def Cost():
    import pickle
    f=open('Passenger_Details.obj','rb')
    R=pickle.load(f)
    D=[]
    d=R[0][1]
    for Rec in R:
        if d!=Rec[1]:
            d=Rec[1]
        if d not in D:
            D.append(d)
    for S in D:
        c=0
        for Rec in R:
            if S==Rec[1]:
                c+=Rec[8]
        print(f'Total PROFIT on {S} is ₹{c}')
