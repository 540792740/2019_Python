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
