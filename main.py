from tkinter import *
from math import *
root = Tk()
root.title('简易计算器')
root.geometry('350x770')
root.resizable(width=False,height=False)
l = Label(root, text="简易计算器", bg="white",fg='black',font=("Arabic", 20), width=400, height=3)
l.pack(side=TOP)
result = StringVar()
result.set('0')
result2 = StringVar()
result2.set('')
label = Label(root,font = ('微软雅黑',20),bg = '#EEE9E9',bd = '9',fg = '#828282',textvariable = result2)
label.place(x=0,y=80,width = 350,height = 200)
label2 = Label(root,font = ('微软雅黑',35),bg ='#EEE9E9',bd = '9',fg = 'black',textvariable = result)
label2.place(x=0,y=200,width = 400,height =150)
#按钮功能设置
def buttonClick(btn):
    content = result2.get()
    a=''
    if btn in '()e%123+456-789*.0/,':
        content += btn
    elif btn in '←':
        content =content[:-1]
    elif btn == 'π':
        content += 'pi'
    elif btn == 'sin':
        content += 'sin('
    elif btn == 'cos':
        content += 'cos('
    elif btn == 'AC':
        content = ''
    elif btn == '^2':
        content += '**2'
    elif btn == 'log':
        content +='log('
    elif btn == '√':
        content +='sqrt('
    elif btn == '=':
        a = '='+str(eval(content))
    result2.set(content)
    result.set(a[:15])
#16个符号
number =['AC','(',')','e','←','^2','√','sin','cos','%','1','2','3','+','log','4','5','6','-',',','7','8','9','*','','.','0','π','/','']
index = 0
for row in range(6):
    for col in range(5):
        num = number[index]
        index+=1
        btnDight = Button(root,text=num,font = ('微软雅黑',20),fg = ('black'),command=lambda x=num:buttonClick(x))
        btnDight.place(x=col*70,y=350+row*70,width=70,height=70)
# 等号美化
btnDight = Button(root,text='=',font = ('微软雅黑',40),fg = ('black'),bg=('gold'),command=lambda x='=':buttonClick(x))
btnDight.place(x=280,y=330+300,width=70,height=140)
# AC美化
btn = Button(root,text='AC',font = ('微软雅黑',20),fg = ('Black'),bg=('red'),command=lambda x='AC':buttonClick(x))
btn.place(x=0,y=350,width=70,height=70)

root.mainloop()
