'''

'''
class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        def parse(email):
            local, domain = email.split('@')
            local = local.split('+')[0].replace('.','')
            return f'{local}@{domain}'
        return len(set(map(parse,emails)))

if __name__ == '__main__':
    S = Solution()
    a = S.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"])
    print(a)
