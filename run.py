from rulex import rulex
#from rulex import rulex1
#Example  1 rulex description
#Presets = [
#        [1,2,'a'], 
#        [1,4,'a'], 
#        [5,2,'a'],
#        [5,4,'a']
#        [2,1,'b',1],
#        [2,3,'b',1],
#        [4,1,'b',1],
#        [4,3,'b',1]
#                    ]
#Example 2
#Presets = [[5,4,'B',1],[5,5,'B',1],[5,6,'B',1],[4,4,'B',1],[3,4,'B',1],[4,6,'B',1]]
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
#Presets = [ [1,1,'A',1], [1,2,'A',1], [2,1,'A',1] ]
#-----------------------------------------------------------------------

# test 1 for the incremental algorithm
#Presets = [[1,2,'a'],[1,4,'a'],[5,2,'a'],[5,4,'a']]

#Presets = [[1,1,'a'],[2,1,'a'],[3,1,'a'],[4,1,'a'],[5,1,'a'],[6,1,'a'],[7,1,'a'],[8,1,'a']]
#Presets = [[1,1,'a'],[2,1,'a'],[3,1,'a']]

#Example section of algorithm complexity
#Presets =[[1,1,'a'],[1,2,'a'],[2,1,'a']] 

# set of presets Table 1 whose rules are in table Table 2
Presets = [
	[100,0.5,'Part A'],
	[100,0.7,'Part A'],
	[150,0.5,'Part A'],
	[150,0.7,'Part A']
	]

# set of presets Table 3 permutation of Table 1
Presets = [
        [100,0.5,'Part A'],
	[150,0.5,'Part A'],
        [100,0.7,'Part A'],
        [150,0.7,'Part A']
        ]

Rules = []

#             presets  rules  dist delete_redundant after each iteration
#             False is the predefined value
rules = rulex(Presets, Rules, 1, True)


#Eliminationg redundant
#print('second version rulex1')
#Presets =[[1,1,'a'],[1,2,'a'],[2,1,'a']]
#R = []
#rules = rulex(Presets, Rules, 1, 1)


#pruebas 26sept2017
#for i in rules:
#    print(i,type(i))
#    for j in i:
#        print(j,type(j))


