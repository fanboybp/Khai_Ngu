#phan tu lon nhi cua danh sach
mlist=[1,3,5,7,8,-2,4,71,2,9,92,92,71,-8,-9,-2,-4,-5]   
mlist.sort()
print(mlist)
max_number = max(mlist)
second_max = float('-inf')  # Giả sử số lớn thứ nhì là âm vô cùng ban đầu
indices = []

for index, num in enumerate(mlist):
    if num == max_number:
        continue
    elif num > second_max:
        second_max = num
        indices = [index]
    elif num == second_max:
        indices.append(index)

print("Số lớn thứ nhì trong danh sách là:", second_max)
print("Các vị trí của số lớn thứ nhì:", indices)