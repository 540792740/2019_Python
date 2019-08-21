class Solution (object):
		def reverse(self,x):
				factor = 1
				if x < 0:
					x *= -1
					factor = -1
				
				sol = int(str(x)[::-1]) * factor
				
				if sol * factor > (2**31 - 1):
						return 0
				return sol
			
if __name__ =="__main__":
		S=Solution()
		a=S.reverse(12543)
		print(a)
