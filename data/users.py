import datetime
from dataclasses import dataclass
from enum import Enum


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone_number: str
    birth_year: int
    birth_month: int
    birth_day: int
    subjects: list
    hobbies: list
    picture: str
    current_address: str
    state: str
    city: str


class Hobbies(Enum):
    Sports = 'Sports'
    Reading = 'Reading'
    Music = 'Music'


date = datetime.date(1991, 8 - 1, 29)

cortny = User(first_name='Cortny',
              last_name='Love',
              email='CLU@mail.com',
              gender="Female",
              phone_number="3133265290",
              birth_year=date.year,
              birth_month=date.month,
              birth_day=date.day,
              subjects=['Maths'],
              hobbies=[Hobbies.Reading.value],
              picture="image.jpg",
              current_address="Javakhishvili St, 47, ap 39",
              state="NCR",
              city="Noida", )
