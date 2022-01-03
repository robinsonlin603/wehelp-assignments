#函式與流程控制
def calculate(min,max):
    sum=0
    for n in range(min,max+1):
        sum=sum+n
    print(sum)
calculate(1,3)
calculate(4,8)

#字典與列表
def avg(data):
    sum=0
    for workers in data["employees"]:
        salary=int(workers["salary"])
        sum=sum+salary
    print(sum/data["count"])
avg({
    "count":3,
    "employees":[
        {
            "name":"Jhon",
            "salary":"30000"
        },
        {
            "name":"Bob",
            "salary":"60000"
        },
        {
            "name":"Jenny",
            "salary":"50000"            
        }
    ]
})

#演算法
def maxProduct(nums):
    length=len(nums)
    a=0
    max=nums[0]*nums[1]
    while a<length:
        for n in range(1,length):
            if nums[a]*nums[n]>max and a!=n:
                max=nums[a]*nums[n]
        a+=1
    print(max)
maxProduct([5,20,2,6])
maxProduct([10,-20,0,3])
maxProduct([-1,2])
maxProduct([-1,0,2])

#演算法
def twoSum(nums,target):
    length=len(nums)
    a=0
    while a<length:
        for n in range(1,length):
            if nums[a]+nums[n]==target:
                return (a,n)
        a+=1
result=twoSum([2,11,7,15],9)
print(result)

#演算法
def maxZeros(nums):
    temp_max=0
    max=0
    for n in nums:
        if n==1:
            temp_max=0
            continue
        temp_max+=1
        if temp_max>max:
            max=temp_max
    print(max)
maxZeros([0,1,0,0])
maxZeros([1,0,0,0,0,1,0,1,0,0])
maxZeros([1,1,1,1,1])
maxZeros([0,0,0,1,1])
