from tkinter import *
root = Tk()
canvas = Canvas(root, width=500, height=500)
canvas.pack()
file1=open('text2','r')
lines=file1.read().split('\n')
print(lines)
lines1=[]
lines1.append(lines[0])
center=[]
k=1
for i in range(1,len(lines)):
    lines1.append(k*int(lines[i]))
    k=k*int(lines[i])
#for i in range(int(lines1[0])):
    #canvas.create_rectangle(0,i*500//int(lines1[0]),500,(i+1)*500//int(lines1[0]))
canvas.create_oval(242,500//int(lines1[0])//2-8,258,500//int(lines1[0])//2+8,fill='purple')
center.append([250,500//int(lines1[0])//2])
for i in range(1,int(lines1[0])):
    for j in range(int(lines1[i])):
        #canvas.create_rectangle(j*500//int(lines1[i]),i*500//int(lines1[0]),(j+1)*500//int(lines1[i]),(i+1)*500//int(lines1[0]))
        canvas.create_oval((2*j+1) * 500 // int(lines1[i])//2-8, ((2*i+1) * 500 // int(lines1[0]))//2-10, (2*j+1) * 500 // int(lines1[i])//2+10,
                                ((2*i+1) * 500 // int(lines1[0]))//2+8,fill='purple')

        center.append([(2*j+1) * 500 // int(lines1[i])//2,((2*i+1) * 500 // int(lines1[0]))//2])
print(center)

for i in range(lines1[1]):
    canvas.create_line(center[0][0],center[0][1],center[i+1][0],center[i+1][1])



for i in range(1,int(lines1[1])+1):#+0 +2 +2 +4 +0 +1 +1 +2
    for j in range(int(lines1[1])+int(lines[2])*i-int(lines[2])+1,int(lines1[1])+int(lines[2])*i+1):
        canvas.create_line(center[i][0],center[i][1],center[j][0],center[j][1])

k=0
for i in range(int(lines1[1])+1,int(lines1[1])+1+int(lines[1])*int(lines[2])):
    k=k+1
    for j in range(int(lines1[1])+int(lines[1])*int(lines[2])+int(lines[3])*k-int(lines[3])+1,int(lines1[1])+int(lines[1])*int(lines[2])+int(lines[3])*k+1):
        canvas.create_line(center[i][0],center[i][1],center[j][0],center[j][1])

def fact(s):
    fact=1
    for i in range(s):
        fact=fact*int(lines[i+1])
    return fact
m=int(lines1[1])+1+int(lines[1])*int(lines[2])
s=3

for b in range(4,len(lines1)):
    k=0
    for i in range(m,m+fact(s)):
        k=k+1
        for j in range(m+fact(s)-1+int(lines[b])*k-int(lines[b])+1,m+fact(s)-1+int(lines[b])*k+1):
            canvas.create_line(center[i][0],center[i][1],center[j][0],center[j][1])
    m=m+fact(s)
    s=s+1





root.mainloop()




