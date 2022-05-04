import mysql.connector
import telebot
from random import randrange
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="polina"
)

mycursor = mydb.cursor()

movies1 = """CREATE TABLE comedies (
   id integer NOT NULL,
   full_name varchar(50),
   link varchar(500)
   );"""
mycursor.execute(movies1)
mydb.commit()

sql = "INSERT INTO comedies (id, full_name, link) VALUES (%s, %s, %s)"
values1 = (1, "Один дома", "https://www.kinopoisk.ru/film/8124/")
values2 = (2, "Джентельмены удачи", "https://www.kinopoisk.ru/film/44386/")
values3 = (3, "Маска", "https://www.kinopoisk.ru/film/6039/")
values4 = (4, "Мальчишник в Вегасе", "https://www.kinopoisk.ru/film/426004/")
mycursor.execute(sql, values1)
mycursor.execute(sql, values2)
mycursor.execute(sql, values3)
mycursor.execute(sql, values4)
mydb.commit()

movies2 = """CREATE TABLE dramas (
   id integer NOT NULL,
   full_name varchar(50),
   link varchar(500)
   );"""
mycursor.execute(movies2)
mydb.commit()

sql = "INSERT INTO dramas (id, full_name, link) VALUES (%s, %s, %s)"
values1 = (1, "1+1", "https://www.kinopoisk.ru/film/535341/")
values2 = (2, "Побег из Шоушенка", "https://www.kinopoisk.ru/film/326/")
values3 = (3, "Достучаться до небес", "https://www.kinopoisk.ru/film/32898/")
values4 = (4, "Дневник памяти", "https://www.kinopoisk.ru/film/3561/")
mycursor.execute(sql, values1)
mycursor.execute(sql, values2)
mycursor.execute(sql, values3)
mycursor.execute(sql, values4)
mydb.commit()

movies3 = """CREATE TABLE horrors (
   id integer NOT NULL,
   full_name varchar(50),
   link varchar(500)
   );"""
mycursor.execute(movies3)
mydb.commit()

sql = "INSERT INTO horrors (id, full_name, link) VALUES (%s, %s, %s)"
values1 = (1, "Поезд в Пусан", "https://www.kinopoisk.ru/film/977288/")
values2 = (2, "Другие", "https://www.kinopoisk.ru/film/494/")
values3 = (3, "Сайлент Хилл", "https://www.kinopoisk.ru/film/78871/")
values4 = (4, "Оно", "https://www.kinopoisk.ru/film/453397/")
mycursor.execute(sql, values1)
mycursor.execute(sql, values2)
mycursor.execute(sql, values3)
mycursor.execute(sql, values4)
mydb.commit()

movies4 = """CREATE TABLE cartoons (
   id integer NOT NULL,
   full_name varchar(50),
   link varchar(500)
   );"""
mycursor.execute(movies4)
mydb.commit()

sql = "INSERT INTO cartoons (id, full_name, link) VALUES (%s, %s, %s)"
values1 = (1, "Зверополис", "https://www.kinopoisk.ru/film/775276/")
values2 = (2, "Король Лев", "https://www.kinopoisk.ru/film/2360/")
values3 = (3, "Шрэк", "https://www.kinopoisk.ru/film/430/")
values4 = (4, "Тайна Коко", "https://www.kinopoisk.ru/film/679486/")
mycursor.execute(sql, values1)
mycursor.execute(sql, values2)
mycursor.execute(sql, values3)
mycursor.execute(sql, values4)
mydb.commit()

movies5 = """CREATE TABLE actions (
   id integer NOT NULL,
   full_name varchar(50),
   link varchar(500)
   );"""
mycursor.execute(movies5)
mydb.commit()

sql = "INSERT INTO actions (id, full_name, link) VALUES (%s, %s, %s)"
values1 = (1, "Гнев человеческий", "https://www.kinopoisk.ru/film/1318972/")
values2 = (2, "Леон", "https://www.kinopoisk.ru/film/389/")
values3 = (3, "Kingsman", "https://www.kinopoisk.ru/film/749540/")
values4 = (4, "Бэтмен", "https://www.kinopoisk.ru/film/47237/")
mycursor.execute(sql, values1)
mycursor.execute(sql, values2)
mycursor.execute(sql, values3)
mycursor.execute(sql, values4)
mydb.commit()
