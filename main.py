from simple_term_menu import TerminalMenu

def main():
	options = ["Add Book", "Delete Book", "Issue Book"]
	terminal_menu = TerminalMenu(options)
	selected_index = terminal_menu.show()
	# selected menu is index number,
	# if esc pressed then value is None
	print(f"seçilen menu index i {selected_index}")

if __name__ == "__main__":
	main()
