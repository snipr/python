import time

def speedFunc(func):

    def speedTime():

        start=time.time()
        func()

        end=time.time()
        print(f"return time: {end-start}") 
    return speedTime
@speedFunc
def testFunc():
    numbers=range(1,20000)
    for num in numbers:

         print (num)
    

testFunc()      