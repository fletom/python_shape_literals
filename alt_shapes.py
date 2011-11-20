
# Just fooling around with possible 3D forms for now

class O:
	def __neg__(self):
		print 'O.__neg__()'
		return self
	
	def __sub__(self, other):
		print 'O.__sub__(' + str(other) + ')'
		return self
	
	def __or__(self, other):
		print 'O.__or__(' + str(other) + ')'
		return self
	
	def __div__(self, other):
		print 'O.__div__(' + str(other) + ')'
		return self
	
	def __call__(self, *args):
		print 'O.__call__(' + str(args) + ')'
		return self
	
	def __getitem__(self, key):
		print 'O.__getitem__(' + str(key) + ')'
		return self

o = l = ol = lo = O()

# a =  (o- - - - -ol['         ']['         ']|o- - - - -o)

a = (o- - - - -ol
    ('         ')
    ('         ')
    ('         ')
    |o- - - - -o)


b =  (o- - - - -ol
    /'         '/l
   /'         '/ l
  /'         '/  l
 |o- - - - -o|   o
 ('         ')  /
 ('         ') /
 ('         ')/
 lo- - - - -o)