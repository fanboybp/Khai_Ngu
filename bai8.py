#tinh tong day so duong dai nhat
def daycosoduongnhieunhat(lst):
    demmax = 0
    dem = 0
    
    for num in lst:
        if num > 0:
            dem += 1
            demmax = max(demmax, dem)
        else:
            dem = 0
    
    return demmax

# Example usage:
mlist=[1,3,5,7,8,-2,4,71,2,9,92,92,71,-8,-9,-2,-4,-5]
print("Day so duong dai nhat la :", daycosoduongnhieunhat(mlist))
           