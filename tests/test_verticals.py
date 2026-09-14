

import pytest

from pages.verticals import vertical

@pytest.mark.smoke              #markers 
def test_trading(page):  #Methods
    varticals=vertical(page)
    varticals.trading_options()
@pytest.mark.smoke   
def test_retails(page):
    varticals=vertical(page)
    varticals.retails_options()
@pytest.mark.smoke
def test_healthcare(page):
    varticals=vertical(page)
    varticals.healthcare_options()
@pytest.mark.smoke
def test_fintech_options(page):
    varticals=vertical(page)
    varticals.fintech_options()
@pytest.mark.smoke
def test_customs(page):
    varticals=vertical(page)
    varticals.customs_options()
    
