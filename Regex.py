import re

message='I am Monkey Lufy. I am the king of the sea.'

#把空格加在可选项里面，不然万一message中没有D，Regex中会出现两个空格
Lufy_Regex=re.compile(r'Monkey (D )?Lufy')

mo=Lufy_Regex.search(message)

print(mo.group())
