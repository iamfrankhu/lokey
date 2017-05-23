#!/usr/bin/env python
#coding:utf-8
import string
def processFile(inputFile, outputFile,sqlname):                         #定义一个函数  
    fin = open(inputFile, 'r')                                  #以读的方式打开文件  
    fout = open(outputFile, 'w')                                #以写得方式打开
    sql = open(sqlname,'w')	
    sql.write('select ')
    eachLine=fin.readline()
    while eachLine:                                        #读取文件的每一行  
        line = eachLine.strip().replace(',',' ').decode('utf-8', 'ignore')  
        str_split = line.split(' ')
        sql.write(str_split[0]+ ',\n')
        if str_split[1]=='character':
            sqlline=line.split(' ',1)
            fout.write(sqlline[0]+':'+sqlline[1]+ ',')
        elif str_split[1]=='double':
            sqlline=line.split(' ',1)
            fout.write(sqlline[0]+':'+sqlline[1]+ ',')
        elif str_split[1]=='timestamp':
            sqlline=line.split(' ')
            fout.write(sqlline[0]+':'+sqlline[1]+ ',')
        else:
            sqlline=line.split(' ')
            if 'numeric' in sqlline[1]:
                fout.write(sqlline[0]+':'+'numeric,')
            else:
                fout.write(sqlline[0]+':'+sqlline[1]+ ',')
        eachLine=fin.readline()
    sql.write('from ')
    fin.close()                                                 #关闭文件  
    fout.close()  
    sql.close()
  
processFile('sqlstring.txt', 'sqlstr.txt','sqlname.txt')              #调用该函数对文件进行处理  
