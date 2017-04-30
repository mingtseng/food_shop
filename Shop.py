import MySQLdb
from MySQLdb import Error
import Settings.Config as Settings


def get_conn():
    conn = MySQLdb.connect(host=Settings.host,
                           user=Settings.user,
                           passwd=Settings.passwd,
                           db=Settings.db,
                           charset=Settings.charset)
    return conn


class Shop:
    good = []
    distributor = []
    good_type = []
    d_country = {}
    d_distributor = {}
    d_good_type = {}
    message = ''

    def __init__(self, name):
        self.name = name
        if get_conn():
            Shop.message = 'Подключнение успешно'

    @staticmethod
    def get_id(_dict, value):
        for k, v in _dict.items():
            if v == value:
                return k

    @staticmethod
    def _get_entity(entity):
        try:
            _dict = {}
            sql = 'SELECT * FROM {}'.format(entity)
            conn = get_conn()
            c = conn.cursor()
            c.execute(sql)
            rows = c.fetchall()
            conn.close()
            rows = [list(a) for a in rows]
            for row in rows:
                _dict[row[0]] = row[1]
            return _dict
        except Exception as error:
            Shop.message = str(error)

    @staticmethod
    def _update_class_storage():
        try:
            conn = get_conn()
            c = conn.cursor()

            c.execute('select * from good')
            Shop.good = [Good(*row) for row in c.fetchall()]

            c.execute('select * from distributor')
            Shop.distributor = [Distributor(*row) for row in c.fetchall()]

            c.execute('select * from good_type')
            Shop.good_type = [GoodType(*row) for row in c.fetchall()]

            conn.close()
        except Exception as error:
            Shop.message = str(error)

    def update_shop(self):
        # Update dicts
        # TODO.0 !Вызывать после каждого изменения, удаления и добавления!
        Shop.d_country = {}
        Shop.d_distributor = {}
        Shop.d_good_type = {}
        Shop.d_country = self._get_entity('country')
        Shop.d_distributor = self._get_entity('distributor')
        Shop.d_good_type = self._get_entity('good_type')

        # Update class-object storage
        self._update_class_storage()

    def __str__(self):
        return self.name

    def authorize(self, login, passw):
        try:
            sql = 'SELECT role FROM user WHERE login = %s and passw = %s'
            args = (login, passw)
            conn = get_conn()
            c = conn.cursor()
            c.execute(sql, args)
            _role = c.fetchone()
            conn.close()
            return _role[0] if _role else _role
        except Exception as error:
            Shop.message = str(error)


class Good:
    def __init__(self, good_id, good_type, name, price, exp_date, country, distributor):
        self.good_id = good_id
        self.good_type = good_type
        self.name = name
        self.price = price
        self.exp_date = exp_date
        self.country = country
        self.distributor = distributor

    def save(self):
        try:
            sql = 'INSERT INTO good (good_type, name, price, exp_date, country, distributor) ' \
                  'VALUES (%s, %s, %s, %s, %s, %s)'
            args = (self.good_type,
                    self.name,
                    self.price,
                    self.exp_date,
                    self.country,
                    self.distributor)
            conn = get_conn()
            c = conn.cursor()
            c.execute(sql, args)
            conn.commit()
            conn.close()
        except Exception as error:
            Shop.message = str(error)

    def delete(self):
        try:
            sql = 'DELETE FROM good WHERE good_id=%s'
            args = (self.good_id,)
            conn = get_conn()
            c = conn.cursor()
            c.execute(sql, args)
            conn.commit()
            conn.close()
        except Exception as error:
            Shop.message = str(error)

    def update(self, name, price, exp_date):
        try:
            sql = 'UPDATE good SET name=%s, price=%s, exp_date=%s WHERE good_id=%s'
            args = (name, price, exp_date, self.good_id)
            conn = get_conn()
            c = conn.cursor()
            c.execute(sql, args)
            conn.commit()
            conn.close()
        except Exception as error:
            Shop.message = str(error)

    def __str__(self):
        good_out = '{!s:<16}{!s:^12}{!s:<14}{!s:16}{!s:18}{!s:<14}'.format(self.name,
                                                                           self.price,
                                                                           self.exp_date,
                                                                           Shop.d_country[self.country],
                                                                           Shop.d_distributor[self.distributor],
                                                                           Shop.d_good_type[self.good_type])
        return good_out


