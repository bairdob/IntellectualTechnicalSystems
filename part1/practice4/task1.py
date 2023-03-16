def even_number():
    n = 0
    while True:
        yield n
        n += 2
    
if __name__ == '__main__':
    x = even_number()
    print(next(x))
    print(next(x))
    print(next(x))
    print(next(x))
