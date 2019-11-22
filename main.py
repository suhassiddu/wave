from wave_parser import Parser
from wave_ast import weval

def main():
	assert str(Parser().parse('9 7 71(0 (2) 4)(3 5) 83+')) == '[Sum(operand_space=[Number(value=9),Number(value=7),Number(value=71),Number(value=0),Number(value=2),Number(value=4),Number(value=3),Number(value=5),Number(value=83)])]'
	
	assert str(Parser().parse('9 7 71(0 (2) 4+)(3 5) 83+')) == '[Sum(operand_space=[Number(value=9),Number(value=7),Number(value=71),Sum(operand_space=[Number(value=0),Number(value=2),Number(value=4)]),Number(value=3),Number(value=5),Number(value=83)])]'
	
	assert str(Parser().parse('9 7 71+(0 (2) 4)+(3 5) 83+')) == '[Sum(operand_space=[Sum(operand_space=[Sum(operand_space=[Number(value=9),Number(value=7),Number(value=71)]),Number(value=0),Number(value=2),Number(value=4)]),Number(value=3),Number(value=5),Number(value=83)])]'
	
	try:
		str(Parser().parse('9 7 71[0 2 4)[3 5] 83+'))
	except Exception as e:
		assert str(e) == 'Syntax Error for PAREN'

	try:
		str(Parser().parse('9 7 71 [0 2 4][3 5 83+'))
	except Exception as e:
		assert str(e) == 'Syntax Error for SQR'
	
	try:
		str(Parser().parse('9 7 71 0 2 4]3 5] 83+'))
	except Exception as e:
		assert str(e) == 'Syntax Error for SQR'
		
	try:
		str(Parser().parse('9 7 71 [0 2 4[3 ]5] 83+'))
	except Exception as e:
		assert str(e) == 'Nested Array not Allowed'
	
	assert weval(Parser().parse('9 7 71[0 2 4][3 5] 83+')[0]) == [173, 177, 177]
	
	assert weval(Parser().parse('9 7 71+(0 (2) 4)+(3 5) 83+')[0]) == 184

if __name__ == "__main__":
	main()
	print("All TestCases Passed")