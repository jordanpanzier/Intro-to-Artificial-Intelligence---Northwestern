from bayesnet import BayesNet, BayesNode
import student_code as sc
import unittest

class BayesTest(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		cls.bn = sc.makeCancerNet()

	'''
	def test1a(self):
		a = sc.ask('Age', True, {}, BayesTest.bn)
		print('P(a)', a)
		self.assertAlmostEqual(0.6, a)


	def test1b(self):
		c = sc.ask('Genes', True, {}, BayesTest.bn)
		print('P(g)=', c)
		self.assertAlmostEqual(0.2, c)


	def test2a(self):
		c = sc.ask('Cancer', True, {'Age':True, 'Genes':True}, BayesTest.bn)
		print('P(c|a,g)=', c)
		self.assertAlmostEqual(0.1, c)

	
	def test2b(self):
		c = sc.ask('Cancer', False, {'Age':True, 'Genes':True}, BayesTest.bn)
		print('P(~c|a,g)=', c)
		self.assertAlmostEqual(0.9, c)

	def test2c(self):
		c = sc.ask('Cancer', False, {'Age':True, 'Genes':False}, BayesTest.bn)
		print('P(~c|a,~g)=', c)
		self.assertAlmostEqual(0.99, c)

	def test2d(self):
		c = sc.ask('Test', 'Positive', {'Cancer': True}, BayesTest.bn)
		print('P(t|c)=', c)
		self.assertAlmostEqual(0.9821428571428571, c, places=4)

	def test2e(self):
		c = sc.ask('Treatment', True, {'Test': 'Positive'}, BayesTest.bn)
		print('P(tr|te)=', c)
		self.assertAlmostEqual(0.9927884615384616, c, places=4)

	def test2f(self):
		c = sc.ask('Prognosis', 1, {'Treatment': True}, BayesTest.bn)
		print('P(p==1|tr)=', c)
		self.assertAlmostEqual(0.10139041597453123, c, places=4)

	def test3(self):
		g = sc.ask('Genes', True, {'Cancer':True}, BayesTest.bn)
		print('P(g|c)=', g)
		self.assertAlmostEqual(0.7142857142857143, g, places=4)

	def test4(self):
		p = sc.ask('Prognosis', 5, {'Age':True, 'Test':'Positive'}, BayesTest.bn)
		print('P(p==5|a,t)=', p)
		self.assertAlmostEqual(0.14891826923076923, p, places=4)

	def test5(self):
		c = sc.ask('Genes', True, {'Test':'Positive'}, BayesTest.bn)
		print('P(g|t)=', c)
		self.assertAlmostEqual(0.46642596356180643, c, places=4)

	# For tests 9-13, values should be exactly as found in the cpt for the node
	def test9(self):
		t = sc.ask('Test', 'Positive', {'Cancer': False}, BayesTest.bn)
		print('P(Test="Positive"|-c', t)
		self.assertAlmostEqual(0.02, t, places=2)

	def test10(self):
		t = sc.ask('Treatment', True, {'Test': 'Negative'}, BayesTest.bn)
		print('P(tr=|-te', t)
		self.assertAlmostEqual(0.199812187, t, places=4)

	def test11(self):
		p = sc.ask('Prognosis', 1, {'Treatment': True, 'Test': 'Positive', 'Age': True}, BayesTest.bn)
		print('P(p=1|tr,te,a)', p)
		self.assertAlmostEqual(0.310714286, p, places=4)

	def test12(self):
		p = sc.ask('Prognosis', 3, {'Treatment': True, 'Test': 'Positive', 'Age': True}, BayesTest.bn)
		print('P(p=3|tr,te,a)', p)
		self.assertAlmostEqual(0.539285714, p, places=4)

	def test13(self):
		p = sc.ask('Prognosis', 1, {'Treatment': False, 'Test': 'Negative', 'Age': False}, BayesTest.bn)
		print('P(p=1|-tr,-te,-a)', p)
		self.assertAlmostEqual(0.010022632, p, places=4)

	'''
	def test1c(self):
		c = sc.ask('Cancer', True, {}, BayesTest.bn)
		print('P(c)=', c)
		self.assertAlmostEqual(0.0224, c)

	def test1d(self):
		c = sc.ask('Test', 'Positive', {}, BayesTest.bn)
		print('P(te)=', c)
		self.assertAlmostEqual(0.0416, c)

	def test1e(self):
		c = sc.ask('Treatment', False, {}, BayesTest.bn)
		print('P(tr)=', c)
		self.assertAlmostEqual(0.7672, c)

	def test1f(self):
		c = sc.ask('Prognosis', 3, {}, BayesTest.bn)
		print('P(p==3)=', c)
		self.assertAlmostEqual(0.1319049234366881, c, places=4)

	def test2g(self):
		c = sc.ask('Prognosis', 5, {'Age': False}, BayesTest.bn)
		print('P(p==5|¬a)=', c)
		self.assertAlmostEqual(0.9482493677603683, c, places=4)

	def test2h(self):
		c = sc.ask('Treatment', True, {'Cancer': False}, BayesTest.bn)
		print('P(tr|¬c)=', c)
		self.assertAlmostEqual(0.21571064747479804, c, places=4)

	def test2i(self):
		c = sc.ask('Genes', True, {'Prognosis': 3}, BayesTest.bn)
		print('P(g|p==3)=', c)
		self.assertAlmostEqual(0.2281383067746976, c, places=4)

	def test3a(self):
		c = sc.ask('Test', 'Negative', {'Prognosis': 3, 'Age': True}, BayesTest.bn)
		print('P(¬te|p==3, a)=', c)
		self.assertAlmostEqual(0.8719779284081078, c, places=4)

	def test3b(self):
		c = sc.ask('Cancer', False, {'Treatment': True, 'Test': 'Positive'}, BayesTest.bn)
		print('P(c|tr, te)=', c)
		self.assertAlmostEqual(0.47115384615384615, c, places=4)

	def test4a(self):
		c = sc.ask('Test', 'Positive', {'Treatment': True, 'Prognosis': 1, 'Genes': False}, BayesTest.bn)
		print('P(te|tr, p==1, ¬g)=', c)
		self.assertAlmostEqual(0.37638133353548264, c, places=4)

	def test5a(self):
		c = sc.ask('Cancer', True, {'Treatment': False, 'Prognosis': 3, 'Age': False, 'Genes': True}, BayesTest.bn)
		print('P(c|¬tr, p==3, ¬a, g)=', c)
		self.assertAlmostEqual(0.0009581593304489263, c, places=4)

	def test6a(self):
		c = sc.ask('Test', 'Negative',
				   {'Cancer': False, 'Treatment': True, 'Prognosis': 5, 'Age': False, 'Genes': True}, BayesTest.bn)
		print('P(¬te|¬c, tr, p==5, ¬a, ¬g)=', c)
		self.assertAlmostEqual(0.9490936726628768, c, places=4)


if __name__== "__main__":
	unittest.main()


