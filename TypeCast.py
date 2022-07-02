from ctypes import sizeof
from itertools import chain, count
import re,os,time,re,sys
from termcolor import colored,cprint
from prettytable.colortable import ColorTable, Themes
f_data=[[]]
table1 = ColorTable(['Datatype','Var Name','Line'],theme=Themes.OCEAN)
table1.align["Line"] = "l"
list_of_datatype=['address','int','str','uint','uint8','uint256','int8','int256','byte','float']



print("\n\t███████╗ ██████╗ ██╗        ",colored("           ████████╗██╗   ██╗██████╗  ██████╗  ","blue"))
print("\t██╔════╝██╔═══██╗██║        ",colored("           ╚══██╔══╝╚██╗ ██╔╝██╔══██╗██╔═══██╗ ","blue"))
print("\t███████╗██║   ██║██║        ",colored(" █████╗       ██║    ╚████╔╝ ██████╔╝██║   ██║ ","blue"))
print("\t╚════██║██║   ██║██║        ",colored(" ╚════╝       ██║     ╚██╔╝  ██╔═══╝ ██║   ██║ ","blue"))
print("\t███████║╚██████╔╝███████╗   ",colored("              ██║      ██║   ██║     ╚██████╔╝ ","blue"))
print("\t╚══════╝ ╚═════╝ ╚══════╝   ",colored("              ╚═╝      ╚═╝   ╚═╝      ╚═════╝  ","blue"))
print("\n\t\t\t\t\t    -  Developer : keyurtalati00@gmail.com")
print("\t\t\t\t\t               -  Veriosn 1.3  20-06-2022")
                                                                          



if (int(len(sys.argv)) < 2):
    print("Invalid Arguments")
    print("\tTry with : TypeCast.py <Smart Contract File Path>")
    sys.exit()
    
f1=open(str(sys.argv[1]),'r')
l=f1.readlines()
found_var=[]
table_size=0
l1=0
for line in l:
    l1+=1
    data=line.split()
    for d in data:
        for datatype in list_of_datatype:
            if datatype == d :
                full_var_name=data[data.index(d)+1]
                if ('=' in full_var_name):
                    x=full_var_name.split("=")
                    if(')' in str(x[0])):
                        found_var.append(x[0].split(')',1)[0])
                        #print("1",x[0].split(')',1)[0])
                        table1.add_row([str(datatype),x[0].split(')',1)[0],"Line:"+str(l1)+" "+line])
                        f_data.append([str(datatype),x[0].split(')',1)[0],"Line:"+str(l1)+" "+line])
                        table_size+=1
                    if(';' in str(x[0])):
                        #print("2",print(x[0].split(';',1)[0]))
                        found_var.append(x[0].split(';',1)[0])
                        table1.add_row([str(datatype),x[0].split(';',1)[0],"Line:"+str(l1)+" "+line])
                        f_data.append([str(datatype),x[0].split(';',1)[0],"Line:"+str(l1)+" "+line])
                        table_size+=1
                    if(',' in str(x[0])):
                        #print("3",print(x[0].split(',',1)[0]))
                        found_var.append(x[0].split(',',1)[0])
                        table1.add_row([str(datatype),x[0].split(',',1)[0],"Line:"+str(l1)+" "+line])
                        f_data.append([str(datatype),x[0].split(',',1)[0],"Line:"+str(l1)+" "+line])
                        table_size+=1
                    else:
                        found_var.append(str(x[0]))
                        #print("4",str(x[0]))
                        table1.add_row([str(datatype),str(x[0]),"Line:"+str(l1)+" "+line])
                        f_data.append([str(datatype),str(x[0]),"Line:"+str(l1)+" "+line])
                        table_size+=1
                    #dataset[table_size][0]=str(datatype)
                    #dataset[table_size][1]=str(x[0])
                    #dataset[table_size][2]=line
                    #table_size+=1
                elif(str(data[data.index(d)+1]) == "public" or str(data[data.index(d)+1]) == "private"):
                        x=str(data[data.index(d)+2]).split("=")
                        if(')' in str(x[0])):
                            #print("5",x[0].split(')',1)[0])
                            found_var.append(x[0].split(')',1)[0])
                            table1.add_row([str(datatype),x[0].split(')',1)[0],"Line:"+str(l1)+" "+line   ])
                            f_data.append([str(datatype),x[0].split(')',1)[0],"Line:"+str(l1)+" "+line   ])
                            table_size+=1
                        if(',' in str(x[0])):
                            #print("6",x[0].split(',',1)[0])
                            found_var.append(x[0].split(',',1)[0]) 
                            table1.add_row([str(datatype),x[0].split(',',1)[0],"Line:"+str(l1)+" "+line   ])
                            f_data.append([str(datatype),x[0].split(',',1)[0],"Line:"+str(l1)+" "+line   ])   
                            table_size+=1
                        if(';' in str(x[0])):
                            #print("7",x[0].split(';',1)[0])
                            found_var.append(x[0].split(';',1)[0])
                            table1.add_row([str(datatype),x[0].split(';',1)[0],"Line:"+str(l1)+" "+line   ])
                            f_data.append([str(datatype),x[0].split(';',1)[0],"Line:"+str(l1)+" "+line   ])
                            table_size+=1
                        else:
                            found_var.append(str(x[0]))
                           # print("8",str(x[0]))
                            table1.add_row([str(datatype),x[0],"Line:"+str(l1)+" "+line   ])
                            f_data.append([str(datatype),x[0],"Line:"+str(l1)+" "+line   ])
                            table_size+=1
                        #dataset[table_size][0]=str(datatype)
                        #dataset[table_size][1]=str(x[0])
                        #dataset[table_size][2]=line
                        #table_size+=1
                else:
                    if(')' in str(data[data.index(d)+1])):
                        #print("9",str(data[data.index(d)+1]).split(')',1)[0])
                        #print(str(data[data.index(d)+1]).split(')',1)[0])
                        found_var.append(str(data[data.index(d)+1]).split(')',1)[0])
                        table1.add_row([str(datatype),str(data[data.index(d)+1].split(')',1)[0]),"Line:"+str(l1)+" "+line   ])
                        f_data.append(([str(datatype),str(data[data.index(d)+1].split(')',1)[0]),"Line:"+str(l1)+" "+line   ]))
                        table_size+=1
                    if(';' in str(data[data.index(d)+1])):
                        #print("10",str(data[data.index(d)+1]).split(';',1)[0])
                        found_var.append(str(data[data.index(d)+1]).split(';',1)[0])
                        table1.add_row([str(datatype),str(data[data.index(d)+1].split(';',1)[0]),"Line:"+str(l1)+" "+line   ])
                        f_data.append(([str(datatype),str(data[data.index(d)+1].split(';',1)[0]),"Line:"+str(l1)+" "+line   ]))
                        table_size+=1
                    if(',' in str(data[data.index(d)+1])):
                        #print("11",str(data[data.index(d)+1]).split(',',1)[0])
                        found_var.append(str(data[data.index(d)+1]).split(',',1)[0])
                        table1.add_row([str(datatype),str(data[data.index(d)+1].split(',',1)[0]),"Line:"+str(l1)+" "+line   ])
                        f_data.append(([str(datatype),str(data[data.index(d)+1].split(',',1)[0]),"Line:"+str(l1)+" "+line   ]))
                        table_size+=1
                    '''else:
                        print("12",str(data[data.index(d)+1]))
                        found_var.append(str(data[data.index(d)+1]))
                        table1.add_row([str(datatype),str(data[data.index(d)+1]),"Line:"+str(l1)+" "+line   ])
                        f_data.append(([str(datatype),str(data[data.index(d)+1]),"Line:"+str(l1)+" "+line   ]))'''
                    
                    #dataset[table_size][0]=str(datatype)
                    #dataset[table_size][1]=str(data[data.index(d)+1])
                    #dataset[table_size][2]=line
                    #table_size+=1
