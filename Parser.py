# -*- coding: utf-8 -*-
fileindex=0
print "\t======> Relational Algebra Engine ᑌ ᑎ  ᐅᐊ π σ ρ<======\n"
def displayfile(filename):
    deleteduplicate(filename)
    print "\n\n\t  Relation name : "+filename+"   \n"
    print "==============================================================================================================================\n"
    target = open(filename,"r")
    k = target.readlines()
    target.close()
    j=0
    for nr in range(len(k)) :
        if nr==0 or nr in range(3,len(k)) :
            if nr!=0 :
                j+=1
                print str(j)+"\t"+"  |  "+k[nr].replace("|","  |  ").replace("\n","")+"\t"
                if nr==1:
                    print "\n"
            else :
                print "No."+"\t"+"  |  "+k[nr].replace("|","  |  ")+"\t"
        if nr==2:
            print "===============================================================================================================================\n"
    return
def deleteduplicate(filename) :
    target = open(filename,"r")
    k = target.readlines()
    target.close()
    nvec = [k[0],k[1],k[2]]
    for nr in range(3,len(k)) :
        repeats=0
        for nl in range(3,nr) :
            if k[nl].replace("\n","").replace(" ","")==k[nr].replace("\n","").replace(" ","") :
                repeats=1
                break
        if repeats == 0 :
            nvec.append(k[nr])
    target = open(filename,"w")
    target.writelines(nvec)
    target.close()
    return
def filecreate(outputvector,filename):
    tr = open(filename,"w")
    tr.writelines(outputvector)
    tr.close
    return
def fileappender(outputvector,filename):
    tr = open(filename,"a")
    tr.write("\n")
    tr.writelines(outputvector)
    tr.close
    return
def select(targetfile , condition ):
    global fileindex
    target = open(targetfile , "r" )
    attrib = target.readline()
    attributes = attrib.replace("\n","").split("|")
    domaintype = target.readline()
    dump = target.readline()
    domaintypes = domaintype.replace("\n","").split("|")
    lines = target.readlines()
    target.close()
    op = [attrib,domaintype,"----------------------------------------------------------------\n"]
    linenumber = 0
    while linenumber < len(lines):
        x = condition
        fieldinline = lines[linenumber].replace("\n","").split("|")
        #print linenumber,fieldinline,"for testing"
        for j in range(len(domaintypes)):
            if domaintypes[j] == "(string)" :
                fieldinline[j] = fieldinline[j].replace(fieldinline[j],'"'+fieldinline[j]+'"')
            if attributes[j] in x  :
                x=x.replace(attributes[j],fieldinline[j])
        x=x.replace("and"," and ")
        x=x.replace("or"," or ")
        if  eval(x) :
            op.append(lines[linenumber])
        if linenumber == len(lines) - 1 :
            break
        linenumber+=1
    return op
def project( targetfile , listattr ):
    lst=listattr.replace(",","|")
    listattr=listattr.replace("'","")
    listattr = listattr.replace("\n","").split(",")
    global fileindex
    target = open(targetfile , "r" )
    attrib = target.readline()
    attributes = attrib.replace("\n","").split("|")
    domaintype = target.readline()
    dump = target.readline()
    domaintypes = domaintype.replace("\n","").split("|")
    lines = target.readlines()
    target.close()
    op=[lst+'\n']
    dom=""
    flag = [] 
    for k in range(len(attributes)) :
        flag.append(int(0))
    domain = []
    for l in range(len(listattr)) :
        domain.append("")
    for l in range(len(listattr)) :
        for k in range(len(attributes)):
            if listattr[l] == attributes[k] :
                domain[l]=domaintypes[k]
                flag[k]=1
                dom=dom+domain[l]+"|"
    dom=dom+"\n"
    dom=dom.replace("|\n","\n")
    op.append(dom)
    #print flag
    op.append("-----------------------------------------------------------\n")
    linenumber = 0
    while linenumber < len(lines):
        fieldinline = lines[linenumber].replace("\n","").split("|")
        #print fieldinline
        linn=""
        for j in range(len(domaintypes)):
            if flag[j] :
                linn=linn+str(fieldinline[j])+"|"
        linn=linn+"\n"
        #print linn
        linn=linn.replace("|\n","\n")
        op.append(linn)     
        linenumber+=1
    return op
def cross(file1,file2):
    t1 = open(file1,"r")
    t2 = open(file2,"r")
    destn = t1.readlines()
    src = t2.readlines()
    t1.close()
    t2.close()
    silt=[ ]
    for initial in range(3) :
        destn[initial]=destn[initial].replace("\n","")
        print src[initial]
        src[initial]=src[initial].replace("\n","")
        if initial==2:
            mid="-"
        else :
            mid="|"
        silt.append(destn[initial]+mid+src[initial]+"\n")
    for nr in range(3,len(destn)):
        for nd in range(3,len(src)):
            tttt=destn[nr].replace("\n","")+"|"+src[nd].replace("\n","")+"\n"
            silt.append(tttt)
    t1 = open(file1,"w")    
    t1.writelines(silt)
    t1.close
    return
