import re

message='Hi,my name is Meiqi Meng and my wechat id is MeiqiMeng,\
you can call me at (86)-18888888888,if it doesn\'t work, you can \
call Meiqi77 by 86-16666666666'

#find_phone_number=re.compile(r'\d\d-\d\d\d\d\d\d\d\d\d\d\d')

#Tips:分成前后两块
find_phone_number=re.compile(r'\((\d{2})\)-(\d{11})')

#找到第一个符合条件的
match_object=find_phone_number.search(message)

# =============================================================================
# #找到所有符合的元素，放在一个列表里
# match_object=find_phone_number.findall(message)
# 
# =============================================================================
print(match_object)

#在search时使用
print(match_object.group())


# =============================================================================
# #找人
# Meiqi_Regex=re.compile(r'Meiqi(Meng|77)')
# match_object=Meiqi_Regex.search(message)
# 
# 
# print(match_object.group())
# =============================================================================
