from Shop import Shop
from Shop import Good
from Shop import Distributor
from Shop import GoodType
import tkinter
from tkinter import *
from tkinter.ttk import Combobox as Combobox
import Utilities as Util
from datetime import datetime

header_prod = '{:<16}{:<12}{:<14}{:<16}{:<18}{:<14}\n'.format('Наименование',
                                                        'Цена(руб)',
                                                        'Годен до:',
                                                        'Страна',
                                                        'Поставщик',
                                                        'Тип товара')
separate_line = '-' * 90 + '\n'

shop = Shop('Лютик')
Shop.update_shop(shop)
root = Tk()
root.title('Авторизация')
root.geometry('220x100')
root.resizable(width=False, height=False)
login_label = Label(root, width=8, font='Verdana 10', text='Логин: ')
passwd_label = Label(root, width=8, font='Verdana 10', text='Пароль: ')
login_field = Entry(root, width=15, font='Verdana 10')
passwd_filed = Entry(root, width=15, font='Verdana 10', show='*')

login_label.grid(row=2, column=1, sticky=E, pady=(10, 0))
passwd_label.grid(row=3, column=1, sticky=E)
login_field.grid(row=2, column=2, padx=(1, 1))
passwd_filed.grid(row=3, column=2, padx=(1, 1))


def authorise():
    # TODO x = debug
    # _login = login_field.get()
    # _passw = passwd_filed.get()
    # if _login.isalnum() and _passw.isalnum():
    if True:
        # TODO x = debug
        # role = Shop.authorize(shop, _login, _passw)
        role = 1
        if role == 1:
            # вызов метода для отображения интерфейса администратора
            role_state = NORMAL
            start_main(role_state)
        else:
            if role == 2:
                # вызов метода для отображения интерфейса простого пользователя
                role_state = DISABLED
                start_main(role_state)
            else:
                # создание окна для отображения ошибки авторизации
                rooter = Tk()
                rooter.title('ОШИБКА')
                root.minsize(50, 35)
                out = Text(rooter, font='Verdana 10 bold', fg='red', width=40, height=5, bd=3)
                out.grid(row=1, column=1, padx=(1, 1))
                out.insert('0.0',
                           'Неверный логин или пароль. \n'
                           'Либо Вы не зарегистрированны в приложении.\n'
                           'Обратитесь к администратору')
                rooter.mainloop()
    else:
        rooter = Tk()
        rooter.title('ОШИБКА')
        root.minsize(50, 35)
        out = Text(rooter, font="Verdana 10 bold", fg='red', width=40, height=5, bd=3)
        out.grid(row=1, column=1, padx=(1, 1))
        out.insert('0.0', 'ОШИБКА!:\nНедопустимые символы в логине или пароле')
        rooter.mainloop()


auth_btn = Button(root, text='Авторизация', font='Verdana 10', width=24, height=1, command=authorise)
auth_btn.grid(row=4, column=1, columnspan=2, pady=(10, 10), padx=(10, 0))


