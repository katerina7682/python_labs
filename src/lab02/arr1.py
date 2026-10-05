def min_max(nums: list[float|int]):
    if not nums:
        return 'ValueError'
    mx=nums[0]
    mn=nums[0]
    for i in nums:
        if i>mx:
            mx=i
        elif i<mn:
            mn=i
    return ((mn,mx))

def unique_sorted(nums: list[float|int]):
    nums=set(nums)
    nums=list(nums)
    return nums

def flatten(mat: list[list|tuple]):
    array=[]
    for i in mat:
        if type(i)==list or type(i)==tuple:
            for j in i:
                array.append(j)
        else:
            return 'TypeError'
    return array