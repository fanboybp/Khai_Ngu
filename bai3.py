#tinh trung binh cong va trung binh cong so duong trong danh sach (list)
list=[1,3,5,7,8,4,2,9,92,71,-8,-9,-2,-4,-5]
tong=0
for x in list:
    tong+=x
dodai=len(list)
tbc=tong/dodai
print("trung binh cong cac phan tu")
print(tbc)
tongsoduong=0
demsoduong=0
for x in list:
    if x>=0:
        tongsoduong+=x
        demsoduong+=1
tbcsoduong=tongsoduong/demsoduong
print(tbcsoduong)
