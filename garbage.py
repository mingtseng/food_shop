# Из Shop, заменено на попроще
def get_good(self):
    try:
        Shop.good = []
        sql = 'SELECT * FROM good'
        conn = get_conn()
        c = conn.cursor()
        c.execute(sql)
        rows = c.fetchall()
        conn.close()
        rows = [list(a) for a in rows]
        for row in rows:
            new_good = Good(*row)
            Shop.good.append(new_good)
    except Error as e:
        Shop.message = e


def get_country(self):
    try:
        Shop.country = []
        sql = 'SELECT * FROM country'
        conn = get_conn()
        c = conn.cursor()
        c.execute(sql)
        rows = c.fetchall()
        conn.close()
        rows = [list(a) for a in rows]
        for row in rows:
            new_country = Country(*row)
            Shop.country.append(new_country)
    except Error as e:
        Shop.message = e

    # ===========================

    @staticmethod
    def get_class(_from):
        try:
            sql = 'SELECT * FROM {}'.format(_from)
            conn = get_conn()
            c = conn.cursor()
            c.execute(sql)
            rows = c.fetchall()
            conn.close()
            rows = [list(a) for a in rows]
            return rows
        except Exception as error:
            Shop.message = str(error)
            # ============================


# class Country:
#     def __init__(self, country_id, name):
#         self.country_id = country_id
#         self.name = name
#
#     def __str__(self):
#         country_out = '{}'.format(self.name)
#         return country_out
#
#
# def test_conn():
#     try:
#         conn = get_conn()
#         if conn:
#             Shop.message = 'Подключение успешно'
#             conn.close()
#     except Exception as error:
#         Shop.message = str(error)

# ===============================================
root = Tk()
root.title('2C: Магазин \"{}\"'.format(shop.name))
root.geometry('850x460')
root.resizable(width=False, height=False)

bottom_frame = Frame(root)
bottom_frame.pack(side=BOTTOM, fill=X)

main_frame = Frame(root, bg='gray', bd=2)
main_frame.pack(side=TOP, fill=Y)

statusbar = Label(bottom_frame, relief=SUNKEN, border=1, anchor=W)
statusbar['text'] = Shop.message
statusbar.pack(side=BOTTOM, fill=X)

root.mainloop()