class Distributor:
    def __init__(self, distributor_id, name):
        self.distributor_id = distributor_id
        self.name = name

    def save(self):
        try:
            sql = 'INSERT INTO distributor (name) VALUES (%s)'
            args = (self.name,)
            conn = get_conn()
            c = conn.cursor()
            c.execute(sql, args)
            conn.commit()
            conn.close()
        except Exception as error:
            Shop.message = str(error)

    def delete(self):
        try:
            sql = 'DELETE FROM distributor WHERE distributor_id=%s'
            args = (self.distributor_id,)
            conn = get_conn()
            c = conn.cursor()
            c.execute(sql, args)
            conn.commit()
            conn.close()
        except Exception as error:
            Shop.message = str(error)

    def __str__(self):
        distributors_out = '{!s:}'.format(self.name)
        return distributors_out

    def update(self, name):
        try:
            sql = 'UPDATE distributor SET name=%s WHERE distributor_id=%s'
            args = (name, self.distributor_id)
            conn = get_conn()
            c = conn.cursor()
            c.execute(sql, args)
            conn.commit()
            conn.close()
        except Exception as error:
            Shop.message = str(error)


class GoodType:
    def __init__(self, good_type_id, name):
        self.good_type_id = good_type_id
        self.name = name

    def save(self):
        try:
            sql = 'INSERT INTO good_type (name) VALUES (%s)'
            args = (self.name,)
            conn = get_conn()
            c = conn.cursor()
            c.execute(sql, args)
            conn.commit()
            conn.close()
        except Exception as error:
            Shop.message = str(error)

    def delete(self):
        try:
            sql = 'DELETE FROM good_type WHERE good_type_id=%s'
            args = (self.good_type_id,)
            conn = get_conn()
            c = conn.cursor()
            c.execute(sql, args)
            conn.commit()
            conn.close()
        except Exception as error:
            Shop.message = str(error)

    def __str__(self):
        good_type_out = '{}'.format(self.name)
        return good_type_out

    def update(self, name):
        try:
            sql = 'UPDATE good_type SET name=%s WHERE good_type_id=%s'
            args = (name, self.good_type_id)
            conn = get_conn()
            c = conn.cursor()
            c.execute(sql, args)
            conn.commit()
            conn.close()
        except Exception as error:
            Shop.message = str(error)


# shop1 = Shop('Магазин')
#
# Shop.update_shop(shop1)
#
# # new_good = Good(0, 3, 'брюква', 65.50, '2018-10-10', 3, 5)
# # print(new_good)
# # new_good.save()
# # print('status: ', Shop.message if Shop.message else '...done')
# # for good in Shop.good:
# #     print(good)
# print('status: ', Shop.message if Shop.message else '...done')
# # Shop.update_shop(shop1)
# print('\nТОВАРЫ:')
# for good in Shop.good:
#     print(good)
# print('\nПОСТАВЩИКИ:')
# for distributor in Shop.distributor:
#     print(distributor)
# print('\nТИПЫ ТОВАРОВ:')
# for good_type in Shop.good_type:
#     print(good_type)
# print('status: ', Shop.message if Shop.message else '...done')
if __name__ == '__main__':
    shop1 = Shop('Магазин')
    Shop.update_shop(shop1)
    role = Shop.authorize(shop1, 'user1', '123qw1')
    if role:
        print('role is {}'.format(role))
    else:
        print('Critical function error...')
