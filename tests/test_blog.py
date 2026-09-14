
import pytest

from pages.blogs import blog



@pytest.mark.smoke 
def test_blog(page):
    blogs=blog(page)
    blogs.blog_options()
