import unittest
import student_code as sc
import expand

dis_map = {
	'Campus':{ 'Campus':0, 'Whole_Food':3, 'Beach':5, 'Cinema':5, 'Lighthouse':1, 'Ryan_Field':2, 'YWCA':12 },
	'Whole_Food':{ 'Campus':3, 'Whole_Food':0, 'Beach':3, 'Cinema':3, 'Lighthouse':4, 'Ryan_Field':5, 'YWCA':8 },
	'Beach':{ 'Campus':5, 'Whole_Food':3, 'Beach':0, 'Cinema':8, 'Lighthouse':5, 'Ryan_Field':7, 'YWCA':12 },
	'Cinema':{ 'Campus':5, 'Whole_Food':3, 'Beach':8, 'Cinema':0, 'Lighthouse':7, 'Ryan_Field':7, 'YWCA':2 },
	'Lighthouse':{ 'Campus':1, 'Whole_Food':4, 'Beach':5, 'Cinema':7, 'Lighthouse':0, 'Ryan_Field':1, 'YWCA':15 },
	'Ryan_Field':{ 'Campus':2, 'Whole_Food':5, 'Beach':7, 'Cinema':7, 'Lighthouse':1, 'Ryan_Field':0, 'YWCA':12 },
	'YWCA':{ 'Campus':12, 'Whole_Food':8, 'Beach':12, 'Cinema':2, 'Lighthouse':15, 'Ryan_Field':12, 'YWCA':0 } }

time_map1 = {
	'Campus':{ 'Campus':None, 'Whole_Food':14, 'Beach':13, 'Cinema':None, 'Lighthouse':11, 'Ryan_Field':None, 'YWCA':None },
	'Whole_Food':{ 'Campus':14, 'Whole_Food':None, 'Beach':14, 'Cinema':13, 'Lighthouse':None, 'Ryan_Field':None, 'YWCA':None },
	'Beach':{ 'Campus':14, 'Whole_Food':14, 'Beach':None, 'Cinema':None, 'Lighthouse':None, 'Ryan_Field':None, 'YWCA':None },
	'Cinema':{ 'Campus':None, 'Whole_Food':14, 'Beach':None, 'Cinema':None, 'Lighthouse':None, 'Ryan_Field':None, 'YWCA':12 },
	'Lighthouse':{ 'Campus':11, 'Whole_Food':None, 'Beach':None, 'Cinema':None, 'Lighthouse':None, 'Ryan_Field':11, 'YWCA':None },
	'Ryan_Field':{ 'Campus':None, 'Whole_Food':None, 'Beach':None, 'Cinema':None, 'Lighthouse':12, 'Ryan_Field':None, 'YWCA':15 },
	'YWCA':{ 'Campus':None, 'Whole_Food':None, 'Beach':None, 'Cinema':13, 'Lighthouse':None, 'Ryan_Field':15, 'YWCA':None } }
time_map2 = {
	'Campus':{ 'Campus':None, 'Whole_Food':28, 'Beach':13, 'Cinema':None, 'Lighthouse':11, 'Ryan_Field':None, 'YWCA':None },
	'Whole_Food':{ 'Campus':14, 'Whole_Food':None, 'Beach':14, 'Cinema':13, 'Lighthouse':None, 'Ryan_Field':None, 'YWCA':None },
	'Beach':{ 'Campus':14, 'Whole_Food':14, 'Beach':None, 'Cinema':None, 'Lighthouse':None, 'Ryan_Field':None, 'YWCA':None },
	'Cinema':{ 'Campus':None, 'Whole_Food':14, 'Beach':None, 'Cinema':None, 'Lighthouse':None, 'Ryan_Field':None, 'YWCA':12 },
	'Lighthouse':{ 'Campus':11, 'Whole_Food':None, 'Beach':None, 'Cinema':None, 'Lighthouse':None, 'Ryan_Field':11, 'YWCA':None },
	'Ryan_Field':{ 'Campus':None, 'Whole_Food':None, 'Beach':None, 'Cinema':None, 'Lighthouse':12, 'Ryan_Field':None, 'YWCA':15 },
	'YWCA':{ 'Campus':None, 'Whole_Food':None, 'Beach':None, 'Cinema':13, 'Lighthouse':None, 'Ryan_Field':15, 'YWCA':None } }
