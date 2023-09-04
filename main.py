from simple_term_menu import TerminalMenu
import sqlite3
def main():
	options = ["Add Book", "Delete Book", "List Books","Issue Book"]
	terminal_menu = TerminalMenu(options,title="Commands")
	con = sqlite3.connect("database.db")
	cur = con.cursor()
	while True:	
		selected_index = terminal_menu.show()
		if selected_index is None:
			con.close()
			break
		if selected_index == 0:
			# insert item into database.
			title= input("title ")
			author = input("author ")
			stmt = ''' INSERT INTO books(title,author,is_issued) VALUES(?,?,?);'''
			cur.execute(stmt,(title, author,"FALSE"))
			con.commit()
		if selected_index == 1:
			title = input("enter title to delete ")
			stmt = ''' delete from books where title = ?'''
			cur.execute(stmt,(title,))
			con.commit()
		if selected_index == 2:
			stmt = ''' select * from books '''
			cur.execute(stmt)
			print("-"*80)
			for item in cur.fetchall():
				print(item[1], item[2],item[3])
		if selected_index == 3:
			name_to = input("name to issue ")
			stmt = ''' update books set is_issued = "TRUE" where title= ?'''
			cur.execute(stmt,(name_to,))
			con.commit()
if __name__ == "__main__":
	main()
