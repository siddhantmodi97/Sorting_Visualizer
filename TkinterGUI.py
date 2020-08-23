from tkinter import *
from tkinter import ttk
import random
from MergeSort import merge_sort
from BubbleSort import bubble_sort
from QuickSort import quick_sort
from InsertionSort import insertion_sort

root = Tk()
root.title('Sorting Algorithm Visualisation')
root.maxsize(900, 600)
root.config(bg='black')

#variables
selected_alg = StringVar()
data=[]

def drawData(data,carr):
    canvas.delete("all")
    c_height = 380
    c_width = 600
    x_width = c_width / (len(data) + 1)
    offset = 30
    spacing = 10
    normalizedData = [ i / max(data) for i in data]
    for i, height in enumerate(normalizedData):
        #top left
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 340
        #bottom right
        x1 = (i + 1) * x_width + offset
        y1 = c_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=carr[i])
        canvas.create_text(x0+2, y0, anchor=SW, text=str(data[i]))
    root.update_idletasks()

def Generate():
    global data
    print('Alg Selected: ' + selected_alg.get())
    try:
        minVal = int(minEntry.get())
    except:
        minVal = 1
    try:
        maxVal = int(maxEntry.get())
    except:
        maxVal = 100
    try:
        size = int(sizeEntry.get())
    except:
        size = 15

    if size > 30 or size < 3: size = 25
    if minVal > maxVal : minVal, maxVal = maxVal, minVal

    data = []
    for _ in range(size):
        data.append(random.randrange(minVal, maxVal+1))
    drawData(data,['cyan' for x in range(len(data))])

def StartAlgorithm():
    global data
    if not data: return

    if algMenu.get() == 'Quick Sort':
        quick_sort(data, 0, len(data) - 1, drawData, speedScale.get())
        drawData(data, ['green' for x in range(len(data))])

    elif algMenu.get() == 'Bubble Sort':
        bubble_sort(data, drawData, speedScale.get())

    elif algMenu.get() == 'Merge Sort':
        merge_sort(data, drawData, speedScale.get())

    elif algMenu.get() == 'Insertion Sort':
        insertion_sort(data, drawData, speedScale.get())

#frame / base lauout
UI_frame = Frame(root, width= 600, height=200, bg='blue')
UI_frame.grid(row=0, column=0, padx=10, pady=5)

canvas = Canvas(root, width=700, height=380, bg='white')
canvas.grid(row=1, column=0, padx=10, pady=5)

#User Interface Area
#Row[0]
Label(UI_frame, text="Algorithm: ", bg='grey').grid(row=0, column=0, padx=5, pady=5, sticky=W)
algMenu = ttk.Combobox(UI_frame, textvariable=selected_alg, values=['Bubble Sort', 'Merge Sort','Quick Sort','Insertion Sort'],state='readonly')
algMenu.grid(row=0, column=1, padx=5, pady=5)
algMenu.current(0)

speedScale = Scale(UI_frame, from_=0.1, to=2.0, length=200, digits=2, resolution=0.2, orient=HORIZONTAL, label="Select Speed [s]")
speedScale.grid(row=0, column=2, padx=1, pady=1)
Button(UI_frame, text="Start", command=StartAlgorithm, bg='yellow').grid(row=0, column=3, padx=5, pady=5)

#Row[1]
Label(UI_frame, text="Size of Array", bg='grey').grid(row=1, column=0, padx=5, pady=5, sticky=W)
sizeEntry = Entry(UI_frame)
sizeEntry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

Label(UI_frame, text="Min Value ", bg='grey').grid(row=1, column=2, padx=1, pady=1, sticky=W)
minEntry = Entry(UI_frame)
minEntry.grid(row=1, column=3, padx=1, pady=1, sticky=W)

Label(UI_frame, text="Max Value ", bg='grey').grid(row=1, column=4, padx=5, pady=5, sticky=W)
maxEntry = Entry(UI_frame)
maxEntry.grid(row=1, column=5, padx=5, pady=5, sticky=W)

Button(UI_frame, text="Generate", command=Generate, bg='white').grid(row=1, column=6, padx=5, pady=5)

root.mainloop()