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

#---------------------------------------------------------------------------
#    test with risk = 2
#    Test 1
#Presets = [[1, 1, 'A', 2], [2, 2, 'A', 2], [3, 3, 'A', 2]]
#    Test   1.1
#Presets = [[1, 1, 'A', 2], [2, 2, 'A', 2], [3, 3, 'A', 2], [1, 3, 'B', 2]]
#---------------------------------------------------------------------------

# Test different types of data
#Presets = [ [ 1, 'cat', 1/3, True, 'A', 1 ], [ 1, 'dog', 1/3, True, 'A', 1 ] ]

#----------------------------------------------------------------------
#                        parameter order independent
#CASE 1
#Presets = [ [1,1,'A',1], [2,1,'A',1], [1,2,'A',1] ]
# invert P1 and P2
#Presets = [ [1,1,'A',1], [1,2,'A',1], [2,1,'A',1] ]
#changin the order of the presets
Presets = [ [1,1,'A',1], [1,2,'A',1], [2,1,'A',1] ]
#-----------------------------------------------------------------------

Rules = []

rules = rulex(Presets, Rules)

