import tkinter
from tkinter import *
import Shop


# метод для авторизации пользователей

# Отрисовка фреймов
def draw_frame(root):
    out_frame = Frame(root, bd=1, relief=SUNKEN)
    left_frame_good = Frame(root, bd=1, relief=SUNKEN)
    left_frame_distributor = Frame(root, bd=1, relief=SUNKEN)
    left_frame_service = Frame(root, bd=1, relief=SUNKEN)
    status_bar_frame = Frame(root, bd=1, relief=SUNKEN)
    time_frame = Frame(root, bd=1, relief=SUNKEN)

    out_frame.place(x=201, y=0, width=848, height=577)
    left_frame_good.place(x=0, y=0, width=200, height=210)
    left_frame_distributor.place(x=0, y=211, width=200, height=210)
    left_frame_service.place(x=0, y=421, width=200, height=151)
    status_bar_frame.place(x=0, y=578, width=950, height=22)
    time_frame.place(x=951, y=578, width=100, height=22)
    return out_frame, left_frame_good, left_frame_distributor, left_frame_service, status_bar_frame, time_frame


# Отрисовка меню
def draw_menu(root, role_state):
    def the_end():
        root.destroy()
        root.quit()

    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Сохранить базу в файл")
    filemenu.add_command(label="Сохранить вывод в файл")
    filemenu.add_separator()
    filemenu.add_command(label="Выход", command=the_end)
    menubar.add_cascade(label="Файл", menu=filemenu)

    viewmenu = Menu(menubar, tearoff=0)
    viewmenu.add_command(label="Показать товары")
    viewmenu.add_command(label="Показать поставщиков")
    viewmenu.add_separator()
    viewmenu.add_command(label="Показать пользователей", state=role_state)
    menubar.add_cascade(label="Просмотр", menu=viewmenu)

    addmenu = Menu(menubar, tearoff=0)
    addmenu.add_command(label="Добавить товар")
    addmenu.add_command(label="Добавить поставщика")
    addmenu.add_separator()
    addmenu.add_command(label="Добавить пользователя")
    menubar.add_cascade(label="Добавить", menu=addmenu, state=role_state)

    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label="Редактировать товар")
    editmenu.add_command(label="Редактировать поставщика")
    editmenu.add_separator()
    editmenu.add_command(label="Редактировать пользователя")
    menubar.add_cascade(label="Правка", menu=editmenu, state=role_state)

    delmenu = Menu(menubar, tearoff=0)
    delmenu.add_command(label="Удалить товар")
    delmenu.add_command(label="Удалить поставщика")
    delmenu.add_separator()
    delmenu.add_command(label="Удалить пользователя?")
    menubar.add_cascade(label="Удалить", menu=delmenu, state=role_state)

    root.config(menu=menubar)
    return filemenu, viewmenu, addmenu, editmenu, delmenu


# Отрисовка подписей
def create_label(root, *frame):
    good_label = Label(frame[0], text='Товары', font='Verdana 10 bold')
    good_label.pack(side=TOP)
    distr_label = Label(frame[1], text='Поставщики', font='Verdana 10 bold')
    distr_label.pack(side=TOP)
    service_label = Label(frame[2], text='Служебные', font='Verdana 10 bold')
    service_label.pack(side=TOP)


# Рисование кнопок.
def create_good_btn(root, frame, role_state):
    prn_good = Button(frame, font='Verdana 10', text='Вывести товары', width=48, height=2)
    add_good = Button(frame, font='Verdana 10', text='Добавить товар', width=48, height=2, state=role_state)
    edt_good = Button(frame, font='Verdana 10', text='Редактировать товар', width=48, height=2, state=role_state)
    del_good = Button(frame, font='Verdana 10', text='Изменить товар', width=48, height=2, state=role_state)
    prn_good.pack(side=TOP, padx=(2, 2), pady=(4, 0))
    add_good.pack(side=TOP, padx=(2, 2), pady=(2, 0))
    edt_good.pack(side=TOP, padx=(2, 2), pady=(2, 0))
    del_good.pack(side=TOP, padx=(2, 2), pady=(2, 0))
    return prn_good, add_good, edt_good, del_good


def create_distr_btn(root, frame, role_state):
    prn_distr = Button(frame, font='Verdana 10', text='Показать поставщиков', width=48, height=2)
    add_distr = Button(frame, font='Verdana 10', text='Добавить поставщика', width=48, height=2, state=role_state)
    edt_distr = Button(frame, font='Verdana 10', text='Редактировать подставщика', width=48, height=2, state=role_state)
    del_distr = Button(frame, font='Verdana 10', text='Изменить поставщика', width=48, height=2, state=role_state)
    prn_distr.pack(side=TOP, padx=(2, 2), pady=(4, 0))
    add_distr.pack(side=TOP, padx=(2, 2), pady=(2, 0))
    edt_distr.pack(side=TOP, padx=(2, 2), pady=(2, 0))
    del_distr.pack(side=TOP, padx=(2, 2), pady=(2, 0))
    return prn_distr, add_distr, edt_distr, del_distr


def create_user_btn(root, frame, role_state):
    prn_user = Button(frame, font='Verdana 10', text='Показать пользователей', width=48, height=2, state=role_state)
    add_user = Button(frame, font='Verdana 10', text='Добавить пользователя', width=48, height=2, state=role_state)
    prn_user.pack(side=TOP, padx=(2, 2), pady=(4, 0))
    add_user.pack(side=TOP, padx=(2, 2), pady=(2, 0))
    return prn_user, add_user
