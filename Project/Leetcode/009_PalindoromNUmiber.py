class Solution (object):
		def isPalindorome(self, x):
				if x < 0:
						return False
				else:
						txt = str(x)
						return txt == txt[::-1]
						
if __name__ == "__main__":
		S = Solution()
		a = S.isPalindorome(-41234321) 
		print(a)
		
