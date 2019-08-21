# Program insertion sort
 
# fungsi insertion sort
def insertion_sort(arr):
 
    # traverse dari 1 sampai len(arr)
    for i in range(1, len(arr)):
 
        key = arr[i]
 
        # Pindahkan elemen arr[0...i-1], yang lebih besar
        # dari key, satu posisi ke kanan
        # dari posisi sekarang
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
 
 
# testing
arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
print ("Sorted array: ")
for i in range(len(arr)):
    print ("%d" %arr[i])