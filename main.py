from tkinter import *
root = Tk()
canvas = Canvas(root, width=500, height=500)
canvas.pack()
file1=open('text3','r')
lines=file1.read().split('\n')
print(lines)
def dfs(graph, start, end, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = [start]
    if start == end:
        return path
    longest_path = []
    visited.add(start)
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            new_path = dfs(graph, neighbor, end, visited, path + [neighbor])
            if len(new_path) > len(longest_path):
                longest_path = new_path
    visited.remove(start)
    return longest_path

def find_diameter(graph):
    max_path_length = 0
    max_path = []
    for start in graph.keys():
        for end in graph.keys():
            if start != end:
                path = dfs(graph, start, end)
                if len(path) > max_path_length:
                    max_path_length = len(path)
                    max_path = path
    return max_path

def find_centroid(graph):
    diameter = find_diameter(graph)
    midpoint = len(diameter) // 2
    if len(diameter) % 2 == 0:
        return [diameter[midpoint - 1], diameter[midpoint]]
    else:
        return [diameter[midpoint]]

result = {}
with open('text3', 'r') as file:
    for line in file:
        pairs = line.strip().split(';')
        for pair in pairs:
            key, value = pair.split('-')
            key = int(key)
            value = int(value)
            if key not in result:
                result[key] = [value]
            else:
                result[key].append(value)

centroid = find_centroid(result)
print("Центроид в графе:", centroid)
print("Самый длинный путь в графе:", find_diameter(result))
print("Диаметр:", len(find_diameter(result)))

d=len(find_diameter(result))

#canvas.create_rectangle(0,0,500,(500//d))
#for i in range((d+1)//2):
    #canvas.create_rectangle(0,(i+1)*(500//d),500,(i+2)*(500//d))

def get_unique_numbers(lines):
    unique_numbers = []
    for line in lines:
        a, b = line.split('-')
        unique_numbers.append(int(a))
        unique_numbers.append(int(b))

    return(list(set(unique_numbers)))

print(get_unique_numbers(lines))

massiv=[]
massiv.append(centroid)

klen=get_unique_numbers(lines)

for i in range((d+1)//2-1):
    massiv.append([])
k=1
for i in range(len(massiv)-1):
    for j in range(len(massiv[i])):
        for u in range(len(klen)):
            if str(massiv[i][j])+'-'+str(klen[u]) in lines:
                massiv[i+1].append(klen[u])

for i in range(len(massiv)):
    massiv[i]=list(set(massiv[i]))

for i in range(0,len(massiv)):
    for j in range(i+1,len(massiv)):
        massiv[j]=list((set(massiv[i])|set(massiv[j]))-set(massiv[i]))
print(massiv)


#canvas.create_oval(235,500//d//2-15,265,500//d//2+15,fill='orange')



for i in range(len(massiv)-1):
    for j in range(len(massiv[i])):
        for u in range(len(massiv[i+1])):
            if (str(massiv[i][j])+'-'+str(massiv[i+1][u])) in lines:
                canvas.create_line((2*j+1)*(500//len(massiv[i]))//2,(2*i+1)*500//d//2,(2*u+1)*(500//len(massiv[i+1]))//2,(2*(i+1)+1)*500//d//2)
                canvas.create_oval((2 * j + 1) * (500 // len(massiv[i])) // 2 - 15, (2 * i + 1) * 500 // d // 2 - 15,
                                   (2 * j + 1) * (500 // len(massiv[i])) // 2 + 15, (2 * i + 1) * 500 // d // 2 + 15,
                                   fill='orange')
                canvas.create_text(((2 * j + 1) * (500 // len(massiv[i])) // 2 - 15+(2 * j + 1) * (500 // len(massiv[i])) // 2 + 15)//2, ((2 * i + 1) * 500 // d // 2 - 15+(2 * i + 1) * 500 // d // 2 + 15)//2,text=str(massiv[i][j]))

for i in range(len(massiv)):
    for j in range(len(massiv[i])):
        for u in range(len(massiv[i])):
            if (str(massiv[i][j])+'-'+str(massiv[i][u])) in lines:
                canvas.create_line((2*j+1)*(500//len(massiv[i]))//2,(2*i+1)*500//d//2,(2*u+1)*(500//len(massiv[i]))//2,(2*i+1)*500//d//2)
                canvas.create_oval((2 * j + 1) * (500 // len(massiv[i])) // 2 - 15, (2 * i + 1) * 500 // d // 2 - 15,
                                   (2 * j + 1) * (500 // len(massiv[i])) // 2 + 15, (2 * i + 1) * 500 // d // 2 + 15,
                                   fill='orange')
                canvas.create_text(((2 * j + 1) * (500 // len(massiv[i])) // 2 - 15+(2 * j + 1) * (500 // len(massiv[i])) // 2 + 15)//2, ((2 * i + 1) * 500 // d // 2 - 15+(2 * i + 1) * 500 // d // 2 + 15)//2,text=str(massiv[i][j]))


for i in range(1,len(massiv)):

    for j in range(len(massiv[i])):

        #canvas.create_rectangle(j*(500//len(massiv[i])),i*500//d,0+(j+1)*(500//len(massiv[i])),(i+1)*500//d)
        canvas.create_oval((2*j+1)*(500//len(massiv[i]))//2-15,(2*i+1)*500//d//2-15,(2*j+1)*(500//len(massiv[i]))//2+15,(2*i+1)*500//d//2+15,fill='orange')
        canvas.create_text(
            ((2 * j + 1) * (500 // len(massiv[i])) // 2 - 15 + (2 * j + 1) * (500 // len(massiv[i])) // 2 + 15) // 2,
            ((2 * i + 1) * 500 // d // 2 - 15 + (2 * i + 1) * 500 // d // 2 + 15) // 2, text=str(massiv[i][j]))
root.mainloop()