time_map3 = {
	'Campus':{ 'Campus':None, 'Whole_Food':22, 'Beach':13, 'Cinema':None, 'Lighthouse':11, 'Ryan_Field':None, 'YWCA':None },
	'Whole_Food':{ 'Campus':14, 'Whole_Food':None, 'Beach':14, 'Cinema':13, 'Lighthouse':None, 'Ryan_Field':None, 'YWCA':None },
	'Beach':{ 'Campus':14, 'Whole_Food':14, 'Beach':None, 'Cinema':None, 'Lighthouse':None, 'Ryan_Field':None, 'YWCA':None },
	'Cinema':{ 'Campus':None, 'Whole_Food':14, 'Beach':None, 'Cinema':None, 'Lighthouse':None, 'Ryan_Field':None, 'YWCA':12 },
	'Lighthouse':{ 'Campus':11, 'Whole_Food':None, 'Beach':None, 'Cinema':None, 'Lighthouse':None, 'Ryan_Field':11, 'YWCA':None },
	'Ryan_Field':{ 'Campus':None, 'Whole_Food':None, 'Beach':None, 'Cinema':None, 'Lighthouse':12, 'Ryan_Field':None, 'YWCA':17 },
	'YWCA':{ 'Campus':None, 'Whole_Food':None, 'Beach':None, 'Cinema':15, 'Lighthouse':None, 'Ryan_Field':15, 'YWCA':None } }
time_map4 = {
	'Campus':{ 'Campus':None, 'Whole_Food':29, 'Beach':13, 'Cinema':None, 'Lighthouse':11, 'Ryan_Field':None, 'YWCA':None },
	'Whole_Food':{ 'Campus':14, 'Whole_Food':None, 'Beach':14, 'Cinema':23, 'Lighthouse':None, 'Ryan_Field':None, 'YWCA':None },
	'Beach':{ 'Campus':14, 'Whole_Food':14, 'Beach':None, 'Cinema':None, 'Lighthouse':None, 'Ryan_Field':None, 'YWCA':None },
	'Cinema':{ 'Campus':None, 'Whole_Food':14, 'Beach':None, 'Cinema':None, 'Lighthouse':None, 'Ryan_Field':None, 'YWCA':12 },
	'Lighthouse':{ 'Campus':11, 'Whole_Food':None, 'Beach':None, 'Cinema':None, 'Lighthouse':None, 'Ryan_Field':11, 'YWCA':None },
	'Ryan_Field':{ 'Campus':None, 'Whole_Food':None, 'Beach':None, 'Cinema':None, 'Lighthouse':12, 'Ryan_Field':None, 'YWCA':16 },
	'YWCA':{ 'Campus':None, 'Whole_Food':None, 'Beach':None, 'Cinema':10, 'Lighthouse':None, 'Ryan_Field':15, 'YWCA':None } }

time_map5 = {
	'Campus':{ 'Campus':None, 'Whole_Food':29, 'Beach':13, 'Cinema':None, 'Lighthouse':11, 'Ryan_Field':None, 'YWCA':None },
	'Whole_Food':{ 'Campus':14, 'Whole_Food':None, 'Beach':14, 'Cinema':23, 'Lighthouse':None, 'Ryan_Field':None, 'YWCA':None },
	'Beach':{ 'Campus':14, 'Whole_Food':14, 'Beach':None, 'Cinema':None, 'Lighthouse':None, 'Ryan_Field':None, 'YWCA':None },
	'Cinema':{ 'Campus':None, 'Whole_Food':14, 'Beach':None, 'Cinema':None, 'Lighthouse':None, 'Ryan_Field':None, 'YWCA':None },
	'Lighthouse':{ 'Campus':11, 'Whole_Food':None, 'Beach':None, 'Cinema':None, 'Lighthouse':None, 'Ryan_Field':11, 'YWCA':None },
	'Ryan_Field':{ 'Campus':None, 'Whole_Food':None, 'Beach':None, 'Cinema':None, 'Lighthouse':12, 'Ryan_Field':None, 'YWCA':None },
	'YWCA':{ 'Campus':None, 'Whole_Food':None, 'Beach':None, 'Cinema':None, 'Lighthouse':None, 'Ryan_Field':None, 'YWCA':None } }
