from Tkinter import *
import tkMessageBox
import base64
import urllib


root=Tk()


root.title("Clothing")
root.geometry("500x500")
root.config(background="lightblue")


f1=Frame()
f1.pack()
f1.config(background="blue")

URL="file:///home/ishita/Desktop/dv.gif"
link=urllib.urlopen(URL)
raw_data=link.read()
link.close()
next=base64.encodestring(raw_data)
image12=PhotoImage(data=next)
label3=Label(f1,image=image12)
label3.config(width=700, height=700)
label3.pack()

text=Text(f1)

title= """Click on the button to start viewing clothes."""

text.delete(1.0, END)
text.insert(END, title)
text.config(width=47, height=5, state="disabled")
text.pack()

b=Button(f1)

def destroy():
	f1.destroy(), f2.pack(), root.config(background="blue")

def good1():
	f2.destroy(), f3.pack(), root.config(background="purple")

def good2():
	f3.destroy(), f4.pack(), root.config(background="green")

def good3():
	f4.destroy(), f5.pack(), root.config(background="pink")

"""def prev1():
	f3.destroy(), f2.pack(), root.config(background="blue")"""

def cart1():
	tkMessageBox.showinfo("Done", "Added to Cart")
	f=open("data.txt","a")
	f.writelines("\nDressberry top added to cart.\n")
	f.close()

def cart2():
	tkMessageBox.showinfo("Done", "Added to Cart")
	f=open("data.txt","a")
	f.writelines("\nKazo pants added to cart.\n")
	f.close()

def cart3():
	tkMessageBox.showinfo("Done", "Added to Cart")
	f=open("data.txt","a")
	f.writelines("\nAdidas shorts added to cart.\n")
	f.close()

def rev1():
	tkMessageBox.showinfo("Done", "Review Submitted")
	f=open("review1.txt","a")
	n=s1.get()
	for i in range(len(n),20):
		n=n+" "
	f.writelines(n+"\n")
	f.close()

def rev2():
	tkMessageBox.showinfo("Done", "Review Submitted")
	f=open("review2.txt","a")
	e=s2.get()
	for i in range(len(e),20):
		e=e+" "
	f.writelines(e+"\n")
	f.close()

def rev3():
	tkMessageBox.showinfo("Done", "Review Submitted")
	f=open("review3.txt","a")
	g=s3.get()
	for i in range(len(g),20):
		g=g+" "
	f.writelines(g+"\n")
	f.close()

	
def price1():
	tkMessageBox.showinfo("Done", "Price is Rs.2030")

def price2():
	tkMessageBox.showinfo("Done", "Price is Rs.3999")

def price3():
	tkMessageBox.showinfo("Done", "Price is Rs.1995")

def details1():
	tkMessageBox.showinfo("Details", "Size of Product is Small.\n Material is Cotton.")

def details2():
	tkMessageBox.showinfo("Details", "Size of Product is Medium.\n Material is Cotton.")

def details3():
	tkMessageBox.showinfo("Details", "Size of Product is Large.\n Material is Cotton.")


b.config(text="Start ", command=destroy)
b.pack()

f2=Frame()
f2.config(background="blue")
f3=Frame()
f3.config(background="purple")
f4=Frame()
f4.config(background="green")
f5=Frame()
f5.config(background="pink")
f6=Frame()
f6.config(background="orange")

text2=Text(f2)
text2.pack(side=TOP)
text2.insert(END, "Dressberry Red Top")
URL="file:///home/ishita/Downloads/c"
link=urllib.urlopen(URL)
raw_data=link.read()
link.close()
next=base64.encodestring(raw_data)
image1=PhotoImage(data=next)
label3=Label(f2,image=image1)
label3.config(width=400, height=400)
label3.pack()
text2.config(width=30, height=5, state="disabled")


b2=Button(f2)
b2.pack(side=TOP)
b2.config(text="Next Product", command=good1)

b3=Button(f2)
b3.pack(side=TOP)
b3.config(text="Add to cart", command=cart1)


b4=Button(f2)
b4.pack()
b4.config(text="Show Price", command=price1)

b4=Button(f2)
b4.pack()
b4.config(text="Show Details", command=details1)


label3=Label(f2,text="Write Reviews:")
label3.pack(side=LEFT)


s1=StringVar()
text5=Text(f2)
text5=Entry(f2, textvariable=s1 , width=30)
text5.pack(side=TOP)


b12=Button(f2)
b12.pack(side=BOTTOM)
b12.config(text="SUBMIT", command=rev1)


text3=Text(f3)
text3.pack()
text3.insert(END,"Black Kazo Pants")
URL="file:///home/ishita/Downloads/b"
link=urllib.urlopen(URL)
raw_data=link.read()
link.close()
next=base64.encodestring(raw_data)
image2=PhotoImage(data=next)
label3=Label(f3,image=image2)
label3.config(width=400, height=400)
label3.pack()
text3.config(width=30, height=3, state="disabled")

b5=Button(f3)
b5.pack()
b5.config(text="Next Product", command=good2)

"""b5=Button(f3)
b5.pack()
b5.config(text="Previous Product", command=prev1)"""

b6=Button(f3)
b6.pack()
b6.config(text="Add to Cart", command=cart2)

b7=Button(f3)
b7.pack()
b7.config(text="Show Price", command=price2)

b4=Button(f3)
b4.pack()
b4.config(text="Show Details", command=details2)

label4=Label(f3,text="Write Reviews:")
label4.pack(side=LEFT)



s2=StringVar()
text6=Text(f3)
text6.pack(side=TOP)
text6=Entry(f3,  textvariable=s2,width=10)

b13=Button(f3)
b13.pack(side=BOTTOM)
b13.config(text="SUBMIT", command=rev2)



text4=Text(f4)
text4.pack()
text4.insert(END, "Blue Adidas Shorts")
URL="file:///home/ishita/Desktop/s.gif"
link=urllib.urlopen(URL)
raw_data=link.read()
link.close()
next1=base64.encodestring(raw_data)
image3=PhotoImage(data=next1)
label3=Label(f4,image=image3)
label3.config(width=400, height=400)
label3.pack()
text4.config(width=30, height=5, state="disabled")

b9=Button(f4)
b9.pack()
b9.config(text="Next Product", command=good3)

b10=Button(f4)
b10.pack()
b10.config(text="Add to cart", command=cart3) 

b11=Button(f4)
b11.pack()
b11.config(text="Show Price", command=price3)

b4=Button(f4)
b4.pack()
b4.config(text="Show Details", command=details3)

label5=Label(f4,text="Write Reviews:")
label5.pack(side=LEFT)

s3=StringVar()
text7=Text(f4)
text7.pack(side=TOP)
text7=Entry(f4, textvariable=s3, width=30)

b14=Button(f4)
b14.pack(side=BOTTOM)
b14.config(text="SUBMIT", command= rev3)

text5=Text(f5)
text5.pack(side=TOP)
text5.insert(END, "You have viewed all the products.Thank you for viewing.")
text5.config(width=70, height=5, state="disabled")

b12=Button(root, text='Quit', command=root.quit).pack(side=BOTTOM)
URL="file:///home/ishita/Desktop/t.gif"
link=urllib.urlopen(URL)
raw_data=link.read()
link.close()
next1=base64.encodestring(raw_data)
image23=PhotoImage(data=next1)
label3=Label(f5,image=image23)
label3.config(width=700, height=700)
label3.pack()

label1=Label(f5)
label1.pack()
root.mainloop()
