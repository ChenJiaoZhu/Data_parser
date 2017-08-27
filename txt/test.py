# coding: utf8
import os
file_name = os.listdir(r'C:\Users\Administrator\Desktop\data')[0]
cs = os.listdir(r'C:\Users\Administrator\Desktop\data\%s' % file_name)

new_cs = []
li = ['20', '50', '100', '200', '500', '1k', '2k', '5k', '10k', '20k', '50k', '100k']
for l in li:
    for x,c in enumerate(cs):
        if l == c[2:-4]:
            new_cs.append(cs[x])

print cs
print new_cs

# cs_ = open(r'C:\Users\Administrator\Desktop\csv.csv')
# lines_ = cs_.readlines()
# no_space_ = []
# for i in lines_:
#     no_space_.append(i[:-1])
#  
# print no_space_

