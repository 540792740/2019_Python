## I. Collections
[link](http://www.google.com)
<br>List * number： [2] * 2 =  [2,2]<br> 

#### 1. Function `'enumerate'`
seq = ['one', 'two', 'three']
for i , element in enumerate(seq):<br>
    print i,element

#### 2. list[::] Control
nums = [7,6,5,4,3,2,1]<br><br>
`nums[:k] = nums[:k][::-1]` [nums[0], nums[1], .... nums[k]] = [nums[k], nums[k-1]...nums[1]]<br>
[5,6,7,4,3,2,1]<br>

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
`list(map(lambda x: x + 1, [1]))` will print [2]    <br>
`'->'.join(map(str, ['0', '2']))`  : 0->2

#### 12. extend
dp = [1, 2] <br>
dp.extend(list(map(lambda x: x + 1, dp))) --> [1, 2, 2, 3]

#### 13. 2 D Array
dp = [[1] * m for _ in range(n)]

#### 14. isalpha() isdigit()
if `c.isalpha()`: c is alpha, return true <br>
if `c.isdigit()`: c is digit, return true

#### 15. pop()
a = [[1,2], [2,3], [3,4]]   <br>
a.`pop(1)`--->[2,3] will pop out, leave [[1,2],[3,,4]]    <br>
a.`pop()` --->[3,4] will pop out, leave [[1,2],[2,3]]     <br>

#### 17 .find()
a = "abcabcbb"  <br>
a.find(c)   --> 2  <br>
a.find('x') --> return `-1`
a.find('a', 2) --> from index = 2, find 'a'

#### 18. divmod
carry, rem = `divmod`(curval + carry, 2)    <br>
equal:      carry = curval + carry `\\` 2     <br>
            rem =   curval + carry `%` 2
               
#### 19. dictionary
w = 'eat'
key = tuple(sorted(w)) --> ('a','e','t')    <br>
d = {}      <br>
d[key] = d.get(key,[]) + [w]    <br>
dict = {'Name': 'Zara', 'Age': 27}  <br>
dict.get('Sex', "Never") --> Never 

#### 20. format: `f'...'`
one_dict = {"name": "江辰",  "hobby" : ["running", "singing"]}    <br>
print(f"姓名：{one_dict['name']},爱好：{one_dict['hobby']}")      <br>
-->姓名：江辰,爱好：['running', 'singing']

#### 22. Replace
a = '11122234'      <br>
a = a.`replace('2', '', 1)`   <br>
---> Means replace 1 '2' into '', Third value means how many neet to be replace<br

#### 22. Sorted, sort()
interval = [[2,6],[8,10],[1,3],[15,18]]<br>
interval =  sorted(interval, key = lambda x: x[0])  <br>
-->[[1, 3], [2, 6], [8, 10], [15, 18]]  <br>
b_dict={1:'e',3:'m',9:'a',5:'e'} <br>
b_dict.sort() --> `Run error` <br>
sorted(b_dict) --> `{1: 'e', 3: 'm', 5: 'e', 9: 'a'}`


#### 24. Zip
a = [1, 2, 3] <br>
b = [4, 5, 6] <br>
zipped = `zip(a, b)`    --> [(1, 4), (2, 5), (3, 6)]    <br>
zip(*zipped) --> [(1, 2, 3), (4, 5, 6)]<br>
list(zip()) --> in python3

#### 25. Bit operation
1 & 2 --> 0 because: 01 & 10 --> 00 <br>
1 | 2 --> 3 because: 01 | 10 --> 11 <br>
1 ^ 3 --> 2 because: 01 ^ 11 --> 10 <br>
~5 --> -(5 + 1)= -6<br>
~(-5) --> -4    <br>
-3 --> 1011: 1101, navigate and plus 1  <br>
if a^b = c, then a^c = b，且 b^c = a  <br>
a = a ^ b, a = a ^ b, a will not change

#### 27, int()
if s[:i] is None, there is no int(s[:i]), return Error

#### 28. Binary Search Tree BST
1. if root.left, root.val > root.left(all Node left root)   <br>
2. if root.right, root.cal < root.right(all Node right root)<br>
3. root.left and root.right are also BST Node               <br>

#### 29. Binary, Ordinary scale
i = '100'   <br>
ORD = int(i, 2)  no neet to transfer in to int, just transfer string<br>
ORD = int(i, 8) if i is octal number <br>
a = '10'    <br>
print(bin(int(a))) --> 0b1010

#### 30. Traversal :
inorder:    `中`序遍歷    左中右，`中在中`        <br>
preorder:   `先`序遍歷    中左右，`中在先`        <br>
postorder:  `後`序遍歷    左右中，`中在后`        <br>

#### 31. count()
array = 'bcddef'     <br>
array.count('d') --> 2, calculate how many 'd' in array
bin(x ^ y).count('1') --> 1 ^ 3 --> 10, count('1') --> 1

#### 32. dic.values()
dic = {'a' : 1,  'b' : 3}   <br>
dic.values() --> dict_values([3, 3])    <br>
for i in dic.values():  <br>
--> i = 1   i = 3 

#### 33. dic.get()
dict.get(key, default=None) <br>
dict = {'Name': 'Zara', 'Age': 27}  <br>**
dict.get('Age') --> 27  <br>
dict.get('Sex', "Never") -->Never   Cuz Never is return when not found <br>

#### 34. all()
def all(iterable):              <br>
    for element in iterable:    <br>
        if not element:         <br>
            return False        <br>
    return True                 <br>
 this function will return True if there is no 0, None, NUll.
 
#### 35. list delete
a = [1, 2, 3, 4]    <br> 
del a[1] -->  [1,3,4]   <br>
a.remove(1) --> [2,3,4] 

#### 36 generate a random number in list
a = random.choice(list)

#### 37 Bit Operation
if n & 1:  --> only last number is 1, can return true, which means
                only odd number can return.
                
#### 38: while 1
while 1 is almost equal but it is faster than while True    <br>        

#### 39: Copy Deepcopy
Shallow Copy: don't creates a copy of nested object, instead it just copies
the reference of nested objects. <br>
DeepCopy: copies all the nested objects recursively.

#### 41. sort dictionary
my_dic = {‘a’:3 , ‘b’:2 , ‘c’: 1}   <br>
sort by value <br>
sorted(my_dic.items(), key =lambda d:d[1], reverse = False) [(‘c’, 1), (‘b’, 2), (‘a’, 3)]  <br>
sorted(my_dic.items(), key =lambda d:d[1], reverse = True) [(‘a’, 3), (‘b’, 2), (‘c’, 1)]   <br>
<br>sort by key
sorted(my_dic.items(), key =lambda d:d[0], reverse = False) <br>
sorted(my_dic.items(), key =lambda d:d[0], reverse = True)  <br>

heapq module: <br>
heapq.heappop(heap) pop smallest number in heap <br>
heapq.heappushpop(heap, i) repush i and pop smallest number in heap <br> 

#### 42. find max value in dic:
{'a': 1, 'ball': 2, 'far': 1, 'after': 1}   <br>
max(dic, dic.get) --> 'ball'

####43.python2 Divide
float(2) / 3 --> 0.666667

####44. heapq 
nums =                  [2, 3, 5, 1, 54, 23, 132]   <br>
heapq.heapify(nums) ->  [1, 2, 5, 3, 54, 23, 132]   <br>
heapq.pop() -->            [2, 3, 5, 132, 54, 23]   <br>
heapq.pop() -->               [3, 23, 5, 132, 54]   <br>
heapq.pop() -->                  [5, 23, 54, 132]   <br>
heapq.heappush(element) --> push element into heap  <br>
heapq.pop() -> O(1)
heapq.push() -> O(log(n))

####45. bisect.insort(seq, item)
二分插入，保持list升序
Complexity O(log(n)) <br>
A = [1,5,8]     <br>
bisect.insort(A, 4) --> [1,4,5,8]

####46. nonlocal key word
def a():    <br>
----times = 0   <br>
----def b():    <br>
    --------nonlocal times  <br>
    --------times += 1  <br>
----b() <br>
----print(times)    <br>
----return times    <br>
a() <br>

####47. defaultdict 
pre_need = collections.defaultdict(int)
pre_need[1] += 1    -> defaultdict(<class 'int'>, {1: 1, 0: 1})
pre_need[0] == 0    -> False

####48. find max values in dic
return max(dic, key = dic.get)

####49. collections.Orderdict
self.d = collections.OrderedDict()  dic with order  <br>
d = OrderedDict([('a', 1), ('b', 2), ('c', 3)]) <br>
print(d.popitem(last=False))    <br>
OrderedDict([('b', 2), ('c', 3)])

####50. Read English

2 ^ 16: two to the sixteenth power
anagram 变形
