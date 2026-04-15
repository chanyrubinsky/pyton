from datetime import datetime

#1

def run_time_dec(func):
    def wrapper():
        start = datetime.now()
        func()
        finish = datetime.now()
        print(finish-start)
    return wrapper


@run_time_dec
def func():
    for i in range(1000):
        print()


func()


#2
my_dict = {}
def dec2(function):
    def wrapper(*args,**kwargs):
        data = my_dict.get(function.__name__())
        if data:
          val = data.get(args)
         if val & data.get(args):
            return val
         else
             result=function(*args,**kwargs)
             my_dict[len(my_dict)]={key:}


