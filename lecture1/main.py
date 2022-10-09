import random, time
from statistics import mean


def initList(lenght: int = 1000000, maxint: int = 999) -> list:
    '''returns list with random generated integer digits'''

    arr = []
    for it in range(lenght):
        arr.append(random.randint(0, maxint))

    return arr

def calcHist(inputList: list) -> list:
    '''returns histrogram of occurencies in 10 intervals'''

    hist = [0]*10
    
    for it in inputList:
        if it in list(range(0, 100)):
            hist[0]+=1
        elif it in list(range(100, 200)):
            hist[1]+=1
        elif it in list(range(200, 300)):
            hist[2]+=1
        elif it in list(range(300, 400)):
            hist[3]+=1
        elif it in list(range(400, 500)):
            hist[4]+=1
        elif it in list(range(500, 600)):
            hist[5]+=1
        elif it in list(range(600, 700)):
            hist[6]+=1
        elif it in list(range(700, 800)):
            hist[7]+=1
        elif it in list(range(800, 900)):
            hist[8]+=1
        else:
            hist[9]+=1

    return hist

def calcTime(inputList: list) -> float:
    '''returns runtime calcHist()'''

    start = time.time()
    calcHist(inputList)
    end = time.time()

    return end - start


if __name__ == '__main__':
    timeList = []

    for it in range(0, 100):
        l = initList()
        timeList.append(calcTime(l))

    print('Runtime calcHist():')
    print('max =', max(timeList))
    print('min =', min(timeList))
    print('mean =', mean(timeList))
