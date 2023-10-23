#!/usr/bin/python3
from sqlalchemy import MetaData, Integer, String, Column, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    bookss = relationship("Book")

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    copyright = Column(Integer, nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'))
    #Alternatively, we can use the backref parameters to specify the attribute name to be added on the other side of the relationship.
    # == bookss = relationship("Book", backref="book") ==> in Author

engine = create_engine("mysql+mysqldb://root:root@localhost/orm_test")
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

a = Author(first_name="john", last_name="doe")
b = Book(title="power", copyright=10, author_id=1)
session.add(a)
session.add(b)
session.commit()
print(Author.bookss)
# for i in session.query(Author).all():
#     print (i.last_name + " " + i.first_name)
session.close()









# from sqlalchemy import create_engine, MetaData, Table, Integer, String, \
#     Column, DateTime, ForeignKey, Numeric, SmallInteger

# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import relationship

# from datetime import datetime

# engine = create_engine("postgres+psycopg2://postgres:pass@localhost/sqlalchemy_tuts")

# Base = declarative_base()

# class Customer(Base):
#     __tablename__ = 'customers'
#     id = Column(Integer(), primary_key=True)
#     first_name = Column(String(100), nullable=False)
#     last_name = Column(String(100), nullable=False)
#     username = Column(String(50), nullable=False)
#     email = Column(String(200), nullable=False)
#     created_on = Column(DateTime(), default=datetime.now)
#     updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
#     orders = relationship("Order", backref='customer')


# class Item(Base):
#     __tablename__ = 'items'
#     id = Column(Integer(), primary_key=True)
#     name = Column(String(200), nullable=False)
#     cost_price =  Column(Numeric(10, 2), nullable=False)
#     selling_price = Column(Numeric(10, 2),  nullable=False)
# #     orders = relationship("Order", backref='customer')
    

# class Order(Base):
#     __tablename__ = 'orders'
#     id = Column(Integer(), primary_key=True)
#     customer_id = Column(Integer(), ForeignKey('customers.id'))
#     date_placed = Column(DateTime(), default=datetime.now)
#     line_items = relationship("OrderLine", secondary="order_lines", backref='order')
    

# class OrderLine(Base):
#     __tablename__ = 'order_lines'
#     id =  Column(Integer(), primary_key=True)
#     order_id = Column(Integer(), ForeignKey('orders.id'))
#     item_id = Column(Integer(), ForeignKey('items.id'))
#     quantity = Column(SmallInteger())
#     item = relationship("Item")


# Base.metadata.create_all(engine)