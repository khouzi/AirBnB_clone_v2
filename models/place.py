#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from models import env
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """ A place to stay """
    def __init__(self, *args, **kwargs):
        """ Initializes Place
        """
        super().__init__(*args, **kwargs)

    if env == "db":
        # DBstorange
        __tablename__ = "places"
        city_id = Column(String(60), ForeignKey('cities.id'),  nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'),  nullable=False)
        name = Column(String(60), nullable=False)
        description = Column(String(1024), nullable=False)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=False)
        longitude = Column(Float, nullable=False)
        reviews = relationship(
            'Review', cascade='all, delete', backref='place')
        # place_amenity = Table('place_amenity', Base.metadata,
        #                    Column('place_id',
        #                    String(60), ForeignKey('places.id')),
        #                    Column('amenity_id',
        #                    String(60), ForeignKey('right.id'))
        #                )
        # amenities = relationship('Amenity',
        # secondary='place_amenity', viewonly=False)
    else:
        # filestorage
        # getter attribute reviews that returns the list
        # of Review instances with place_id getter attribute reviews
        # that returns the list of Review instances with place_id
        @property
        def reviews(self):
            places_reviews_instances = []
            all_reviews = models.storage.all(Review)
            for one_review in all_reviews:
                if one_review.place_id == Place.id:
                    places_reviews_instances.append(one_review)
            return places_reviews_instances

        @property
        def amenities(self):
            amenity_ids = []
            place_amenity_instance = []
            all_amenities = models.storage.all(Amenity)
            for one_amenity in all_amenities:
                if one_amenity.id in amenity_ids:
                    place_amenity_instance.append(one_amenity)
            return place_amenity_instance

        @property
        def amenities(self, amenity_obj):
            amenity_ids = []
            if isinstance(Amenity, amenity_obj):
                for one_amenity in models.storage.all(Amenity):
                    amenity_ids.append(one_amenity.id)
            else:
                pass
