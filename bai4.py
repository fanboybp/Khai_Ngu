list=[1,3,5,-3,7,8,4,2,9,92,71,-8,-9,-2,-4,-5]
vitri=0
for i in range(len(list)):
    x=list[i]
    if x<0:
        vitri=i
        break

print(vitri)
