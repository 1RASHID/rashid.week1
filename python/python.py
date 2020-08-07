#print("Chairman Rashid")
#fullname = "Chairman Rashid"
#age = 100
#married = True
#hobbies = ['singing','dancing','parting']
#kids = {
   # "paul": "male",
  #  "maurice": "male",
 #   "ama":"female"
#}
#print(hobbies)
#if(married == False):
 #   print("Happy marriage")
#else:
 #   print("save the date!")
# function definition
#def sayHello():
 #   print("Hello world")
score = 0
num = 3

while (True):
    if(num % 3 == 0):
        response = input("please input a multiple")
        score = score + num 
        num = int(response)
    else:
            print("Game over,your score: " + str(score))
            break