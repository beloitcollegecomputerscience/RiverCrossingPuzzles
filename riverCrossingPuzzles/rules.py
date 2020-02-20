'''Rules class'''

class Rules:
    def __init__(self, rules_file):
        self.rules = {}
        self.rules_file = rules_file

    def readRules(self):
        # Read the rules file into dictionary
        with open(self.rules_file) as rules_file:
            for line in rules_file:
                key, vals = line.split(':')
                split_vals = [v.strip() for v in vals.split(',')]
                self.rules[key] = split_vals