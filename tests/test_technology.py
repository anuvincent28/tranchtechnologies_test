







import pytest

from pages.technologys import technology

@pytest.mark.smoke 
def test_technology(page):
    technologys=technology(page)
    technologys.ecomm_options()
@pytest.mark.smoke 
def test_mobileapp(page):
    technologys=technology(page)
    technologys.mobileapp_options()
@pytest.mark.smoke 
def test_Ai(page):
    technologys=technology(page)
    technologys.Ai_Options()


    

