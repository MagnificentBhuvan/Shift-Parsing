from  tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import networkx as nx
import math
def neighbors1(self, n):
        
    try:
        return iter(self._adj[n])
    except KeyError:
        raise NetworkXError("The node %s is not in the graph." % (n,))
def non_neighbors1(graph, node):
    
    nbors = set(neighbors1(graph, node)) | set([node])
    return (nnode for nnode in graph if nnode not in nbors)
def non_edges1(graph):
    
    if graph.is_directed():
        for u in graph.nodes():
            for v in non_neighbors1(graph, u):
                yield (u, v)
    else:
        S = set()
        for u in graph.nodes():
            for v in non_neighbors1(graph, u):
                if (u, v) not in S:
                    yield (u, v)
                    S.add((v, u))
                    
def common_neighbors1(G, u, v):
    
    if u not in G:
        raise nx.NetworkXError('u is not in the graph.')
    if v not in G:
        raise nx.NetworkXError('v is not in the graph.')

    # Return a generator explicitly instead of yielding so that the above
    # checks are executed eagerly.
    return (w for w in G[u] if w in G[v] and w not in (u, v))

def jaccard_coefficient1(G, ebunch=None):
    
    if ebunch is None:
        ebunch = non_edges1(G)

    def predict(u, v):
        cnbors = list(common_neighbors1(G, u, v))
        union_size = len(set(G[u]) | set(G[v]))
        if union_size == 0:
            return 0
        else:
            return float(len(cnbors) / union_size)

    return ((u, v, predict(u, v)) for u, v in ebunch)

def adamic_adar_index1(G, ebunch=None):
    
    if ebunch is None:
        ebunch = non_edges1(G)

    def predict(u, v):
        return sum(1 / math.log(G.degree(w))
                   for w in common_neighbors1(G, u, v))

    return ((u, v, predict(u, v)) for u, v in ebunch)

root = Tk()
root.geometry("1024x769")
temp1=list()
temp2=list()
def openfile():
   #msg = messagebox.showinfo( "Hello Python", "Hello World")
    root.filename =  filedialog.askopenfilename(initialdir = "F:/mini project 1/",title = "choose your file",filetypes = (("GML files","*.gml"),("all files","*.*")))
    print (root.filename)
    if len(root.filename)==0:
        msg = messagebox.showinfo( "Error", "No file is Selected")
    else:
        E1.insert(0,root.filename)

def jaccard_coefficient():
    if len(E1.get())==0:
        msg = messagebox.showinfo( "Error", "No file is Selected")
    else:
        print("I am in Adamic Adar")
        G=nx.read_gml(E1.get())
        preds = jaccard_coefficient1(G)
    #print(*preds, sep='  ')
        temp=0.0
        
        for u, v, p in preds:
            if p>0.0:
                temp2.append([u,v,p])
            if p>temp:
                u1=u
                v1=v
                temp=p
                
            '(%s, %s) -> %.8f' % (u, v, p)
            #print(u,',',v,',',p)
        print(u1,',',v1,',',temp)
        print(temp2)
        temp2.sort(key=lambda x: x[2],reverse=True)
        var6 = StringVar()
        label6=Label(root,textvariable = var6,relief = FLAT)
        var6.set("Author 1 : "+str(u1)+"\n Author 2 : "+str(v1)+"\n Jaccard co-efficient : "+str(temp))
        label6.pack(side=LEFT)
        label6.place(x=100,y=450)
        Lb2 = Listbox(root,width=50)
        q=0
        for each in temp2:
            Lb2.insert(END, each)
            q=+1
        Lb2.pack()
        Lb2.place(x=400,y=400)    
        
def adamic_adar():
    if len(E1.get())==0:
        msg = messagebox.showinfo( "Error", "No file is Selected")
    else:
        print("I am in Adamic Adar")
        G=nx.read_gml(E1.get())
        preds = adamic_adar_index1(G)
    #print(*preds, sep='  ')
        temp=0.0
        
        for u, v, p in preds:
            if p>0.0:
                temp1.append([u,v,p])
            if p>temp:
                u1=u
                v1=v
                temp=p
                
            '(%s, %s) -> %f' % (u, v, p)
            #print(u,',',v,',',p)
        print(u1,',',v1,',',temp)
        print(temp1)
        temp1.sort(key=lambda x: x[2],reverse=True)
        var4 = StringVar()
        label4=Label(root,textvariable = var4,relief = FLAT)
        var4.set("Author 1 : "+str(u1)+"\n Author 2 : "+str(v1)+"\n Adamic Adar index : "+str(temp))
        label4.pack(side=LEFT)
        label4.place(x=100,y=200)
        Lb1 = Listbox(root,width=50)
        q=0
        for each in temp1:
            Lb1.insert(END, each)
            q=+1
        Lb1.pack()
        Lb1.place(x=400,y=150)
       
var = StringVar()
label = Label( root, textvariable = var, relief = RAISED ,font=ACTIVE )
var.set("Link Prediction in Co Authorship Network ")
label.pack()

var1 = StringVar()
label1=Label(root,textvariable = var1,relief = FLAT )
var1.set("Enter the Filename ")
label1.pack(side=LEFT)
label1.place(x=100,y=50)

E1 = Entry(root, bd = 5,width=30)
E1.pack()
E1.place(x=300,y=50)

B = Button(root, text = "Open", command = openfile)
B.place(x = 500,y = 50)

var1 = StringVar()
label1=Label(root,textvariable = var1,relief = FLAT)
var1.set("ADAMIC ADAR INDEX ")
label1.pack(side=LEFT)
label1.place(x=450,y=100)

B1 = Button(root, text = "Calculate Adamic Adar", command = adamic_adar)
B1.place(x = 600,y = 50)

B2 = Button(root, text = "Calculate Jaccard Coefficient", command = jaccard_coefficient)
B2.place(x = 750,y = 50)

var5 = StringVar()
label5=Label(root,textvariable = var5,relief = FLAT)
var5.set(" JACCARD COEFFICIENT ")
label5.pack(side=LEFT)
label5.place(x=450,y=350)

root.mainloop()
print (root.filename)
#root.withdraw()
