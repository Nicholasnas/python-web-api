"""Tornar a aplicação Flask instalável com setuptools."""

"Instalador da aplicação Flask"

from setuptools import setup


# Criando um objeto de criação esse tradicional

# poetry é mais moderno e mais completo

setup(
    name="flask_blog",
    version="0.1.0",
    packages=["blog"],
    install_requires=[
        "flask",
        "flask_pymongo",
        "dynaconf",
        "flask-bootstrap",
        "unidecode",
        "mistune",
    ],
)
