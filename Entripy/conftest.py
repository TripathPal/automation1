import pytest
from selenium import webdriver


@pytest.fixture(scope='class')
def test_setup(request):
    driver = webdriver.Chrome(executable_path="C:\\Users\\Tripath\\Desktop\\drivers\\chromedriver.exe")
    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
    print("test completed")
