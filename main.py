from simple_term_menu import TerminalMenu
import sqlite3
def main():
	options = ["Add Book", "Delete Book", "Issue Book"]
	terminal_menu = TerminalMenu(options)
	selected_index = terminal_menu.show()
	# selected menu is index number,
	# if esc pressed then value is None
	# print(f"seçilen menu index i {selected_index}")
	con = sqlite3.connect("database.db")	
	cur = con.cursor()
	if selected_index == 0:
		# insert item into database.
		title= input("title ")
		author = input("author ")
		stmt = ''' INSERT INTO books(title,author) VALUES(?,?);'''
		cur.execute(stmt,(title, author))
		con.commit()
	if selected_index == 1:
		print("deleted the book")
	if selected_index == 2:
		print("book issued")

if __name__ == "__main__":
	main()
