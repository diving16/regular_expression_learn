import re

text = 'I am sooooooo happy right now,yeah~~~~~~'

# =============================================================================
# #找多个的方法
# #加号是一到多
# Happy_guy_Regex=re.compile(r'yeah(~)+') 
# Happy_guy_Regex=re.compile(r'yeah(~)*') 
# 
# mo=Happy_guy_Regex.search(text)
# 
# print(mo.group())
# =============================================================================

#指定重复次数
Happy_guy_Regex=re.compile(r'yeah(~){3}') 

mo=Happy_guy_Regex.search(text)

print(mo.group())

