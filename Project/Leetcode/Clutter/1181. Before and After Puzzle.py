class Solution(object):

    def beforeAndAfterPuzzles(self, phrases):
        """
        :type phrases: List[str]
        :rtype: List[str]
        """
        # Using two dicts and two lists:
        # 1. Save first word, dic_first
        # 3. Save result index and res as res_index, res
        dic_first, res, res_index = {}, [], []
        phrases = sorted(phrases)

        # Save all first and last words into dict, at the same time find matched sentences
        for i in range(len(phrases)):
            phrases[i] = phrases[i].split()
            if phrases[i]:
                dic_first[phrases[i][0]] = dic_first.get(phrases[i][0], []) + [i]


        for i, sentence in enumerate(phrases):
            if sentence[-1] in dic_first:
                res_index.append([i, dic_first[sentence[-1]]])

        # Init function to generate res based on res_index
        def generate_res(res_index, res):
            for r in res_index:
                for r_index in r[1]:
                    if r_index != r[0]:
                        temp1 = phrases[r[0]][:len(phrases[r[0]]) - 1]
                        print(temp1, phrases[r[0]][:-1])
                        temp2 = phrases[r_index]
                        temp = ' '.join(temp1 + temp2)
                        if temp not in res:
                            res.append(temp)

        generate_res(res_index, res)
        return sorted(res)

if __name__ == '__main__':
    S = Solution()
    test = S.beforeAndAfterPuzzles(["mission statement","a quick bite to eat","a chip off the old block", "chocolate bar","mission impossible", "a man on a mission","block party","eat my words","bar of soap a"])
    test = S.beforeAndAfterPuzzles(["ghanuo qxi b vxbjg stdsoe xylid e jss skzkhfy f dihh id","vxbjg","wy uia bbg ulfoyo wmss e uia qznglzi kuoqsjm jjarip sdfrvleh agq qznglzi dihh skfm","wmss b chyfiw z chyfiw uvq qjrfodti pgjuaolq id aee ncbd cjmnmexu zclfup gwgeyw qxi aee id skzkhfy","wmss uia xylid bbg jjarip agq chyfiw skzkhfy uhmc aee ddicv e sdfrvleh nq","jss wj f agq uhmc pkore vxbjg ghanuo ddicv","qjrfodti e jss uhmc agq qznglzi nq id nq z aee vnckr skzkhfy pgjuaolq zclfup ulfoyo","pgjuaolq rwlxefgf gwgeyw kuoqsjm wj wmss b e","e aekq wmss agq uhmc vlyp wj qxi jss uhmc uvq ncbd vn wj agq","skfm jjarip wy agq pxqqtzw vn skfm z yoskkg zclfup e qjrfodti vlyp jjarip wj e b","sdfrvleh qznglzi uhmc id aee qznglzi z agq stdsoe","kuoqsjm cfjo skzkhfy rwlxefgf aekq chyfiw sdfrvleh nq e zclfup vlyp","qxi","agq kuoqsjm z skfm z jjarip aekq qznglzi skfm jss pxqqtzw ddicv skzkhfy e cfjo skzkhfy wy e","vxbjg qxi jjarip vn","id z jjarip jjarip yoskkg ncbd uia uia cjmnmexu","rwlxefgf cfjo pxqqtzw f chyfiw ddicv gwgeyw qxi vlyp jjarip pkore uvq f skzkhfy","wy uhmc vxbjg agq ghanuo zclfup z aee","bbg uia rwlxefgf skfm z z","z uvq zclfup wj agq stdsoe vnckr vlyp jjarip z ncbd b vnckr vlyp dihh f dihh vlyp agq pxqqtzw f","aekq z qznglzi chyfiw uia aee zclfup zclfup stdsoe z aee gwgeyw uhmc uyotjsgg thifuxm f","qznglzi cjmnmexu wy pkore vnckr wj wj wj","xylid z wmss e cfjo ulfoyo wy vn bbg ncbd yoskkg ghanuo b qznglzi ncbd xylid","gwgeyw pxqqtzw vnckr dihh sdfrvleh f z","e jjarip aekq bbg aekq wj z ghanuo pkore pgjuaolq","vn chyfiw uhmc id uvq","f vnckr z rwlxefgf f skzkhfy ncbd qznglzi thifuxm qjrfodti stdsoe uyotjsgg z id","kuoqsjm qznglzi wj yoskkg cjmnmexu gwgeyw gwgeyw thifuxm","gwgeyw f e ncbd aee xylid ddicv vlyp yoskkg ulfoyo z yoskkg chyfiw b qxi qjrfodti bbg","z vnckr sdfrvleh aekq uyotjsgg e vxbjg wy ulfoyo aekq skzkhfy wj f rwlxefgf pxqqtzw","e jjarip vnckr skfm rwlxefgf qjrfodti sdfrvleh aee wmss f","aee qznglzi qjrfodti uyotjsgg e z b vn uia cfjo ghanuo f thifuxm cjmnmexu aee z uhmc thifuxm pkore","wy uhmc sdfrvleh aekq zclfup kuoqsjm kuoqsjm z aee","qjrfodti z jss skzkhfy wj wy","bbg pgjuaolq zclfup wy","vxbjg vn wy","z e pxqqtzw vnckr pxqqtzw pkore b wmss gwgeyw uia ghanuo z cjmnmexu wj wj chyfiw jss","thifuxm vn kuoqsjm z vnckr wj yoskkg ncbd uvq kuoqsjm skzkhfy jss yoskkg chyfiw vlyp skfm dihh wy b","uvq uia qjrfodti cjmnmexu dihh vlyp jjarip qznglzi wmss wj","uvq z vn vn stdsoe uyotjsgg qxi z","uhmc aee stdsoe","f cfjo ddicv bbg skfm kuoqsjm qjrfodti e","chyfiw id f uhmc ddicv e qxi zclfup z vn e","id pkore e dihh uhmc stdsoe wj vn","aee skzkhfy jjarip uyotjsgg z aekq e wj pkore uvq wy dihh jss f","wy qznglzi pkore qjrfodti vlyp agq qxi","cjmnmexu dihh sdfrvleh stdsoe vnckr vxbjg uvq cjmnmexu uhmc agq xylid b","e z cjmnmexu uhmc qxi ddicv jss cjmnmexu vnckr e jjarip jjarip aekq ncbd e dihh","wmss vn qznglzi id skfm ncbd aee ghanuo zclfup wj pxqqtzw ulfoyo id","rwlxefgf stdsoe cjmnmexu f qxi ghanuo e uvq agq thifuxm stdsoe jss ulfoyo vlyp b ddicv e z"])
    print(test)

