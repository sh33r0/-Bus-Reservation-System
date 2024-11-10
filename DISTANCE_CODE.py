import pickle
f=open("DISTANCE.obj",'wb')
L=[['Jamshedpur','Narwa',20],
   ['Jamshedpur','Chandil',30],
   ['Jamshedpur','Saraikela',42],
   ['Jamshedpur','Ghatshila',48],
   ['Jamshedpur','Hazaribagh',77],
   ['Jamshedpur','Ranchi',126],
   ['Jamshedpur','Bokaro',133],
   ['Jamshedpur','Dhandbad',140],
   ['Narwa','Jamshedpur',20],
   ['Chandil','Jamshedpur',30],
   ['Saraikela','Jamshedpur',42],
   ['Ghatshila','Jamshedpur',48],
   ['Hazaribagh','Jamshedpur',77],
   ['Ranchi','Jamshedpur',126],
   ['Bokaro','Jamshedpur',133],
   ['Dhandbad','Jamshedpur',140]]
pickle.dump(L,f)
f.close()

