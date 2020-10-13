'''
This module provides the Database Operations for the MIS part 2 

e-mail : jimutbahanpal@yahoo.com
website : https://jimut123.github.io/

'''


import tkinter as tk
from tkinter import *
from tkinter import font
from tkinter.filedialog   import askopenfilename
from tkinter import ttk
import textwrap
#from AppOperations import AppOperations as ao  			# the class build for this purpose
#from tkMessageBox import *
from tkinter import messagebox
# last parent6


import sqlite3
conn = sqlite3.connect("appDb.sqlite")
cur = conn.cursor()

col_name = ""

'''
MIS_labels contains the all possible MIS sorting operations that can be performed within the MIS
'''

info = [
		("Name (TEXT):",1),
		("e-mail (TEXT):",2),
		("Flat no. (TEXT):",3),
		("Tower no. (TEXT):",4),
		("Area (NUMBER):",5),
		("Parking (TEXT):",6),
		("Recpt. Fess (NUMBER):",7),
		("Address (TEXT):",8),
		("Contact number (TEXT):",9)
		]
e=["","","","","","","","","",""]



MIS_labels = [
				("Column name ", 1),
				("Equal to ",2),
				("Greater than ",3),
				("Less than ",4),
				("substring ",5),
			]

MIS_entry = ["","","","","",""]

class junk_Decor:
	def print_sep():
		print("###########################################################################################")
class MIS_calculations:
	def separate_data_equal(data,value):
		'''
		data will contain the data part ex "sl_no" or "name" or "e_mail etc."
		value will conatin the value of the data to be separated or sorted out from
		based on equality!
		'''
		junk_Decor.print_sep()
		t_items = cur.execute(''' SELECT * FROM details WHERE %s = ?'''%data,(value,))
		list_db = []

		for item in t_items:
			list_db.append(item)
		junk_Decor.print_sep()
			
		#print(list_db)
		return list_db		# this will return the result
		# Now this will create an output file for the entry

	def separate_data_greater(data,value):
		'''
		data will contain the data part ex "sl_no" or "name" or "e_mail etc."
		value will conatin the value of the data to be separated or sorted out from
		based on greater than the value
		'''
		junk_Decor.print_sep()

		t_items = cur.execute(''' SELECT * FROM details WHERE %s > ?'''%data,(value,))
		list_db = []

		for item in t_items:
			list_db.append(item)
		junk_Decor.print_sep()
			
		#print(list_db)
		return list_db		# this will return the result


	def separate_data_less(data,value):
		'''
		data will contain the data part ex "sl_no" or "name" or "e_mail etc."
		value will conatin the value of the data to be separated or sorted out from
		based on lesser than the value
		'''
		t_items = cur.execute(''' SELECT * FROM details WHERE %s < ?'''%data,(value,))
		list_db = []

		for item in t_items:
			list_db.append(item)
		junk_Decor.print_sep()
			
		#print(list_db)
		return list_db		# this will return the result

	def separate_data_substring(data,value):
		# substring is like substring
		# Testing version
		'''
		data will contain the data part ex "sl_no" or "name" or "e_mail etc."
		value will conatin the value of the data to be separated or sorted out from
		based on substring than the value (applying regex)
		'''
		t_items = cur.execute(''' SELECT * FROM details WHERE %s  like ? '''%data,(('%'+value+'%'),))
		list_db = []

		for item in t_items:
			list_db.append(item)
		junk_Decor.print_sep()
			
		#print(list_db)
		return list_db		# this will return the result

row_no = 0		# global row no

# the values

col_name = ""
equal_to = ""
greater_than = ""
less_than = ""
substring = ""

counter_mode_checker = 0 		# this is the mode checker

