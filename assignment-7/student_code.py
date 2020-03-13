import math
import re


class Bayes_Classifier:

    def __init__(self):

        self.positive_dict = {}
        self.negative_dict = {}

        self.num_pos = 0
        self.num_neg = 0

        self.unique_words = 0
        self.unique_positive = 0
        self.unique_negative = 0

    def train(self, lines):

        for line in lines:
            line = line.replace('\n', '')
            sections = line.split('|')
            star_rating = sections[0]
            review = sections[2]
            clean_review = self.clean_review(review)

            if star_rating == '5':
                self.num_pos += 1
                for word in clean_review.split():
                    if word not in self.positive_dict:
                        self.positive_dict[word] = 1
                        self.unique_positive += 1

                        if word not in self.negative_dict:
                            self.unique_words += 1

                    else:
                        self.positive_dict[word] += 1
                        self.unique_positive += 1
            else:
                self.num_neg += 1
                for word in clean_review.split():
                    if word not in self.negative_dict:
                        self.negative_dict[word] = 1
                        self.unique_negative += 1

                        if word not in self.positive_dict:
                            self.unique_words += 1

                    else:
                        self.negative_dict[word] += 1
                        self.unique_negative += 1

    def classify(self, lines):

        predictions = []

        for line in lines:
            line = line.replace('\n', '')
            sections = line.split('|')
            review = sections[2]
            clean_review = self.clean_review(review)

            p_prob = self.num_pos / float(self.num_pos + self.num_neg)
            n_prob = self.num_neg / float(self.num_pos + self.num_neg)

            p_prob = math.log10(p_prob)
            n_prob = math.log10(n_prob)

            for word in clean_review.split():
                if word in self.positive_dict:
                    p_prob += math.log10((self.positive_dict[word] + 1) / float(self.unique_positive + self.unique_words))
                else:
                    p_prob += math.log10(1 / float(self.unique_positive + self.unique_words))

                if word in self.negative_dict:
                    n_prob += math.log10((self.negative_dict[word] + 1) / float(self.unique_negative + self.unique_words))
                else:
                    n_prob += math.log10(1 / float(self.unique_negative + self.unique_words))

            if p_prob > n_prob:
                predictions.append('5')
            else:
                predictions.append('1')

        return predictions

    def clean_review(self, review):
        stop_words = [ 'a','about','above','after','again','against','all','am','an','and',
                           'any','are','as','at','be','because','been','before','being',
                           'below','between','both','but','by','cant','cannot','could',
                           'did','do','does','doing','down','during','each',
                           'few','for','from','further','had','has','have',
                           'having','he','her','here','hers','herself',
                           'him','himself','his','how','hows','i','im','if','in',
                           'into','is','it','its','its','itself','lets','me','more','most',
                           'my','myself','no','nor','not','of','off','on','once','only',
                           'or','other','ought','our','ours','ourselves','out','over','own',
                           'same','she','should','so',
                           'some','such','than','that','thats','the','their','theirs','them',
                           'themselves','then','there','theres','these','they','theyd','theyll',
                           'theyve','this','those','through','to','too',
                           'under','until','up','very','was','we','wed','well','were',
                           'weve','were','what','whats','when','whens','where',
                           'wheres','which','while','who','whos','whom','why','whys','with',
                           'wont','would','you','youd','youll','youre','youve','your',
                           'yours','yourself','yourselves' ]

        punctuation = ['!', '"', '#', '$', '%', '&', '(', ')', '*', '+',
                       ',', '.', '/', ':', ';', '=', '?', '!']

        review = review.lower()

        for character in review:
            if character in punctuation:
                review = review.replace(character, ' ')

        split = review.split()

        for i in range(len(split)):
            if split[i] == 'not' and i + 1 != len(split):
                split[i] = split[i] + split[i+1]
                split[i+1] = ''

        for word in split:
            if word in stop_words:
                split.remove(word)

        clean_review = ' '.join(map(str, split))

        return clean_review
