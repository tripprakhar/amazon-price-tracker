# Amazon product price tracker 
import bs4 as bs 
import sys 
import schedule 
import time 
import urllib.request 
from PyQt5.QtWebEngineWidgets import QWebEnginePage 
from PyQt5.QtWidgets import QApplication 
from PyQt5.QtCore import QUrl 
import smtplib
import winsound 

frequency = 2500  
duration = 1000  


class Page(QWebEnginePage): 

	def __init__(self, url): 
		self.app = QApplication(sys.argv) 
		QWebEnginePage.__init__(self) 
		self.html = '' 
		self.loadFinished.connect(self._on_load_finished) 
		self.load(QUrl(url)) 
		self.app.exec_() 

	def _on_load_finished(self): 
		self.html = self.toHtml(self.Callable) 
		print('Load finished') 

	def Callable(self, html_str): 
		self.html = html_str 
		self.app.quit() 

def exact_url(url): 
	index = url.find("B0") 
	index = index + 10
	current_url = "" 
	current_url = url[:index] 
	return current_url 
	

def mainprogram(): 
	url = input("Your URL: ")
	exacturl = exact_url(url) 
	page = Page(exacturl) 
	soup = bs.BeautifulSoup(page.html, 'html.parser') 
	js_test = soup.find('span', id ='priceblock_ourprice') 
	print("working.")
	if js_test is None: 
		js_test = soup.find('span', id ='priceblock_dealprice')		 
	str = "" 
	for line in js_test.stripped_strings : 
		str = line 
	
	str = str.replace(",", "") 
	current_price = int(float(str[3:])) 
	your_price = int(input("Enter your price: "))
	if current_price < your_price:
		print("Price decreased book now") 
		winsound.Beep(frequency, duration)
		mail("Price decreased book now")
	else: 
		print("Price is high please wait for the best deal") 
	


def mail(message):
    s = smtplib.SMTP('smtp.gmail.com', 587)  
    s.starttls() 
    s.login("yash.15.ty@gmail.com", "yashwantmurty15") 
    mail_me = input("Enter your mail address: ")
    s.sendmail("yash.15.ty@gmail.com", mail_me, message) 
    s.quit() 		
	
mainprogram()
