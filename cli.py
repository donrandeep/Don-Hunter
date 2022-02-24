import random
import string

print('''\033[92m

          
          ____________    __      ____________             
          \_____     /   /_ \     \     _____/             
           \_____    \____/  \____/    _____/              
            \_____                    _____/               
               \________________________/                  
                                                           
    ____   ___  _   _    _   _             _                 
   |  _ \ / _ \| \ | |  | | | |_   _ _ __ | |_ ___ _ __    
   | | | | | | |  \| |  | |_| | | | | '_ \| __/ _ \ '__|   
   | |_| | |_| | |\  |  |  _  | |_| | | | | ||  __/ |      
   |____/ \___/|_| \_|  |_| |_|\__,_|_| |_|\__\___|_|      
                                                           
                                Created By </Don Randeep>    

 ''')


chars = "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(_+)=[{}]|\/.,?""':;"

# chars = string.printable
chars_list = list(chars)


password = input("Enter Password : ")

guess_password = ""

while(guess_password != password):
    guess_password = random.choices(chars_list, k=len(password) )

    print("\033[96m<=================="+ str(guess_password)+ "==================>")

    if(guess_password == list(password)):
        print("\033[33mYour password is : "+ "".join(guess_password))
        break

