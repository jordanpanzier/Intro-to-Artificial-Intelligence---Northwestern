import unittest
import read, copy
from logical_classes import *
from student_code import KnowledgeBase

class KBTest(unittest.TestCase):

    def setUp(self):
        # Assert starter facts
        file = 'statements_kb4.txt'
        self.data = read.read_tokenize(file)
        data = read.read_tokenize(file)
        self.KB = KnowledgeBase([], [])
        for item in data:
            if isinstance(item, Fact) or isinstance(item, Rule):
                self.KB.kb_assert(item)
      
     
    def test1(self):
        # Did the student code contain syntax errors, AttributeError, etc.
        ask1 = read.parse_input("fact: (motherof ada ?X)")
        print(' Asking if', ask1)
        answer = self.KB.kb_ask(ask1)
        #pprint_justification(answer)
        self.assertEqual(str(answer[0]), "?X : bing")
    
    def test2(self):
        # Can fc_infer actually infer
        ask1 = read.parse_input("fact: (grandmotherof ada ?X)")
        print(' Asking if', ask1)
        answer = self.KB.kb_ask(ask1)
        #pprint_justification(answer)
        self.assertEqual(str(answer[0]), "?X : felix")
        self.assertEqual(str(answer[1]), "?X : chen")
    
    
    def test3(self):
        # Does retract actually retract things 
        r1 = read.parse_input("fact: (motherof ada bing)")
        print(' Retracting', r1)
        self.KB.kb_retract(r1)
        ask1 = read.parse_input("fact: (grandmotherof ada ?X)")
        print(' Asking if', ask1)
        answer = self.KB.kb_ask(ask1)
        #pprint_justification(answer)
        self.assertEqual(len(answer), 1)
        self.assertEqual(str(answer[0]), "?X : felix")
    
    def test4(self):
        # makes sure retract does not retract supported fact
        ask1 = read.parse_input("fact: (grandmotherof ada ?X)")
        print(' Asking if', ask1)
        answer = self.KB.kb_ask(ask1)
        #pprint_justification(answer)
        self.assertEqual(str(answer[0]), "?X : felix")
        self.assertEqual(str(answer[1]), "?X : chen")

        r1 = read.parse_input("fact: (grandmotherof ada chen)")
        print(' Retracting', r1)
        self.KB.kb_retract(r1)

        print(' Asking if', ask1)
        answer = self.KB.kb_ask(ask1)
        #pprint_justification(answer)
        self.assertEqual(str(answer[0]), "?X : felix")
        self.assertEqual(str(answer[1]), "?X : chen")
    
    def test5(self):
        # makes sure retract does not deal with rules
        ask1 = read.parse_input("fact: (parentof ada ?X)")
        print(' Asking if', ask1)
        answer = self.KB.kb_ask(ask1)
        #pprint_justification(answer)
        self.assertEqual(str(answer[0]), "?X : bing")
        r1 = read.parse_input("rule: ((motherof ?x ?y)) -> (parentof ?x ?y)")
        print(' Retracting', r1)
        self.KB.kb_retract(r1)
        print(' Asking if', ask1)
        answer = self.KB.kb_ask(ask1)
        #pprint_justification(answer)
        self.assertEqual(str(answer[0]), "?X : bing")
    
    def test6(self):
        r1 = read.parse_input("fact: (motherof bing chen)")
        print(' Retracting', r1)
        self.KB.kb_retract(r1)

        ask1 = read.parse_input("fact: (grandmotherof ada ?X)")
        print(' Asking if', ask1)
        answer = self.KB.kb_ask(ask1)
        self.assertEqual(len(answer), 1)
        self.assertEqual(str(answer[0]), "?X : felix")

    def test7(self):
        in1 = read.parse_input("fact: (sisters bing dannydevito)")
        print(' Asserting in', in1)
        self.KB.kb_assert(in1)

        a1 = read.parse_input("fact: (auntof dannydevito ?X)")
        print(' Asking if', a1)
        answer = self.KB.kb_ask(a1)
        self.assertEqual(str(answer[0]), "?X : chen")

        r1 = read.parse_input("fact: (sisters bing dannydevito)")
        print(' Retracting', r1)
        self.KB.kb_retract(r1)

        a2 = read.parse_input("fact: (auntof dannydevito ?X)")
        print(' Asking if', a2)
        answer = self.KB.kb_ask(a2)
        self.assertEqual(answer, [])
    
    
    def test8(self):
        # tests with a new rule that makes new inferences
        in1 = read.parse_input("rule: (grandmotherof ?x ?y) -> (homie ?y)")
        print(' Asserting in', in1)
        self.KB.kb_assert(in1)

        a1 = read.parse_input("fact: (homie ?X)")
        print(' Asking if', a1)
        answer = self.KB.kb_ask(a1)
        self.assertEqual(str(answer[0]), "?X : felix")
        self.assertEqual(str(answer[1]), "?X : chen")

        r1 = read.parse_input("fact: (motherof ada bing)")
        print(' Retracting', r1)
        self.KB.kb_retract(r1)

        a2 = read.parse_input("fact: (homie ?X)")
        print(' Asking if', a2)
        answer = self.KB.kb_ask(a2)
        self.assertEqual(str(answer[0]), "?X : felix")
    
    
    def test9(self):
        in1 = read.parse_input("fact: (motherof chen jesus)")
        print(' Asserting in', in1)
        self.KB.kb_assert(in1)

        in2 = read.parse_input("rule: ((parentof ?x ?y) (parentof ?y ?z) (parentof ?z ?zz)) -> (greatgrandmotherof ?x ?zz)")
        print(' Asserting in', in2)
        self.KB.kb_assert(in2)

        a1 = read.parse_input("fact: (greatgrandmotherof ?X jesus)")
        print(' Asking if', a1)
        answer = self.KB.kb_ask(a1)
        self.assertEqual(str(answer[0]), "?X : ada")

        r1 = read.parse_input("fact: (motherof ada bing)")
        print(' Retracting', r1)
        self.KB.kb_retract(r1)

        a2 = read.parse_input("fact: (greatgrandmotherof ?X jesus)")
        print(' Asking if', a2)
        answer = self.KB.kb_ask(a2)
        self.assertEqual(answer, [])
    

def pprint_justification(answer):
    """Pretty prints (hence pprint) justifications for the answer.
    """
    if not answer: print('Answer is False, no justification')
    else:
        print('\nJustification:')
        for i in range(0,len(answer.list_of_bindings)):
            # print bindings
            print(answer.list_of_bindings[i][0])
            # print justifications
            for fact_rule in answer.list_of_bindings[i][1]:
                pprint_support(fact_rule,0)
        print

def pprint_support(fact_rule, indent):
    """Recursive pretty printer helper to nicely indent
    """
    if fact_rule:
        #print(' '*indent, "Support for")

        if isinstance(fact_rule, Fact):
            print(' '*(indent+1), fact_rule.statement)
        else:
            print(' '*(indent+1), '(', ') '.join([str(s) for s in fact_rule.lhs]), ')', "->", fact_rule.rhs)

        if fact_rule.supported_by:
            for pair in fact_rule.supported_by:
                print(' '*(indent+2), "support option")
                for next in pair:
                    pprint_support(next, indent+2)



if __name__ == '__main__':
    unittest.main()