def start_main(role_state):
    root.withdraw()
    root_main = Tk()
    root_main.title('2C: Магазин \"{}\"'.format(shop.name))
    root_main.geometry('1050x600')
    root_main.resizable(width=False, height=False)

    def update_status(text_message):
        statusbar['text'] = text_message if text_message else Shop.message
        statusbar.update()

    def print_good_func():
        output.delete('0.0', END)
        output.insert(1.0, header_prod)
        output.insert(2.0, separate_line)
        for _good in Shop.good:
            output.insert('3.0', str(_good) + '\n')
        update_status('Список товаров: {}'.format(len(Shop.good)))

    def add_good_func():
        child = Toplevel(root_main)
        child.title('Добавление товара')
        child.geometry('370x190')
        child.resizable(width=FALSE, height=FALSE)
        child.grab_set()
        child.focus_set()

        l1 = Label(child, text='Тип товара:', font='Verdana 10')
        l2 = Label(child, text='Наименование:', font='Verdana 10')
        l3 = Label(child, text='Цена:', font='Verdana 10')
        l4 = Label(child, text='Годен до (ХХХХ-ХХ-ХХ):', font='Verdana 10')
        l5 = Label(child, text='Страна:', font='Verdana 10')
        l6 = Label(child, text='Поставщик:', font='Verdana 10')
        l1.grid(row=1, column=1, padx=(10, 10), sticky=W)
        l2.grid(row=2, column=1, padx=(10, 10), sticky=W)
        l3.grid(row=3, column=1, padx=(10, 10), sticky=W)
        l4.grid(row=4, column=1, padx=(10, 10), sticky=W)
        l5.grid(row=5, column=1, padx=(10, 10), sticky=W)
        l6.grid(row=6, column=1, padx=(10, 10), sticky=W)

        good_type = Combobox(child, values=list(Shop.d_good_type.values()), width=19, height=3)
        good_type.set(Shop.d_good_type[list(Shop.d_good_type.keys())[0]])
        name = Entry(child, width=22)
        price = Entry(child, width=22)
        exp_date = Entry(child, width=22)
        country = Combobox(child, value=list(Shop.d_country.values()), width=19, height=5)
        country.set(Shop.d_country[list(Shop.d_country.keys())[0]])
        distributor = Combobox(child, value=list(Shop.d_distributor.values()), width=19, height=5)
        distributor.set(Shop.d_distributor[list(Shop.d_distributor.keys())[0]])

        good_type.grid(row=1, column=2, padx=(20, 10))
        name.grid(row=2, column=2, padx=(20, 10))
        price.grid(row=3, column=2, padx=(20, 10))
        exp_date.grid(row=4, column=2, padx=(20, 10))
        country.grid(row=5, column=2, padx=(20, 10))
        distributor.grid(row=6, column=2, padx=(20, 10))

        def add_btn():
            _good_type = good_type.get()
            _name = name.get()
            _price = price.get()
            _exp_date = exp_date.get()
            _country = country.get()
            _distributor = distributor.get()
            _good_type = Shop.get_id(Shop.d_good_type, _good_type)
            _country = Shop.get_id(Shop.d_country, _country)
            _distributor = Shop.get_id(Shop.d_distributor, _distributor)
            new_good = Good(0, _good_type, _name, _price, _exp_date, _country, _distributor)
            new_good.save()
            update_status('Товар добавлен')
            Shop.update_shop(shop)
            child.destroy()

        add_btn = Button(child, text='Добавить товар', command=add_btn)
        add_btn.grid(row=7, column=2, pady=(20, 20))
        root_main.wait_window(child)

    def edit_good_func():
        pass

    def delete_good_func():
        pass

    def print_distr_func():
        output.delete('0.0', END)
        output.insert(1.0, 'Наименование\n')
        output.insert(2.0, '---------------------\n')
        for _distr in Shop.distributor:
            output.insert('3.0', str(_distr) + '\n')
        update_status('Список поставщиков: {}'.format(len(Shop.distributor)))

    def add_distr_func():
        pass

    def edit_distr_func():
        pass

    def delete_distr_func():
        pass

    def print_user_func():
        pass

    def add_user_func():
        pass

    #  Frames list:
    #  out_frame, left_frame_good, left_frame_distributor, left_frame_service, status_bar_frame
    out_fr, lfg_fr, lfd_fr, lfs_fr, sb_fr, t_fr = Util.draw_frame(root_main)
    filemenu, viewmenu, addmenu, editmenu, delmenu = Util.draw_menu(root_main, role_state)
    # viewmenu.configure(command=print_good)

    Util.create_label(root_main, lfg_fr, lfd_fr, lfs_fr)

    output = Text(out_fr, bg='white', font='Consolas 11', width=500, height=500, wrap=WORD)
    scrollbar = Scrollbar(out_fr, command=output.yview)
    output.configure(yscrollcommand=scrollbar.set)

    scrollbar.pack(side=RIGHT, fill=Y)
    output.pack(fill=BOTH)

    statusbar = Label(sb_fr, relief=SUNKEN, border=0, anchor=W)
    statusbar['text'] = Shop.message
    statusbar.pack(side=BOTTOM, fill=X)

    dt = datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")
    time = Label(t_fr, border=0)
    time.configure(text=str(dt))

    prn_good, add_good, edt_good, del_good = Util.create_good_btn(root_main, lfg_fr, role_state)
    prn_good['command'] = print_good_func
    add_good['command'] = add_good_func
    edt_good['command'] = edit_good_func
    del_good['command'] = delete_good_func

    prn_distr, add_distr, edt_distr, del_distr = Util.create_distr_btn(root_main, lfd_fr, role_state)
    prn_distr['command'] = print_distr_func
    add_distr['command'] = add_distr_func
    edt_distr['command'] = edit_distr_func
    del_distr['command'] = delete_distr_func

    prn_user, add_user = Util.create_user_btn(root_main, lfs_fr, role_state)
    prn_user['command'] = print_user_func
    add_user['command'] = add_user_func


root.mainloop()