print("\n\n",colored("[+] 1/4 : \tDetecting DataTypes for the Variables ...","yellow"))   
time.sleep(1)     
print("\n",colored("[+] 2/4 : \tTotal No of Variables ...","yellow"),table_size)   
time.sleep(1)                
print("\n\n",colored("\t   TOTAL VARIABLES FOUND WITH DATATYPES","blue"))
time.sleep(1)
table1.sortby="Var Name"
print(table1)
time.sleep(1)
print("\n\n",colored("[+] 3/4 : \tDetecting Variables With Different DataTypes ...\n","yellow"))   
time.sleep(1)
count=[]
tmp=[]
no_of_issue=0
found_var1 = list(dict.fromkeys(found_var))
for var in found_var1:
    #print(var)
    for i in range(0,table_size):
        if table1.rows[i][1] == var:
            tmp.append(table1.rows[i][0])
        #print(tmp)
    tmp = list(dict.fromkeys(tmp))
    #print(tmp)
    if(len(tmp)>1):
        no_of_issue+=1
        print(colored("\n\t ["+str(no_of_issue)+"] : WARNING /!\ Same Var With Multiple DataTyepes","red"))
        print("\t\t\tVariable Name        : ",colored(var,"red"))
        print("\t\t\tDetected Datatypes   : ",colored(tmp,"red"))
        print("\t\t\tVulnerable Code Line : ",colored(table1.rows[i][2],"red"))
        print("-----------------------------------------------------------------------")
    tmp.clear()
time.sleep(1)



#list_of_datatype=['address','int','str','uint','uint8','uint256','int8','int256','byte']
#found_v=['a','b)']
#print(found_var1)
print("\n\n",colored("[+] 4/4 : \tDetecting External TypeCasting ...","yellow"))
l1=0
c=0
for line in l:
    l1+=1
    for j in range (0,len(list_of_datatype)):
        for k in range(0,len(found_var1)):
            regex1=" "+list_of_datatype[j]+"\("+str(found_var1[k])+"\)"
            out=re.compile(regex1)
            if(out.findall(line)!=[]):
                c+=1
                print(colored("\n\t ["+str(c)+"] : ALERT /!\ External TypeCast Found","red"))
                print("\t\t\tVariable Name        : ",colored(found_var1[k],"red"))
                print("\t\t\tExternal TypeCasting : ",colored(out.findall(line),"red"))
                print("\t\t\tVulnerable Code Line : ",colored(line,"red"))
                print("-----------------------------------------------------------------------")

time.sleep(1)
print(colored("\n\tSCANNING COMPLETED\n","green")) 
print("\n",colored("[+]\tTotal Number Of Warnings : ","yellow"),no_of_issue)
print("",colored("[+]\tTotal Number Of Alert    : ","red"),c)


    #print(typecast)