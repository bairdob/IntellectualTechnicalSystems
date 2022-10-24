import json


class NNClassifier:
    def __init__(self, file):
        try: 
            f = open(file)
        except OSError:
            print('Could not open file:', file)
        with f:
            self.data = json.load(f)

    def type(self, hist: list, k: int) -> str:
        '''returns type object close to type in collections'''

        distanceNamed = {} # {distance: 'type1', ...}
        for index, value in enumerate(self.data['collections']):
            distanceNamed[NNClassifier.histDistance(value['hist'], hist)] = value['type']
        sortedDistanceNamed = {it: distanceNamed[it] for it in sorted(distanceNamed)[0:k]}

        typesCnt = dict.fromkeys(set(distanceNamed.values()), 0)# {type : 0, ...}
        for type in sortedDistanceNamed.values():
            typesCnt[type] = typesCnt[type] + 1

        return sorted(typesCnt)[0]
    
    @staticmethod
    def histDistance(hist1: list, hist2:list) -> float:
        '''returns distance between vectors'''
        sum = 0
        for it, value in enumerate(hist1):
            sum += (hist2[it] - hist1[it])**2
        return sum**(0.5)


if __name__ == '__main__':
    hist = [1, 2, 3, 4, 5]
    c = NNClassifier('collections.json')
    print(c.type(hist, 3))
