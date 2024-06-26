#!/usr/bin/python3
"""Roadmap Class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship
import models
import os


class Roadmap(BaseModel, Base):
    """Roadmap Class"""
    __tablename__ = "roadmaps"
    title = Column(String(256), nullable=False)
    description = Column(String(4096), nullable=False)
    slug = Column(String(256), nullable=False)
    # course_count = Column(Integer, nullable=True)
    image = Column(String(4096), nullable=True)
    courses = relationship("Course", cascade="all,delete,delete-orphan", backref="roadmap")
    progresses = relationship("Progress", cascade="all,delete,delete-orphan", backref="roadmap")
