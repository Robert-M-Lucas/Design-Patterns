import time

class Pool():
    def __init__(self, create_object):
        self.free_object = []
        self.create_object = create_object
    def get_object(self):
        if len(self.free_object) == 0:
            return self.create_object()
        else:
            obj = self.free_object[-1]
            self.free_object.pop(-1)
            return obj
    def return_object(self, obj):
        self.free_object.append(obj)
    
# Expensive to instantiate object    
class ExpObj:
    def __init__(self):
        time.sleep(1)
    def doSomething(self):
        pass
    
start = time.time()
a = ExpObj()
a.doSomething()
b = ExpObj()
b.doSomething()
print("Slow method:", time.time()-start)

start = time.time()
pool = Pool(ExpObj)
a = pool.get_object()
a.doSomething()
pool.return_object(a)
b = pool.get_object()
a.doSomething()
pool.return_object(b)
print("Fast method:", time.time()-start)