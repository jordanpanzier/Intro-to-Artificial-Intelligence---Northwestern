import read, copy
from util import *
from logical_classes import *


class KnowledgeBase(object):
    def __init__(self, facts=[], rules=[]):
        self.facts = facts
        self.rules = rules

    def __repr__(self):
        return 'KnowledgeBase({!r}, {!r})'.format(self.facts, self.rules)

    def __str__(self):
        string = "Knowledge Base: \n"
        string += "\n".join((str(fact) for fact in self.facts)) + "\n"
        string += "\n".join((str(rule) for rule in self.rules))
        return string

    def kb_assert(self, fact):
        """Assert a fact or rule into the KB

        Args:
            fact (Fact or Rule): Fact or Rule we're asserting in the format produced by read.py
        """

        #print("Asserting {!r}".format(fact))

        if (isinstance(fact, Fact) and (fact not in self.facts)):
            self.facts.append(fact)
        

        
    def kb_ask(self, fact):
        """Ask if a fact is in the KB

        Args:
            fact (Fact) - Fact to be asked

        Returns:
            ListOfBindings|False - ListOfBindings if result found, False otherwise
        """
        #print("Asking {!r}".format(fact))

        if (isinstance(fact,Fact)):
            lst = ListOfBindings()

            for f in self.facts:
                
                bindOrNaw = match(f.statement, fact.statement)
               
                if (bindOrNaw):
                    print("f fact")
                    print(f.statement)
                    print("fact fact")
                    print(fact.statement)
                    print("here is a binding")
                    print(bindOrNaw.bindings)
                    lst.add_bindings(bindOrNaw, f)

            if (len(lst) == 0):
                return False 
            else:
                print("here is the entire list")
                print(' '.join(map(str, lst)))
                print('')
                return lst
        
        else:
            return False








