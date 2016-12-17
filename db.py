from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Date, ForeignKey
import os


if os.path.exists("myDB.db"):
    os.remove("myDB.db")

engine = create_engine("sqlite:///myDB.db") # подключение к базе данных
metadata = MetaData()

user_table = Table('user', metadata,
               Column('id_user', Integer, primary_key=True, unique=True, nullable=False),
               Column('login_user', String, unique=True, nullable=False),
               Column('password', String, nullable=False),
               Column('name_user', String, unique=True, nullable=False),
               Column('email', String),
               Column('id_photo', Integer, ForeignKey('photo_table.id_photo'))
             )

news_table = Table('news', metadata,
               Column('id_news', Integer, ForeignKey('news_photo_table.id_news'), primary_key=True, unique=True, nullable=False),
               Column('text_news', String, nullable=False),
               Column('header_news', String, nullable=False)
             )

trends_table = Table('trends', metadata,
               Column('id_trend', Integer, ForeignKey('trends_photo_table.id_trend'), primary_key=True, unique=True, nullable=False),
               Column('name_trend', String, nullable=False),
               Column('text_trend', String, nullable=False),
               Column('season', String, nullable=False)
             )

fashion_shows_table = Table('fashion_shows', metadata,
               Column('id_show', Integer, ForeignKey('shows_photo_table.id_show'), primary_key=True, unique=True, nullable=False),
               Column('name_shows', String, nullable=False),
               Column('text_shows', String, nullable=False),
               Column('data', Date, nullable=False)
             )

photo_table = Table('photo', metadata,
               Column('id_photo', Integer, ForeignKey('news_photo_table.id_photo', 'trends_photo_table.id_photo', 'shows_photo_table.id_photo'),
               	primary_key=True, unique=True, nullable=False),
               Column('picture', String, nullable=False),
             )

news_photo_table = Table('news_photo', metadata,
               Column('id_news', Integer, ForeignKey('news_table.id_news'), nullable=False),
               Column('id_photo', Integer, ForeignKey('photo_table.id_photo'), nullable=False),
             )

trends_photo_table = Table('trends_photo', metadata,
               Column('id_trend', Integer, ForeignKey('trends_table.id_trend'), nullable=False),
               Column('id_photo', Integer, ForeignKey('photo_table.id_photo'), nullable=False),
             )

shows_photo_table = Table('shows_photo', metadata,
               Column('id_show', Integer, ForeignKey('fashion_shows_table.id_show'), nullable=False),
               Column('id_photo', Integer, ForeignKey('photo_table.id_photo'), nullable=False),
             )