'''
['a chip off the old block', 
'a man on a mission', 
'a quick bite to eat', 
'bar of soap a', 
'block party', 
'chocolate bar', 
'eat my words', 
'mission impossible', 
'mission statement']
'''

class Solution(object):
    def beforeAndAfterPuzzles(self, phrases):
        """
        :type phrases: List[str]
        :rtype: List[str]
        """
        # Using one dict and two lists:
        # 1. Save first word into dic_first
        # 2. Save result's index into res_index
        # 3. Save restult into res[]

        dic_first, res, res_index = {}, [], []  # Init dic_first, res

        phrases = sorted(phrases)  # Sort phrases

        # Split phrases and Save first word into dic_first
        for i in range(len(phrases)):
            phrases[i] = phrases[i].split()  # Split phrases and Save into a list

            # Save all first word into dic, if there is duplicate word, save as a list of each index
            dic_first[phrases[i][0]] = dic_first.get(phrases[i][0], []) + [i]

        # Find all possible res when last word in dic_first
        for i, sentence in enumerate(phrases):
            if sentence[-1] in dic_first:
                res_index.append([i, dic_first[sentence[-1]]])

        # Init a function to generate result based on the index:
        def generate_res(res_index, res):
            for index in res_index:
                for first_word_index in index[1]:
                    if index[0] != first_word_index:  # Avoid connect with sentense itself, eg: 'a bb bb a'
                        temp1 = phrases[index[0]][:-1]
                        temp2 = phrases[first_word_index]
                        temp = ' '.join(temp1 + temp2)
                        if temp not in res: res.append(temp)
            return

        generate_res(res_index, res)
        return sorted(res)




