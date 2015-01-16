filename = raw_input()
file_pointer = open(filename[:-3]+"xml",'w');
flag = 1
first = 1
new = 0
with open(filename) as fp:
    file_pointer.write("<QuestionsDoc>")
    for line in fp:
        if(line[0]==' '):
            line = ' '.join(line.split())
        if(line[0] == "\n"):
            continue
        if (line[0:26] == "Single Correct Answer Type"):
            if(flag):
                file_pointer.write("<questionSection>");                
                flag=0
            file_pointer.write("<questionSectiontype>"+line+"</questionSectiontype>");
        elif(line[0]>='0' and line[0]<='9'):
            if(new):
                file_pointer.write("</answerinfo></answer>");
                new = 0
            if(not(first)):
                file_pointer.write("</answer>")                
                file_pointer.write("</question>")
            file_pointer.write("<question>")
            file_pointer.write("<qno>"+line[0]+"</qno>");
            file_pointer.write("<questioninfo>"+line[2:]+"</questioninfo>")
            file_pointer.write("<answer>")
            first = 0 
        elif(line[0]=='('):
            i = 0 
            while(line):
                if(new):
                    file_pointer.write("</answerinfo></answer>");
                    new = 0
                file_pointer.write("<answer>");
                file_pointer.write("<opt>");
                file_pointer.write(line[1]);
                file_pointer.write("</opt><answerinfo>")
                line = line[3:]   
                for i in range(len(line)-1):
                    if((line[i]=='a' or line[i]=='b' or line[i]=='c' or line[i]=='d') and line[i+1] == ')'):
                        file_pointer.write(line[0:i-1]);
                        line = line[i-1:]
                        new = 1
                        break;
                if(i == len(line)-2):
                    file_pointer.write(line[0:]);
                    new = 1
                    line = ""
            
        elif(line[0]=='a' or line[0]=='b' or line[0]=='c' or line[0]=='d'):
            i = 0 
            while(line):
                if(new):
                    file_pointer.write("</answerinfo></answer>");
                    new = 0
                file_pointer.write("<answer>");
                file_pointer.write("<opt>");
                file_pointer.write(line[0]);
                file_pointer.write("</opt><answerinfo>")
                line = line[2:]   
                for i in range(len(line)-1):
                    if((line[i]=='a' or line[i]=='b' or line[i]=='c' or line[i]=='d') and line[i+1] == ')'):
                        file_pointer.write(line[0:i]);
                        line = line[i:]
                        new = 1
                        break;
                if(i == len(line)-2):
                    file_pointer.write(line[0:]);
                    new = 1
                    line = ""
        else:
            if(first):
                file_pointer.write("<questionspreamble>"+line+"</questionspreamble>")
            else:
                file_pointer.write(" "+line);

    if(new):
        file_pointer.write("</answerinfo></answer>");
        new = 0        
    if(not(first)):
        file_pointer.write("</answer>")                
        file_pointer.write("</question>")
    
    file_pointer.write("</questionSection></QuestionsDoc>");
