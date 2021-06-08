### Import all required modules
import easygui#Read file from file explorer
from shapely.geometry import LineString #For converting coordinates to line segment objects
from unionFind import union_find #Class to implement Union-Find Algorithm
import time #For computing and comparing loop execution time
from copy import deepcopy

### Reading file and Data Sanitization: Read coordinates from text file: each row is a line segment: x1,y1,x2,y2
print("Reading file....")
file = easygui.fileopenbox()
with open(file) as f:
    orig_coords = [list(float(c) for c in line.split()) for line in f]
print(f"Reading file: {file}: done")
print("1. Start Data Sanitization....")
#Filter out empty list elements
filtered_coords = list(filter(None, orig_coords))
print("1.1 Filter empty list elements: done")
#For each line segment, place the left-most point on the left
left_sorted_coords = deepcopy(filtered_coords)
for line in left_sorted_coords:
    if line[2]<line[0]:
        temp_x1 = line[0]
        temp_y1 = line[1]
        line[0] = line[2]
        line[1] = line[3]
        line[2] = temp_x1
        line[3] = temp_y1
print("1.2 Place the left-most point to the left: done")
#Sort the line segments by their left-most x-coordinate so that intersecting lines can be grouped early on
sorted_coords = sorted(left_sorted_coords, key=lambda x: x[0])
print("1.3 Sort the line segments by their left-most x-coordinate: done")

### Check if line segments intersect and implement union-find
print("2. Check if line segments intersect and implement union-find....")

print("2.1 Implementing on filtered coordinates....")
#Creating a list of lines from filtered coordinates
line_list1 = list(map(lambda x: LineString([(x[0],x[1]),(x[2],x[3])]), filtered_coords))
#Implementing Union-Find method
myset = union_find(len(line_list1))
start_time=time.time()
for i in range(len(line_list1)-1):
    for j in range(i+1,len(line_list1)):
            if (line_list1[i].intersects(line_list1[j])==True):
                union_find.union(myset,i,j)
end_time=time.time()
print(f"Time elapsed: {end_time-start_time} s")
print(f"Number of groups: {union_find.count(myset)}")

print("2.2 Implementing on left-sorted coordinates....")
#Creating a list of lines from left-sorted coordinates
line_list1 = list(map(lambda x: LineString([(x[0],x[1]),(x[2],x[3])]), left_sorted_coords))
#Implementing Union-Find method
myset = union_find(len(line_list1))
start_time=time.time()
for i in range(len(line_list1)-1):
    for j in range(i+1,len(line_list1)):
            if (line_list1[i].intersects(line_list1[j])==True):
                union_find.union(myset,i,j)
end_time=time.time()
print(f"Time elapsed: {end_time-start_time} s")
print(f"Number of groups: {union_find.count(myset)}")

print("2.3 Implementing on left-sorted coordinates with a check for existing connectivity....")
#Creating a list of lines from left-sorted coordinates
line_list1 = list(map(lambda x: LineString([(x[0],x[1]),(x[2],x[3])]), left_sorted_coords))
#Implementing Union-Find method
myset = union_find(len(line_list1))
start_time=time.time()
for i in range(len(line_list1)-1):
    for j in range(i+1,len(line_list1)):
        if union_find.connected(myset,i,j)==False: #If parent are not the same, check for intersection. Else, skip.
            if (line_list1[i].intersects(line_list1[j])==True):
                union_find.union(myset,i,j)
end_time=time.time()
print(f"Time elapsed: {end_time-start_time} s")
print(f"Number of groups: {union_find.count(myset)}")

print("2.4 Implementing on left-to-right sorted coordinates with a check for existing connectivity....")
#Creating a list of lines from left-sorted coordinates
line_list1 = list(map(lambda x: LineString([(x[0],x[1]),(x[2],x[3])]), sorted_coords))
#Implementing Union-Find method
myset = union_find(len(line_list1))
start_time=time.time()
for i in range(len(line_list1)-1):
    for j in range(i+1,len(line_list1)):
        if union_find.connected(myset,i,j)==False: #If parent are not the same, check for intersection. Else, skip.
            if (line_list1[i].intersects(line_list1[j])==True):
                union_find.union(myset,i,j)
end_time=time.time()
print(f"Time elapsed: {end_time-start_time} s")
print(f"Number of groups: {union_find.count(myset)}")

print("Implemented all versions of Union-Find.")