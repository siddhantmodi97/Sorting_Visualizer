import time

def bubble_sort(arr,drawData,sleeptime):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j]>arr[j+1]:
                arr[j+1], arr[j]=arr[j],arr[j+1]
                drawData(arr,['black' if c==j or c==j+1 else 'cyan' for c in range(len(arr))])
                time.sleep(sleeptime)
    drawData(arr, ['green' for x in range(len(arr))])