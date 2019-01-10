from tkinter import *
from math import *
e = 2.71828
root = Tk()
root.title('计算器2.0')
root.geometry('320x650')
root.resizable(width=False,height=False)
l = Label(root, text="欢迎使用计算器2.0", bg="white", font=("Arabic", 20), width=400, height=3)
l.pack(side=TOP)
result = StringVar()
result.set('0')
result2 = StringVar()
result2.set('')
label = Label(root,font = ('微软雅黑',20),bg = '#EEE9E9',bd = '9',fg = '#828282',textvariable = result2)
label.place(x=0,y=80,width = 320,height = 220)
label2 = Label(root,font = ('微软雅黑',35),bg ='#EEE9E9',bd = '9',fg = 'black',textvariable = result)
label2.place(x=0,y=200,width = 400,height =100)
#按钮功能设置
def buttonClick(btn):
    content = result2.get()
    a=''
    b=''
    if btn in '0123456789.+-*/()'+'**':
        content += btn
    elif btn in '←':
        content =content[:-1]
    elif btn == 'AC':
        content = ''
    elif btn == '=':
        a = '='+str(eval(content))
    elif btn == 'cos':
        a = str(cos(eval(content)))[:8]
        content = ''
    elif btn == 'sin':
        a = str(sin(eval(content)))[:8]
        content = ''
    elif btn == 'e':
        content += str(e)
    elif btn == '!':
        a = factorial(eval(content))
        content = ''
    result2.set(content)
    result.set(a)
#16个符号
number =['1','2','3','+','4','5','6','-','7','8','9','*','!','cos','sin','e','.','0','','/']
index = 0
for row in range(5):
    for col in range(4):
        num = number[index]
        index+=1
        btnDight = Button(root,text=num,font = ('微软雅黑',20),fg = ('#4F4F4F'),command=lambda x=num:buttonClick(x))
        btnDight.place(x=col*80,y=350+row*60,width=80,height=60)
#等号美化      
btnDight = Button(root,text='=',font = ('微软雅黑',40),fg = ('orange'),command=lambda x='=':buttonClick(x))
btnDight.place(x=160,y=280+250+60,width=80,height=60)
#AC美化
btn = Button(root,text='AC',font = ('微软雅黑',20),fg = ('red'),command=lambda x='AC':buttonClick(x))
btn.place(x=0,y=290,width=80,height=60)     
#4个符号
opearaters=['(',')','←']
index=0
for col in range(3):
    opt = opearaters[index]
    btn = Button(root,text=opt,font = ('微软雅黑',20),fg = ('#4F4F4F'),command=lambda x=opt:buttonClick(x))
    btn.place(x=80+80*index,y=290,width=80,height=60)
    index += 1
root.mainloop()