def copyfile(destn,src):
    t1=open(destn,"w")
    t2=open(src,"r")
    t1.writelines(t2.readlines())
    t1.close()
    t2.close()
    return
def renameop(newname,oldname,listattr):
    old = open(oldname,"r")
    yut = old.readlines()
    old.close
    new = open(newname,"w")
    old = open(oldname,"r")
    if len(listattr)==0 : 
            new.writelines(old.readlines())
            return 0
    listatr=listattr.split(",")
    if len(old.readline().split("|")) != len(listatr) :
        return 1
    satir = [listattr.replace(",","|").replace("\n","")+"\n",old.readline(),old.readline()]
    for indexing in range(3,len(yut)) :
        satir.append(yut[indexing].replace("\n","")+"\n")
    new.writelines(satir)
    new.close()
    old.close()
    old = open(oldname,"w")
    old.close()
    return 0
def union(file1,file2) :
    t1 = open(file1,"r")
    t2 = open(file2,"r")
    destn = t1.readlines()
    src = t2.readlines()
    t1.close()
    t2.close()
    if src[1].replace("\n","").replace(" ","")!=destn[1].replace("\n","").replace(" ",""):
        return 1
    t1 = open(file1,"a")
    t1.write("\n")
    t1.writelines(src[3:len(src)])
    t1.close()
    return 0
def diff(file1,file2) :
    t1 = open(file1,"r")
    t2 = open(file2,"r")
    destn = t1.readlines()
    src = t2.readlines()
    t1.close()
    t2.close()
    if src[1].replace("\n","").replace(" ","")!=destn[1].replace("\n","").replace(" ",""):
        return 1
    silt = [destn[0],destn[1],destn[2]]
    for i in range(3,len(src)):
                   src[i]=src[i].replace("\n","")
    for i in range(3,len(destn)):
                   destn[i]=destn[i].replace("\n","")                   
    for nr in range(3,len(destn)):
        if destn[nr] in src[3:len(src)]:
            continue
        silt.append(destn[nr].replace("\n","")+"\n")
    filecreate(silt,file1)
    return 0
def intersect(file1,file2) :
    t1 = open(file1,"r")
    t2 = open(file2,"r")
    destn = t1.readlines()
    src = t2.readlines()
    t1.close()
    t2.close()
    if src[1].replace("\n","").replace(" ","")!=destn[1].replace("\n","").replace(" ",""):
        return 1
    silt = [destn[0],destn[1],destn[2]]
    for nr in range(3,len(destn)):
        for nd in range(3,len(src)):
            if destn[nr].replace("\n","")==src[nd].replace("\n",""):
                silt.append(destn[nr].replace("\n","")+"\n")
    filecreate(silt,file1)
    return 0
def expression(expvector,index):
     tt = []
     k=0
     global fileindex
     if expvector[0]=="help" or expvector[0]=="HELP" or expvector[0]=="Help" or expvector[0]=="hELP" :
        document()
        return tt,1
     if expvector[0]=="assumptions" or expvector[0]=="ASSUMPTIONS" or expvector[0]=="Assumptions" or expvector[0]=="aSSUMPTIONS" :
        assume()
        return tt,1
     if expvector[0]=="display" or expvector[0]=="DISPLAY" or expvector[0]=="Display" or expvector[0]=="dISPLAY" :
        if len(expvector) == 2:
            filenaming = expvector[1]
        else :
            k=fileindex
            fileindex+=1
            xxx,dump = expression(expvector[1:len(expvector)],fileindex)            
            if len(xxx)==0:
                return tt,1
            filenaming = xxx[0]
        displayfile(filenaming)
        return tt,0
# Select
     if expvector[0] == "sigma" or expvector[0] == "select" or expvector[0] == "Select" or expvector[0] == "SELECT":
         if expvector[len(expvector) - 2]!="on"   :
             print "# SyntaxError in Expresion.System Rolling Back "
             errno = [' argument instead of " on " ',' length of the expression: number of arguments ']
             print "Unexpected"+errno[len(expvector) % 2 + 1]+'\n'
             return tt,1
         elif len(expvector) == 4 :
             fil = expvector[1]
         else :
             k=fileindex
             fileindex+=1
             xxx,dump = expression(expvector[1:len(expvector)-2],fileindex)
             if len(xxx)==0 :
                 return tt,1
             fil = xxx[0]
         output = select(fil , expvector[len(expvector) - 1])
         filecreate(output,"temp"+str(k))
         tt.append("temp"+str(k))
         return tt,1    
# Projection
     elif expvector[0] == "pi" or expvector[0] == "project" or expvector[0] == "PROJECT" or expvector[0] == "Project":
        if   expvector[2]!="from"   :
             print "# SyntaxError in Expresion.System Rolling Back "
             errno = ' argument instead of " from " '
             print "Unexpected"+errno+'\n'
             return tt,1
        elif len(expvector) == 4 :
             fil = expvector[3]
        else :
             k=fileindex
             print "hjgfghjkljh",k
             fileindex+=1
             xxx,dump = expression(expvector[3:len(expvector)],fileindex)
             if len(xxx)==0 :
                 return tt,1
             fil = xxx[0]
        output = project(fil , expvector[1])
        filecreate(output,"temp"+str(k))
        tt.append("temp"+str(k))
        return tt,1    
