import pickle
f=open('LoginDetails.obj','wb')
L=[['Mrinmoy','qwerty12'],
   ['Ishita','Asdfg34'],
   ['Priyanshu','Mann07'],
   ['Dharmendar','Dhar56'],
   ['Karan','zxcvb78'],
   ['Dipti','pokm90']]
pickle.dump(L,f)
f.close()
