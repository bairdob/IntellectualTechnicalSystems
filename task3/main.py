import json


class NNClassifier:
    def __init__(self, file):
        f = open(file)
        self.data = json.load(f)
        f.close()

    def type(self, hist: list) -> str:
        '''returns type object close to type in collections'''

        minIndex = 0
        minDistance = NNClassifier.histDistance(self.data['collections'][0]['hist'], hist)
    
        for index, value in enumerate(self.data['collections']):
            distance = NNClassifier.histDistance(value['hist'], hist)
            if distance < minDistance:
                minIndex = index
                minDistance = distance

        return self.data['collections'][minIndex]['type']
    
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
    print(c.type(hist))
