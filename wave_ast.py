from utils import kw2attr

__all__ = ['weval', 'Sum', 'Number', 'Array']

def weval(obj):
	return obj.__weval__()

class Operator:
	pass

class Operand:
	pass

class Sum(Operator):
	def __init__(self, **kwargs):
		kw2attr(self, kwargs)

	def add_bin(self, left, right):
		if isinstance(left, int):
			if isinstance(right, int):
				return left+right
			elif isinstance(right, list):
				return [left+e for e in right]
		elif isinstance(left, list):
			if isinstance(right, int):
				return [right+e for e in left]
			elif isinstance(right, list):
				left_len = len(left)
				right_len = len(right)
				if left_len > right_len:
					left, right = right, left
					left_len, right_len = right_len, left_len
				return [left[i % left_len]+right[i] for i in range(right_len)]

	def reduce(self, space):
		space_len = len(space)
		if space_len == 0:
			return 0
		elif space_len == 1:
			return space[0]
		else:
			mid = int(space_len/2)
			return self.add_bin(self.reduce(space[:mid]), self.reduce(space[mid:]))

	def __weval__(self):
		evaled_space = list(map(weval, self.operand_space))
		return self.reduce(evaled_space)

	def __repr__(self):
		return 'Sum(operand_space=[{}])'.format(
			','.join(map(repr, self.operand_space))
		)

class Number(Operand):
	def __init__(self, **kwargs):
		kw2attr(self, kwargs)

	def __weval__(self):
		return self.value

	def __repr__(self):
		return 'Number(value={})'.format(self.value)

class Array(Operand):
	def __init__(self, **kwargs):
		kw2attr(self, kwargs)

	def __weval__(self):
		return list(map(weval, self.space))

	def __repr__(self):
		return 'Array(space=[{}])'.format(
			','.join(map(repr, self.space))
		)