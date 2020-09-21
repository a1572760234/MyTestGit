import time
time.sleep(1)
print('hello github!')

def gitfunc(num):
    '''num:循环次数'''
    for i in range(num):
        
        print(f"第{i}次问候:hello git!")


if __name__ == "__main__":
    gitfunc(100)