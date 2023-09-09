from tkinter import *
from tkinter import messagebox
import mysql.connector
from PIL import ImageTk, Image
import random
import ordered_set
from ordered_set import OrderedSet

con = mysql.connector.connect(user = 'root', password = 'Flyguy2003', host= 'localhost', database = 'hangman')
mycursor = con.cursor()

lotion = 1100
image0 = 23
image1= 67
lbl1 = 123
lbl2 = 4333

#defining login screen

def login():
    window = Tk()   
    window.title('Hangman')
    window.geometry('230x230')
    window.iconbitmap(r'C:\Users\scxrp\Downloads\projects\python\Hanging Man\Hangman.ico') 
    window.configure(background = 'black')

    Label(window, text = 'HANGMAN', bg = 'black', fg = 'white', font = 'verdana 20 bold').pack()
    Label(window, text = 'Login', bg = 'black', fg = 'white', font = 'verdana 16 bold').pack()
    Label(window, text = 'username: ', bg = 'black', fg = 'white', font = 'verdana 12').pack()
    username = Entry(window, width = 20, bg = 'white')
    username.pack()
    Label(window, text = 'password: ', bg = 'black', fg = 'white', font = 'verdana 12').pack()
    password = Entry(window, width = 20, bg = 'white', show = '*')
    password.pack()

    def click0():    #defining what to do when the button is pressed
        entered_username = username.get()
        entered_password = password.get()
        print("Username: %s\nPassword: %s" % (username.get(), password.get()))
    
        inserting = """insert into loginfo(Username, Password) values(%s, %s)"""
        details = [(entered_username, entered_password)]

        mycursor.execute('drop table if exists loginfo')
        mycursor.execute('create table loginfo (Username varchar(100) primary key, Password varchar(100))')
        mycursor.executemany(inserting, details)
        con.commit()

    def quit0():    #defining closure of one window and opening of the other
            window.destroy()

    Button(window, text = 'Submit', width = 6, command = click0).pack()
    Button(window, text = 'Next', width = 4, command = quit0).pack()

    window.mainloop()   #keeps the window open unlike turtle
    
login()

