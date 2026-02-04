#TempConvert.py
#Name: Nidhi Agarwal
#Date: 02/04/2026
#Assignment: Temperature conversion


def main():
  #Prompt the user for a Fahrenheit temperature
  #Convert that temperature to celsius, rounding to 1 decimal percision
  #Output converted temperature.

  user_input = input("Please enter temperature in Fahrenheit:  ")
  tempF = float (user_input)
 
  tempC = (tempF -32) * 5/9
  tempC = round (tempC,1)

  print(tempF, "is ", tempC, "degrees celsius.")
if __name__ == '__main__':
  main()
