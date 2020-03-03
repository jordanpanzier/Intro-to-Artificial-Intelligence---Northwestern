import read, copy
from util import *
from logical_classes import *

verbose = 0

class KnowledgeBase(object):
    def __init__(self, facts=[], rules=[]):
        self.facts = facts
        self.rules = rules
        self.ie = InferenceEngine()

    def __repr__(self):
        return 'KnowledgeBase({!r}, {!r})'.format(self.facts, self.rules)

    def __str__(self):
        string = "Knowledge Base: \n"
        string += "\n".join((str(fact) for fact in self.facts)) + "\n"
        string += "\n".join((str(rule) for rule in self.rules))
        return string

    def _get_fact(self, fact):
        """INTERNAL USE ONLY
        Get the fact in the KB that is the same as the fact argument

        Args:
            fact (Fact): Fact we're searching for

        Returns:
            Fact: matching fact
        """
        for kbfact in self.facts:
            if fact == kbfact:
                return kbfact

    def _get_rule(self, rule):
        """INTERNAL USE ONLY
        Get the rule in the KB that is the same as the rule argument

        Args:
            rule (Rule): Rule we're searching for

        Returns:
            Rule: matching rule
        """
        for kbrule in self.rules:
            if rule == kbrule:
                return kbrule

    def kb_add(self, fact_rule):
        """Add a fact or rule to the KB
        Args:
            fact_rule (Fact|Rule) - the fact or rule to be added
        Returns:
            None
        """
        printv("Adding {!r}", 1, verbose, [fact_rule])
        if isinstance(fact_rule, Fact):
            if fact_rule not in self.facts:
                self.facts.append(fact_rule)
                for rule in self.rules:
                    self.ie.fc_infer(fact_rule, rule, self)
            else:
                if fact_rule.supported_by:
                    ind = self.facts.index(fact_rule)
                    for f in fact_rule.supported_by:
                        self.facts[ind].supported_by.append(f)
                else:
                    ind = self.facts.index(fact_rule)
                    self.facts[ind].asserted = True
        elif isinstance(fact_rule, Rule):
            if fact_rule not in self.rules:
                self.rules.append(fact_rule)
                for fact in self.facts:
                    self.ie.fc_infer(fact, fact_rule, self)
            else:
                if fact_rule.supported_by:
                    ind = self.rules.index(fact_rule)
                    for f in fact_rule.supported_by:
                        self.rules[ind].supported_by.append(f)
                else:
                    ind = self.rules.index(fact_rule)
                    self.rules[ind].asserted = True

    def kb_assert(self, fact_rule):
        """Assert a fact or rule into the KB

        Args:
            fact_rule (Fact or Rule): Fact or Rule we're asserting
        """
        printv("Asserting {!r}", 0, verbose, [fact_rule])
        self.kb_add(fact_rule)

    def kb_ask(self, fact):
        """Ask if a fact is in the KB

        Args:
            fact (Fact) - Statement to be asked (will be converted into a Fact)

        Returns:
            listof Bindings|False - list of Bindings if result found, False otherwise
        """
        print("Asking {!r}".format(fact))
        if factq(fact):
            f = Fact(fact.statement)
            bindings_lst = ListOfBindings()
            # ask matched facts
            for fact in self.facts:
                binding = match(f.statement, fact.statement)
                if binding:
                    bindings_lst.add_bindings(binding, [fact])

            return bindings_lst if bindings_lst.list_of_bindings else []

        else:
            print("Invalid ask:", fact.statement)
            return []

    def kb_retract(self, fact_or_rule):
        """Retract a fact from the KB

        Args:
            fact (Fact) - Fact to be retracted

        Returns:
            None
        """
        printv("Retracting {!r}", 0, verbose, [fact_or_rule])
        ####################################################
        # Student code goes here


        if (isinstance(fact_or_rule, Fact) and (fact_or_rule in self.facts)):
            
            ourFact = self._get_fact(fact_or_rule)

            if (len(ourFact.supported_by) == 0):
                
                if (len(ourFact.supports_facts) != 0):
                    
                    count = len(ourFact.supports_facts)
                    for k in range(0,count):
                        self.kb_retract_helper(ourFact.supports_facts[k])

                if (len(ourFact.supports_rules) != 0):
                    
                    count2 = len(ourFact.supports_rules)
                    for k in range(0,count2):
                        self.kb_retract_helper(ourFact.supports_rules[k])

                self.facts.remove(ourFact)

            else:
                return
            
        else:
            return

    
    def kb_retract_helper(self, fact_or_rule):

        if isinstance(fact_or_rule, Fact):
            ourFact = self._get_fact(fact_or_rule)
            
            if (len(ourFact.supported_by) != 0):
                
                if (len(ourFact.supports_facts) != 0):

                    count = len(ourFact.supports_facts)
                    for k in range(0,count):
                        self.kb_retract_helper(ourFact.supports_facts[k])

                if (len(ourFact.supports_rules) != 0):
                    
                    count2 = len(ourFact.supports_rules)
                    for k in range(0,count2):
                        self.kb_retract_helper(ourFact.supports_rules[k])

                self.facts.remove(ourFact)
            else:
                return

        else:
            ourRule = self._get_rule(fact_or_rule)
            
            if (len(ourRule.supported_by) != 0):
              
                if (len(ourRule.supports_facts) != 0):

                    count = len(ourRule.supports_facts)
                    for k in range(0,count):
                        self.kb_retract_helper(ourRule.supports_facts[k])

                if (len(ourRule.supports_rules) != 0):
                    
                    count2 = len(ourRule.supports_rules)
                    for k in range(0,count2):
                        self.kb_retract_helper(ourRule.supports_rules[k])
                

                self.rules.remove(ourRule)
            else:
                return
       

class InferenceEngine(object):
    def fc_infer(self, fact, rule, kb):
        """Forward-chaining to infer new facts and rules

        Args:
            fact (Fact) - A fact from the KnowledgeBase
            rule (Rule) - A rule from the KnowledgeBase
            kb (KnowledgeBase) - A KnowledgeBase

        Returns:
            Nothing            
        """
        printv('Attempting to infer from {!r} and {!r} => {!r}', 1, verbose,
            [fact.statement, rule.lhs, rule.rhs])
        ####################################################
        # Student code goes here

        #Getting those bindings
        theBindings = match(fact.statement, rule.lhs[0])
        
        
        #If there are bindings, here's what we do
        if (theBindings):

            #If there's only one thing on the lhs, we're creating new facts maybe
            if (len(rule.lhs) == 1):
                theStatement = instantiate(rule.rhs, theBindings)
                newFact = Fact(theStatement)

                newFact.supported_by.append([fact,rule])
                fact.supports_facts.append(newFact)
                rule.supports_facts.append(newFact)
                kb.kb_assert(newFact)

            #If there's more than one thing on the lhs, we're creating new rules maybe
            else:
                #Finding how many parts are on the lhs
                count = len(rule.lhs)

                ruleLandR = []
                leftStatements = []

                #Creating the lhs of a new rule
                for k in range(1, count):
                    theLStatement = instantiate(rule.lhs[k], theBindings)
                    leftStatements.append(theLStatement)

                rightStatement = instantiate(rule.rhs, theBindings)
                ruleLandR = [leftStatements, rightStatement]
                newRule = Rule(ruleLandR)

                fact.supports_rules.append(newRule)
                rule.supports_rules.append(newRule)
                newRule.supported_by.append([fact,rule])
                kb.kb_assert(newRule)

              