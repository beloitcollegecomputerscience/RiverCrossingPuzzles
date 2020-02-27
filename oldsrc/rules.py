
class Rules:
    '''Contains rules as object read in from file'''
    def __init__(self, rules_file):
        self.rules = {}
        self.rules_file = rules_file

    def readRules(self):
        # Read the rules file into dictionary
        with open(self.rules_file) as rules_file:
            for line in rules_file:
                key, values = line.split(':')
                split_values = [v.strip() for v in values.split(',')]
                self.rules[key] = split_values
        return self.rules