class MIS_GUI:
	def show_MIS():
		Col_helper.show_col_names()			# to call the pop-up helper column thingie
		# this function will show only specific MIS applications
		global row_no
		global col_name 			# column name
		parent7 = Tk()
		parent7.title("FLAT-INVENTORY   JIMSOFT (MIS DETAILS MODE)")
		parent7.geometry("1000x400+200+200")
		data, num = MIS_labels[0]		# to get the column and value of the column, the first entry of the row
		tk.Label(parent7, justify=tk.LEFT, padx =10, pady = 10, 
						text=data,font=font.Font(family='Helvetica', size=20, 
						weight='bold')).grid(row=row_no,column=1,sticky=W, pady=4)
		MIS_entry[num] = tk.Entry(parent7,width = 100)
		MIS_entry[num].grid(row=row_no, column=2,sticky=W, pady=4)
		Button(parent7, justify=tk.LEFT, padx =10, pady = 10, 
					text='check', command=MIS_GetVal.get_MIS_val).grid(row=row_no, column=3, sticky=W, pady=4)
		row_no = 1
		for item in MIS_labels[1:]:
			data,num = item
			tk.Label(parent7, justify=tk.LEFT, padx =10, pady = 10, 
						text=data,font=font.Font(family='Helvetica', size=20, 
						weight='bold')).grid(row=row_no,column=1,sticky=W, pady=4)
			MIS_entry[num] = tk.Entry(parent7,width = 100)
			MIS_entry[num].grid(row=row_no, column=2,sticky=W, pady=4)
			Button(parent7, justify=tk.LEFT, padx =10, pady = 10, 
					text='check', command=MIS_GetVal.get_MIS_val).grid(row=row_no, column=3, sticky=W, pady=4)
			row_no = row_no + 1
	
	def show_SORTED(list_t1, mode_name,col_name):
		'''
		This function is used to show the sorted values after performing all the operations
		mode_name will contain the name of the mode to be executed
		#################################
		This will use a counter checker variable which will tell if the thing is to be :
			2. equal to
			3. greater than
			4. less than 
			5. substring
		'''
		# This will use a tree structure 

		def wrap(string, lenght=30):
			# this is used to cut the line and adjust accordingly
			return '\n'.join(textwrap.wrap(string, lenght))

		
		title_parent8 = ""
		global counter_mode_checker
		
		# changing the variable according to the parameters supplied

		if counter_mode_checker == 2:
			title_parent8 = " "+col_name+" Equal to "+mode_name+" "

		if counter_mode_checker == 3:
			title_parent8 = " "+col_name+" Greater than "+mode_name+" "

		if counter_mode_checker == 4:
			title_parent8 = " "+col_name+" Less than "+mode_name+" "

		if counter_mode_checker == 5:
			title_parent8 = " "+col_name+" Substring "+mode_name+" "
		parent8 = Tk()
		
		title_p8 = "FLAT-INVENTORY   JIMSOFT ( "+title_parent8+" )"			# the actual title

		parent8.title(title_p8)
		parent8.geometry("1900x400+200+200")

		frame = Frame(parent8)
		frame.pack()
		count = ['sl_no']
		# count the no. of columns present in the db
		count = [0]		# the first one, sl_no

		global info

		for data, num in info:
			count.append(num)
		count.append(10)	# time stamp
		#print(count)
		tuple_count = tuple(count)	# contains the tuple of the total no. of columns present in the db
		#print(tuple_count)
		tree = ttk.Treeview(frame, columns = tuple_count, height = 30, show = "headings")
		tree.pack(side = 'left')
		tree.heading(0, text = "sl_no")
		tree.column(0, width = 70)			# sl no. width
		for data, num in info:
			#setting width accordingly
			if num == 1 or num == 2:
				width_tree = 200
			if num == 8:
				width_tree = 300
			if num in(3,4,5,6,7):
				width_tree = 130
			if num == 9:
				width_tree = 140
			num_i = data.find('(')
			tree.heading(num, text = data[:num_i])
			tree.column(num, width = width_tree)
		tree.heading(10, text = "time stamp")
		tree.column(10, width = 200)
		scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
		scroll.pack(side = 'right', fill = 'y')
		tree.configure(yscrollcommand=scroll.set)

		#print()
		for item in list_t1:
			#print(item,"$$$$$$$$$$$$$$$$$$$$$$$")
			values_t = [] 
			k = 0
			for items in item:
				print(items)
				#directly printing the values in the tree format
				values_t.insert(k,wrap(str(items)))
				k=k+1
			tuple_A = tuple(values_t)
			tree.insert('','end', values = tuple_A)
			




class MIS_GetVal:
	'''
	get_MIS_val gets called everytime in the button, then it is sorted according to the values got!
	'''
	def get_MIS_val():
		'''
		For parllel searching!
		'''
		# to get the values of the datas in the MIS
		equal_to = ""
		greater_than = ""
		less_than = ""
		substring = ""
		col_name = ""
		
		col_name = MIS_entry[1].get()
		equal_to = MIS_entry[2].get()
		greater_than = MIS_entry[3].get()
		less_than = MIS_entry[4].get()
		substring = MIS_entry[5].get()
		
		#print("Type of col_name ", type(col_name_v))
		#print("equal_to : ",equal_to," greater_than : ",greater_than," less_than : ",less_than," substring : ",substring)

		# these parts only get executed when there is any value in the list
		global counter_mode_checker
		if col_name:
			print(" col_name : ",col_name)
		else:
			print("Column name mandatory!")
		if equal_to:
			print(" equal_to : ",equal_to)
			print("Printing all values that is equal to the column name : ", col_name, " with value : ", equal_to)
			counter_mode_checker = 2 			# for being equal
			
			# collecting the list extracted from the tuple
			list_t = MIS_calculations.separate_data_equal(col_name,equal_to)
			
			# sending the list for tree view
			MIS_GUI.show_SORTED(list_t,equal_to,col_name)

		if greater_than:
			print(" greater_than : ",greater_than)
			counter_mode_checker = 3 			# for being greater than
			
			list_t = MIS_calculations.separate_data_greater(col_name,greater_than)

			# sending the list for tree view
			MIS_GUI.show_SORTED(list_t,greater_than,col_name)

		if less_than:
			print(" less_than : ",less_than)
			counter_mode_checker = 4 			# for being less than
			
			list_t = MIS_calculations.separate_data_less(col_name,less_than)

			# sending the list for tree view
			MIS_GUI.show_SORTED(list_t,less_than,col_name)

		if substring:
			print(" substring : ",substring)
			counter_mode_checker = 5 			# for substring

			list_t = MIS_calculations.separate_data_substring(col_name,substring)

			# sending the list for tree view
			MIS_GUI.show_SORTED(list_t,substring,col_name)

class Col_helper:
	def show_col_names():
		#pop-up helper column thingie
		row_no = 0
		parent9 = Tk()
		row = Frame(parent9)
		parent9.title("FLAT-INVENTORY   JIMSOFT ( COLUMN HELPER ? )")
		parent9.geometry("700x200+200+200")

		S = Scrollbar(parent9)
		T = Text(parent9, height=800, width=800)
		S.pack(side=RIGHT, fill=Y)
		T.pack(side=LEFT, fill=Y)
		S.config(command=T.yview)
		T.config(yscrollcommand=S.set)
		quote = """
				Name of column  Vs	To be written
				sl_no          :->:	  sl_no
				Name           :->:	  name
				e-mail         :->:   e_mail
				Flat no.       :->:	  flat
				Tower no.      :->:   tower
				Area           :->:   area
				Parking        :->:	  parking
				Recpt. Fees    :->:   recpt_fees
				Address        :->:   addr
				Contact number :->:   contact_no
				time stamp     :->:   timestmp

		"""
		T.insert(END, quote)
		




