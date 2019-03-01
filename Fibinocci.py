# Program to display the Fibonacci sequence up to n-th term where n is provided by the user
class Fibinocci:

	@staticmethod
	def getFibinocci(nterms):
		# first two terms
		ls = []
		n1 = 0
		n2 = 1
		count = 0
		sm=0

		# check if the number of terms is valid
		if nterms <= 0:
			return "Please_enter_a_positive_Number_other_than_zero"
		elif nterms == 1:
			#print"Fibonacci sequence upto",nterms,":")
			ls.append(n1)
		else:
			#print("Fibonacci sequence upto",nterms,":")
			while count < nterms:
				#print(n1,end=' , ')
				ls.append(n1)				
				nth = n1 + n2
				sm=sm+nth
				# update values
				n1 = n2
				n2 = nth
				count += 1
		return ls

	
