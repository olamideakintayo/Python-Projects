# average.py

def average(number, *args):
    return (number + sum(args)) / (1 + len(args))

print(average(45))               
print(average(10, 20))            
print(average(50, 80, 60, 45, 67, 89))     