# Rename
     elif expvector[0] == "rho" or expvector[0] == "rename" or expvector[0] == "Rename" or expvector[0] == "RENAME":
         #print "Rho for Rename operator"
         if len(expvector)< 5 :
             print "    # Error in the number of arguments . Try Again "
             return tt,1
         if expvector[len(expvector)-3]!="to":
             print "    # SyntaxError : Expected 'to' at this place "
             return tt,1
         listofattr=expvector[len(expvector)-1]
         if len(expvector)==5 :
             oldname=expvector[1]
         else :
             hyt,uhu = expression(expvector[1:len(expvector)-3],fileindex)
             if len(hyt)==0 :
                 return tt,1
             oldname=hyt[0]
         k=renameop(expvector[len(expvector)-2],oldname,listofattr)
         if k==1:
             print "  # SyntaxError : Error in the number of new attribute names . Type again "
             return tt,1
         tt.append(expvector[len(expvector)-2])
         return tt,1 
# Union
     elif expvector[0] == "union" or expvector[0] == "U" or expvector[0] == "UNION" or expvector[0] == "Union":
         #print "Union "
         if len(expvector) == 2 :
             fillist = expvector[1]
         else :
             print "     # SyntaxError : Error in the number of arguments.Type again "
             return tt,1
         fillist = fillist.split(",")
         t1 = open(fillist[0],"r")
         t2 = open("crosstemp","w")
         t2.writelines(t1.readlines())
         t1.close()
         t2.close()
         for fileptr in range(1,len(fillist)) :
             errorflag=union("crosstemp",fillist[fileptr])
             if errorflag:
                 print "     # SyntaxError : Error in the Union compatibility.Type again the filetype "
                 return tt,1         
         tt.append("crosstemp")
         return tt,1            
# Intersection
     elif expvector[0] == "intersection" or expvector[0] == "ᑎ" or expvector[0] == "Intersection" or expvector[0] == "INTERSECTION" or expvector[0] == "n":
         if len(expvector) == 2 :
             fillist = expvector[1]
         else :
             print "     # SyntaxError : Error in the number of arguments.Type again "
             return tt,1
         fillist = fillist.split(",")         
         t1 = open(fillist[0],"r")
         t2 = open("crosstemp","w")
         t2.writelines(t1.readlines())
         t1.close()
         t2.close()
         for fileptr in range(1,len(fillist)) :
             errorflag=intersect("crosstemp",fillist[fileptr])
             if errorflag:
                 print "     # SyntaxError : Error in the Set Difference compatibility.Type again the filetype "
                 return tt,1
         tt.append("crosstemp")
         return tt,1        
# Difference
     elif expvector[0] == "-" or expvector[0] == "minus" or expvector[0] == "diff" or expvector == "difference":
         if len(expvector) == 2 :
             fillist = expvector[1]
         else :
             print "     # SyntaxError : Error in the number of arguments.Type again "
             return tt,1
         fillist = fillist.split(",")
         if len(fillist)!=2:
             print "     # SyntaxError : Error in the number of relations.Use only 2 relations.Type again "
         t1 = open(fillist[0],"r")
         t2 = open("crosstemp","w")
         t2.writelines(t1.readlines())
         t1.close()
         t2.close()
         for fileptr in range(1,len(fillist)) :
             errorflag=diff("crosstemp",fillist[fileptr])
             if errorflag:
                 print "     # SyntaxError : Error in the Set Difference compatibility.Type again the filetype "
                 return tt,1
         tt.append("crosstemp")
         return tt,1
# Cross Product
     elif expvector[0] == "X" or expvector[0] == "cross" or expvector[0] == "Cross" or expvector[0] == "CROSS":
         if len(expvector) == 2 :
             fillist = expvector[1]
         else :
             print "     # SyntaxError : Error in the number of arguments.Type again "
             return tt,1
         fillist = fillist.split(",")
         t1 = open(fillist[0],"r")
         t2 = open("crosstemp","w")
         t2.writelines(t1.readlines())
         t1.close()
         t2.close()
         for fileptr in range(1,len(fillist)) :
             cross("crosstemp",fillist[fileptr])
         tt.append("crosstemp")
         return tt,1 
#Program UI goes here==============================================================================================>>>>>>>>>>>>>>>>>>
choc=1
print "\t \t Enter an Expression  \n"  
while choc:
    expr = raw_input("Expression>> ")
    """if expr=="Manual" or expr=="help" or expr=="syntax" or expr=="manual" :  
        print "SYNTAX MANUAL"
        doc = open("Help.txt","r")
        print doc.read()
        doc.close()
    elif expr=="exit" :
        break"""
    expr = expr.replace(" ","")
    expvector = expr.split('|')
    expr="display|"+expr
    expvector = expr.split("|")
    fileindex = 0
    ll,choc = expression(expvector,fileindex) 
#n = raw_input("")
