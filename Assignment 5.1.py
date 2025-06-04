try:
     SL = {'Alice':78,'Mark':91,'Harry':77,'Eric':83,'Tim':65}
     a = str(input("Enter your name: "))
     print(a,"'s mark is: ",SL[a])
except:
     if KeyError:
         print("Student not found")