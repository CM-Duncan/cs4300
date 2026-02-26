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
