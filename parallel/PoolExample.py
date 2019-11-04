import multiprocessing as mp
import os

def cube(x):
    print (str(os.getpid())+" "+str(os.getppid()))
    return x**3

#MAIN
if __name__=="__main__":
    pool = mp.Pool(processes=4)
    results = pool.map(cube,range(1,7))
    print(results)
