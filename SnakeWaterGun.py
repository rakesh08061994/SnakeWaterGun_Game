import random    
from termcolor import colored     


def SWG_Game(user):         
    """This is popular game Snake/Water/Gun, Take one 
    user input from s/w/g and return result in different color"""
    try:
        computer = random.choice(["s","w","g"]) 
        flag = ""                               
        if(computer == user):                   
            flag =  None                        
        elif((computer == "s") and (user == "w")):  
            flag =  False                           
        elif((computer == "s") and (user == "g")):
            flag = True                             

        elif((computer == "w") and (user == "s")):
            flag =  True
        elif((computer == "w") and (user == "g")):
            flag =  False

        elif((computer == "g") and (user == "s")):
            flag =  False
        elif((computer == "g") and (user == "w")):
            flag =  True

        print(f"\t\t\t Computer Turn: {computer}\n\t\t\t Your turn : {user}")    
        if flag == None:
            return (colored('\n\t\t********** Match is Tie **********', 'yellow', attrs=['bold']))                                                           
        elif(flag):                                                     
            return (colored('\n\t\t********** You Win **********', 'green', attrs=['bold']))              
        else:                                                         
            return (colored('\n\t\t********** You loose **********', 'red', attrs=['bold']))      
    except ValueError:
        print("Incorrect.... Please watch your input")       
    except ValueError as e:
        print(f"Module not found {e}")
    except ImportError as e:
        print(f"Import Error: {e}")
    except ModuleNotFoundError:
        print("Module Not Found")


# -----------------------------------***************--------------------------------------
if __name__ == "__main__":

    TakeInput = input ("Enter Your Turn : ")
    print(SWG_Game(user=TakeInput))                                 
    
    
