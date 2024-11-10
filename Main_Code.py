from bus_details import Distance,NewBus,DeleteBus,DisplayBus,AllBooking,Cost
from Booking_Code import FindDay,login,FindBus,Bookingid,SeatCheck,NewBooking,DisplayBooking,CancelBooking


def Customer():
    print('\t\t\t1. Book A Bus \n\t\t\t2. Cancel Bus Booking \n\t\t\t3. Check your Booking\n\t\t\t4. Exit')
    print('_'*44)
    ch=int(input('Enter Your Choice:'))
    while ch in [1,2,3]:
        if ch==1:
            NewBooking()
        elif ch==2:
            CancelBooking()
        elif ch==3:
            DisplayBooking()
        print('\t\t\t1. Book A Bus \n\t\t\t2. Cancel Bus Booking \n\t\t\t3. Check your Booking\n\t\t\t4. Exit')
        print('_'*44)
        ch=int(input('Again enter Your Choice(4.exit):'))

        
def employee():
    print('\t\t\t1. Add a New Bus \n\t\t\t2. Delete a Bus Booking \n\t\t\t3. Display All Bus\n\t\t\t4. Display All Booking \n\t\t\t5. Display Profit of each Date 6. Exit')
    print('_'*44)
    ch=int(input('Enter Your Choice:'))
    while ch in [1,2,3,4,5]:
        if ch==1:
            NewBus()
        elif ch==2:
            DeleteBus()
        elif ch==3:
            DisplayBus()
        elif ch==4:
            AllBooking()
        elif ch==5:
            Cost()
        print('\t\t\t1. Add a New Bus \n\t\t\t2. Delete a Bus Booking \n\t\t\t3. Display All Bus\n\t\t\t4. Display All Booking \n\t\t\t5. Display Profit of each Date 6. Exit')
        print('_'*44)
        ch=int(input('Again enter Your Choice(6.exit):'))


#MAIN PROGRAM
print('\t\t\t\t\tBUS RESERVATION PROGRAM')
print('\t\t\t\t\t--------------------------------------------')
ans1='y'
while ans1 in 'yY':
    q=input('ARE YOU A CUSTOMER(Y/N):')
    print('='*88)
    if (q in 'yY'):
        Customer()
    else:
        an=login()
        if an==1:
            print('^^LOGIN SUCESSFULL^^')
            employee()
            break
        else:
            print('WRONG PASSWORD')
    ans1=input('Want to continue(Y/N):')
    print('='*88)
print('!!! THE PROGRAM IS SUCCESSFULLY CLOSED !!!')

