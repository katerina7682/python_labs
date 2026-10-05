def transpose(mat: list[list[float|int]]):
    '''Меняет строки и столбцы местами

    Args:
        mat: Матрица

    Returns:
        mat2: Транспонированная матрица

    Raises:
        ValueError: Строки разной длины
    '''
    if mat==[]:
        return []
    m=max(list(map(len,mat)))
    mat2=[[[] for i in range(len(mat))] for j in range(m)]
    for i in range(len(mat)):
        
        if len(mat[i])<m:  return 'ValueError'
        for j in range(len(mat[i])):
            mat2[j][i]=mat[i][j]
    return mat2
def row_sums(mat:list[list[float|int]]):
    '''Сумма по каждой строке

    Args: 
        mat: Матрица чисел

    Returns:
        mat2: Список сумм по строке

    Raises:
        ValueError: Строки разной длины
    '''
    mat2=[]
    m=list(map(len,mat))
    m=set(m)
    if len(m)>1: return 'ValueError'
    for i in mat:
        mat2.append(sum(i))
    return mat2
def col_sums(mat:list[list[float|int]]):
    '''Сумма по каждому столбцу

    Args:
        mat: Матрица чисел

    Returns:
        m2: Список сумм по столбцам

    Raises:
        ValueError: Строки разной длины
    '''
    m=list(map(len,mat))
    if len(set(m))>1: return 'ValueError'
    m2=[0]*m[0]
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            m2[j]+=mat[i][j]
    return m2