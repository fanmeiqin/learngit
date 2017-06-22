#-*- encoding:utf-8 -*-
import math
import os
import sys
import re

def parse_data(file_path):
    f = open(file_path)
    tmp = map(lambda x : x.strip(), f.readlines())
    #format_print(tmp)
    f.close()
    str_x = []
    for i in range(0,len(tmp)):
        str_x.append(tmp[i].split(","))
    n = len(tmp)
    m = len(tmp[0].split(","))
    #format_print(str_x)
    x = []
    for i in str_x:
        x.append(map(float, map(lambda x : x.strip(), i)))
        #pass
    return n,m,x

def data_standard1(n,m,x):
    arv_xj = []
    s_sqrt = []
    xij_p = []
    for j in range(0,m):
        tmp_list_avr = []
        tmp_list_s = []
        for i in range(0,n):
            tmp_list_avr.append(x[i][j])
        s = reduce(lambda x,y : x + y, tmp_list_avr)
        arv_xj.append(s/n)

        for i in range(0,n):
            tmp_list_s.append(pow((x[i][j] - arv_xj[j]), 2))
        s1 = reduce(lambda x,y : x + y, tmp_list_s)
        s_sqrt.append(math.sqrt(s1/n))
        xij_p.append(float((x[i][j] - arv_xj[j]) / s_sqrt[j]))
    #print("arv_xj: ", arv_xj)
    #print("sj: ", s_sqrt)
    return xij_p

def data_standard2(n,m,x):
    x_ij_p = []
    for i in range(0,n):
        x_ij_p_tmp = []
        for j in range(0,m):
            x_ij_p_tmp.append((x[i][j] - min(x[i])) / (max(x[i]) - min(x[i])))
        x_ij_p.append(x_ij_p_tmp)
    return x_ij_p

def set_relation(n,m,x,C):
    r_ij = []
    for i in range(0,n):
        r_ij_tmp = []
        for j in range(0,m):
            if(i == j):
               r_ij_tmp.append(1)
            else:
               s_tmp = 0            
               for k in range(0,m):
                   s_tmp = abs(x[i][k] - x[j][k]) + s_tmp
               r_ij_tmp.append(1 - C * s_tmp)
        r_ij.append(r_ij_tmp)
    return r_ij

def format_print(list):
    length = []
    for i in list:
        for j in i:
            length.append(len(str(j)))
    max_length = max(length)
    
    for i in list:
        print(map(lambda x : x.ljust(max_length), map(str, i)))

def arg_check(args):
    if(len(args) >= 3):
       return
    else:
       print("\033[1;32;40m")
       print("USAGE:")
       print("python test.py {command}  输入矩阵文件 [-C]")
       print("eg:python test.py -Sdevication  /home/data.log")
       print("eg:python test.py -devication  /home/data.log")
       print("eg:python test.py -Fmatrix  /home/data.log")
       print("\033[0m")
       sys.exit(1)

arg_check(sys.argv)
command = sys.argv[1]
file_path = sys.argv[2]
n,m,x = parse_data(file_path)
if(command == "-Sdeviation"):
   result1 = data_standard1(n,m,x)
   print("Sdeviation:")
   print(result1)

if(command == "-devication"):
   result2 = data_standard2(n,m,x)
   print("data_standard2:")
   format_print(result2)

if(command == "-Fmatrix"):
   c = re.sub("-C", "", sys.argv[3])
   sqrt_data = set_relation(n,m,x,float(c))
   print("Fmatrix:")
   format_print(sqrt_data)
