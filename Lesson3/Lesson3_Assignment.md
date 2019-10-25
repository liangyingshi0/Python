
## 1. 实现`print`函数
定义一个函数`print_string`，返回一个字符串。  
`print_string`函数支持输入多个参数，每个参数间使用参数`sep`(默认一个空格)的字符进行连接，并且最后还要添加一个`end`(默认一个换行)参数的字符。  
比如
- `print_string('This is a test')` 返回`This is a test\n`  
- `print_string('This', 'is', 'a', 'test')` 返回`This is a test\n`
- `print_string('This', 'is', 'a', 'test', sep = '-')` 返回`This-is-a-test\n`
- `print_string('This', 'is', 'a', 'test', ',', 'Yes', sep = '_', end = '.')` 返回`This_is_a_test_,_Yes.`


```python
def print_string(*strs, sep=' ', end='\n'):
    for index,s in enumerate(strs):
        if index+1 == len(strs):
            print(s, end)
        else:
            print(s, end=sep)

print_string('This is a test')
print_string('This', 'is', 'a', 'test')
print_string('This', 'is', 'a', 'test', sep = '-')
print_string('This', 'is', 'a', 'test', ',', 'Yes', sep = '_', end = '.')
```

    This is a test 
    
    This is a test 
    
    This-is-a-test 
    
    This_is_a_test_,_Yes .
    

## 2. 打印斐波那契数列
以三种方式打印波那契数列    
给定一个数值n，将前n项的波那契数列打印出来


```python
# 第一种：

def Fibnonacci(n):
    nums = list()
    if n<=0:
        print('输入错误。')
    else:
        for i in range(n):
            if i<=1:
                nums.append(1)
            else:
                num = nums[i-1]+nums[i-2]
                nums.append(num)
    print(nums)

n = int(input('请输入n：'))
Fibnonacci(n)
```

    请输入n：4
    [1, 1, 2, 3]
    


```python
# 第二种：

n = int(input('请输入n：'))
nums = []
for i in range(n):
    if i<=1:
        nums.append(1)
    else:
        num = nums[i-1]+nums[i-2]
        nums.append(num)
print(nums)
```

    请输入n：5
    [1, 1, 2, 3, 5]
    


```python
# 第三种：

n = int(input('请输入n：'))
nums = []
i = 0
while i<n:
    if i<=1:
        nums.append(1)
    else:
        num = nums[i-1]+nums[i-2]
        nums.append(num)
    i+=1
print(nums)
```

    请输入n：6
    [1, 1, 2, 3, 5, 8]
    

不会使用notebook，使用作业.PDF文件查看作业，上传.py文件
