# import external methods that will use later on in the code
import sympy as sy
# create a class called integral


class Integral:
	# create the constructors is to initialize values
	# input the question you ask and the equation you're using
	def __init__(self, question, equation):
		self.types = None  # conclude what type of question
		self.ranges = []  # conclude the range of the integral
		self.x_value = 0  # conclude the x value
		self.y_value = 0  # conclude the y value
		self.question = question  # set variable "question"
		self.equation = equation  # set variable "equation"
		self.slope = 0  # conclude the slope of the line
		self.count = 0  # a variable that helps counting
		self.integral = 0  # conclude the result of the integral
		self.index = 0  # a variable that concludes the index of a string
	# create a function called typess
	# help determine what type of question is this
	# taking derivative or integral

	def typess(self):
		# see if the word "slope" is inside the question
		if 'slope' in self.question:
			self.types = 'slope'  # if yes, set type = slope
			return self.types
		# see if the word "integral" is in side the question
		if 'area' in self.question:
			self.types = 'integral'  # if yes, set type = integral
			return self.types
		else:  # other cases
			return "I cannot solve it"  # cannot solve so far
	# create a function called rangess
	# help determine the ranges for integral
	# or the x, y value if taking derivative

	def rangess(self):
		# determine the type of question first
		if self.types == 'integral':  # if the type = integral
			# find the index of the first range of integral
			range_first = self.question.index('[') + 1
			# find the index of the second range of integral
			range_second = self.question.index(']') - 1
			# pull out the value of the first range of integral
			range_first = int(self.question[range_first])
			# pull out the value of the second range of integral
			range_second = int(self.question[range_second])
			# set the ranges for the integral
			self.ranges.append(range_first)
			self.ranges.append(range_second)
			# return the ranges of the integral
			return self.ranges
		# determine the type of question first
		if self.types == 'slope':  # if the type = derivative
			# find the index of the x value of the question
			self.x_value = self.question.index('(') + 1
			# find the index of the x value of the question
			self.y_value = self.question.index(')') - 1
			# set the variable of the x value of the question
			self.x_value = int(self.question[self.x_value])
			# set the variable of the y value of the question
			self.y_value = int(self.question[self.y_value])
		return self.ranges  # return the ranges of the question
	# create a function called calculate
	# calculate the value of the derivative
	# or calculate the value of the integral

	def calculate(self):
		x = sy.Symbol('x')  # set 'x' to the equation symbol 'x'
		if self.types == 'slope':  # if the type = derivative
			# find the derivative equation
			eq = sy.diff(eval(self.equation))
			# plug in x and find the slope
			self.slope = float(eq.subs(x, self.x_value))
			return self.slope  # return the slope
		if self.types == 'integral':  # if the type = integral
			eq = eval(self.equation)  # change string to real equation
			# check if the range is from small to big
			if int(self.ranges[0]) < int(self.ranges[1]):
				# taking the integral and find its value
				fi = self.ranges[0]
				se = self.ranges[1]
				i = sy.integrate(eq, (x, fi, se))
				# set the integral value
				self.integral = float(i)
				return self.integral  # return the integral value
			if int(self.ranges[0]) > int(self.ranges[1]):
				# taking the integral and find its value
				fi = self.ranges[0]
				se = self.ranges[1]
				i = float(sy.integrate(eq, (x, se, fi)))
				# set the integral value
				self.integral = -i
				return self.integral  # return the integral value
	# create a function called equations
	# help change the input equation into a proper equation

	def equations(self):
		self.count = 0  # variable that helps count
		self.index = 0  # variable that include the index
		# remove all the '=', 'y', " " characters
		self.equation = self.equation.replace('=', '')
		self.equation = self.equation.replace('y', '')
		self.equation = self.equation.replace(" ", '')
		if '^' in self.equation:  # change ^ into **
			# find and remove all '^'
			self.count = self.equation.index('^')
			self.equation = self.equation.replace('^', '')
			eq = self.equation  # make the line shorter
			# replace all the '^' with "**" so that sympy can read
			self.equation = eq[:self.count] + '**' + eq[self.count:]
			self.count = 0  # reset the variable
		# plus a "*" between number and 'x'(etc: 2x = 2*x)
		while self.count < 100:
			# check if number and 'x' are together or not
			if (str(self.count) + 'x') in self.equation:
				# set total = the number and 'x'
				total = str(self.count) + 'x'
				eq = self.equation
				# find the index of total in the equation
				self.index = eq.index(total)
				# remove all number with 'x'
				self.equation = eq.replace(str(self.count) + 'x', '')
				# make it shorter :)
				eq = self.equation
				i = self.index
				c = self.count
				# replace the number and 'x' with a '*' in it
				self.equation = eq[:i] + str(c) + '*' + 'x' + eq[i:]
			self.count = self.count + 1  # add 1 to loop properly
		return self.equation  # return the new equation


# **************************
# test functions starts here
# set the input question = string
string1 = 'Find the area of the following equation in the interval of [2, 8]'
# create the first testing value
va = Integral(string1, 'y = x^2 + 2x + 2')
# set the input question = string
string2 = 'Find the slope of the following equation at (2, 8)'
# create the second testing value
sl = Integral(string2, 'y = x^2 + 2x + 2')
# set the input question = string
string3 = 'Determine the area with the interval of [8, 2]'
# create the third testing value
va2 = Integral(string3, 'y = x^2 + 2x + 2')


def test_integral():
	assert callable(Integral)
	assert va.question == string1
	assert va.equation == 'x**2+2*x+2'
	assert sl.question == string2
	assert sl.equation == 'x**2+2*x+2'
	assert va2.question == string3
	assert va2.equation == 'x**2+2*x+2'


def test_types():
	assert callable(Integral.typess)
	assert type(va.typess()) == str
	assert type(va2.typess()) == str
	assert type(sl.typess()) == str
	assert va.typess() == 'integral'
	assert va2.typess() == 'integral'
	assert sl.typess() == 'slope'


def test_rangess():

	assert callable(Integral.rangess)
	assert type(va.rangess()) == list
	assert type(va2.rangess()) == list
	assert type(sl.x_value) == int
	assert type(sl.y_value) == int
	# reset all the variables in order for the test to work
	va.ranges = []
	va2.ranges = []
	assert va.rangess() == [2, 8]
	assert va2.rangess() == [8, 2]
	assert sl.x_value == 2
	assert sl.y_value == 8


def test_calculate():
	# have to run first in order for the calculate function work
	va.rangess()
	va2.rangess()
	sl.rangess()
	assert callable(Integral.calculate)
	assert type(va.calculate()) == float
	assert type(va2.calculate()) == float
	assert type(sl.calculate()) == float
	assert va.calculate() == 240
	assert sl.calculate() == 6
	assert va2.calculate() == -240


def test_equations():
	assert callable(Integral.equations)
	assert type(va.equations()) == str
	assert type(va2.equations()) == str
	assert type(sl.equations()) == str
	assert va.equation == 'x**2+2*x+2'
	assert sl.equation == 'x**2+2*x+2'
	assert va2.equation == 'x**2+2*x+2'


print(test_equations())
print(test_types())
print(test_calculate())
print(test_rangess())
print(test_integral())
