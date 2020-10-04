import xml.etree.ElementTree as ET 
import csv
tree=ET.parse("books.xml")
root=tree.getroot()

book_data=open("xml.csv",'w')
csv_writer=csv.writer(book_data)
book_head=[]

count=0
for book in root.findall('book'):
	bookinfo=[]
	if count==0:
		bookname=book.find('title').tag
		book_head.append(bookname)
		author=book.find('author').tag
		book_head.append(author)
		genre=book.find('genre').tag
		book_head.append(genre)
		price=book.find('price').tag
		book_head.append(price)
		publish_date=book.find("publish_date").tag
		book_head.append(publish_date)
		description=book.find('description').tag
		book_head.append(description)
		csv_writer.writerow(book_head)
		count=count + 1
	bookname=book.find('title').text
	bookinfo.append(bookname)
	author=book.find('author').text
	bookinfo.append(author)
	genre=book.find('genre').text
	bookinfo.append(genre)
	price=book.find('price').text
	bookinfo.append(price)
	publish_date=book.find("publish_date").text
	bookinfo.append(publish_date)
	description=book.find('description').text
	bookinfo.append(description)
	csv_writer.writerow(bookinfo)
book_data.close()
