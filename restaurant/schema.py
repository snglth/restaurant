from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Sequence, Date, ForeignKey, Enum
import enum

Base = declarative_base()


class Recipe(Base):
    __tablename__ = 'Recipe'
    id = Column(Integer, Sequence('recipe_id_seq'), primary_key=True)
    title = Column(String)
    brief_title = Column(String)
    creation_date = Column(Date)
    author = Column(Integer)
    category = Column(String)


class Author(Base):
    __tablename__ = 'Author'
    id = Column(Integer, Sequence('author_id_seq'), primary_key=True)
    full_name = Column(String)
    date_of_birth = Column(Date)


class Units(enum.Enum):
    gram = 'g.'
    piece = 'pcs.'
    mililitre = 'ml.'


class Ingredient(Base):
    __tablename__ = 'Ingredient'
    title = Column(String, primary_key=True)
    unit = Column(Enum(Units))


class RecipeIngredient(Base):
    __tablename__ = 'RecipeIngredient'
    recipe = Column(Integer, ForeignKey("Recipe.id"), primary_key=True)
    ingredient = Column(String, ForeignKey("Ingredient.title"), primary_key=True)
    quantity = Column(Float)


class Menu(Base):
    __tablename__ = 'Menu'
    id = Column(Integer, Sequence('menu_id_seq'), primary_key=True)
    company = Column(String, primary_key=True)
    date = Column(Date, primary_key=True)


class MenuItem(Base):
    __tablename__ = 'MenuItem'
    menu = Column(Integer, ForeignKey("Menu.id"), primary_key=True)
    recipe = Column(Integer, ForeignKey("Recipe.id"), primary_key=True)


class Category(Base):
    __tablename__ = 'Category'
    title = Column(String, primary_key=True)