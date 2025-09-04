'''def nm():
    print("Name: ----")
def rno():
    print("Roll No:----")

print(__name__)
nm()
rno()

def nm():
    print("Name: ----")
def rno():
    print("Roll No:----")
def main():
    nm()
    rno()
    
if __name__ == "__main__":
    main()

def nm():
    print("name: Raju")
def id():
    print("id no: 1122")
    
#math module
    
import math
dir(math)



import math
print(math.pi)
print(math.e)
print(math.factorial(5))
print(math.floor(1122.35))
print(math.gcd(50,90))
    

from math import pi,e
print(math.pi)
print(math.e)

import time
print(dir(time))

import time
print("Altzone (DST offset in seconds):", time.altzone)
print()
current_time = time.localtime() 
print("Asctime:", time.asctime(current_time))

epoch_time = time.time()
print("Ctime:", time.ctime(epoch_time))

print("Daylight :", time.daylight)

clock_info = time.get_clock_info('time')
print("Get Clock Info for 'time':", clock_info)

utc_time = time.gmtime(epoch_time)
print("GMT (UTC Time Tuple):", utc_time)

local_time = time.localtime(epoch_time)
print("Local Time Tuple:", local_time)

seconds_since_epoch = time.mktime(local_time)
print("Mktime (seconds since epoch):", seconds_since_epoch)



print(time.localtime())
print(time.gmtime())

import time
obj1 = time.gmtime(1627987508.6496193)
time_sec = time.mktime(obj1)
print("Local time (in seconds):", time_sec)

#23 : 12: 2024
#2024,Dec 23

import time

local_time = time.localtime()

print(local_time.tm_mday,":",local_time.tm_mon,":",local_time.tm_year)
#print(local_time.tm_year,",",time.asctime(local_time).tm_,local_time.tm_mday)

import time

def trffc_sgnl():
    for _ in range(3):
        print("Red light stop")
        time.sleep(0.1)
        
        print("Yellow light prepare to start")
        time.sleep(0.5)
        print("Green light - go")
        time.sleep(0.5)
trffc_sgnl()

  
  
  
  
import random
print(dir(random))
print(random.random())
print(random.getstate())
print(random.randrange(0,8))
print("Random float between 0 and 1:", random.random())
print(random.randint(1, 10))

my_list = [1, 2, 3, 4, 5]
print("Random choice from the list:", random.choice(my_list))
print(my_list)

import random
no = str(random.randrange(1000000000, 9000000000))
formatted_no = " ".join([no[i:i+4] for i in range(0, 12, 4)])
print(formatted_no)
   
import datetime
x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))
   '''

import pkg.details
pkg.details.nm()
pkg.details.id()






