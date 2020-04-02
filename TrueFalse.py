#Josh Stiller Chameleon Challenge Logic/Data Problems 1

num=int(input("Enter a number for check if the number odd or even: ")) #this is the print statement that will displayed for the user
def find_Evenodd(num):
    
    if(num%2==0): #this is using 2 as a divisable number to determine if even 
        print(num," Is an even number") #print statements to display outcome of user input
    else:
        print(num," is an odd number") #print statements 


find_Evenodd(num);