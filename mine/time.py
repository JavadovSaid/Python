import random,time

operetors = ['*','+','-']

min = 2
max = 12
total_problems = 10
def generation():
    left = random.randint(min,max)

    right = random.randint(min,max)
    operetor= random.choice(operetors)
    operation = str(left) +" "+ operetor +" " +str(right)
    answer = eval(operation)
    return operation,answer

wrong = 0
print("__________________________")
input('Do you wanna start press enter!')
start = time.time()
for i in range(total_problems):
     operation,answer = generation()
     while True:
         guess = input("\nProblem #"+str(i+1)+":   "+ operation +" = ")

         if guess == str(answer):
             break
         wrong+=1

end = time.time()

time = end-start

print("Congureguation,you got "+str(wrong)+" mistakes and achieve it in "+str(round(time,2))+" seconds")
print("__________________________")







