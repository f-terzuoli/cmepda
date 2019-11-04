from multiprocessing import Process

def f(name):
    print('Hello '+name) # define a example function

#MAIN
if __name__=="__main__":
    p = Process(target=f, args=('World',))
    p.start()
    p.join()
