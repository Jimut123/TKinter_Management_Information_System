'''
This module provides the Database Operations for the MIS 

e-mail : jimutbahanpal@yahoo.com
website : https://jimut123.github.io/

'''

__version__ = "0.0.1-beta"
__author__ = "Jimut Bahan Pal <jimutbahanpal@yahoo.com>"

import sqlite3
from tkinter import *
from tkinter import font
from tkinter.filedialog   import askopenfilename
from datetime import datetime


# making the connection
conn = sqlite3.connect("appDb.sqlite")
cur = conn.cursor()

# email address is the primary key
cur.executescript('''

CREATE TABLE IF NOT EXISTS details(
	sl_no INTEGER,
	name TEXT,
	e_mail TEXT,
	flat TEXT,
	tower TEXT,
	area INTEGER,
	parking TEXT,
	recpt_fees INTEGER,
	addr TEXT,
	contact_no TEXT,
	timestmp DATE

);

''')
total_record = 0
class Rec:
	def countTotalRec():
		# To count the total no. of records in the table.
		cur.execute('''SELECT count( * ) as  total_record FROM details''')
		total_record = cur.fetchone()[0]
		print("Total data present : ",total_record)
		return total_record
	def timestmp():
		# to return the current timestamp for making it an unique primary key
		tmestmp = datetime.now().isoformat(timespec='seconds')
		#print(type(tmestmp))
		return tmestmp

class AppOperations:
	def save_root():
		# To save the data on closing the whole application, by comitting it
		print("Saving  your  data !")
		conn.commit()
	def insertData(name, e_mail, tower, flat, area, parking, recpt_fees, addr, contact_no):
		'''
		To insert the data into the database
		'''
		try :
			cur.execute('''INSERT  
					   INTO details (sl_no, name, e_mail, tower, flat, area, parking, recpt_fees, addr, contact_no, timestmp)
                       VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? )''', 
                       ( (Rec.countTotalRec()+1),name,e_mail,tower,flat,area,parking,recpt_fees,addr,contact_no,Rec.timestmp(),))
			conn.commit()
			return 1
		except:
			print("Ops! something went wrong during insertion of the data!!")
			return 0
		return 1

	def displayData():				# returns all the data present in the db, list of tuples
		'''
		This module returns the data that is to be send for displaying 
		'''
		data_fetch = cur.execute(''' SELECT * FROM details ''')
		list_db = []
		for item in data_fetch:
			list_db.append(item)
		#print(list_db)
		return list_db

	def countTotalItems():
		total_items = 0			# contains the total no. of items present in the table
		data_fetch = cur.execute(''' SELECT * FROM details ''')
		for item in data_fetch:
			total_items = total_items + 1
		return total_items

	def test_d():
		k = '2018-07-25T21:48:28'
		iitems = cur.execute(''' SELECT * FROM details WHERE timestmp = ?''',(k))
		for item in items:
			print(item)
	
	def reset_slno():
		'''
		This part resets the sl. no. of the whole db
		'''
		def update_Sl(slno_dum,first):
			cur.execute(''' UPDATE details SET sl_no = ? WHERE timestmp = ?''',(slno_dum,first,))
		#cur.execute(''' UPDATE details SET sl_no = ? WHERE timestmp = ?''',(40,dt))
		data_fetch = cur.execute(''' SELECT * FROM details''')
		slno_dum = 0
		list_a = []
		for item in data_fetch:
			first = item[10]
			slno_dum = slno_dum + 1
			list_a.append((slno_dum,first))
		print(list_a)
		for item in list_a:
			a, b = item
			update_Sl(a,b)
		conn.commit()

	def update_values(val_date):
		print("date obtained = ",val_date)
		rowfetch = cur.execute(''' SELECT * FROM details where timestmp = ?''',(val_date,))
		tuple_needed = tuple(rowfetch)[0]
		#print("Row fetched! : ", tuple_needed)
		return tuple_needed
	def updateData(slno,name, e_mail, flat, tower,  area, parking, recpt_fees, addr, contact_no,tmestmp):
		print("values to be updated : ",slno," ",name," ",e_mail," ", tower, flat, area, parking, recpt_fees, addr, contact_no,tmestmp)
		cur.execute(''' UPDATE details SET sl_no = ?, name = ?, e_mail = ?, tower = ?, flat = ?, area = ?, parking = ?, 
			recpt_fees = ?, addr = ?, contact_no = ? WHERE timestmp = ?''',
			(slno,name, e_mail, tower, flat, area, parking, recpt_fees, addr, contact_no,tmestmp))
		conn.commit()

	def delete_selected(slno,tmestmp):
		cur.execute(''' DELETE FROM details WHERE  sl_no = ? AND timestmp = ? ''',(slno,tmestmp))
		conn.commit()
		print("values to deleted :$$$$$$$$ ",slno,tmestmp)
		

