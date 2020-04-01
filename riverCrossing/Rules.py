import os
import json
import pprint


class Rules:
    """
    Contains rules as object read in from file
    """

    def __init__(self, rules_file):
        self.rules = {}
        working_dir = os.path.dirname(os.path.realpath(__file__))
        self.rules_file = working_dir + "/" + rules_file

        self.rules = self.readJsonRules()
        # output current rules
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(self.rules)


    def readJsonRules(self):
        with open(self.rules_file) as rules_file:
            data = json.load(rules_file)
        return data


    def readRules(self):
        # Read the rules file into dictionary
        with open(self.rules_file) as rules_file:
            for line in rules_file:
                key, values = line.split(':')
                split_values = [v.strip() for v in values.split(',')]
                self.rules[key] = split_values
        return self.rules