time_map6 = {
	'Campus':{ 'Campus':None, 'Whole_Food':29, 'Beach':13, 'Cinema':None, 'Lighthouse':11, 'Ryan_Field':None, 'YWCA':None },
	'Whole_Food':{ 'Campus':14, 'Whole_Food':None, 'Beach':14, 'Cinema':23, 'Lighthouse':None, 'Ryan_Field':None, 'YWCA':None },
	'Beach':{ 'Campus':14, 'Whole_Food':14, 'Beach':None, 'Cinema':None, 'Lighthouse':None, 'Ryan_Field':None, 'YWCA':None },
	'Cinema':{ 'Campus':None, 'Whole_Food':14, 'Beach':None, 'Cinema':None, 'Lighthouse':None, 'Ryan_Field':None, 'YWCA':12 },
	'Lighthouse':{ 'Campus':11, 'Whole_Food':None, 'Beach':None, 'Cinema':None, 'Lighthouse':None, 'Ryan_Field':11, 'YWCA':None },
	'Ryan_Field':{ 'Campus':None, 'Whole_Food':None, 'Beach':None, 'Cinema':None, 'Lighthouse':12, 'Ryan_Field':None, 'YWCA':16 },
	'YWCA':{ 'Campus':None, 'Whole_Food':None, 'Beach':None, 'Cinema':19, 'Lighthouse':None, 'Ryan_Field':15, 'YWCA':10 } }
time_map7 = {
	'Campus':{ 'Campus':None, 'Whole_Food':29, 'Beach':13, 'Cinema':None, 'Lighthouse':11, 'Ryan_Field':None, 'YWCA':None },
	'Whole_Food':{ 'Campus':14, 'Whole_Food':None, 'Beach':14, 'Cinema':23, 'Lighthouse':None, 'Ryan_Field':None, 'YWCA':None },
	'Beach':{ 'Campus':14, 'Whole_Food':14, 'Beach':None, 'Cinema':None, 'Lighthouse':None, 'Ryan_Field':None, 'YWCA':None },
	'Cinema':{ 'Campus':None, 'Whole_Food':34, 'Beach':None, 'Cinema':None, 'Lighthouse':None, 'Ryan_Field':None, 'YWCA':12 },
	'Lighthouse':{ 'Campus':11, 'Whole_Food':None, 'Beach':None, 'Cinema':None, 'Lighthouse':None, 'Ryan_Field':11, 'YWCA':None },
	'Ryan_Field':{ 'Campus':None, 'Whole_Food':None, 'Beach':None, 'Cinema':None, 'Lighthouse':12, 'Ryan_Field':None, 'YWCA':None },
	'YWCA':{ 'Campus':None, 'Whole_Food':None, 'Beach':None, 'Cinema':10, 'Lighthouse':None, 'Ryan_Field':None, 'YWCA':None } }
time_map8 = {
	'Campus':{ 'Campus':None, 'Whole_Food':None, 'Beach':13, 'Cinema':None, 'Lighthouse':11, 'Ryan_Field':None, 'YWCA':None },
	'Whole_Food':{ 'Campus':14, 'Whole_Food':None, 'Beach':14, 'Cinema':13, 'Lighthouse':None, 'Ryan_Field':None, 'YWCA':None },
	'Beach':{ 'Campus':14, 'Whole_Food':14, 'Beach':None, 'Cinema':None, 'Lighthouse':None, 'Ryan_Field':None, 'YWCA':None },
	'Cinema':{ 'Campus':None, 'Whole_Food':14, 'Beach':None, 'Cinema':None, 'Lighthouse':None, 'Ryan_Field':None, 'YWCA':12 },
	'Lighthouse':{ 'Campus':11, 'Whole_Food':None, 'Beach':None, 'Cinema':None, 'Lighthouse':None, 'Ryan_Field':11, 'YWCA':None },
	'Ryan_Field':{ 'Campus':None, 'Whole_Food':None, 'Beach':None, 'Cinema':None, 'Lighthouse':12, 'Ryan_Field':None, 'YWCA':None },
	'YWCA':{ 'Campus':None, 'Whole_Food':None, 'Beach':None, 'Cinema':15, 'Lighthouse':None, 'Ryan_Field':15, 'YWCA':None } }


