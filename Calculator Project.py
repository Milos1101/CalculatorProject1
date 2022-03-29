import unicodedata
import math
from tkinter import *

root = Tk()
f = Frame(root)
f.pack(side=TOP, anchor=NW)


def calculator():
    frame1 = Frame(root)
    frame2 = Frame(root)
    frame3 = Frame(root)
    frame4 = Frame(root)
    frame1.pack(side=TOP)
    frame2.pack(side=TOP)
    frame3.pack(side=TOP)
    frame4.pack(side=TOP)

    label = Label(frame1, text='Calculator Prototype!')
    label.grid(row=0)
    label2 = Label(frame1, text='Square roots, cube roots, sin, cos, tan, and factorial')
    label2.grid(row=1)
    label3 = Label(frame1, text='are only accepted in the first entry')
    label3.grid(row=2)
    label.config(fg='WHITE', bg='BLACK')
    label2.config(fg='WHITE', bg='BLACK')
    label3.config(fg='WHITE', bg='BLACK')

    def shut_down():
        return root.destroy()

    def get_sum():
        a = e.get()
        s = list(a.split())
        a1 = e1.get()
        s1 = list(a1.split())
        if a == 'pi':
            sum0 = math.pi + float(s1[0])
            print('Result = ', sum0)
            print('-------------------------')

        elif a == 'e':
            sum0 = math.e + float(s1[0])
            print('Result = ', sum0)
            print('-------------------------')

        elif a1 == 'e':
            sum0 = math.e + float(s[0])
            print('Result = ', sum0)
            print('-------------------------')

        elif a1 == 'pi':
            sum0 = math.pi + float(s[0])
            print('Result = ', sum0)
            print('-------------------------')
        else:
            try:
                sum0 = float(s[0]) + float(s1[0])
                print('Result = ', sum0)
                print('-------------------------')
            except ValueError:
                print("Invalid entry")

    def get_subtraction():
        a = e.get()
        s = list(a.split())
        a1 = e1.get()
        s1 = list(a1.split())
        if a == 'pi':
            sub0 = math.pi - float(s1[0])
            print('Result = ', sub0)
            print('-------------------------')

        elif a == 'e':
            sub0 = math.e - float(s1[0])
            print('Result = ', sub0)
            print('-------------------------')

        elif a1 == 'e':
            sub0 = math.e - float(s[0])
            print('Result = ', sub0)
            print('-------------------------')

        elif a1 == 'pi':
            sub0 = math.pi - float(s[0])
            print('Result = ', sub0)
            print('-------------------------')

        else:
            try:
                sub0 = float(s[0]) - float(s1[0])
                print('Result = ', sub0)
                print('-------------------------')
            except ValueError:
                print("Invalid entry")

    def get_multiplication():
        a = e.get()
        s = list(a.split())
        a1 = e1.get()
        s1 = list(a1.split())
        if a == 'pi':
            mul0 = math.pi * float(s1[0])
            print('Result = ', mul0)
            print('-------------------------')

        elif a == 'e':
            mul0 = math.e * float(s1[0])
            print('Result = ', mul0)
            print('-------------------------')

        elif a1 == 'e':
            mul0 = math.e * float(s[0])
            print('Result = ', mul0)
            print('-------------------------')

        elif a1 == 'pi':
            mul0 = math.pi * float(s[0])
            print('Result = ', mul0)
            print('-------------------------')

        else:
            try:
                mul0 = float(s[0]) * float(s1[0])
                print('Result = ', mul0)
                print('-------------------------')
            except ValueError:
                print("Invalid entry")

    def get_division():
        a = e.get()
        s = list(a.split())
        a1 = e1.get()
        s1 = list(a1.split())
        if a == 'pi':
            div0 = math.pi / float(s1[0])
            print('Result = ', div0)
            print('-------------------------')

        elif a == 'e':
            div0 = math.e / float(s1[0])
            print('Result = ', div0)
            print('-------------------------')

        elif a1 == 'e':
            div0 = math.e / float(s[0])
            print('Result = ', div0)
            print('-------------------------')

        elif a1 == 'pi':
            div0 = math.pi / float(s[0])
            print('Result = ', div0)
            print('-------------------------')

        else:
            try:
                div0 = float(s[0]) / float(s1[0])
                print('Result = ', div0)
                print('-------------------------')
            except ValueError:
                print("Invalid entry")

    def get_square_root():
        a = e.get()
        s = list(a.split())
        if a == 'pi':
            sqrt = math.sqrt(math.pi)
            print('Result = ', sqrt)
            print('-------------------------')

        elif a == 'e':
            sqrt = math.sqrt(math.e)
            print('Result = ', sqrt)
            print('-------------------------')
        else:
            try:
                sqrt = math.sqrt(float(s[0]))
                print("Result = ", sqrt)
                print('-------------------------')
            except ValueError:
                print("Invalid entry")

    def get_cube_root():
        a = e.get()
        s = list(a.split())
        if a == 'pi':
            cbrt = (math.pi) ** (1 / 3)
            print('Result = ', cbrt)
            print('-------------------------')

        elif a == 'e':
            cbrt = (math.e) ** (1 / 3)
            print('Result = ', cbrt)
            print('-------------------------')
        else:
            try:
                cbrt = (float(s[0])) ** (1 / 3)
                print("Result = ", cbrt)
                print('-------------------------')
            except ValueError:
                print("Invalid entry")

    def get_sin():
        a = e.get()
        s = list(a.split())
        if a == 'pi':
            sin = math.sin(math.pi)
            print('Result = ', sin)
            print('-------------------------')

        elif a == 'e':
            sin = math.sin(math.e)
            print('Result = ', sin)
            print('-------------------------')
        else:
            try:
                sin = math.sin(float(s[0]))
                print("Result = ", sin)
                print('-------------------------')
            except ValueError:
                print("Invalid entry")

    def get_cos():
        a = e.get()
        s = list(a.split())
        if a == 'pi':
            cos = math.cos(math.pi)
            print('Result = ', sin)
            print('-------------------------')

        elif a == 'e':
            cos = math.cos(math.e)
            print('Result = ', cos)
            print('-------------------------')
        else:
            try:
                cos = math.cos(float(s[0]))
                print("Result = ", cos)
                print('-------------------------')
            except ValueError:
                print("Invalid entry")

    def get_tan():
        a = e.get()
        s = list(a.split())
        if a == 'pi':
            tan = math.tan(math.pi)
            print('Result = ', tan)
            print('-------------------------')

        elif a == 'e':
            tan = math.tan(math.e)
            print('Result = ', tan)
            print('-------------------------')
        else:
            try:
                tan = math.tan(float(s[0]))
                print("Result = ", tan)
                print('-------------------------')
            except ValueError:
                print("Invalid entry")

    def get_factorial():
        a = e.get()
        s = list(a.split())
        if a == 'pi':
            n = int(math.pi)
            f = 1
            for i in range(1, n + 1):
                f = f * i

            print("The factorial is = ", f)
            print('-------------------------')
        elif a == 'e':
            n = int(math.e)
            f = 1
            for i in range(1, n + 1):
                f = f * i

            print("The factorial is = ", f)
            print('-------------------------')
        else:
            try:
                n = int(s[0])
                f = 1
                for i in range(1, n + 1):
                    f = f * i

                print("The factorial is = ", f)
                print('-------------------------')
            except ValueError:
                print("Invalid entry")

    def get_pi():
        print(unicodedata.lookup("GREEK SMALL LETTER PI"), '=', math.pi)
        print('-------------------------')

    def get_euler():
        print('e = ', math.e)
        print('-------------------------')

    label1 = Label(frame2, text='Enter number:')
    label1.grid(row=0, column=0, sticky=W, pady=1)

    label2 = Label(frame2, text='Enter number:')
    label2.grid(row=1, column=0, sticky=W, pady=1)

    e = Entry(frame2)
    e.grid(row=0, column=1, sticky=W, pady=1)

    e1 = Entry(frame2, text='Enter number:')
    e1.grid(row=1, column=1, sticky=W, pady=1)

    button2 = Button(frame3, text='+', command=get_sum)
    button2.grid(row=0, column=0, sticky=W, pady=1)

    button3 = Button(frame3, text='-', command=get_subtraction)
    button3.grid(row=0, column=1, sticky=W, pady=1)

    button4 = Button(frame3, text='x', command=get_multiplication)
    button4.grid(row=0, column=2, sticky=W, pady=1)

    button5 = Button(frame3, text='/', command=get_division)
    button5.grid(row=0, column=3, sticky=W, pady=1)

    button6 = Button(frame3, text='Sqrt', command=get_square_root)
    button6.grid(row=0, column=4, sticky=W, pady=1)

    button7 = Button(frame3, text='CubeRt', command=get_cube_root)
    button7.grid(row=0, column=5, sticky=W, pady=1)

    button8 = Button(frame3, text='sin', command=get_sin)
    button8.grid(row=0, column=6, sticky=W, pady=1)

    button9 = Button(frame3, text='cos', command=get_cos)
    button9.grid(row=0, column=7, sticky=W, pady=1)

    button10 = Button(frame3, text='tan', command=get_tan)
    button10.grid(row=0, column=8, sticky=W, pady=1)

    button11 = Button(frame3, text='!', command=get_factorial)
    button11.grid(row=0, column=9, sticky=W, pady=1)

    button12 = Button(frame3, text=unicodedata.lookup("GREEK SMALL LETTER PI"), command=get_pi)
    button12.grid(row=0, column=10, sticky=W, pady=1)

    button13 = Button(frame3, text='e', command=get_euler)
    button13.grid(row=0, column=11, sticky=W, pady=1)

    button14 = Button(frame4, text='Close', command=shut_down)
    button14.grid()


if __name__ == "__main__":

    def get_login():

        username = E1.get()
        password = E2.get()

        if username == 'admin' and password == 'admin':

            print("You are logged in!")
            print("Welcome back boss\U0001F60E")
            calculator()

        else:
            print("Invalid username or password")


    L1 = Label(f, text='Username: ')
    L1.grid(row=0)

    L2 = Label(f, text='Password: ')
    L2.grid(row=1)

    E1 = Entry(f)
    E1.grid(row=0, column=1)

    E2 = Entry(f)
    E2.grid(row=1, column=1)

    B1 = Button(f, text="Login", command=get_login)
    B1.grid(row=2, sticky='NW')

    B2 = Button(f, text='Close', command=root.destroy)
    B2.grid(row=2, column=5, sticky='NW')

root.mainloop()
