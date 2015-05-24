# Exercise 2.2-4:
# See the pseudocode below.

def job_not_done():
	# For a given solvable problem, there should be a way to check if it's solved or not
	# Here is the part that verifies a solution.
	return check_result

def work(input_data):
	# For a given solvable problem, it should be solved using finite amount of time and space
	# Here is the part that solves the problem.
	pass

def fun(input_data):
	while job_not_done():
		# We can stop the algorithm by checking if the work is already done.
		# The earlier we check, the shorter the best case running time can be.
		work(input_data)
	return output_data