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
