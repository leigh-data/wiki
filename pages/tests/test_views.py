import pytest

from django.urls import reverse

from pages.views import HomePageView


def test_get_home_page(rf):
    request = rf.get(reverse('pages:home'))
    response = HomePageView.as_view()(request)
    assert response.status_code == 200
