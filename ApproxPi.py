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

while not (0<= precision <=10):
  print("Please enter a value between 0 and 10 ")
  precision = int(input("Enter decimal precision upto 10: "))
 
start = time.time()
   #calculate pi using the approximation technique
   #Loop until the level of percision is reached

approxPi =4/1
sign = -1
denom = 3
realPi = math.pi
while round (approxPi, precision) != round (realPi , precision) :
  RoundApp_Pi = round (approxPi, precision)
  print(f"ApproxPi = {RoundApp_Pi}")
  approxPi = approxPi + (sign*4/denom)
  sign =sign*-1
  denom=denom+2
  
end = time.time()

elapsedTime = end - start
print(f"Elapsed time : {elapsedTime}")

if __name__ == '__main__':
  main()
