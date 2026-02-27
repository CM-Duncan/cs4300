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

def test_duration_zero(self):
        "Zero-length movie is likely invalid"
        movie = Movie(title="Test", description="desc", release_date=date.today(), duration=0)
        with pytest.raises(ValidationError):
            movie.full_clean()

    def test_duration_negative(self):
        movie = Movie(title="Test", description="desc", release_date=date.today(), duration=-10)
        with pytest.raises(ValidationError):
            movie.full_clean()

    def test_duration_none_raises(self):
        movie = Movie(title="Test", description="desc", release_date=date.today(), duration=None)
        with pytest.raises(ValidationError):
            movie.full_clean()

def test_duration_very_large(self):
        "long duration is at least stored without error"
        movie = Movie(title="Test", description="desc", release_date=date.today(), duration=99999)
        movie.full_clean()

def test_release_date_in_future(self):
        "future release dates should be allowed"
        movie = Movie(title="Test", description="desc", release_date=date(2099, 1, 1), duration=90)
        movie.full_clean()

def test_release_date_very_old(self):
        movie = Movie(title="Test", description="desc", release_date=date(1888, 10, 14), duration=90)
        movie.full_clean()

def test_release_date_none_raises(self):
        movie = Movie(title="Test", description="desc", release_date=None, duration=90)
        with pytest.raises(ValidationError):
            movie.full_clean()


def test_str_returns_title(self):
        movie = Movie(title=" ", description="desc", release_date=date.today(), duration=148)
        assert str(movie) == " "

def test_str_with_special_characters(self):
        movie = Movie(title="½", description="", release_date=date.today(), duration=130)
        assert str(movie) == " "
