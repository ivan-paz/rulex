"""
    Basic rulex implementation
    that works with risk factor == 1

"""
from copy import deepcopy
#-------------------------------------------------------------
def preset_into_rule(preset):
    strict_rule = []
    for i in range( len(preset) - 2 ):
        strict_rule.append( set( [ preset[i] ] ) ) #Python 3
    strict_rule.append(preset[-2])                 #Class label
    strict_rule.append(preset[-1])                 #Risk factor
    return strict_rule
#print(preset_to_rule([1,2,3,'A',1]))
#-------------------------------------------------------------
#   Before  is_compressible
def pattern_found(rule1,rule2):
    unions = []
    indexes = []
    if rule1[-2] == rule2[-2]:
        difference = 0
        for i in range( len(rule1) - 2 ):
            intersection =  rule1[i] & rule2[i]
            union = rule1[i] | rule2[i]
            unions.append(union)
            if intersection == set() or len(union) > len(intersection):# i.e if NO intersection. Note that this condition is rule formation, it isn't "intersection" between min and max.
                difference +=1
                indexes.append(i)
        if difference <= 1:    #    rule1[-1]:     # risk factor  r == 1
            return [True, unions, indexes]
        else:
            return [False, None, None]
    else:
        return [False, None, None]
#print( pattern_found( [{1}, {2}, 'A', 1], [{2}, {2}, 'A', 1])  )
#print( pattern_found([{2}, {2}, 'A', 1],[{1}, {3}, 'A', 1])  )
#print( pattern_found([{1}, {2}, 'A', 1],[{1}, {2,3},'A',1]))

def create_rule(rule1, rule2):
    [pattern, unions, indexes] = pattern_found(rule1,rule2)
    if pattern == True:
        rule = rule1
        for index in indexes:
            rule[index] = unions[index]
        return rule
    else:
        return None
#print( create_rule([{1}, {2}, 'A', 1],[{2}, {2}, 'A', 1])  )
#print( create_rule([{2}, {2}, 'A', 1],[{1}, {3}, 'A', 1]) )
#print( create_rule([{1}, {2}, 'A', 1],[{1}, {2,3},'A',1]))

#  True if a rule1 is subset of rule2, False otherwhise
def contained( rule1, rule2 ):
    if rule1[-2] == rule2[-2]:
        equalParameters = 0
        for i in range( len(rule1) - 2 ):
            if rule1[i].issubset(rule2[i]):
                equalParameters +=1
        if equalParameters == len(rule1) - 2:
            return True
        else:
            return False
    else:
        return False
# TESTS
#print(contained( [{1},{1},'A',1],[{1},{1,2,3},'A',1]) )
#print(  contained( [{2},{7},'D',1],[{2,5},{7},'D',1]   )   )

def deleteRedundant( rules ):
    for i in range(0, len(rules)):
        redundant = False
        rule1 = rules[i]
        #print('rule1',  rule1)
        for j in range(0, len(rules)):
            rule2 = rules[j]
         #   print(rule2)
            if rule1 != None and rule2 != None and i != j and contained(rule1,rule2) == True:
          #      print(rule1,'contained in', rule2)
                redundant = True
        if redundant == True:
            rules[i] = None
    return rules
# -----    test    -----
#rules = [ [{5}, {5}, 'D', 1], [{2}, {7}, 'D', 1], [{5}, {5, 7}, 'D', 1], [{2, 5}, {7}, 'D', 1] ]

#RULEX
def rulexBasic( Presets, Rules ):
    if len(Rules) == 0:
        #move the first preset to rules tramsform it into a rule --->  {}, {}, 'A', 1
        Rules.append( preset_into_rule(Presets[0]) )
        del Presets[0]
    preset_counter = -1
    for preset in Presets:
        preset_copy = deepcopy(preset)
        preset_counter +=1
        preset = preset_into_rule(preset)
        for i in range(len(Rules)):
            [pattern,b,c] = pattern_found(preset,Rules[i])#is compress OR possible_rule_formation
            if pattern == True:
                print('create : ', create_rule( preset, Rules[i] ) )
                Rules.append(create_rule( preset, Rules[i]))#APPEND RULE
                Rules.append( preset_into_rule(preset_copy))#APPEND PRESET
        Rules.append(preset_into_rule(preset_copy))#APPEND PRESET
        Presets[preset_counter] = None
    deleteRedundant(Rules)
    clean_rules = []
    for r in Rules:
        if r != None: clean_rules.append(r)
    print(clean_rules)
    return clean_rules
#Presets = [       [1,2,'A',1], [2,2,'A',1], [1,1,'B',1]  ]
#Presets = [ [ 5, 5, 'D', 1],[ 2, 7, 'D', 1],[ 5, 7, 'D', 1] ]
#Presets = [       [1,  6, 'A', 1],[3,  6, 'A', 1],[2,  4, 'A', 1],[2,  8, 'A', 1]]
#Presets = [
#        [1,4,'A',1],
#        [1,6,'A',1],
#        [2,4,'A',1],
#        [2,6,'A',1],
#        [3,4,'A',1],
#        [3,6,'A',1],
#        [8,4,'A',1],
#        [8,6,'A',1],
#        [11,4,'A',1],
#        [11,6,'A',1]
#         ]


#   Test 2  EXAMPLE 2  in documentation
Presets = [ [5,4,'B',1],  [5,5,'B',1],  [5,6,'B',1],  [4,4,'B',1],  [3,4,'B',1],  [4,6,'B',1] ]

#Presets = [[1, 1, "A", 1], [2, 1, "A", 1], [1, 3, "A", 1], [1, 4, "B", 1], [1, 11, "A", 1], [1, 12, "A", 1]]
#Presets = [  [  3 ,  4, 'B', 1],   [  4,   4, 'B', 1]  ]
#Rules = [   [ {5}, {5,4}, 'BE', 1] ]

#  Test  EXAMPLE 1
Presets = [ [1,2,'a',1], [1,4,'a',1], [5,2,'a',1],[5,4,'a',1],[2,1,'b',1],[2,3,'b',1],[4,1,'b',1] ,[4,3,'b',1] ]

Rules = []

rulexBasic( Presets, Rules )

