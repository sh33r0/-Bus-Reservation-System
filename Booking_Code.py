def FindDay(date):
    import calendar
    d=date.split('/')
    D,M,Y=int(d[0]),int(d[1]),int(d[2])
    wno=calendar.weekday(Y,M,D)
    w=['Mon','Tue','Wed','Thr','Fri','Sat','Sun']
    return(w[wno])

 
def login():
    import pickle
    f=open('LoginDetails.obj','rb')
    Uid=input('Enter UserName:')
    Pwd=input('Enter Password:')
    R=pickle.load(f)
    for i in R:
        if (i[0]==Uid and i[1]==Pwd):
            return(1)
    return(0)


def SeatCheck(L):
    import pickle
    f=open('Passenger_Details.obj','rb')
    try:
        R=pickle.load(f)
        c=0
        for i in R:
            if i[3]==L[0]:
                c+=1
        if c<L[4]:
            return(1,c+1)
        else:
            return(0,c+1)
    except:
        return(1,1)
def FindBus(From,To):
    global NB
    NB=[]
    import pickle
    f=open('Bus_Details.obj','rb')
    R=pickle.load(f)
    for Rec in R:
        if Rec[2]==From and Rec[3]==To:
            print(f'\nBusid-{Rec[0]}\nBus Name-{Rec[1]}\nFrom-{Rec[2]}\nTo-{Rec[3]}\nDistance-{Rec[6]}\nTime-{Rec[7]}\nTeriff-{Rec[8]}\nTotalFare-{Rec[9]}')
            q,Sno=SeatCheck(Rec)
            print('AVAILABLE DAYS:')
            for i in Rec[5]:
                print(i,end='\n')
            w=input('Want to Book this Bus(Y/N):')
            if w not in 'yY':
                break
            if q==1:
                Date=input('Enter Your applicable Date(D/M/Y):')
                while True:
                    Day=FindDay(Date)
                    if Day in Rec[5]:
                        print(f'The Date {Date} is available for this bus. ')
                        break
                    else:
                        Date=input('This Date is not availabe \n Please write another Date(D/M/Y):')
                NB=[Date,Sno,Rec[0],Rec[1],From,To,Rec[7],Rec[9]]
            break
    else:
            print('##WRONG BUS DESTINATION##')
    f.close()

def Bookingid(B):
    import pickle
    f=open('Passenger_Details.obj','rb')
    R=pickle.load(f)
    c=1
    for i in R:
        if i[3]==B:
            c+=1
    e=B+'_'+str(c)
    return(e)


def NewBooking():
    print('\nBOOKING A BUS:-')
    import pickle
    f=open('Passenger_Details.obj','rb')
    N=pickle.load(f)
    From=input('Enter pickup Location:')
    To=input('Enter Destination:')
    FindBus(From,To)
    if len(NB)!=0:
        Bookid=Bookingid(NB[2])
        Name=input('Enter Passenger\'s Name:')
        Age=int(input('Enter Passenger\'s Age:'))
        Phone=int(input('Enter Passenger\'s Mobile no.:'))
        Mail=input('Enter Passenger\'s Mail-id: ')
        print('\nYour Booking Id is:',Bookid)
        Rec=[Bookid]+NB+[Name,Age,Phone,Mail]
        f=open('Passenger_Details.obj','wb')
        N.append(Rec)
        pickle.dump(N,f)
        f.close()
        print('\nBOOKING PLACED SUCESSFULY\n')
    else:
        print('---NO SEAT AVAILABLE---')
    print('.'*187)


def DisplayBooking():
    print('SHOWING YOUR BOOKING:-')
    Id=input('Enter your Booking Id:')
    m=input('Enter your Mail Id:')
    import pickle
    f=open('Passenger_Details.obj','rb')
    R=pickle.load(f)
    for Rec in R:
        if Rec[0]==Id and Rec[12]==m:
            print(f'\nBooking id-{Rec[0]}\nBus Date-{Rec[1]}\nSeat No.:{Rec[2]}\nBus Id-{Rec[3]}\nBusname-{Rec[4]}\nFrom-{Rec[5]}\nTo-{Rec[6]}\nTime-{Rec[7]}\nTotalFare-{Rec[8]}\nName-{Rec[9]}\nAge-{Rec[10]}\nMobile-{Rec[11]}\nMail Id-{Rec[12]}\n')
            break
    else:
        print('**WRONG BOOKING ID OR E-MAIL**')
    f.close()
    print('.'*187)


def CancelBooking():
    print('CANCELING YOUR BOOKING')
    import pickle
    f=open('Passenger_Details.obj','rb')
    R=pickle.load(f)
    lst=[]
    Bid=input('Enter Booking id:')
    m=input('Enter your Mail Id:')
    for Rec in R:
        if Rec[0]==Bid and Rec[12]==m:
            pass
        else:
            lst.append(Rec)
    f.close()
    f=open('Passenger_Details.obj','wb')
    pickle.dump(lst,f)
    f.close()
    print('BOOKING CANCELLED SUCESSFULLY')
    print('.'*187)

