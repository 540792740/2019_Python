## I. Collections
[link](http://www.google.com)

<br>List * number： [2] * 2 =  [2,2]<br> 

#### 1. Function `'enumerate'`
seq = ['one', 'two', 'three']
for i , element in enumerate(seq):<br>
    print i,element

#### 2. list[::] Control
nums = [1,2,3,4,5,6,7]<br>
`nums[:] = nums[::-1]`    Reverse List    <br>
nums = [7,6,5,4,3,2,1]<br><br>
`nums[:k] = nums[:k][::-1]` [nums[0], nums[1], .... nums[k]] = [nums[k], nums[k-1]...nums[1]]<br>
[5,6,7,4,3,2,1]<br>
nums[:k][::-1] : [nums[k], nums[k-1], ... nums[1]]<br><br>
`nums[k:] = nums[k:][::-1] `<br>
[5,6,7,1,2,3,4]
<br>
digit = '123'   <br>
digit[1:] = '23'    <br>

#### 3. Set
`set(nums)`: Set List into set, which will auto delete duplicate element.<br>
set：{1，2，3}<br>
`s.add(4)`: add '4' into set 's'<br>
`s.remove(3)` : remove 'e' from set 's'<br>
`s.clear()` : clear all element in set 's'

#### 4. Reverse in Loop：
for c in reversed(s):   <br>
    print(c)

#### 5. Dic：
parmap = {')':'(', '}':'{',']':"["} <br>
')' in parmap ----> true    <br>
'(' in parmap ----> False   ]<br>

#### 6. ASCII
`ord('c')` --> ASCII Number<br>
Select 0-9 from string<br>
if a > ord('0') and a < ord('9')<br>

#### 7. ListNode
`head.next` The way to move<br>
while l1 and l2: ---when l1 and l2 exist both <br>
cur.next = l1 or l2 --- when l1 exist or l2 exist, cur.next will be that head<br>

#### 8. //
Integer Division<br>
`4 / 2 = 2.0`<br>
`4 // 2 = 2`<br>

#### 9. >> <<
2 << 2 --> Binary[2] == 01,   left shift 2 bit,  100 --> 4 <br>
10 >>1 --> Binary[10] ==1010, right shift 1 bit, 101 --> 5 <br>

#### 10. lambda
f = lambda x, y, z : x + y + z + 1<br>
f(1,2,3) = 1 + 2 + 3 + 1 = 7<br>

#### 11. map
map(function, iterable)<br>
`iterable`: list is iterable !!<br>
However, in python3, function map generate iterator, if we want to get value, we need to add `list(map())`<br>
`map(lambda x: x + 1, [1])` will print <map object at 0x000001D8816D3DD8> <br>
`list(map(lambda x: x + 1, [1]))` will print [2]

#### 12. extend
dp = [1, 2] <br>
dp.extend(list(map(lambda x: x + 1, dp)))

#### 13. 2 D Array
dp = [[1] * m for i in range(n)]

#### 14. isalpha() isdigit()
if `c.isalpha()`: c is alpha, return true <br>
if `c.isdigit()`: c is digit, return true

#### 15. pop()
a = [[1,2], [2,3], [3,4]]   <br>
a.`pop(1)`--->[2,3] will pop out, leave [[1,2],[3,,4]]    <br>
a.`pop()` --->[3,4] will pop out, leave [[1,2],[2,3]]     <br>

#### 16. set()
_set = set()  
_set.add() use this function replace list, can improve efficient

#### 17 .find()
a = "abcabcbb"  <br>
a.find(c)   <br>
---> 2

#### 18. divmod
carry, rem = `divmod`(curval + carry, 2)    <br>
equal:      carry = curval + carry `\\` 2     <br>
            rem =   curval + carry `%` 2
               
#### 19. dictionary
w = 'eat'
key = tuple(sorted(w)) --> ('a','e','t')    <br>
d = {}      <br>
d[key] = d.get(key,[]) + [w]    <br>
