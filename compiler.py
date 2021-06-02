functions=["NOP", "LDA", "LMA", "ADD", "ADM", "SBD", "SBM", "OUT", "STA", "JMP", "JMZ"]
variables=[]
values=[]
pr=open("program.ic","r")
s=""
c=0;
lc=0;
error=False;
for x in pr:
    if(x.find("\n")!=-1):
        x=x[:-1]
    fx=False
    for i in range(11):
        if(x[:x.find("(")]==functions[i]):
            s+=str(i)+"\n"
            fx=True
            c+=1
            if(x[x.find("(")+1:x.find(")")]!=""):
                c+=1
                try:
                    s+=str(int(x[x.find("(")+1:x.find(")")]))+"\n"
                except:
                    s+=x[x.find("(")+1:x.find(")")]+"\n"
                    ne=True;
                    for i in range(len(variables)):
                        ne=ne and not(variables[i]==x[x.find("(")+1:x.find(")")])
                    if(ne):
                        print("Error in line "+str(lc+1)+", undefined variable.")
                        error=True
                        break
    if(x=="HLT()"):
        s+="255"+"\n"
        fx=True
        c+=1
    if(x[:4]=="var "):
        if(x.find("=")==-1):
            variables.append(x[4:])
            values.append(0)
        else:
            variables.append(x[4:x.find("=")].strip())
            values.append(int(x[x.find("=")+1:].strip()))
        fx=True
    if(not fx):
        print("Error in line "+str(lc+1)+", compiling error")
        error=True
        break
    lc+=1
if(not error):
    for i in range(len(variables)):
        s=s.replace(variables[i],str(c))
        s+=str(values[i])+"\n"
        c+=1
    for i in range(c,256):
        s+="0\n"
    s=s[:-1]
    op=open("ram.txt","w")
    op.write(s)
    op.close()
pr.close()