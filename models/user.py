#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
import models


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    def __init__(self, *args, **kwargs):
        """ Initializes User
        """
        super().__init__(*args, **kwargs)

    if models.env == "db":
        # DBstorage
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=False)
        last_name = Column(String(128), nullable=False)
        places = relationship('Place', backref='user', cascade="all, delete")
        reviews = relationship('Review', cascade='all, delete', backref='user')
    else:
        # filestorage
        1 == 1
