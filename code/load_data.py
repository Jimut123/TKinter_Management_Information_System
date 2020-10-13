'''
This module provides the loading of data from the xls file provided to the database directly, for the MIS 
This module directly imports data from the spreadsheet or xls file to the database so that no manual insertion is required!

e-mail : jimutbahanpal@yahoo.com
website : https://jimut123.github.io/


'''

# to make the xlrd object


import xlrd
import sqlite3
from tkinter import *
from tkinter import font
from tkinter.filedialog   import askopenfilename
from datetime import datetime

from AppOperations import Rec
# making the connection
conn = sqlite3.connect("appDb.sqlite")
cur = conn.cursor()
from time import sleep

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


# creating the workbook
workbook = xlrd.open_workbook('akankha.xls')
print("Workbook obj. created! : ",workbook)

no_of_sheetsv = 0

tuple_workbook = []
class Load_XLS:
	def get_sheet_names():
		# to get and print the sheet names
		sheet_names = workbook.sheet_names()
		# print(sheet_names)

		# to get the no. of sheet present, assigning it here!
		global no_of_sheetsv
		no_of_sheetsv = len(sheet_names)

		return sheet_names 		#to return a list of sheet name

class NO_XLS_sheet:
	def no_of_sheets():
		# global version of the sheet to be returned
		print(Load_XLS.get_sheet_names())
		global no_of_sheetsv

		return no_of_sheetsv

class GET_XLS:
	def get_row_col_tuple():
		try:
			sheets = workbook.sheets()
			#for sheet in sheets:
				#print("SHEET : ",sheet)
			rows = sheets[0].nrows
			cols = sheets[0].ncols
			print("row : ",rows,"cols : ",cols)
			# to get the whole tuple
			# to get the total no. of records present
			list_names = Load_XLS.get_sheet_names()
			total_no = NO_XLS_sheet.no_of_sheets()
			print("FINAL : ",total_no)
			# iterate over the names in the list of names
			all_list = []
			for list_name in range(len(list_names)):
				name_cur_list = workbook.sheet_by_index(list_name)
				for iter_row in range(1,rows+1):
					list1 = []
					row_slice = name_cur_list.row_slice(rowx=iter_row, start_colx=0, end_colx=cols)
					#print(row_slice)
					for item in row_slice:
						list1.append(item)
					all_list.append(list1)
			return all_list
		except:
			return all_list

class cleanData:
	'''
	This class cleans the data that is provided text:'000' format
	'''
	def cleanItem(item):
		# to clean the item present
		#print(item)
		item1 = str(item)
		first_ = item1.find("'")
		#print(first_)
		item2 = item1[first_+1:]
		#print(item2)
		last_ = item2.find("'")
		item3 = item2[:last_]
		#print(last_)
		#print(item3)
		return item3

if __name__ == "__main__":
	#print(Load_XLS.get_sheet_names())
	list_l = GET_XLS.get_row_col_tuple()
	#print(list_l)
	for item in list_l[2:]:
		#print(item[1],item[2],item[3],item[4],item[5],item[6],item[7])
		name = cleanData.cleanItem(item[1])
		tower = cleanData.cleanItem(item[2])
		flat = cleanData.cleanItem(item[3])
		addr = cleanData.cleanItem(item[4])
		landline = cleanData.cleanItem(item[5])
		mobile = cleanData.cleanItem(item[6])
		email = cleanData.cleanItem(item[7])

		print(name," ",tower," ",flat," ",addr," ",landline," ",mobile," ",email)
		try :
			cur.execute('''INSERT  
					   INTO details (sl_no, name, e_mail, tower, flat, area, parking, recpt_fees, addr, contact_no, timestmp)
                       VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? )''', 
                       ( (Rec.countTotalRec()+1),name,email,tower,flat,0,'',0,addr,mobile,Rec.timestmp(),))
			# the flat anf area and parking are set to default values !
			conn.commit()
			sleep(1) # wait for 1 second to generate an unique timestamp
		except:
			print("Ops! something went wrong during insertion of the data!!")
			#return 0
		

