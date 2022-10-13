def histDistance(hist1: list, hist2:list) -> float:
    '''returns disntance between vectors'''
    sum = 0
    for it, value in enumerate(hist1):
        sum += (hist2[it] - hist1[it])**2
    return sum**(0.5)

def readHist(file: str) -> list:
    '''returns the histogram read from the file'''
    with open(file, 'r') as f:
        line = f.read()
    l = map(float, line.rstrip().split(','))
    return list(l) 

def writeHist(file: str, hist: list) -> list:
    '''writes hist to file'''
    text = ', '.join(str(it) for it in hist)
    with open(file, 'w') as f:
        f.write(text)

def triangle(size):
    print(*(('{:^'+str(2*size+1)+'}').format('*'*row) for row in range(1, 2*size+1, 2)), sep='\n')


if __name__ == '__main__':
    l1 = [4, -6, 3]
    l2 = [-1, 5, 4]
    file = 'test.txt'

    print('distance =', histDistance(l1, l2))
    writeHist(file, l1)
    print('readed list =', readHist('test.txt'))
    triangle(3)
