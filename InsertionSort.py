import time

def insertion_sort(arr,drawData,sleeptime):
    for i in range(1,len(arr)):
        key=arr[i]
        drawData(arr, ['red' if c == i else 'cyan' for c in range(len(arr))])
        time.sleep(sleeptime)
        j=i-1
        while j>=0 and key<arr[j]:
            drawData(arr, ['black' if c == j or c == j + 1 else 'cyan' for c in range(len(arr))])
            time.sleep(sleeptime)
            arr[j+1]= arr[j]
            j-=1
        arr[j+1]=key
    drawData(arr, ['green' for x in range(len(arr))])