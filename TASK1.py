'''Task 1
1-Searching an element in an array and its index
2-Finding largest number in an array
3-Finding smallest
4-Reversing an array
5-Rotating an array by Kth position'''
import numpy as np
n=int(input("Enter the size of 1D array : "))
arr=np.random.randint(0,10,n)
print("1.Enter a no. to search it in array and know its index",
      "2.To know the largest no.",
      "3.To know the smallest no.",
      "4.To reverse the array",
      "5.To rotate the array by Kth position",
     "6.To Exit",sep="\n")
print("Array : ",arr)
while True:
    ch=int(input("Enter Choice : "))
    if ch==1:
        x=int(input("Enter the no. : "))
        index=0
        found=0
        for k in arr:
            if k==x:
                print("Present and its index is ",index)
                found=1
                break
            else:
                index+=1
                continue
        if found==0:
            print("Not Present")
    elif ch==2:
        largest=arr[0]
        for k in arr:
            if k>largest:
                largest=k
            else:
                continue
        print("Largest no. : ",largest)
    elif ch==3:
        smallest=arr[0]
        for k in arr:
            if k<smallest:
                smallest=k
            else:
                continue
        print("Smallest no. : ",smallest)
    elif ch==4:
        '''for k in range(0,len(arr)):
            reverse_arr=arr[::-1]
        print(reverse_arr)'''
        l=len(arr)
        for i in range(l//2):
            arr[i],arr[l-i-1]=arr[l-i-1],arr[i]
        print("Reversed Array : ",arr)
    elif ch==5:
        x=int(input("Enter the position to be rotated : "))
        if x>len(arr):
            print("Can't be rotated")
        else:
            arr1=arr.copy()
            l=len(arr)
            for k in range(x):
                arr1[k]=arr1[l-x+k]
            for k in range(l-x):
                arr1[k+x]=arr[k]
            print("Rotated Array by position ",x,":",arr1)
    elif ch==6:
        break
    else:
        print("Invalid Choice")