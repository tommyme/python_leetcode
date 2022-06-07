import time

def timeit(f):
    def warpper(*args, **kwargs):
        st = time.time()
        f(*args, **kwargs)
        print(f"{f.__name__} costs {1000*(time.time()-st):.4f}ms")
    
    return warpper

