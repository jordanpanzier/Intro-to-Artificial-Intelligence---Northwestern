import pandas as pd
from bayesnet import BayesNet, BayesNode


def makeCancerNet():
    df = pd.read_csv('cancer_data.csv')
    bn = BayesNet()
    total = len(df)

    # P(Age)
    # Add a BayesNode associated with Age to bn following P(Genes) example below
    # calculate P(Age > 55)
    # Add your code here
    age_rule = (df['Age'] > 55)
    age = len(df[age_rule])
    age_prob = age / total
    bn.add(BayesNode('Age', None, (True, False), {
        '': {True: age_prob, False: 1 - age_prob}}))

    # P(Genes)
    gen_rule = df['Genes'] == 'T'
    gen = len(df[gen_rule])
    gen_prob = gen / total
    bn.add(BayesNode('Genes', None, (True, False), {
        '': {True: gen_prob, False: 1 - gen_prob}}))

    # P(Cancer| Age, Genes)
    # Add a BayesNode associated with Cancer given Age and Genes to bn
    # calculate P(Cancer | Age, Genes)
    # calculate P(Cancer | Age, ~Genes)
    # calculate P(Cancer | ~Age, Genes)
    # calculate P(Cancer | ~Age, ~Genes)

    ### Add your code here
    age_rule = df['Age'] > 55
    df_age = df[age_rule]
    age_gene_rule = df_age['Genes'] == 'T'
    df_age_gene = df_age[age_gene_rule]
    age_gene = len(df_age_gene)
    cancer_rule = df_age_gene['Cancer'] == 'T'
    cancer = len(df_age_gene[cancer_rule])
    p_cancer_t_t = cancer / age_gene

    age_rule = df['Age'] > 55
    df_age = df[age_rule]
    age_gene_rule = df_age['Genes'] == 'F'
    df_age_gene = df_age[age_gene_rule]
    age_gene = len(df_age_gene)
    cancer_rule = df_age_gene['Cancer'] == 'T'
    cancer = len(df_age_gene[cancer_rule])
    p_cancer_t_f = cancer / age_gene

    age_rule = df['Age'] <= 55
    df_age = df[age_rule]
    age_gene_rule = df_age['Genes'] == 'T'
    df_age_gene = df_age[age_gene_rule]
    age_gene = len(df_age_gene)
    cancer_rule = df_age_gene['Cancer'] == 'T'
    cancer = len(df_age_gene[cancer_rule])
    p_cancer_f_t = cancer / age_gene

    age_rule = df['Age'] <= 55
    df_age = df[age_rule]
    age_gene_rule = df_age['Genes'] == 'F'
    df_age_gene = df_age[age_gene_rule]
    age_gene = len(df_age_gene)
    cancer_rule = df_age_gene['Cancer'] == 'T'
    cancer = len(df_age_gene[cancer_rule])
    p_cancer_f_f = cancer / age_gene

    bn.add(BayesNode('Cancer', ['Age', 'Genes'], (True, False),{
        (True, True): {True: p_cancer_t_t, False: 1 - p_cancer_t_t},
        (True, False): {True: p_cancer_t_f, False: 1 - p_cancer_t_f},
        (False, True): {True: p_cancer_f_t, False: 1 - p_cancer_f_t},
        (False, False): {True: p_cancer_f_f, False: 1 - p_cancer_f_f}
    }))

    # P(Test | Cancer)
    # Add a BayesNode associated with Test given Cancer to bn
    # calculate P(Test | Cancer)
    # calculate P(Test | ~Cancer)

    ### Add your code here
    cancer_rule = df['Cancer'] == 'T'
    df_cancer = df[cancer_rule]
    cancer = len(df_cancer)
    test_rule = df_cancer['Test'] == 'P'
    test = len(df_cancer[test_rule])
    p_test_t = test / cancer

    cancer_rule = df['Cancer'] == 'F'
    df_cancer = df[cancer_rule]
    cancer = len(df_cancer)
    test_rule = df_cancer['Test'] == 'P'
    test = len(df_cancer[test_rule])
    p_test_f = test / cancer

    bn.add(BayesNode('Test', ['Cancer'], ('Positive', 'Negative'), {
        True: {'Positive': p_test_t, 'Negative': 1 - p_test_t},
        False: {'Positive': p_test_f, 'Negative': 1 - p_test_f }}))

    # P(Treatment | Test)
    test_rule = df['Test'] == 'P'
    df_test = df[test_rule]
    test = len(df_test)
    trtmt_rule = df_test['Treatment'] == 'T'
    trtmt = len(df_test[trtmt_rule])
    trtmt_p = trtmt / test

    test_rule = df['Test'] == 'N'
    df_test = df[test_rule]
    test = len(df_test)
    trtmt_rule = df_test['Treatment'] == 'T'
    trtmt = len(df_test[trtmt_rule])
    trtmt_n = trtmt / test

    bn.add(BayesNode('Treatment', ['Test'], (True, False), {
        'Positive': {True: trtmt_p, False: 1 - trtmt_p},
        'Negative': {True: trtmt_n, False: 1 - trtmt_n}
    }))

    # P(Prognosis | Age, Test, Treatment)
    # Add a BayesNode associated with Prognosis given Age, Test, Treatment to bin
    # calculate P(Prognosis | Age, Test, Treatment)
    # calculate P(Prognosis | ~Age, Test, Treatment)
    # calculate P(Prognosis | Age, ~Test, Treatment)
    # calculate P(Prognosis | ~Age, ~Test, Treatment)
    # calculate P(Prognosis | Age, Test, ~Treatment)
    # calculate P(Prognosis | ~Age, Test, ~Treatment)
    # calculate P(Prognosis | Age, ~Test, ~Treatment)
    # calculate P(Prognosis | ~Age, ~Test, ~Treatment)
    # Add your code here

    # Prognosis 1
    age_rule = df['Age'] > 55
    df_age = df[age_rule]
    age_test_rule = df_age['Test'] == 'P'
    df_age_test = df_age[age_test_rule]
    age_test_trtmt_rule = df_age_test['Treatment'] == 'T'
    df_age_test_trtmt = df_age_test[age_test_trtmt_rule]
    age_test_trtmt = len(df_age_test_trtmt)
    prognosis_rule = df_age_test_trtmt['Prognosis'] == 1
    prognosis = len(df_age_test_trtmt[prognosis_rule])
    p_prog1_t_t_t = prognosis / age_test_trtmt

    age_rule = df['Age'] <= 55
    df_age = df[age_rule]
    age_test_rule = df_age['Test'] == 'P'
    df_age_test = df_age[age_test_rule]
    age_test_trtmt_rule = df_age_test['Treatment'] == 'T'
    df_age_test_trtmt = df_age_test[age_test_trtmt_rule]
    age_test_trtmt = len(df_age_test_trtmt)
    prognosis_rule = df_age_test_trtmt['Prognosis'] == 1
    prognosis = len(df_age_test_trtmt[prognosis_rule])
    p_prog1_f_t_t = prognosis / age_test_trtmt

    age_rule = df['Age'] > 55
    df_age = df[age_rule]
    age_test_rule = df_age['Test'] == 'N'
    df_age_test = df_age[age_test_rule]
    age_test_trtmt_rule = df_age_test['Treatment'] == 'T'
    df_age_test_trtmt = df_age_test[age_test_trtmt_rule]
    age_test_trtmt = len(df_age_test_trtmt)
    prognosis_rule = df_age_test_trtmt['Prognosis'] == 1
    prognosis = len(df_age_test_trtmt[prognosis_rule])
    p_prog1_t_f_t = prognosis / age_test_trtmt

    age_rule = df['Age'] <= 55
    df_age = df[age_rule]
    age_test_rule = df_age['Test'] == 'N'
    df_age_test = df_age[age_test_rule]
    age_test_trtmt_rule = df_age_test['Treatment'] == 'T'
    df_age_test_trtmt = df_age_test[age_test_trtmt_rule]
    age_test_trtmt = len(df_age_test_trtmt)
    prognosis_rule = df_age_test_trtmt['Prognosis'] == 1
    prognosis = len(df_age_test_trtmt[prognosis_rule])
    p_prog1_f_f_t = prognosis / age_test_trtmt

    age_rule = df['Age'] > 55
    df_age = df[age_rule]
    age_test_rule = df_age['Test'] == 'P'
    df_age_test = df_age[age_test_rule]
    age_test_trtmt_rule = df_age_test['Treatment'] == 'F'
    df_age_test_trtmt = df_age_test[age_test_trtmt_rule]
    age_test_trtmt = len(df_age_test_trtmt)
    prognosis_rule = df_age_test_trtmt['Prognosis'] == 1
    prognosis = len(df_age_test_trtmt[prognosis_rule])
    p_prog1_t_t_f = prognosis / age_test_trtmt

    age_rule = df['Age'] <= 55
    df_age = df[age_rule]
    age_test_rule = df_age['Test'] == 'P'
    df_age_test = df_age[age_test_rule]
    age_test_trtmt_rule = df_age_test['Treatment'] == 'F'
    df_age_test_trtmt = df_age_test[age_test_trtmt_rule]
    age_test_trtmt = len(df_age_test_trtmt)
    prognosis_rule = df_age_test_trtmt['Prognosis'] == 1
    prognosis = len(df_age_test_trtmt[prognosis_rule])
    p_prog1_f_t_f = prognosis / age_test_trtmt

    age_rule = df['Age'] > 55
    df_age = df[age_rule]
    age_test_rule = df_age['Test'] == 'N'
    df_age_test = df_age[age_test_rule]
    age_test_trtmt_rule = df_age_test['Treatment'] == 'F'
    df_age_test_trtmt = df_age_test[age_test_trtmt_rule]
    age_test_trtmt = len(df_age_test_trtmt)
    prognosis_rule = df_age_test_trtmt['Prognosis'] == 1
    prognosis = len(df_age_test_trtmt[prognosis_rule])
    p_prog1_t_f_f = prognosis / age_test_trtmt

    age_rule = df['Age'] <= 55
    df_age = df[age_rule]
    age_test_rule = df_age['Test'] == 'N'
    df_age_test = df_age[age_test_rule]
    age_test_trtmt_rule = df_age_test['Treatment'] == 'F'
    df_age_test_trtmt = df_age_test[age_test_trtmt_rule]
    age_test_trtmt = len(df_age_test_trtmt)
    prognosis_rule = df_age_test_trtmt['Prognosis'] == 1
    prognosis = len(df_age_test_trtmt[prognosis_rule])
    p_prog1_f_f_f = prognosis / age_test_trtmt

    #Prognosis 3
    age_rule = df['Age'] > 55
    df_age = df[age_rule]
    age_test_rule = df_age['Test'] == 'P'
    df_age_test = df_age[age_test_rule]
    age_test_trtmt_rule = df_age_test['Treatment'] == 'T'
    df_age_test_trtmt = df_age_test[age_test_trtmt_rule]
    age_test_trtmt = len(df_age_test_trtmt)
    prognosis_rule = df_age_test_trtmt['Prognosis'] == 3
    prognosis = len(df_age_test_trtmt[prognosis_rule])
    p_prog3_t_t_t = prognosis / age_test_trtmt

    age_rule = df['Age'] <= 55
    df_age = df[age_rule]
    age_test_rule = df_age['Test'] == 'P'
    df_age_test = df_age[age_test_rule]
    age_test_trtmt_rule = df_age_test['Treatment'] == 'T'
    df_age_test_trtmt = df_age_test[age_test_trtmt_rule]
    age_test_trtmt = len(df_age_test_trtmt)
    prognosis_rule = df_age_test_trtmt['Prognosis'] == 3
    prognosis = len(df_age_test_trtmt[prognosis_rule])
    p_prog3_f_t_t = prognosis / age_test_trtmt

    age_rule = df['Age'] > 55
    df_age = df[age_rule]
    age_test_rule = df_age['Test'] == 'N'
    df_age_test = df_age[age_test_rule]
    age_test_trtmt_rule = df_age_test['Treatment'] == 'T'
    df_age_test_trtmt = df_age_test[age_test_trtmt_rule]
    age_test_trtmt = len(df_age_test_trtmt)
    prognosis_rule = df_age_test_trtmt['Prognosis'] == 3
    prognosis = len(df_age_test_trtmt[prognosis_rule])
    p_prog3_t_f_t = prognosis / age_test_trtmt

    age_rule = df['Age'] <= 55
    df_age = df[age_rule]
    age_test_rule = df_age['Test'] == 'N'
    df_age_test = df_age[age_test_rule]
    age_test_trtmt_rule = df_age_test['Treatment'] == 'T'
    df_age_test_trtmt = df_age_test[age_test_trtmt_rule]
    age_test_trtmt = len(df_age_test_trtmt)
    prognosis_rule = df_age_test_trtmt['Prognosis'] == 3
    prognosis = len(df_age_test_trtmt[prognosis_rule])
    p_prog3_f_f_t = prognosis / age_test_trtmt

    age_rule = df['Age'] > 55
    df_age = df[age_rule]
    age_test_rule = df_age['Test'] == 'P'
    df_age_test = df_age[age_test_rule]
    age_test_trtmt_rule = df_age_test['Treatment'] == 'F'
    df_age_test_trtmt = df_age_test[age_test_trtmt_rule]
    age_test_trtmt = len(df_age_test_trtmt)
    prognosis_rule = df_age_test_trtmt['Prognosis'] == 3
    prognosis = len(df_age_test_trtmt[prognosis_rule])
    p_prog3_t_t_f = prognosis / age_test_trtmt

    age_rule = df['Age'] <= 55
    df_age = df[age_rule]
    age_test_rule = df_age['Test'] == 'P'
    df_age_test = df_age[age_test_rule]
    age_test_trtmt_rule = df_age_test['Treatment'] == 'F'
    df_age_test_trtmt = df_age_test[age_test_trtmt_rule]
    age_test_trtmt = len(df_age_test_trtmt)
    prognosis_rule = df_age_test_trtmt['Prognosis'] == 3
    prognosis = len(df_age_test_trtmt[prognosis_rule])
    p_prog3_f_t_f = prognosis / age_test_trtmt

    age_rule = df['Age'] > 55
    df_age = df[age_rule]
    age_test_rule = df_age['Test'] == 'N'
    df_age_test = df_age[age_test_rule]
    age_test_trtmt_rule = df_age_test['Treatment'] == 'F'
    df_age_test_trtmt = df_age_test[age_test_trtmt_rule]
    age_test_trtmt = len(df_age_test_trtmt)
    prognosis_rule = df_age_test_trtmt['Prognosis'] == 3
    prognosis = len(df_age_test_trtmt[prognosis_rule])
    p_prog3_t_f_f = prognosis / age_test_trtmt

    age_rule = df['Age'] <= 55
    df_age = df[age_rule]
    age_test_rule = df_age['Test'] == 'N'
    df_age_test = df_age[age_test_rule]
    age_test_trtmt_rule = df_age_test['Treatment'] == 'F'
    df_age_test_trtmt = df_age_test[age_test_trtmt_rule]
    age_test_trtmt = len(df_age_test_trtmt)
    prognosis_rule = df_age_test_trtmt['Prognosis'] == 3
    prognosis = len(df_age_test_trtmt[prognosis_rule])
    p_prog3_f_f_f = prognosis / age_test_trtmt

    # Prognosis 5
    age_rule = df['Age'] > 55
    df_age = df[age_rule]
    age_test_rule = df_age['Test'] == 'P'
    df_age_test = df_age[age_test_rule]
    age_test_trtmt_rule = df_age_test['Treatment'] == 'T'
    df_age_test_trtmt = df_age_test[age_test_trtmt_rule]
    age_test_trtmt = len(df_age_test_trtmt)
    prognosis_rule = df_age_test_trtmt['Prognosis'] == 5
    prognosis = len(df_age_test_trtmt[prognosis_rule])
    p_prog5_t_t_t = prognosis / age_test_trtmt

    age_rule = df['Age'] <= 55
    df_age = df[age_rule]
    age_test_rule = df_age['Test'] == 'P'
    df_age_test = df_age[age_test_rule]
    age_test_trtmt_rule = df_age_test['Treatment'] == 'T'
    df_age_test_trtmt = df_age_test[age_test_trtmt_rule]
    age_test_trtmt = len(df_age_test_trtmt)
    prognosis_rule = df_age_test_trtmt['Prognosis'] == 5
    prognosis = len(df_age_test_trtmt[prognosis_rule])
    p_prog5_f_t_t = prognosis / age_test_trtmt

    age_rule = df['Age'] > 55
    df_age = df[age_rule]
    age_test_rule = df_age['Test'] == 'N'
    df_age_test = df_age[age_test_rule]
    age_test_trtmt_rule = df_age_test['Treatment'] == 'T'
    df_age_test_trtmt = df_age_test[age_test_trtmt_rule]
    age_test_trtmt = len(df_age_test_trtmt)
    prognosis_rule = df_age_test_trtmt['Prognosis'] == 5
    prognosis = len(df_age_test_trtmt[prognosis_rule])
    p_prog5_t_f_t = prognosis / age_test_trtmt

    age_rule = df['Age'] <= 55
    df_age = df[age_rule]
    age_test_rule = df_age['Test'] == 'N'
    df_age_test = df_age[age_test_rule]
    age_test_trtmt_rule = df_age_test['Treatment'] == 'T'
    df_age_test_trtmt = df_age_test[age_test_trtmt_rule]
    age_test_trtmt = len(df_age_test_trtmt)
    prognosis_rule = df_age_test_trtmt['Prognosis'] == 5
    prognosis = len(df_age_test_trtmt[prognosis_rule])
    p_prog5_f_f_t = prognosis / age_test_trtmt

    age_rule = df['Age'] > 55
    df_age = df[age_rule]
    age_test_rule = df_age['Test'] == 'P'
    df_age_test = df_age[age_test_rule]
    age_test_trtmt_rule = df_age_test['Treatment'] == 'F'
    df_age_test_trtmt = df_age_test[age_test_trtmt_rule]
    age_test_trtmt = len(df_age_test_trtmt)
    prognosis_rule = df_age_test_trtmt['Prognosis'] == 5
    prognosis = len(df_age_test_trtmt[prognosis_rule])
    p_prog5_t_t_f = prognosis / age_test_trtmt

    age_rule = df['Age'] <= 55
    df_age = df[age_rule]
    age_test_rule = df_age['Test'] == 'P'
    df_age_test = df_age[age_test_rule]
    age_test_trtmt_rule = df_age_test['Treatment'] == 'F'
    df_age_test_trtmt = df_age_test[age_test_trtmt_rule]
    age_test_trtmt = len(df_age_test_trtmt)
    prognosis_rule = df_age_test_trtmt['Prognosis'] == 5
    prognosis = len(df_age_test_trtmt[prognosis_rule])
    p_prog5_f_t_f = prognosis / age_test_trtmt

    age_rule = df['Age'] > 55
    df_age = df[age_rule]
    age_test_rule = df_age['Test'] == 'N'
    df_age_test = df_age[age_test_rule]
    age_test_trtmt_rule = df_age_test['Treatment'] == 'F'
    df_age_test_trtmt = df_age_test[age_test_trtmt_rule]
    age_test_trtmt = len(df_age_test_trtmt)
    prognosis_rule = df_age_test_trtmt['Prognosis'] == 5
    prognosis = len(df_age_test_trtmt[prognosis_rule])
    p_prog5_t_f_f = prognosis / age_test_trtmt

    age_rule = df['Age'] <= 55
    df_age = df[age_rule]
    age_test_rule = df_age['Test'] == 'N'
    df_age_test = df_age[age_test_rule]
    age_test_trtmt_rule = df_age_test['Treatment'] == 'F'
    df_age_test_trtmt = df_age_test[age_test_trtmt_rule]
    age_test_trtmt = len(df_age_test_trtmt)
    prognosis_rule = df_age_test_trtmt['Prognosis'] == 5
    prognosis = len(df_age_test_trtmt[prognosis_rule])
    p_prog5_f_f_f = prognosis / age_test_trtmt

    bn.add(BayesNode('Prognosis', ['Age', 'Test', 'Treatment'], (1, 3, 5),{
        (True, 'Positive', True): {1: p_prog1_t_t_t, 3: p_prog3_t_t_t, 5: p_prog5_t_t_t},
        (False, 'Positive', True): {1: p_prog1_f_t_t, 3: p_prog3_f_t_t, 5: p_prog5_f_t_t},
        (True, 'Negative', True): {1: p_prog1_t_f_t, 3: p_prog3_t_f_t, 5: p_prog5_t_f_t},
        (False, 'Negative', True): {1: p_prog1_f_f_t, 3: p_prog3_f_f_t, 5: p_prog5_f_f_t},
        (True, 'Positive', False): {1: p_prog1_t_t_f, 3: p_prog3_t_t_f, 5: p_prog5_t_t_f},
        (False, 'Positive', False): {1: p_prog1_f_t_f, 3: p_prog3_f_t_f, 5: p_prog5_f_t_f},
        (True, 'Negative', False): {1: p_prog1_t_f_f, 3: p_prog3_t_f_f, 5: p_prog5_t_f_f},
        (False, 'Negative', False): {1: p_prog1_f_f_f, 3: p_prog3_f_f_f, 5: p_prog5_f_f_f},
    }))

    return bn


def ask(var, value, evidence, bn):
    # Add your code here
    # Use joint probability chain ruling

    q = {}
    for x in bn.get_var(var).space:
        new_evidence = dict(evidence)
        new_evidence[var] = x
        q[x] = enumerate_all(bn.variables, new_evidence, bn)

    numerator = q[value]
    denominator = 0

    for x in bn.get_var(var).space:
        denominator += q[x]

    return numerator/denominator


def enumerate_all(vars, e, bn):
    if len(vars) == 0 or vars is None:
        return 1.0
    else:
        y = vars[0]
        if y.name in e:
            value = e[y.name]
            return bn.get_var(y.name).probability(value, e) * enumerate_all(vars[1:], e, bn)
        else:
            count = 0
            for x in y.space:
                new_evidence = dict(e)
                new_evidence[y.name] = x
                count = count + bn.get_var(y.name).probability(x, e) * enumerate_all(vars[1:], new_evidence, bn)

            return count



if __name__ == '__main__':
    net = makeCancerNet()
    print(net)