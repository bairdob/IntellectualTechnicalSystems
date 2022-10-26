import os, time


def readData(path):
    try:
        f = open(path, 'r')
    except OSError:
        print('Could not open/read file:', readpath)
    with f:
        floats = list(map(float, f))
        return (floats)


if __name__ == '__main__':
    path = 'data.txt'
    data = readData(path)
    while 1:
        for number in data:
            print(number)
            time.sleep(1)
            cmd = 'mosquitto_pub -t \'test/topic\' -m \'{}\''.format(number)
            try:
                os.system(cmd)
            except Exception as e:
                print(e)
