#!/usr/bin/env python

import csv
import json
import random

from dataclasses import dataclass
from typing import Dict


@dataclass
class Ingredient:
    title: str
    unit: str


@dataclass
class Recipe:
    title: str
    brief_title: str
    category: str
    ingredients: Dict[Ingredient, float]  # {ingredient: quantity}


def read_ingredients(ingredients_file: str):
    with open(ingredients_file) as fd:
        reader = csv.reader(fd)
        for row in reader:
            yield Ingredient(row[0], row[1])


def read_templates(templates_file: str):
    with open(templates_file) as fd:
        reader = csv.reader(fd)
        for row in reader:
            yield row[0].split(','), row[1]


def generate_recipe(template, ingredients):
    chosen_ingredients = [
        random.choice(
            [ingredient.title for ingredient in ingredients if ingredient.unit == unit]
        )
        for unit in template[0]
    ]
    return template[1].format(*chosen_ingredients)
