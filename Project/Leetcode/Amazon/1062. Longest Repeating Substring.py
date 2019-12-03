
# 100% beat, O(N ** 2)
def longestRepeatingSubstring(S):
    ls = len(S)
    i, j, res = 0, 1, 0
    while j < ls:
        sub = S[i : j]
        if sub in S[i + 1:]:
            res = max(res, j - i)
            j += 1
        else:
            i += 1
            if i == j:
                j += 1
    return res

# sliding window
# TLE
def longestRepeatingSubstring(S):
    """
    :type S: str
    :rtype: int
    """
    for ls in range(len(S) - 2, 0, -1):
        ls_string = S[:ls]
        seen = {ls_string}
        for element in range(ls, len(S)):
            ls_string = ls_string[1:] + S[element]
            if ls_string in seen:
                return ls
            seen.add(ls_string)
    return 0

print(longestRepeatingSubstring("abbaba"))
print(longestRepeatingSubstring("bbwfowdeauwderbddpwzrfowybhpvfoyvfdrsgjiytfxxawkctyfvrywxqwwoculuoiqzmsbaonhtswpmachjaademrwznqbkrravioseyibmqeuuayrnxzyptpuwlblkpvhgkufnjhprgsecqzpgfdjdgagjgiifjiftyiimgegotdylcxhdakzwgicnbzefvmdbhbbgbvxbdueewyzrpvxfcbigaprdudvbxreavzgwpcxldwcfnqrbbfvcmeiyafbhtixegibfnugfytiqczwqclfsksameergvxljtxeranlnozzhpdexkfwysuzeavvzqoxogxsixiczwrwrefqnefkumlzdzknqwizvqzyginiakjxllvpttdrhorinzhkxirfkryymvqezvdifjbndxdlflzsbigypltvuyocbudqidyxfknoslylcwwvidlrfjntfkgmzpvkkzscspslrnypbgziknzawqpfvmarzjwdwbezcudhmedfcmdwutehzeayufgmkbnuxaozypkakonotapbzeambrileusrfzhijejuggvtakwsnxuzubdojfgkzwrvsetjvmwqobtagebxgicsgrtgzmrzjnzitxknocptmayabfwrupscpwmclknwqlhkyejhyfxuiunasfbiuttrfotckztxozawqgqwswvwfdnozbmocmdmlyupaoayxnzwrvapputncymzpefiozqimezggqvwlhtpdaseputojdrjxfueemvzdjhhwhfvsauvhpkhldwvwuvonpginysnltfgqawamilcpxdreyjwnmlxcbdurpeasxnabftirkappyrbwsuccrkrzsvlwrwyivctvdmrmdrrxipbqusmicdbqasklcadkianuctcxkewctdrdllodyrpskipsybwrldbsvpjuxmgdbxwhuweizihgiulzrsjsdesdodhmqzwtayfpdtbhnjyjvsilfspghnwytnhoqpcaaawsvxvuotfjkqismsjvevloccfzyubzbucdorgasyhnmemaetpgjruhrbvzdqdjycgybrfxlviqjosqamighivronqyguaunuoxyxnlvysuitxeibyhndoarjbcxxvovleuygweqbsmqtsgvvnwcyooikmeqjjeypfcomywiuyxuwcvlpnypqmaqeuckjgkmhofvbjqubrybeovxtyvgxoodyfjkiicqxfrwhqhnrgfuxtcxyswwluiwpmfdoqsuijjauophmzyyydleuaipsnfpswjfgmaqdigiuzyxtbsgxabbrxlcprzamzwzljbyqnnfhfitnmmruidqcuudwtqstloatznninzmezliprpkzxgoahevghjpwbodqmgcywwanykmijimsdbohmhrgxvkuevuqrlxhgzasmcycwzijwxklmiyfcvyycmfrilqowhsqpqcyexjuhpmcveyipnljcbroiuzizwdclcsbqxzeg"))