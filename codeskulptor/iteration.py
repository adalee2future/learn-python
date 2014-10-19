def count_odd(numbers):
    count = 0
    for num in numbers:
        if num % 2 == 1:
            count += 1
    return count
    
def check_odd(numbers):
    for num in numbers:
        if num % 2 == 1:
            return True
    return False
    
def remove_odd(numbers):
    remove = []
    for num in numbers:
        if num % 2 == 1:
            remove.append(num)
    for num in remove:
        numbers.remove(num)

def remove_last_odd(numbers):
    has_odd = False
    last_odd = 0
    for num in numbers:
        if num % 2 == 1:
            has_odd = True
            last_odd = num
            
    if has_odd:
        numbers.remove(last_odd)
        
def run():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    print numbers
    #remove_odd(numbers)
    remove_last_odd(numbers)
    print numbers
    
run()