from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#import base restaurant and menuitem classes from the .py file created 
from database_setup import Base, Restaurant, MenuItem

#let the program know which database engine to communicate with
engine = create_engine("sqlite:///restaurantmenu.db")
#bind the engine with base class(this makes the connection with the class
#definitions and the corresponding tables)
Base.metadata.bind = engine
#connection between code execution and engine we created 
DBSession = sessionmaker(bind = engine)

#session execute data base operations persist after calling commit command 
session = DBSession()

"""
syntax : 
    newEntry = ClassName(property = "Value", ...)
    session.add(newEntry)
    session.commit()
"""

myFirstRestaurant = Restaurant(name = "Pizza Place")
session.add(myFirstRestaurant)
# store to the data base
session.commit()
#find the table and return all details within the table 
print(session.query(Restaurant).all())


cheesepizza = MenuItem(name = "Cheese Pizza",
                       description = "Made with fresh ingredients and fresh mozzarilla",
                       course = "Entree",
                       price = "$8.99",
                       restaurant = myFirstRestaurant)

session.add(cheesepizza)
session.commit()
session.query(MenuItem).all()
