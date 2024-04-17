import sys
# 要從Cpython 去找答案

# sys.getsizeof([0]* 3)

# sys.getsizeof([0, 0, 0])

# sys.getsizeof([0 for _ in range(3)])

import dis

dis.dis('[0]  * 3')
# 0           0 RESUME                   0

#   1           2 LOAD_CONST               0 (0)
#               4 BUILD_LIST               1
#               6 LOAD_CONST               1 (3) => 這一行3個load
#               8 BINARY_OP                5 (*)
#              12 RETURN_VALUE
#   0           0 RESUME                   0

#   1           2 BUILD_LIST               0
#               4 LOAD_CONST               0 ((0, 0, 0))
#               6 LIST_EXTEND              1
#               8 RETURN_VALUE

# 一個tuple 為list
# 指針 64作業系統 8 type 
# 一個空指針 56 byte
# 3個指針 一個空的List = 80 byte

dis.dis('[0, 0, 0]')
# 0           0 RESUME                   0

#   1           2 LOAD_CONST               0 (<code object <listcomp> at 0x10048c030, file "<dis>", line 1>)
#               4 MAKE_FUNCTION            0
#               6 PUSH_NULL
#               8 LOAD_NAME                0 (range)
#              10 LOAD_CONST               1 (3)
#              12 PRECALL                  1
#              16 CALL                     1
#              26 GET_ITER
#              28 PRECALL                  0
#              32 CALL                     0
#              42 RETURN_VALUE

# list_resize(3)
# List append => 又是 list_resize 觸發四次 他會給操過一點內存空間 
# new_alllcoated = ((size_t)newsize + (newsize >> 3 ) + 6) & (size_t)3); 
#  new_size 帶入 二進位 去弔末兩碼 1000 = 八個內存 = 8 * 8 +56 = 120 

dis.dis('[0 for _ in range(3)]')



# Disassembly of <code object <listcomp> at 0x106cf0030, file "<dis>", line 1>:
#   1           0 RESUME                   0
#               2 BUILD_LIST               0
#               4 LOAD_FAST                0 (.0)
#         >>    6 FOR_ITER                 4 (to 16)
#               8 STORE_FAST               1 (_)
#              10 LOAD_CONST               0 (0)
#              12 LIST_APPEND              2
#              14 JUMP_BACKWARD            5 (to 6)
#         >>   16 RETURN_VALUE

# LIST_APPEND  => resize(1)  resize(2) resize(3)
# 4* 8 + 56 = 88 byte 
# 88 byte