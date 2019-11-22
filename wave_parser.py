import ply.lex as lex
import wave_lexer
from wave_ast import Sum, Array, Number, weval

__all__ = ['Parser']

class Parser:
	def __init__(self):
		self.parent_t = None
		self.lexer = lex.lex(module=wave_lexer)
		self.sqr_count = 0
		self.paren_count = 0

	def parse(self, data):
		self.lexer.input(data)
		return self.parser()

	def parser(self):
		temp_space = []
		while True:
			token = self.lexer.token()
			if not token: break
			t = token.type

			if t == 'SUM':
				temp_space = [Sum(
					operand_space=temp_space
				)]

			elif t == 'NUMBER':
				temp_space.append(Number(
					value=token.value
				))

			elif t == 'LSQR':
				self.parent_t = t
				self.sqr_count += 1
				if self.sqr_count > 1:
					raise Exception('Nested Array not Allowed')
				temp_space.append(Array(
					space=self.parser()
				))

			elif t == 'RSQR':
				self.sqr_count -= 1
				if self.parent_t == 'LSQR':
					return temp_space
				if self.sqr_count != 0:
					raise Exception('Syntax Error for SQR')

			elif t == 'LPAREN':
				self.parent_t = t
				self.paren_count += 1
				temp_space.extend(self.parser())

			elif t == 'RPAREN':
				self.paren_count -= 1
				if self.parent_t == 'LPAREN':
					return temp_space
				if self.paren_count != 0:
					raise Exception('Syntax Error for PAREN')

			else:
				raise Exception('Unknown Token')

		if self.sqr_count != 0:
			raise Exception('Syntax Error for SQR')

		if self.paren_count != 0:
			raise Exception('Syntax Error for PAREN')

		return temp_space