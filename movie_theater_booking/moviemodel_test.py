"Caroline Duncan, 2/26/26, Test for Movie model "
import pytest
from datetime import date
from django.core.exceptions import ValidationError
from django.db.utils import DataError
from .models import Movie
@pytest.mark.django_db

def test_title_empty_string_fails(self):
        movie = Movie(title="", description="desc", release_date=date.today(), duration=90)
        with pytest.raises(ValidationError):
            movie.full_clean()

def test_title_max_length_boundary(self):
        movie = Movie(title="A" * 200, description="desc", release_date=date.today(), duration=90)
        movie.full_clean()
 def test_title_exceeds_max_length(self):
        movie = Movie(title="A" * 201, description="desc", release_date=date.today(), duration=90)
        with pytest.raises(ValidationError):
            movie.full_clean()

 def test_title_whitespace_only(self):
        movie = Movie(title="   ", description="desc", release_date=date.today(), duration=90)
        movie.full_clean()

def test_title_none_raises(self):
        movie = Movie(title=None, description="desc", release_date=date.today(), duration=90)
        with pytest.raises(ValidationError):
            movie.full_clean()
def test_description_empty_string(self):
        """TextField allows empty strings by default."""
        movie = Movie(title="Test", description="", release_date=date.today(), duration=90)
        movie.full_clean()
 def test_description_very_large(self):
        movie = Movie(title="Test", description="x" * 100_000, release_date=date.today(), duration=90)
        movie.full_clean()
