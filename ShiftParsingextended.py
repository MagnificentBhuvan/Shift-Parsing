import copy
def stackreduce(stack,optiprorule,a):
      for i in list(range(1,len(stack))):
        if ''.join(stack[i:]) in optiprorule:
            newnonterminal=productionrule[optiprorule.index(''.join(stack[i:]))][0]
            del stack[''.join(stack[0:]).find(''.join(stack[i:])):]
            print ("New Non Terminal is ",end='')
            print (newnonterminal)
            stack.append(newnonterminal)
            print ("After Reducing stack is ",end='')
            print (stack)
            if len(tempqueue)==1 and a==0: 
                  pass
            elif len(tempqueue)>1:
                  stackreduce(stack,optiprorule,a)
            else:
                  a=a+1
a=0
productionrule=input("Enter the Production Rule").split(" ")
queue=[x for x in input("Enter the Input Symbols")]
queue.append('$')
stack=['$']
tempqueue=copy.deepcopy(queue)
print ("Production Rules are ",end='')
print (productionrule)
optiprorule=[eachrule[3:] for eachrule in productionrule]
for eachsymbol in queue[:len(queue)-1]:
    print ("Input Symbol queue ",end='')
    print (tempqueue)
    print ("Stack ",end='')
    print (stack)
    print ("Taken input symbols is ",end='')
    print (eachsymbol)
    stack.append(eachsymbol)
    tempqueue.pop(0)
    stackreduce(stack,optiprorule,a)
print ("--------------------------------------")
print("Stack is ",end='')
print (stack)
print("QUEUE is ",end='')
print (tempqueue)
if stack[0]=='$' and stack[1]==productionrule[0][0] and tempqueue[0]=='$':
      print ("ACCEPT, SUCCESSFULLY PARSING")
else:
      print ("UNSUCCESSFULLY PARSING")
             
            
            
            
                
