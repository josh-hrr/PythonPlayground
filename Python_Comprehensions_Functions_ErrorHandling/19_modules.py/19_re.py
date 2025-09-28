
'''

regular expressions are transversal - meaning: look similar in other programming language


'''

import re

text =  "hello world 123 test 999"
result = re.findall('\d+', text)
print(result)



