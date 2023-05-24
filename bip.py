from tkinter import *
root = Tk()
canvas = Canvas(root, width=500, height=500)
canvas.pack()
file1=open('text','r')
lines=file1.read().split('\n')
print(lines)
ver1=[]
ver2=[]
for i in range(len(lines)):
    ver1.append(int(lines[i][0]))
print(ver1)
group1 = []
for i in ver1:
  if i not in group1:
    group1.append(i)
print(group1)
for i in range(len(lines)):
    ver2.append(int(lines[i][2]))
print(ver2)
group2 = []
for i in ver2:
  if i not in group2:
    group2.append(i)
print(group2)

for i in range(len(group1)):
    for j in range(len(group2)):
        if str(group1[i])+'-'+str(group2[j]) in lines:
            canvas.create_line(125,(2*i+1)*500//len(group1)//2,375, (2 * j + 1) * 500 // len(group2) // 2)
for i in range(len(group1)):
    #canvas.create_rectangle(0,i*500//len(group1),250,(i+1)*500//len(group1))
    canvas.create_oval(110,((2*i+1)*500//len(group1))//2-15,140,((2*i+1)*500//len(group1))//2+15,fill='orange')
    canvas.create_text(125,(2*i+1)*500//len(group1)//2,text=str(group1[i]))
for i in range(len(group2)):
    #canvas.create_rectangle(250,i*500//len(group2),500,(i+1)*500//len(group2))
    canvas.create_oval(360, ((2 * i + 1) * 500 // len(group2)) // 2 - 15, 390,
                       ((2 * i + 1) * 500 // len(group2)) // 2 + 15,fill='pink')
    canvas.create_text(375, (2 * i + 1) * 500 // len(group2) // 2, text=str(group2[i]))
root.mainloop()