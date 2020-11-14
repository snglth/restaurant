import enum
import uuid

from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    Sequence,
    Date,
    ForeignKey,
    Enum,
    Table,
)
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from restaurant.app import db


class Author(db.Model):
    __tablename__ = "Author"
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    full_name = Column(String)
    date_of_birth = Column(Date)


class Units(enum.Enum):
    gram = "g"
    piece = "pcs"
    mililitre = "ml"


class Ingredient(db.Model):
    __tablename__ = "Ingredient"
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    title = Column(String)
    unit = Column(String)
    calorific = Column(Float)
    fats = Column(Float)
    proteins = Column(Float)
    carbohydrates = Column(Float)


class Category(db.Model):
    __tablename__ = "Category"
    id = Column(UUID(as_uuid=True), ForeignKey("Recipe.id"))
    title = Column(String, primary_key=True)


class RecipeIngredient(db.Model):
    __tablename__ = "RecipeIngredient"
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    recipe_id = Column(UUID(as_uuid=True), ForeignKey("Recipe.id"))
    ingredient_id = Column(UUID(as_uuid=True), ForeignKey("Ingredient.id"))
    quantity = Column(Integer)
    ingredient = relationship("Ingredient")


class Recipe(db.Model):
    __tablename__ = "Recipe"
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    title = Column(String)
    creation_date = Column(Date)
    category = Column(String)
    ingredients = relationship("RecipeIngredient")


menu_recipe_assoc = Table(
    "MenuRecipe",
    db.Model.metadata,
    Column("menu_id", Integer, ForeignKey("Menu.id")),
    Column("recipe_id", Integer, ForeignKey("Recipe.id")),
)


class Menu(db.Model):
    __tablename__ = "Menu"
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    company = Column(String)
    date = Column(Date)
    recipes = relationship("Recipe", secondary=menu_recipe_assoc)
