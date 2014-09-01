# class Counter
class Counter:
    __secretCount = 0
    
    def count(self):
        self.__secretCount += 1
        print self.__secretCount

# instantiation        
counter = Counter()

counter.count()
counter.count()

try:
    print Counter.__secretCount
except:
    print 'Permission denied.'
    
# access secretCount
print counter._Counter__secretCount