class SearchTest(unittest.TestCase):
	
	def test1(self):
		expand.expand_count = 0
		path = sc.a_star_search(dis_map, time_map1, 'Campus', 'Cinema')
		self.assertEqual(path, ['Campus', 'Whole_Food', 'Cinema'])
		self.assertEqual(expand.expand_count, 4)
	
	def test2(self):
		expand.expand_count = 0
		path = sc.a_star_search(dis_map, time_map2, 'Campus', 'Cinema')
		self.assertEqual(path, ['Campus', 'Beach', 'Whole_Food', 'Cinema'])
		self.assertEqual(expand.expand_count, 6)
	
	def test3(self):
		expand.expand_count = 0
		path = sc.a_star_search(dis_map, time_map3, 'Campus', 'Cinema')
		self.assertEqual(path, ['Campus', 'Whole_Food', 'Cinema'])
		self.assertEqual(expand.expand_count, 5)

	def test4(self):
		expand.expand_count = 0
		path = sc.a_star_search(dis_map, time_map4, 'Campus', 'Cinema')
		self.assertEqual(path, ['Campus', 'Lighthouse', 'Ryan_Field', 'YWCA', 'Cinema'])
		self.assertEqual(expand.expand_count, 6)
	
	def test5(self):
		expand.expand_count = 0
		path = sc.a_star_search(dis_map, time_map1, 'Ryan_Field', 'Beach')
		self.assertEqual(path, ['Ryan_Field', 'Lighthouse', 'Campus', 'Beach'])
		self.assertEqual(expand.expand_count, 4)
	
	def test6(self):
		# Island
		# The test should return an empty list because we are trying to
		# reach an unreachable node that isn't connected to anything.
		expand.expand_count = 0
		path = sc.a_star_search(dis_map, time_map5, 'Campus', 'YWCA')
		self.assertEqual(path, [])
		self.assertEqual(expand.expand_count, 6)
	
	def test7(self):
		# Self Loop
		# There is a self loop at the beginning node. The search should still
		# proceed as normal because graph search won't look at the beginning node twice.
		expand.expand_count = 0
		path = sc.a_star_search(dis_map, time_map6, 'YWCA', 'Campus')
		self.assertEqual(path, ['YWCA', 'Ryan_Field', 'Lighthouse', 'Campus'])
		self.assertEqual(expand.expand_count, 5)

	def test8(self):
		# Big Exit
		# There is only one path to get past the first two nodes in the
		# beginning. The path cost is ridiculously high, but the search should
		# still go through it because graph search won't consider going backwards.
		expand.expand_count = 0
		path = sc.a_star_search(dis_map, time_map7, 'YWCA', 'Campus')
		self.assertEqual(path, ['YWCA', 'Cinema', 'Whole_Food', 'Campus'])
		self.assertEqual(expand.expand_count, 3)

	def test9(self):
		# One way streets
		# Testing if the code won't break despite some of the streets being only one way.
		expand.expand_count = 0
		path = sc.a_star_search(dis_map, time_map8, 'Lighthouse', 'Cinema')
		self.assertEqual(path, ['Lighthouse', 'Campus', 'Beach', 'Whole_Food', 'Cinema'])
		self.assertEqual(expand.expand_count, 5)
	
	## Time Map 1
	## Tests a trivial case where start is the same as end
	def test_start_is_end(self):
		expand.expand_count = 0
		path = sc.a_star_search(dis_map, time_map1, 'Campus', 'Campus')
		self.assertEqual(path, ['Campus'])
		self.assertEqual(expand.expand_count, 0)
	
	## Time Map 1
	## Tests a hike across the map where you almost get there from multiple directions
	def test_cross_map(self):
		expand.expand_count = 0
		path = sc.a_star_search(dis_map, time_map1, 'YWCA', 'Campus')
		self.assertEqual(path, ['YWCA', 'Ryan_Field', 'Lighthouse', 'Campus'])
		self.assertEqual(expand.expand_count, 5)
	

if __name__== "__main__": unittest.main()