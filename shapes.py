#!/usr/bin/python

# Example Usage
# 
# Run "python -i shapes.py" for interactive mode.
# 
# Then, try the following:
# 	o- - - -o
# 	len(o- - -o)
# 	(o- - - -o) * 4
# 	(o- - - - -o) + (o- -o)
# 	(o- - - - -o) * (o- - - - - - -o)

class Rectangle:
	r"""
		A simple rectangle "literal" thingy. It uses operator overloading and the singleton LineMaker o to visually denote any rectangle of integer dimensions.
		Note that the "literals" are 100% valid Python syntax.
		
		A line literal of width ten:
		>>> a = o- - - - - - - - - -o
		>>> a - (o- - - -o)
		(o- - - - - -o)
		>>> a**2
		(o- - - - - - - - - -o
		|[                   ]
		|[                   ]
		|[                   ]
		|[                   ]
		|[                   ]
		|[                   ]
		|[                   ]
		|[                   ]
		|o- - - - - - - - - -o)
		
		
		
		A five by five square:
		
		>>> b = \
		... (o- - - - -o
		... |[         ]
		... |[         ]
		... |[         ]
		... |o- - - - -o)
		>>> len(b)
		25
		>>> b*2
		(o- - - - - - - - - -o
		|[                   ]
		|[                   ]
		|[                   ]
		|[                   ]
		|[                   ]
		|[                   ]
		|[                   ]
		|[                   ]
		|o- - - - - - - - - -o)
		
		
		
		
		A five by two rectangle:
		
		c =  \
		(o- - - - -o
		|o- - - - -o)
		
		
		
		A one by five rectangle:
		
		d = \
		(o-o
		|[ ]
		|[ ]
		|[ ]
		|o-o)
		
		
		Warning:
			Due to operator precedence, most of the following require parentheses around each shape literal to work properly.
			Otherwise, you might get something like "AttributeError: LineMaker instance has no attribute 'height'".
		
		Supported operations:
			+ Addition -- adds the dimensions of a rectangle
			- Subtraction -- substracts the dimensions of a rectangle
			* Scalar multiplication -- multiplies dimensions by a number, as long as the results are integers
			* Multiplication -- multiplies two lines to create a rectangle
			/ Scalar division -- divides each dimension by a number, as long as the results are integers
			** Exponentiation -- For a given rectangle r, returns r*r, r, or Rectangle(1, 1), for exponents 2, 1, and 0 respectively.
			~ Inversion -- Returns a new rectangle with the opposite dimensions. Length becomes height and vice versa.
			== Equality comparison -- True if two rectangles have the same width and height
			!= Inequality comparison -- True if two rectangles have different width or different height
		
		Other:
			repr(rect) or str(rect) returns the string which constructs the given rectangle, in the format seen above
			rect.area() returns the area of the shape (so does len(rect))
			"if rect in other_rect" returns True if either rect or ~rect (orientation doesn't matter) could be physically fit into other_rect 
		
		Note that for the addition, subtraction, and Scalar multiplication, a line will act as if it has one dimension of zero.
		This is so that (o- -o)*2, (o- -o) + (o- -o), and (o- - - - - -o) - (o- -o) will all equal (o- - - -o), and will not have
		heights 2, 2, and 0 respectively.
	"""
	
	def __init__(self, width=1, height=1):
		if width < 1:
			raise ValueError, 'width must be at least one'
		elif height < 1:
			raise ValueError, 'height must be at least one'
		elif width % 1 != 0:
			raise ValueError, 'width must be an integer'
		elif height % 1 != 0:
			raise ValueError, 'height must be an integer'
		
		self.width = int(width)
		self.height = int(height)
	
	def __repr__(self):
		if self.height == 1:
			return '(o-' + ' -'*(self.width - 1) + 'o)'
		else:
			r = '(o-' + ' -'*(self.width - 1) + 'o'
			for _ in range(self.height - 2):
				r += '\n|[' + ' '*(self.width * 2 - 1) + ']'
			r += '\n|o-' + ' -'*(self.width - 1) + 'o)'
			return r
	
	__str__ = __unicode__ = __repr__
	
	def __len__(self):
		return self.area()
	
	def __sub__(self, other):
		# We don't want anything to have a width of zero, and it's logical to assume that (o---o) - (o--o) == (o-o)
		# even thought technically their heights cancel out.
		return Rectangle((self.width - other.width) or 1, (self.height - other.height) or 1)
		
	def __add__(self, other):
		# We want (o--o) + (o--o) to equal (o----o), so if both operands have a lenght of one, so will the result, etc.
		if self.width == 1 and  other.width == 1:
			return Rectangle(1, self.height + other.height)
		if self.height == 1 and  other.height == 1:
			return Rectangle(self.width + other.width, 1)
		else:
			return Rectangle(self.width + other.width, self.height + other.height)
	
	def __or__(self, other):
		# This overloads the | operator for rows and for now it doesn't care what other is
		return Rectangle(self.width, self.height + 1)
	
	def __mul__(self, other):
		if isinstance(other, Rectangle):
			if (self.height != 1 and self.width != 1) or (self.height != 1 and self.width != 1):
				raise ValueError, 'Cannot multiply two two-dimensional shapes'
			
			if self.width != 1 and other.width != 1:
				# Dealing with two o-----o
				return Rectangle(self.width, other.width)
			elif self.height != 1 and other.height != 1:
				# Dealing with two height-only
				return Rectangle(self.height, other.height)
			else:
				# Dealing with one width-only and one height-only, keep each as appropriate dimension
				return Rectangle(max(self.width, other.width), max(self.height, other.height))
		try:
			other = float(other)
		except ValueError:
			raise ValueError, 'you must either multiply two shapes or a shape and a number'
		try:
			# Again, in this case we want (o--o)*2 to equal (o----o), so we have to count 1-height as if it were zero, etc.
			if self.width != 1 and self.height != 1:
				return Rectangle(self.width*other, self.height*other)
			elif self.width != 1:
				return Rectangle(self.width*other, 1)
			elif self.height != 1:
				return Rectangle(1, self.height*other)
			else:
				return Rectangle()
		except ValueError:
			raise ValueError, 'multiplication must result in an integer value for both dimensions'
	
	def __rmul__(self, other):
		# To cover 2*x as well as x*2
		return self.__mul__(other)
	
	def __div__(self, other):
		width = self.width
		height = self.height
		
		if width != 1:
			width = width/float(other)
			if width % 1 != 0:
				raise ValueError, 'width is not a multiple of ' + str(other)
		if height != 1:
			height = height/float(other)
			if height % 1 != 0:
				raise ValueError, 'height is not a multiple of ' + str(other)
		
		return Rectangle(width, height)
	
	def __pow__(self, other):
		if other == 2:
			return self * self
		if other == 1:
			return Rectangle(self.width, self.height)
		if other == 0:
			return Rectangle()
		else:
			raise ValueError, 'Cannot raise to a power other than 0, 1, or 2'
	
	def __invert__(self):
		return Rectangle(self.height, self.width)
	
	def __contains__(self, other):
		if not isinstance(other, Rectangle):
			return False
		if (self.width >= other.width and self.height >= other.height) or (self.width >= other.height and self.height >= other.width):
			return True
	
	def __eq__(self, other):
		if isinstance(other, Rectangle) and ((self.width == other.width and self.height == other.height) or (self.width == other.height and self.height == other.width)):
			return True
		else:
			return False
	
	def __ne__(self, other):
		return not self == other
	
	def area(self):
		return self.width * self.height

class LineMaker:
	def __init__(self, width=0):
		self.width = width
	
	def not_opened_with_o(*args):
		raise SyntaxError, 'You must use o to open a line as well as close it'
		
	# When people try to use an unopened line, e.g. "- -o", not_opened_with_o is called. Not technically a SyntaxError, but these aren't technically shape literals either.
	__repr__ = __str__ = __unicode__ = __len__ = __add__ = __sub__ = __or__ = __mul__ = __rmul__ = __div__ = __pow__ = __invert__ = __contains__ = __eq__ = area = not_opened_with_o
	
	def __neg__(self):
		return LineMaker(self.width + 1)
	
	def __sub__(self, other):
		if not isinstance(other, LineMaker):
			not_opened_with_o()
		# Make sure that this is the only way for LineMakers to become Rectangles, as both o's are required in literals
		return Rectangle(other.width + 1) # To account for the "o-" at the beginning

o = LineMaker()


import doctest
doctest.testmod()