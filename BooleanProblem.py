
def BooleanProblem(s1, s2, n):
    # Create two matrix , one for storing the count for true values
    # for each expression and other one for false count
    
	dpf = [[0 for i in range(n + 1)]
		for i in range(n + 1)]
	dpt = [[0 for i in range(n + 1)]
		for i in range(n + 1)]
 
	# Using gap strategy
	# For gap = 0 where i == j  i.e the center most diagonal
 
	for i in range(n):
		if s1[i] == 'F':
			# Expression will give false value only in string is F
			dpf[i][i] = 1
		else:
			dpf[i][i] = 0

		if s1[i] == 'T':
			# Expression will give true value only in string is T
			dpt[i][i] = 1
		else:
			dpt[i][i] = 0

	# Since we completed for gap == 0 above , starting from gap == 1
	# i will always start from 0 and j starts from gap value
	# Refer to diagram here : 
	
	for gap in range(1, n):
		i = 0
		for j in range(gap, n):
			dpt[i][j] = dpf[i][j] = 0
   
			for g in range(gap):

				#find place of parenthesization using current value of gap
				k = i + g

				# Any expression consists of a left side expression , right side expression and an operator
				# Right side of an expression can be found from index i to k
				# Left side can be founf out by k + 1 to j 
				# Tik -> Total value of left expression of True and False Matrix
				# Tkj -> Total value of right expression of True and False matrix 
    
				tik = dpt[i][k] + dpf[i][k]
				tkj = dpt[k + 1][j] + dpf[k + 1][j]

				#  recursive formulas  according to the current operator
	
 
				if s2[k] == '&':
					dpt[i][j] += dpt[i][k] * dpt[k + 1][j]
					dpf[i][j] += (tik * tkj - dpt[i][k] *
								dpt[k + 1][j])
				if s2[k] == '|':
					dpf[i][j] += dpf[i][k] * dpf[k + 1][j]
					dpt[i][j] += (tik * tkj - dpf[i][k] *
								dpf[k + 1][j])
				if s2[k] == '^':
					dpt[i][j] += (dpf[i][k] * dpt[k + 1][j] +
								dpt[i][k] * dpf[k + 1][j])
					dpf[i][j] += (dpt[i][k] * dpt[k + 1][j] +
								dpf[i][k] * dpf[k + 1][j])
			i += 1
	return dpt[0][n - 1]

# Input the String and Operators

s1 = input()	#Eg : TFFT

s2 = input()	#Eg : &|^

n = len(s1)

print(BooleanProblem(s1,s2, n))
