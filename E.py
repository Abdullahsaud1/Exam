
import datetime

nwe = datetime.datetime.today()
class name :
    def __init__(slef , f_name ,balance ):
        slef.f_name = f_name
        slef.balance = balance
    def n(slef):
        print("Wlcom MR." , slef.f_name ,"is  balance " , slef.balance)

n1 = name("Abdullah " , 0 )
n1.n()

class deposit:
    def D(slef ):
        # slef.plus = plus
        plus = int(input("How much you want to deposit?"))
 
        print("تم ايداع ", plus , "ريال لرصيدك البنكي في يوم " ,nwe )
    # def DI(slef , ): 
        # slef.i= i   
        i = int(input("Enter the bix "))
    
        
        if  i<2000:
            print("تم خصم" , i, "من رصيدك في " , nwe)
        else:
            print("رصيدك لايسمح ")
    # def DM(slef ):
        R = int(plus  - i)
        print( " رصيدك هو " , R , "في " , nwe)
        
        
class discount:
   pass
    # def DI(slef , i): 
    #     slef.i= i   
    #     # i = int(input("Enter the bix "))
    
        
    #     if  i<2000:
    #         print("تم خصم" , i, "من رصيدك في " , nwe)
    #     else:
    #         print("رصيدك لايسمح ")

class inquiry(deposit ,discount):
    pass
#     # def DO(slef):
#     #     DI.__int__(slef)
#     #     D.__int__(slef)
#     #     print()
    
class fun(inquiry ,deposit ,discount) :
    
    pass
ojc=fun()
ojc.D()
# ojc.DI()
# ojc.DM()
# ojc.DO()