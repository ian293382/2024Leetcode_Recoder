def is_self_dividing(n):
    str_n = str(n)
    for i in str_n:
        if i == '0'or n % int(i) !=0:
            return False
        return True
    
def max_self_diving_difference(a, b):
    diving_list = []
    for i in range(a, b+1):
        if is_self_dividing(i):
            diving_list.append(i)
    if not diving_list or len(diving_list) < 2:
        return None
    
    max_diff = 0 
    max_diff_pair = None

    for i in range(len[len(diving_list])