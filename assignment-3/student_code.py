from expand import expand

def a_star_search (dis_map, time_map, start, end):
	
	path = []

	if (start and end in dis_map and time_map):
		open_list = []
		close_list = []

		start_node = Node(start, 0, 0, None)

		open_list.append(start_node)

		while (open_list != []):

			compare = float('inf')
			current = Node(start, float('inf'), float('inf'), None)
			for x in open_list:
				if x.g + x.h <= compare:
					if x.g + x.h == compare:
						if x.name < current.name:
							current = x
							compare = x.g + x.h
					else:
						current = x
						compare = x.g + x.h

			open_list.remove(current)

			if current.name == end:
				#RETURN PATH
				return get_path(current)
			else:
				if current.name not in close_list:

					for neighbor in get_successors(dis_map, time_map, current, end):
						tentative_score = current.g + time_map[current.name][neighbor.name]

						if tentative_score < neighbor.g:
							neighbor.parent = current
							neighbor.g = tentative_score
							neighbor.h = dis_map[neighbor.name][end]
							if neighbor not in open_list:
								open_list.append(neighbor)
					close_list.append(current.name)
	

	return path


def get_path(current):
	path = []

	if current.parent == None:
		path.insert(0, current.name)
		return path

	else:
		more_to_get = True
		while(more_to_get):

			if current == None: 
				more_to_get = False

			else:
				path.insert(0, current.name)
				current = current.parent
			
	return path


def get_successors(dis_map, time_map, start, end):
	successors = []

	for x in expand(start.name, time_map):

		successor_node = Node(x, float('inf'), float('inf'), start)
		successors.append(successor_node)

	return successors


class Node: 

	def __init__(self, name, g, h, parent):

		self.name = name
		self.g = g
		self.h = h
		self.parent = parent

	def __str__(self):

		return ("The name is " + self.name + ", the g is " + 
			str(self.g) + ", the h is " + str(self.h))