home=Tk()
home.title("Hangman")
home.geometry("1920x1080+0+0")
home.configure(background = 'black')
image0=ImageTk.PhotoImage(Image.open(r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\titlehang.png").resize((1920, 1080), Image.ANTIALIAS))
image1=ImageTk.PhotoImage(Image.open(r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\wlcm.png").resize((1920, 1080), Image.ANTIALIAS))
Frame_slider=Frame(home)
Frame_slider.place(x=150, y=50,width=1350)
lbl1=Label(home,image= image0, borderwidth = 0)
lbl1.place(x=0,y=0)
lbl2=Label(home,image= image1, borderwidth = 0)
lbl2.place(x=1100,y=0)

def slider_func():
      global lotion, image0, image1, lbl1, lbl2
      lotion-=3
      lbl1.config(image=image1)
      lbl2.config(image=image0)
      lbl2.place(x=lotion, y=0)
      lbl2.after(1, slider_func)
      
slider_func()

def polo():
      home.destroy()
           
img5 = ImageTk.PhotoImage(Image.open(r'C:\Users\scxrp\Downloads\projects\python\Hanging Man\Button Sprites\play.png'))
panel3 = Button(home, image = img5, command = polo, borderwidth = 0)
panel3.place(x = 680, y = 400)

img6 = ImageTk.PhotoImage(Image.open(r'C:\Users\scxrp\Downloads\projects\python\Hanging Man\finish line.png'))
panel2 = Label(home, image = img6, borderwidth = 0)
panel2.place(x = 500, y = 10)

home.mainloop()

#defining hangman window
    
hangman = Tk()
hangman.title('Hangman')
hangman.iconbitmap(r'C:\Users\scxrp\Downloads\projects\python\Hanging Man\Hangman.ico')
hangman.geometry('1920x1080')
hangman.configure(background = 'black')
                                                                                               
img = Image.open(r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\0.png")
img.resize((586, 624), Image.ANTIALIAS)
img1 = ImageTk.PhotoImage(img)
panel = Label(hangman, image = img1, bg = 'black')
panel.place(x = 0, y = 175)

def photoshoot():
    photo1 = r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\1.png"
    photo2 = r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\2.png"
    photo3 = r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\3.png"
    photo4 = r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\4.png"
    photo5 = r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\5%%.png"
    photo6 = r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\6%%.png"
    photo7 = r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\7%%.png"
    photo8 = r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\8%%.png"
    photo9 = r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\9%%.png"
    photo10 = r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\10%%%.png"

    if guesses == 1:
            img = Image.open(photo1)
            img.resize((586, 624), Image.ANTIALIAS)
            img1 = ImageTk.PhotoImage(img)
            panel = Label(hangman, image = img1, bg = 'black')
            panel.ngc = img1
            panel.place(x = 0, y = 175)
    elif guesses == 2:
            img = Image.open(photo2)
            img.resize((586, 624), Image.ANTIALIAS)
            img1 = ImageTk.PhotoImage(img)
            panel = Label(hangman, image = img1, bg = 'black')
            panel.ngc = img1
            panel.place(x = 0, y = 175)
    elif guesses == 3:
            img = Image.open(photo3)
            img.resize((586, 624), Image.ANTIALIAS)
            img1 = ImageTk.PhotoImage(img)
            panel = Label(hangman, image = img1, bg = 'black')
            panel.ngc = img1
            panel.place(x = 0, y = 175)
    elif guesses == 4:
            img = Image.open(photo4)
            img.resize((586, 624), Image.ANTIALIAS)
            img1 = ImageTk.PhotoImage(img)
            panel = Label(hangman, image = img1, bg = 'black')
            panel.ngc = img1
            panel.place(x = 0, y = 175)
    elif guesses == 5:
            img = Image.open(photo5)
            img.resize((586, 624), Image.ANTIALIAS)
            img1 = ImageTk.PhotoImage(img)
            panel = Label(hangman, image = img1, bg = 'black')
            panel.ngc = img1
            panel.place(x = 0, y = 175)
    elif guesses == 6:
            img = Image.open(photo6)
            img.resize((586, 624), Image.ANTIALIAS)
            img1 = ImageTk.PhotoImage(img)
            panel = Label(hangman, image = img1, bg = 'black')
            panel.ngc = img1
            panel.place(x = 0, y = 175)
    elif guesses == 7:
            img = Image.open(photo7)
            img.resize((586, 624), Image.ANTIALIAS)
            img1 = ImageTk.PhotoImage(img)
            panel = Label(hangman, image = img1, bg = 'black')
            panel.ngc = img1
            panel.place(x = 0, y = 175)
    elif guesses == 8:
            img = Image.open(photo8)
            img.resize((586, 624), Image.ANTIALIAS)
            img1 = ImageTk.PhotoImage(img)
            panel = Label(hangman, image = img1, bg = 'black')
            panel.ngc = img1
            panel.place(x = 0, y = 175)
    elif guesses == 9:
            img = Image.open(photo9)
            img.resize((586, 624), Image.ANTIALIAS)
            img1 = ImageTk.PhotoImage(img)
            panel = Label(hangman, image = img1, bg = 'black')
            panel.ngc = img1
            panel.place(x = 0, y = 175)
    elif guesses == 10:
            img = Image.open(photo10)
            img.resize((586, 624), Image.ANTIALIAS)
            img1 = ImageTk.PhotoImage(img)
            panel = Label(hangman, image = img1, bg = 'black')
            panel.ngc = img1
            panel.place(x = 0, y = 175)

    #creating the number of textboxes as letters in the word

list_of_topics = ['animals','food','plants','countries','teachers']
topic = random.choice(list_of_topics)
query = 'select %s from lotion' % topic
mycursor.execute(query)
fetcha = mycursor.fetchall()
zumba = str(fetcha[random.randint(0,9)])
zumba = zumba.lstrip("',() ")   # "("',hotdog,)""
zumba = zumba.rstrip("',() ")

Label(hangman, text = 'Topic:', bg = 'black', fg = 'blue', font = 'verdana 28 underline').place(x = 1225, y = 303)
Label(hangman, text = topic, bg = 'black', fg = 'blue', font = 'verdana 20').place(x = 1230, y = 350)

jolly = []
for i in range(len(zumba)):
   jolly.append(zumba[i])
foogle = len(jolly)

guesses = 0
guessed = []
    
appears = []
entryboxes = []

while foogle < 10 and foogle > 3:
    if foogle == 4:
        appears1 = StringVar() 
        entrybox1 = Entry(hangman, state = 'readonly', textvariable = appears1, width = 2, font = 'verdana 30 bold')
        entrybox1.place(x = 737.5, y = 100)
        appears.insert(0, appears1)
        entryboxes.insert(0, entrybox1)
        
        appears2 = StringVar()
        entrybox2 = Entry(hangman, state = 'readonly', textvariable = appears2, width = 2, font = 'verdana 30 bold')
        entrybox2.place(x = 817.5, y = 100)
        appears.insert(1, appears2)
        entryboxes.insert(1, entrybox2)

        appears3 = StringVar()
        entrybox3 = Entry(hangman, state = 'readonly', textvariable = appears3, width = 2, font = 'verdana 30 bold')
        entrybox3.place(x = 897.5, y = 100)
        appears.insert(2, appears3)
        entryboxes.insert(2, entrybox3)
        
        appears4 = StringVar()
        entrybox4 = Entry(hangman, state = 'readonly', textvariable = appears4, width = 2, font = 'verdana 30 bold')
        entrybox4.place(x = 977.5, y = 100)
        appears.insert(3, appears4)
        entryboxes.insert(3, entrybox4)

        wordb = ['','','','']
        foogle = 0
    
    elif foogle == 5:
        appears1 = StringVar()
        entrybox1 = Entry(hangman, state = 'readonly', textvariable = appears1, width = 2, font = 'verdana 30 bold')
        entrybox1.place(x = 697.5, y = 100)
        appears.insert(0, appears1)
        entryboxes.insert(0, entrybox1)
        
        appears2 = StringVar()
        entrybox2 = Entry(hangman, state = 'readonly', textvariable = appears2, width = 2, font = 'verdana 30 bold')
        entrybox2.place(x = 777.5, y = 100)
        appears.insert(1, appears2)
        entryboxes.insert(1, entrybox2)

        appears3 = StringVar()
        entrybox3 = Entry(hangman, state = 'readonly', textvariable = appears3, width = 2, font = 'verdana 30 bold')
        entrybox3.place(x = 857.5, y = 100)
        appears.insert(2, appears3)
        entryboxes.insert(2, entrybox3)
        
        appears4 = StringVar()
        entrybox4 = Entry(hangman, state = 'readonly', textvariable = appears4, width = 2, font = 'verdana 30 bold')
        entrybox4.place(x = 937.5, y = 100)
        appears.insert(3, appears4)
        entryboxes.insert(3, entrybox4)
        
        appears5 = StringVar()
        entrybox5 = Entry(hangman, state = 'readonly', textvariable = appears5, width = 2, font = 'verdana 30 bold')
        entrybox5.place(x = 1017.5, y = 100)
        appears.insert(4, appears5)
        entryboxes.insert(4, entrybox5)

        wordb = ['','','','','']
        foogle = 0
            
    elif foogle == 6:
        appears1 = StringVar()
        entrybox1 = Entry(hangman, state = 'readonly', textvariable = appears1, width = 2, font = 'verdana 30 bold')
        entrybox1.place(x = 657.5, y = 100)
        appears.insert(0, appears1)
        entryboxes.insert(0, entrybox1)
        
        appears2 = StringVar()
        entrybox2 = Entry(hangman, state = 'readonly', textvariable = appears2, width = 2, font = 'verdana 30 bold')
        entrybox2.place(x = 737.5, y = 100)
        appears.insert(1, appears2)
        entryboxes.insert(1, entrybox2)

        appears3 = StringVar()
        entrybox3 = Entry(hangman, state = 'readonly', textvariable = appears3, width = 2, font = 'verdana 30 bold')
        entrybox3.place(x = 817.5, y = 100)
        appears.insert(2, appears3)
        entryboxes.insert(2, entrybox3)
        
        appears4 = StringVar()
        entrybox4 = Entry(hangman, state = 'readonly', textvariable = appears4, width = 2, font = 'verdana 30 bold')
        entrybox4.place(x = 897.5, y = 100)
        appears.insert(3, appears4)
        entryboxes.insert(3, entrybox4)
        
        appears5 = StringVar()
        entrybox5 = Entry(hangman, state = 'readonly', textvariable = appears5, width = 2, font = 'verdana 30 bold')
        entrybox5.place(x = 977.5, y = 100)
        appears.insert(4, appears5)
        entryboxes.insert(4, entrybox5)

        appears6 = StringVar()
        entrybox6 = Entry(hangman, state = 'readonly', textvariable = appears6, width = 2, font = 'verdana 30 bold')
        entrybox6.place(x = 1057.5, y = 100)
        appears.insert(5, appears6)
        entryboxes.insert(5, entrybox6)

        wordb = ['','','','','','']
        foogle = 0
            
    elif foogle == 7:
        appears1 = StringVar()
        entrybox1 = Entry(hangman, state = 'readonly', textvariable = appears1, width = 2, font = 'verdana 30 bold')
        entrybox1.place(x = 617.5, y = 100)
        appears.insert(0, appears1)
        entryboxes.insert(0, entrybox1)
        
        appears2 = StringVar()
        entrybox2 = Entry(hangman, state = 'readonly', textvariable = appears2, width = 2, font = 'verdana 30 bold')
        entrybox2.place(x = 697.5, y = 100)
        appears.insert(1, appears2)
        entryboxes.insert(1, entrybox2)

        appears3 = StringVar()
        entrybox3 = Entry(hangman, state = 'readonly', textvariable = appears3, width = 2, font = 'verdana 30 bold')
        entrybox3.place(x = 777.5, y = 100)
        appears.insert(2, appears3)
        entryboxes.insert(2, entrybox3)
        
        appears4 = StringVar()
        entrybox4 = Entry(hangman, state = 'readonly', textvariable = appears4, width = 2, font = 'verdana 30 bold')
        entrybox4.place(x = 857.5, y = 100)
        appears.insert(3, appears4)
        entryboxes.insert(3, entrybox4)
        
        appears5 = StringVar()
        entrybox5 = Entry(hangman, state = 'readonly', textvariable = appears5, width = 2, font = 'verdana 30 bold')
        entrybox5.place(x = 937.5, y = 100)
        appears.insert(4, appears5)
        entryboxes.insert(4, entrybox5)

        appears6 = StringVar()
        entrybox6 = Entry(hangman, state = 'readonly', textvariable = appears6, width = 2, font = 'verdana 30 bold')
        entrybox6.place(x = 1017.5, y = 100)
        appears.insert(5, appears6)
        entryboxes.insert(5, entrybox6)

        appears7 = StringVar()
        entrybox7 = Entry(hangman, state = 'readonly', textvariable = appears7, width = 2, font = 'verdana 30 bold')
        entrybox7.place(x = 1097.5, y = 100)
        appears.insert(6, appears7)
        entryboxes.insert(6, entrybox7)

        wordb = ['','','','','','','']
        foogle = 0
            
    elif foogle == 8:
        appears1 = StringVar()
        entrybox1 = Entry(hangman, state = 'readonly', textvariable = appears1, width = 2, font = 'verdana 30 bold')
        entrybox1.place(x = 577.5, y = 100)
        appears.insert(0, appears1)
        entryboxes.insert(0, entrybox1)
        
        appears2 = StringVar()
        entrybox2 = Entry(hangman, state = 'readonly', textvariable = appears2, width = 2, font = 'verdana 30 bold')
        entrybox2.place(x = 657.5, y = 100)
        appears.insert(1, appears2)
        entryboxes.insert(1, entrybox2)

        appears3 = StringVar()
        entrybox3 = Entry(hangman, state = 'readonly', textvariable = appears3, width = 2, font = 'verdana 30 bold')
        entrybox3.place(x = 737.5, y = 100)
        appears.insert(2, appears3)
        entryboxes.insert(2, entrybox3)
        
        appears4 = StringVar()
        entrybox4 = Entry(hangman, state = 'readonly', textvariable = appears4, width = 2, font = 'verdana 30 bold')
        entrybox4.place(x = 817.5, y = 100)
        appears.insert(3, appears4)
        entryboxes.insert(3, entrybox4)
        
        appears5 = StringVar()
        entrybox5 = Entry(hangman, state = 'readonly', textvariable = appears5, width = 2, font = 'verdana 30 bold')
        entrybox5.place(x = 897.5, y = 100)
        appears.insert(4, appears5)
        entryboxes.insert(4, entrybox5)

        appears6 = StringVar()
        entrybox6 = Entry(hangman, state = 'readonly', textvariable = appears6, width = 2, font = 'verdana 30 bold')
        entrybox6.place(x = 977.5, y = 100)
        appears.insert(5, appears6)
        entryboxes.insert(5, entrybox6)

        appears7 = StringVar()
        entrybox7 = Entry(hangman, state = 'readonly', textvariable = appears7, width = 2, font = 'verdana 30 bold')
        entrybox7.place(x = 1057.5, y = 100)
        appears.insert(6, appears7)
        entryboxes.insert(6, entrybox7)

        appears8 = StringVar()
        entrybox8 = Entry(hangman, state = 'readonly', textvariable = appears8, width = 2, font = 'verdana 30 bold')
        entrybox8.place(x = 1137.5, y = 100)
        appears.insert(7, appears8)
        entryboxes.insert(7, entrybox8)

        wordb = ['','','','','','','','']
        foogle = 0
            
    elif foogle == 9:
        appears1 = StringVar()
        entrybox1 = Entry(hangman, state = 'readonly', textvariable = appears1, width = 2, font = 'verdana 30 bold')
        entrybox1.place(x = 537.5, y = 100)
        appears.insert(0, appears1)
        entryboxes.insert(0, entrybox1)
        
        appears2 = StringVar()
        entrybox2 = Entry(hangman, state = 'readonly', textvariable = appears2, width = 2, font = 'verdana 30 bold')
        entrybox2.place(x = 617.5, y = 100)
        appears.insert(1, appears2)
        entryboxes.insert(1, entrybox2)

        appears3 = StringVar()
        entrybox3 = Entry(hangman, state = 'readonly', textvariable = appears3, width = 2, font = 'verdana 30 bold')
        entrybox3.place(x = 697.5, y = 100)
        appears.insert(2, appears3)
        entryboxes.insert(2, entrybox3)
        
        appears4 = StringVar()
        entrybox4 = Entry(hangman, state = 'readonly', textvariable = appears4, width = 2, font = 'verdana 30 bold')
        entrybox4.place(x = 777.5, y = 100)
        appears.insert(3, appears4)
        entryboxes.insert(3, entrybox4)
        
        appears5 = StringVar()
        entrybox5 = Entry(hangman, state = 'readonly', textvariable = appears5, width = 2, font = 'verdana 30 bold')
        entrybox5.place(x = 857.5, y = 100)
        appears.insert(4, appears5)
        entryboxes.insert(4, entrybox5)

        appears6 = StringVar()
        entrybox6 = Entry(hangman, state = 'readonly', textvariable = appears6, width = 2, font = 'verdana 30 bold')
        entrybox6.place(x = 937.5, y = 100)
        appears.insert(5, appears6)
        entryboxes.insert(5, entrybox6)

        appears7 = StringVar()
        entrybox7 = Entry(hangman, state = 'readonly', textvariable = appears7, width = 2, font = 'verdana 30 bold')
        entrybox7.place(x = 1017.5, y = 100)
        appears.insert(6, appears7)
        entryboxes.insert(6, entrybox7)

        appears8 = StringVar()
        entrybox8 = Entry(hangman, state = 'readonly', textvariable = appears8, width = 2, font = 'verdana 30 bold')
        entrybox8.place(x = 1097.5, y = 100)
        appears.insert(7, appears8)
        entryboxes.insert(7, entrybox8)
            
        appears9 = StringVar()
        entrybox9 = Entry(hangman, state = 'readonly', textvariable = appears9, width = 2, font = 'verdana 30 bold')
        entrybox9.place(x = 1177.5, y = 100)
        appears.insert(8, appears9)
        entryboxes.insert(8, entrybox9)

        wordb = ['','','','','','','','','']
        foogle = 0
#==================================================================================================================
qp = ImageTk.PhotoImage(Image.open(r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\Button Sprites\q1.png"))
q = Button(hangman, image = qp, command = lambda : press('Q'))
q.place(x = 684, y = 580)
wp = ImageTk.PhotoImage(Image.open(r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\Button Sprites\w1.png"))
w = Button(hangman, image = wp, command = lambda : press('W'))
w.place(x = 739, y = 580)
ep = ImageTk.PhotoImage(Image.open(r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\Button Sprites\e1.png"))
e = Button(hangman, image = ep, command = lambda : press('E'))
e.place(x = 794, y = 580)
rp = ImageTk.PhotoImage(Image.open(r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\Button Sprites\r1.png"))
r = Button(hangman, image = rp, command = lambda : press('R'))
r.place(x = 849, y = 580)
tp = ImageTk.PhotoImage(Image.open(r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\Button Sprites\t1.png"))
t = Button(hangman, image = tp, command = lambda : press('T'))
t.place(x = 904, y = 580)
yp = ImageTk.PhotoImage(Image.open(r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\Button Sprites\y1.png"))
y = Button(hangman, image = yp, command = lambda : press('Y'))
y.place(x = 959, y = 580)
up = ImageTk.PhotoImage(Image.open(r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\Button Sprites\u1.png"))
u = Button(hangman, image = up, command = lambda : press('U'))
u.place(x = 1014, y = 580)
ip = ImageTk.PhotoImage(Image.open(r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\Button Sprites\i1.png"))
i = Button(hangman, image = ip, command = lambda : press('I'))
i.place(x = 1069, y = 580)
op = ImageTk.PhotoImage(Image.open(r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\Button Sprites\o1.png"))
o = Button(hangman, image = op, command = lambda : press('O'))
o.place(x = 1124, y = 580)
pp = ImageTk.PhotoImage(Image.open(r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\Button Sprites\p1.png"))
p = Button(hangman, image = pp, command = lambda : press('P'))
p.place(x = 1179, y = 580)
ap = ImageTk.PhotoImage(Image.open(r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\Button Sprites\a1.png"))
a = Button(hangman, image = ap, command = lambda : press('A'))
a. place(x = 714, y = 635)
sp = ImageTk.PhotoImage(Image.open(r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\Button Sprites\s1.png"))
s = Button(hangman, image = sp, command = lambda : press('S'))
s. place(x = 769, y = 635)
dp = ImageTk.PhotoImage(Image.open(r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\Button Sprites\d1.png"))
d = Button(hangman, image = dp, command = lambda : press('D'))
d.place(x = 824, y = 635)
fp = ImageTk.PhotoImage(Image.open(r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\Button Sprites\f1.png"))
f = Button(hangman, image = fp, command = lambda : press('F'))
f.place(x = 879, y = 635)
gp = ImageTk.PhotoImage(Image.open(r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\Button Sprites\g1.png"))
g = Button(hangman, image = gp, command = lambda : press('G'))
g.place(x = 934, y = 635)
hp = ImageTk.PhotoImage(Image.open(r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\Button Sprites\h1.png"))
h = Button(hangman, image = hp, command = lambda : press('H'))
h.place(x = 989, y = 635)
jp = ImageTk.PhotoImage(Image.open(r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\Button Sprites\j1.png"))
j = Button(hangman, image = jp, command = lambda : press('J'))
j.place(x = 1044, y = 635)
kp = ImageTk.PhotoImage(Image.open(r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\Button Sprites\k1.png"))
k = Button(hangman, image = kp, command = lambda : press('K'))
k.place(x = 1099, y = 635)
lp = ImageTk.PhotoImage(Image.open(r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\Button Sprites\l1.png"))
l = Button(hangman, image = lp, command = lambda : press('L'))
l.place(x = 1154, y = 635)
zp = ImageTk.PhotoImage(Image.open(r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\Button Sprites\z1.png"))
z = Button(hangman, image = zp, command = lambda : press('Z'))
z.place(x = 744, y = 690)
xp = ImageTk.PhotoImage(Image.open(r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\Button Sprites\x1.png"))
x = Button(hangman, image = xp, command = lambda : press('X'))
x.place(x = 799, y = 690)
cp = ImageTk.PhotoImage(Image.open(r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\Button Sprites\c1.png"))
c = Button(hangman, image = cp, command = lambda : press('C'))
c.place(x = 854, y = 690)
vp = ImageTk.PhotoImage(Image.open(r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\Button Sprites\v1.png"))
v = Button(hangman, image = vp, command = lambda : press('V'))
v.place(x = 909, y = 690)
bp = ImageTk.PhotoImage(Image.open(r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\Button Sprites\b1.png"))
b = Button(hangman, image = bp, command = lambda : press('B'))
b.place(x = 964, y = 690)
np = ImageTk.PhotoImage(Image.open(r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\Button Sprites\n1.png"))
n = Button(hangman, image = np, command = lambda : press('N'))
n.place(x = 1019, y = 690)
mp = ImageTk.PhotoImage(Image.open(r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\Button Sprites\m1.png"))
m = Button(hangman, image = mp, command = lambda : press('M'))
m.place(x = 1074, y = 690)
    
#==================================================================================================================
def press(guess):
    global guesses, guessed, ap, bp, cp, dp, ep, fp, gp, hp, ip, jp, kp, lp, mp, np, op, pp, qp, rp, sp, tp, up, vp, wp, xp, yp, zp, buttonsp, buttonspr, buttonspw, buttons, appears

    buttons = {'Q': q, 'W': w, 'E': e, 'R': r, 'T': t, 'Y': y, 'U': u, 'I': i, 'O': o, 'P': p,
                    'A': a, 'S': s, 'D': d, 'F': f, 'G': g, 'H': h, 'J': j, 'K': k, 'L': l,
                    'Z': z, 'X': x, 'C': c, 'V': v, 'B': b, 'N': n, 'M': m}

    buttonsp = {'Q': qp, 'W': wp, 'E': ep, 'R': rp, 'T': tp, 'Y': yp, 'U': up, 'I': ip, 'O': op, 'P': pp,
                    'A': ap, 'S': sp, 'D': dp, 'F': fp, 'G': gp, 'H': hp, 'J': jp, 'K': kp, 'L': lp,
                    'Z': zp, 'X': xp, 'C': cp, 'V': vp, 'B': bp, 'N': np, 'M': mp}
        
    buttonspr = {'Q': ImageTk.PhotoImage(Image.open(r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\Button Sprites\qr.png")), 'W': ImageTk.PhotoImage(Image.open(r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\Button Sprites\wr.png")), 'E': ImageTk.PhotoImage(Image.open(r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\Button Sprites\er.png")), 'R': ImageTk.PhotoImage(Image.open(r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\Button Sprites\rr.png")),
                    'T': ImageTk.PhotoImage(Image.open(r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\Button Sprites\tr.png")), 'Y': ImageTk.PhotoImage(Image.open(r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\Button Sprites\yr.png")), 'U': ImageTk.PhotoImage(Image.open(r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\Button Sprites\ur.png")), 'I': ImageTk.PhotoImage(Image.open(r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\Button Sprites\ir.png")),
                    'O': ImageTk.PhotoImage(Image.open(r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\Button Sprites\or.png")), 'P': ImageTk.PhotoImage(Image.open(r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\Button Sprites\pr.png")), 'A': ImageTk.PhotoImage(Image.open(r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\Button Sprites\ar.png")), 'S': ImageTk.PhotoImage(Image.open(r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\Button Sprites\sr.png")),
                    'D': ImageTk.PhotoImage(Image.open(r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\Button Sprites\dr.png")), 'F': ImageTk.PhotoImage(Image.open(r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\Button Sprites\fr.png")), 'G': ImageTk.PhotoImage(Image.open(r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\Button Sprites\gr.png")), 'H': ImageTk.PhotoImage(Image.open(r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\Button Sprites\hr.png")),
                    'J': ImageTk.PhotoImage(Image.open(r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\Button Sprites\jr.png")), 'K': ImageTk.PhotoImage(Image.open(r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\Button Sprites\kr.png")), 'L': ImageTk.PhotoImage(Image.open(r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\Button Sprites\lr.png")), 'Z': ImageTk.PhotoImage(Image.open(r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\Button Sprites\zr.png")),
                    'X': ImageTk.PhotoImage(Image.open(r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\Button Sprites\xr.png")), 'C': ImageTk.PhotoImage(Image.open(r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\Button Sprites\cr.png")), 'V': ImageTk.PhotoImage(Image.open(r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\Button Sprites\vr.png")), 'B': ImageTk.PhotoImage(Image.open(r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\Button Sprites\br.png")),
                    'N': ImageTk.PhotoImage(Image.open(r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\Button Sprites\nr.png")), 'M': ImageTk.PhotoImage(Image.open(r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\Button Sprites\mr.png"))}

    buttonspw = {'Q': ImageTk.PhotoImage(Image.open(r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\Button Sprites\qw.png")), 'W': ImageTk.PhotoImage(Image.open(r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\Button Sprites\ww.png")), 'E': ImageTk.PhotoImage(Image.open(r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\Button Sprites\ew.png")), 'R': ImageTk.PhotoImage(Image.open(r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\Button Sprites\rw.png")),
                    'T': ImageTk.PhotoImage(Image.open(r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\Button Sprites\tw.png")), 'Y': ImageTk.PhotoImage(Image.open(r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\Button Sprites\yw.png")), 'U': ImageTk.PhotoImage(Image.open(r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\Button Sprites\uw.png")), 'I': ImageTk.PhotoImage(Image.open(r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\Button Sprites\iw.png")),
                    'O': ImageTk.PhotoImage(Image.open(r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\Button Sprites\ow.png")), 'P': ImageTk.PhotoImage(Image.open(r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\Button Sprites\pw.png")), 'A': ImageTk.PhotoImage(Image.open(r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\Button Sprites\aw.png")), 'S': ImageTk.PhotoImage(Image.open(r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\Button Sprites\sw.png")),
                    'D': ImageTk.PhotoImage(Image.open(r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\Button Sprites\dw.png")), 'F': ImageTk.PhotoImage(Image.open(r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\Button Sprites\fw.png")), 'G': ImageTk.PhotoImage(Image.open(r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\Button Sprites\gw.png")), 'H': ImageTk.PhotoImage(Image.open(r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\Button Sprites\hw.png")),
                    'J': ImageTk.PhotoImage(Image.open(r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\Button Sprites\jw.png")), 'K': ImageTk.PhotoImage(Image.open(r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\Button Sprites\kw.png")), 'L': ImageTk.PhotoImage(Image.open(r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\Button Sprites\lw.png")), 'Z': ImageTk.PhotoImage(Image.open(r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\Button Sprites\zw.png")),
                    'X': ImageTk.PhotoImage(Image.open(r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\Button Sprites\xw.png")), 'C': ImageTk.PhotoImage(Image.open(r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\Button Sprites\cw.png")), 'V': ImageTk.PhotoImage(Image.open(r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\Button Sprites\vw.png")), 'B': ImageTk.PhotoImage(Image.open(r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\Button Sprites\bw.png")),
                    'N': ImageTk.PhotoImage(Image.open(r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\Button Sprites\nw.png")), 'M': ImageTk.PhotoImage(Image.open(r"C:\Users\scxrp\Downloads\projects\python\Hanging Man\Button Sprites\mw.png"))}

    buttonsx = {'Q': 684, 'W': 739, 'E': 794, 'R': 849, 'T': 904, 'Y': 959, 'U': 1014, 'I': 1069, 'O': 1124, 'P': 1179,
                    'A': 714, 'S': 769, 'D': 824, 'F': 879, 'G': 934, 'H': 989, 'J': 1044, 'K': 1099, 'L': 1154,
                    'Z': 744, 'X': 799, 'C': 854, 'V': 909, 'B': 964, 'N': 1019, 'M': 1074}

    buttonsy = {'Q': 580, 'W': 580, 'E': 580, 'R': 580, 'T': 580, 'Y': 580, 'U': 580, 'I': 580, 'O': 580, 'P': 580,
                    'A': 635, 'S': 635, 'D': 635, 'F': 635, 'G': 635, 'H': 635, 'J': 635, 'K': 635, 'L': 635,
                    'Z': 690, 'X': 690, 'C': 690, 'V': 690, 'B': 690, 'N': 690, 'M': 690}

    if guess.casefold() in jolly:
        for ch in range(len(jolly)):
            if guess.casefold() == jolly[ch]:                                                   
                string1 = " "                                                                             
                string1+=guess                                                               
                appears[ch].set(string1)
                wordb[ch] = string1.lower().lstrip()

                buttons[guess].configure(state = DISABLED)
                buttonsp[guess] = buttonspr[guess]
                buttons[guess] = Button(hangman, image = buttonspr[guess])
                buttons[guess].ngc = buttonspr[guess]
                buttons[guess].place(x = buttonsx[guess], y = buttonsy[guess])
                
                if wordb == jolly:                              #win condition
                    win = Tk()   
                    win.title('Hangman')
                    win.iconbitmap(r'C:\Users\scxrp\Downloads\projects\python\Hanging Man\Hangman.ico')
                    win.configure(background = 'black')

                    def asdfquit():
                        win.destroy()
                        hangman.destroy()
                        
                    www = Label(win, text = 'You Win!', fg = 'green', bg = 'black', font = 'verdana 48 bold')
                    www.pack()
                    close = Button(win, text = 'Close', font = 'verdana 12 bold', command = asdfquit)
                    close.pack()
    else:
        guessed.append(guess)
        guessed = OrderedSet(guessed)
        guessed = list(guessed)
        guesses = len(guessed)

        buttons[guess].configure(state = DISABLED)
        buttonsp[guess] = buttonspw[guess]
        buttons[guess] = Button(hangman, image = buttonspw[guess])
        buttons[guess].ngc = buttonspw[guess]
        buttons[guess].place(x = buttonsx[guess], y = buttonsy[guess])

        photoshoot()

        if guesses == 10:                                       #lose condition
            lose = Tk()   
            lose.title('Hangman')
            lose.iconbitmap(r'C:\Users\scxrp\Downloads\projects\python\Hanging Man\Hangman.ico')
            lose.configure(background = 'black')

            def asdfquit():
                lose.destroy()
                hangman.destroy()
                    
            lll = Label(lose, text = 'You Lose!', fg = 'red', bg = 'black', font = 'verdana 48 bold')
            lll.pack()
            word = Label(lose, text = 'lmaoo idiot the word was %s' % zumba, fg = 'white', bg = 'black', font = 'verdana 36 bold')
            word.pack()
            close = Button(lose, text = 'Close', font = 'verdana 12 bold', command = asdfquit)
            close.pack()

hangman.mainloop()