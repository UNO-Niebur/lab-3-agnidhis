#ApproxPi.py
#Name: Nidhi Agarwal
#Date: 2/3/2026
#Assignment: decimal precision practice 
import math
import time


#PLEASE NOTE - This is an optional, extra credit portion of the lab.
#  #ask user for decimal percision (up to 10)

def main():
 realPi = math.pi

 precision = int(input("Enter decimal precision upto 10: "))
 if 0<= precision <=10:
   return 
 else:
   print("Please enter a value between 0 and 10 ")

decimal_precision = get_precision()
print(f"You have selected a decimal precision of: {decimal_precision}")

start = time.time()
  #calculate pi using the approximation technique
  #Loop until the level of percision is reached

end = time.time()

elapsedTime = end - start
print(elapsedTime)

if __name__ == '__main__':
  main()
