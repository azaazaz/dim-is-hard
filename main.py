#to do after
#     fill ans list/dict                      #DONE
#     write down every subj on main window
#     red green managent                      #DONE
#     move from column to column with keyboard #NEED HELP ON THIS


from collections import UserDict
import tkinter as tk
from tkinter import *
from tkinter.tix import COLUMN

#characteristics of main windows
root = tk.Tk()
root.geometry("600x600") #size of pic
bg = tk.PhotoImage(file = "pixel_clouds.png")
label1 = tk.Label( root, image = bg).place(x=0, y= 0)

#row - y
#column | x

ans = {"1":["a","b","c","d","a","a","b","c","d","a","a","b","c","d","a","a","b","c","d","a","a","b","c","d","a"], "2":["c","b" ,"a", "d", "a", "c", "e","c","b" ,"a", "d", "a", "c", "e""c","b" ,"a", "d", "a", "c", "e","c","b" ,"c","b" ,"a", "d", "a", "c", "e","c","b" ,"a", "d", "a", "c", "e","c","b" ,"a", "d", "a", "c", "e","c","b""c","b" ,"a", "d", "a", "c", "e","c","b" ,"a", "d", "a", "c", "e","c","b" ,"a", "d", "a", "c", "e","c","b"],"3":["b","c", "a","c","b" ,"a", "d", "a", "c", "e","c","b" ,"a", "d", "a", "c", "e","c","b" ,"a", "d", "a", "c", "e","c","b","c","b" ,"a", "d", "a", "c", "e","c","b" ,"a", "d", "a", "c", "e","c","b" ,"a", "d", "a", "c", "e","c","b","c","b" ,"a", "d", "a", "c", "e","c","b" ,"a", "d", "a", "c", "e","c","b" ,"a", "d", "a", "c", "e","c","b"]}


#answer window
def new_win():
   global entry
   string= entry.get()
   new = Toplevel(root)

   lenn = len(ans[string])
   leng = lenn//10

   def check():
      for i in range(lenn): #for each Q
         orig = ans[string][i]
         student = new.grid_slaves(row=((i//10)+1), column=(i%10)+1)[0].get()
         print(student)
         if orig == student:
            new.grid_slaves(row=((i//10)+1), column= (i%10)+1)[0].configure(bg = "#AFE664")
            #green
            print("right")
         elif student == "":
            new.grid_slaves(row=((i//10)+1), column= (i%10)+1)[0].configure(bg = "#FDDC39")
            #yellow
            print("not given")
         else:
            new.grid_slaves(row=((i//10)+1), column= (i%10)+1)[0].configure(bg = "#FF4057")
            #red
            print("wrong")
         

   tk.Label(new, text= " ").grid(row = 0, column = 0)

   for i in range(1,11):
      tk.Label(new, text = i).grid(row = 0, column = i)
   for y in range (leng+1):
      tk.Label(new,text = y*10).grid(row = y+1, column = 0)
      for k in range (1,11):
         tk.Entry(new).grid(row = y+1, column = k)
   tk.Button(new, text= "Ready!", command = check).grid(row = 13, column = 13)
   
   
entry= Entry(root)
entry.focus_set()
entry.pack()
tk.Button(root, text= "Okay", command= new_win).pack()

l1 = tk.Label(root,text = "MATH").pack()
l11 = tk.Label(root, text = "1 -> Function Y = KX + b \n 2 -> Function Y = X/K + B \n 3 -> sin x = y \n 4 -> cos x = y").pack()
#TO DO

root.mainloop()