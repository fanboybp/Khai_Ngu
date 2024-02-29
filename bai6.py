#tim so dau tien la so am trong python
list=[1,3,5,7,8,-2,4,2,9,92,92,71,-8,-9,-2,-4,-5]   
max_number=max(list)
for i in range(len(list) - 1, -1, -1):
    if list[i] == max_number:
        last_index = i
        break

print("Vị trí của số lớn nhất cuối cùng trong danh sách là:", last_index)
            
    