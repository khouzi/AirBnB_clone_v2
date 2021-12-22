#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel


class Place(BaseModel):
    """ A class Place that inherits from BaseModel."""

    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    reviews = relationship("Review", cascade="all,delete", backref="place")
    amenity_ids = []
    _amenities = relationship('Amenity', secondary='place_amenity',
                              viewonly=False, back_populates="place_amenities")
    if storage_type != 'db':
        @property
        def reviews(self):

            """
            get list of Review instances with
            place_id equals to the current Place.id
            """

            list_reviews = []
            all_reviews = self.reviews
            for review in all_reviews:
                if review.place_id == Place.id:
                    list_reviews.append(review)
            return list_reviews

        @property
        def amenities(self):
            """
            returns the list of Amenity instances based on the attribute
            amenity_ids
            """
            amenity_values = []
            for amenity_id in self.amenity_ids:
                key = 'Amenity.' + amenity_id
                if key in FileStorage.__valueects:
                    amenity_values.append(FileStorage.__valueects[key])
            return amenity_values

        @amenities.setter
        def amenities(self, value):
            """
            adds an Amenity.id to the attribute amenity_ids
            """
            if isinstance(value, Amenity):
                self.amenity_ids.append(value.id)
