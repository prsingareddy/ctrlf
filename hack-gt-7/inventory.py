import kivy
import pymysql

kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.image import Image as image
from kivy.lang import Builder
from kivy.config import Config
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from pyzbar.pyzbar import decode
from PIL import Image
from pprint import pprint

Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '750')

# connection to google cloud sql
connection = pymysql.connect(host='127.0.0.1',
                             port=1433,
                             user='root',
                             password='',
                             db='inventory')

cursor = connection.cursor()

filename = ''


# returns results from query from database
def return_query(query):
    cursor.execute(query)
    answer = cursor.fetchall()
    return answer


# decodes qr, returns string
def decode_qr(qr_fn):
    qr_decode = decode(Image.open(qr_fn))
    qr_str = str(list(qr_decode[0])[0])[2:-1]
    return qr_str


# takes qr, returns queried data from string from database
def str_query(qr_fn):
    qr_str = decode_qr(qr_fn)
    pprint(qr_str)
    query = f"SELECT * FROM items WHERE Category  LIKE '%{qr_str}%' LIMIT 5"
    result = return_query(query)
    return result


class ListScreen(App):
    def build(self):
        a = AnchorLayout(anchor_x='center', anchor_y='center')
        img = image(source="inventory.png")
        a.add_widget(img)

        result = str_query(filename)

        layout = GridLayout(cols=3, row_force_default=True, row_default_height=100, padding = [0, 100, 0, 300])

        label1 = Label(text=result[0][0])
        price1 = Label(text=str('{:.2f}'.format(result[0][1])))
        number1 = Label(text=str(result[0][3]))
        label1.bind(
            width=lambda *x: label1.setter('text_size')(label1, (label1.width, None)))

        label2 = Label(text=result[1][0])
        price2 = Label(text=str('{:.2f}'.format(result[1][1])))
        number2 = Label(text=str(result[1][3]))
        label2.bind(
            width=lambda *x: label2.setter('text_size')(label2, (label2.width, None)))

        label3 = Label(text=result[2][0])
        price3 = Label(text=str('{:.2f}'.format(result[2][1])))
        number3 = Label(text=str(result[2][3]))
        label3.bind(
            width=lambda *x: label3.setter('text_size')(label3, (label3.width, None)))

        label4 = Label(text=result[3][0])
        price4 = Label(text=str('{:.2f}'.format(result[3][1])))
        number4 = Label(text=str(result[3][3]))
        label4.bind(
            width=lambda *x: label4.setter('text_size')(label4, (label4.width, None)))

        label5 = Label(text=result[4][0])
        price5 = Label(text=str('{:.2f}'.format(result[4][1])))
        number5 = Label(text=str(result[4][3]))
        label5.bind(
            width=lambda *x: label5.setter('text_size')(label5, (label5.width, None)))

        layout.add_widget(label1)
        layout.add_widget(price1)
        layout.add_widget(number1)

        layout.add_widget(label2)
        layout.add_widget(price2)
        layout.add_widget(number2)

        layout.add_widget(label3)
        layout.add_widget(price3)
        layout.add_widget(number3)

        layout.add_widget(label4)
        layout.add_widget(price4)
        layout.add_widget(number4)

        layout.add_widget(label5)
        layout.add_widget(price5)
        layout.add_widget(number5)

        a.add_widget(layout)

        return a


if __name__ == '__main__':
    ListScreen().run()
