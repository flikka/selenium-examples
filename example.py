
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PingTests(unittest.TestCase):
	def setUp(self):
		self.__driver = webdriver.Chrome('./chromedriver')
			
	def tearDown(self):
		self.__driver.close()
		
	def test_google_up(self):
		driver = self.__driver
		driver.get("http://www.google.com")
		assert "Google" in driver.title
		
	def test_statoil_up(self):
		driver = self.__driver
		driver.get("http://www.statoil.com")
		assert "Statoil" in driver.title
	
	def tests_vg_up(self):
		driver = self.__driver
		driver.get("http://www.vg.no")
		assert "VG" in driver.title
		
	def test_yammer_statoil_up(self):
		driver = self.__driver
		driver.get("https://www.yammer.com/statoil.com#/threads/company?type=general")
		assert "All Company" in driver.title
	
if __name__ == '__main__':
	unittest.main()
	