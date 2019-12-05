import sys
import dis

with open('code2Trace.dat') as c2T:
    cnt=1
    new_string = ''
    for line in c2T:
                    #read_line = t2D.readline()
        if (line == '**EOT**'):
            c2T.close()
            break
        if (".py" in line):
            chopped_line = ''
            marker = False
            for c in line:
                #need to remove the front bit
                if c.startswith('\t'):
                    pass
                elif (marker):
                    chopped_line += c
                    cnt += 1
                    #new_string += chopped_line
                if c == ':':
                    marker = True
            new_string += chopped_line
            #print( chopped_line)
            #dis.dis('this = 2')
            
            
#print(new_string)

dis.dis(new_string)

print('**EOD**')
