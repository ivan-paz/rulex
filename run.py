from rulex import rulex

Presets = [
        [1,2,'a',1], 
        [1,4,'a',1], 
        [5,2,'a',1],
        [5,4,'a',1],
        [2,1,'b',1],
        [2,3,'b',1],
        [4,1,'b',1],
        [4,3,'b',1]]



#    Test 1
#Presets = [[1, 1, 'A', 2], [2, 2, 'A', 2], [3, 3, 'A', 2]]
#    Test   1.1
Presets = [[1, 1, 'A', 2], [2, 2, 'A', 2], [3, 3, 'A', 2], [1, 3, 'B', 2]]

#Presets = [ [1, 1,'A',2], [ 2, 2,'A',2], [1,2,'B',2],[4,3,'B',2] ]
Rules = []

rules = rulex(Presets, Rules)

