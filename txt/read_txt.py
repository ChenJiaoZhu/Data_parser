# coding: utf8
# import os
# print os.path.abspath(".")
import csv
import os
file_name = os.listdir(r'C:\Users\Administrator\Desktop\data')[0]
cs = os.listdir(r'C:\Users\Administrator\Desktop\data\%s' % file_name)


num = 1500
cs_ = open(r'C:\Users\Administrator\Desktop\csv.csv','wb+')
for x,n_ in enumerate(cs[:1]):
    write = csv.writer(cs_)
    f = open(r'C:\Users\Administrator\Desktop\data\%s\%s' % (file_name,n_))
    lines = f.readlines()
    no_space = []
    for i in lines:
        no_space.append(i[:-1])
    
    for n,line in enumerate(lines):
        if line[:5] == 'Point' and line[:6] != 'Points':
            first_index = n
        if line[:6] == 'Center':
            end_index = n-1
    
    title = no_space[first_index][16:].split()
    first = title[0]+' '+  title[1]
    second = title[2]+' '+  title[3]
    title_ = [first,second]
    na = n_.split('-')
    na[1] = na[1][:-4]
    if x == 0:
        write.writerow(title_)
        write.writerow(['',''])
        write.writerow(na)
    
        for i in no_space[first_index+1 : end_index]:
            data = i[17:].split()
            write.writerow(data)
        control = num - len(no_space[first_index+1 : end_index]) - 3
        for i in range(control):
            write.writerow(['',''])
    else:

        cs_.close()
        cs_ = open(r'C:\Users\Administrator\Desktop\csv.csv')
        lines_ = cs_.readlines()
        no_space_ = []
        for i in lines_:
            no_space_.append(i[:-1])
        cs_.close()
        
        for index,y in enumerate(no_space_):
            if len(y.split(',')) != x*2:
                ind = index
                break
            else:
                ind = index+1
        
        new_data = []
        if (len(no_space[first_index+1:end_index])+3) <= ind:
            for n,i in enumerate(no_space_):
                if n==0:
                    r1 = i.split(',')
                    r1.append(first)
                    r1.append(second)
                    new_data.append(r1)
                else:
                    if n==1:
                        r2 = i.split(',')
                        r2.append('')
                        r2.append('')
                        new_data.append(r2)
                    else:
                        if n==2:
                            r3 = i.split(',')
                            r3.append(na[0])
                            r3.append(na[1])
                            new_data.append(r3)
                        else:
                            if (n-3) <= (len(no_space[first_index+1:end_index])-1):
                                k = no_space[first_index+1:end_index][n-3]
                                data = k[17:].split()
                                r4 = i.split(',')
                                r4.append(data[0])
                                r4.append(data[1])
                                new_data.append(r4)
                            else:
                                r4 = i.split(',')
                                new_data.append(r4)
        else:
            r1 = no_space_[0].split(',')
            r1.append(first)
            r1.append(second)
            new_data.append(r1)
            r2 = no_space_[1].split(',')
            r2.append('')
            r2.append('')
            new_data.append(r2)
            r3 = no_space_[2].split(',')
            r3.append(na[0])
            r3.append(na[1])
            new_data.append(r3)
            for n,i in enumerate(no_space[first_index+1:end_index]):
                if n <= (len(no_space[first_index+1:end_index])-4):
                    data = i[17:].split()
                    r4 = no_space_[n+3].split(',')
                    r4.append(data[0])
                    r4.append(data[1])
                    new_data.append(r4)
                else:
                    data = i[17:].split()
                    r4 = ['', ''] * x
                    r4.append(data[0])
                    r4.append(data[1])
                    new_data.append(r4)
                
        cs__ = open(r'C:\Users\Administrator\Desktop\csv.csv','wb+')
        write = csv.writer(cs__)
        for d in new_data:
            write.writerow(d)
        cs__.close()
    f.close()
    print 'Seccessfully copy %s into the csv.' % n_
    
    
    