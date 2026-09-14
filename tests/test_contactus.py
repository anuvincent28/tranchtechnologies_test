import pytest

from pages.contactus import contact

@pytest.mark.smoke
def test_contacts(page):
    contactus=contact(page)
    contactus.contactus_options()
@pytest.mark.smoke
def test_socicalmedia(page):
    contactus=contact(page)
    contactus.media_options()

