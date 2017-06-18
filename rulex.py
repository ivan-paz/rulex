from rulex_for_class import rulex_for_class
def splitClasses(Presets, Rules):
    dictionary_of_classes = dict()
    for preset in Presets:
        preset_class = preset[-2]
        if preset_class not in dictionary_of_classes:
            dictionary_of_classes[preset_class] = [[],[]]
            dictionary_of_classes[preset_class][0].append(preset)
        else:
            dictionary_of_classes[preset_class][0].append(preset)
    for rule in Rules:
        rule_class = rule[-2]
        if rule_class not in doctionary_of_classes:
            dictionary_of_classes[rule_class] = [[],[]]
            dictionary_of_classes[rule_class][1].append(rule)
        else:
            dictionary_of_classes[rule_class][1].append(rule)
    return dictionary_of_classes
#-----------------------------------------------------------------

def rulex(Presets,Rules):
    Extracted_rules = []
    dictionary_of_classes = splitClasses(Presets,Rules)
    for key in dictionary_of_classes:
        presets_other_classes = []
        for key1 in dictionary_of_classes:
            if key1 != key:
                for p in dictionary_of_classes[key1][0]:
                    presets_other_classes.append(p)
            else:
                presets_same_class = dictionary_of_classes[key][0]
                rules_same_class = dictionary_of_classes[key][1]
        print('presets same class as',key, presets_same_class)
        print('key',key, presets_other_classes)
        rules = rulex_for_class(presets_same_class,rules_same_class,presets_other_classes)
        for r in rules:
            if r != None:
                Extracted_rules.append(r)
    print('Extracted Rules', Extracted_rules)
    return Extracted_rules
