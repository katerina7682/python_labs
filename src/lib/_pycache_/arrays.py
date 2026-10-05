def min_max(nums: list[float|int]):
    ''' Вычисляет максимум и минимум в списке

    Args: 
        nums: Список чисел (целых и вещественных)

    Returns:
        Кортеж (минимум, максимум)

    Raises:
        ValueError: Если список пустой
    '''
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
     
    '''Возвращает отсортированный список уникальных значений

    Args:
        nums: Список чисел (целых и вещественных)

    Returns:
        Отсортированный список
    '''
    nums=set(nums)
    nums=list(nums)
    return nums

def flatten(mat: list[list|tuple]):
    '''Переводит матрицу в вектор

    Args:
        mat: Список, в котором содержатся списки и кортежи
    
    Returns:
        array: Список
    
    Raises:
        TypeError: Если передана не матрица
    '''
    array=[]
    for i in mat:
        if type(i)==list or type(i)==tuple:
            for j in i:
                array.append(j)
        else:
            return 'TypeError'
    return array