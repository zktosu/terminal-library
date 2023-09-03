from simple_term_menu import TerminalMenu
import sqlite3
def main():
	options = ["Add Book", "Delete Book", "List Books"]
	terminal_menu = TerminalMenu(options)
	con = sqlite3.connect("database.db")	
	cur = con.cursor()
	while True:	
		selected_index = terminal_menu.show()
		if selected_index is None:
			break
		if selected_index == 0:
			# insert item into database.
			title= input("title ")
			author = input("author ")
			stmt = ''' INSERT INTO books(title,author) VALUES(?,?);'''
			cur.execute(stmt,(title, author))
			con.commit()
		if selected_index == 1:
			title = input("enter title to delete ")
			stmt = ''' delete from books where title = ?'''
			cur.execute(stmt,(title,))
			con.commit()
		if selected_index == 2:
			stmt = ''' select * from books '''
			cur.execute(stmt)
			f = open("printout","w")
			for item in cur.fetchall():
				f.write("%s %s\n" % (item[1],item[2]))
if __name__ == "__main__":
	main()
