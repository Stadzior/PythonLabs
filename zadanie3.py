import npyscreen


class TestApp(npyscreen.NPSAppManaged):

	def onStart(self):
		self.addForm("MAIN", MainForm, name = "Zadanie 3",)

class MainForm(npyscreen.ActionForm):
	ms = None
	db = None
	gd = None

	def create(self):
		self.ms = self.add(npyscreen.TitleSelectOne, max_height=7, value = [0,], name="Wybierz opcje:", values = ["Laduj baze z pliku","Zapisz baze do pliku", "Dodaj nowy wpis do bazy", "Usun wpis z bazy"], scroll_exit=True)
		self.gd = self.add(npyscreen.GridColTitles, relx = 20, rely=10, width=50, col_titles = ['Imie', 'Nazwisko'], select_whole_line=True)
		self.gd.values = []
		for x in range(36):
			row = []
			for y in range(x, x+36):
				row.append(y)
			self.gd.values.append(row)
		self.gd.hidden = len(self.gd.values) == 0
	def on_ok(self):
		if self.ms.value[0] == 0:
			try:
				with open(npyscreen.selectFile(),'r') as f:
					content = f.readlines()
				self.db = [x.strip().split(" ") for x in content]
			except:
				npyscreen.notify_confirm("Ladowanie bazy z pliku nie powiodlo sie.\n\n{}".format(str(e)), title="Blad ladowania bazy")
		elif self.ms.value[0] == 1:
			try:
				with open(npyscreen.selectFile(),'w') as f:
					for row in self.db:
						print('{} {}'.format(row[0],row[1]),file=f)
			except Exception as e:
				npyscreen.notify_confirm("Zapis bazy do pliku nie powiodl sie.\n\n{}".format(str(e)), title="Blad zapisu bazy")
		elif self.ms.value[0] == 3:
			selectedRowIndex = self.gd.edit_cell[0]
			deletionConfirmed = npyscreen.notify_ok_cancel("Jestes pewny, ze chcesz usunac {} {} z bazy?".format(self.db[selectedRowIndex][0],self.db[selectedRowIndex][1]), title='Usuwanie wpisu z bazy')
			if deletionConfirmed:
				
	def on_cancel(self):
		exit()

	def divideNames(self, text):
		newList = []
		names = text.split(",")
		
		for value in names:
			value = value.strip()
			value = value.split(" ")
			newList.append(value)
		return newList	

	def buildMessageString(self, names):
		string = ""
		for value in names:
			string += value[0] + " " + value[1] + "\n"

		return string
		

if __name__ == "__main__":
	App = TestApp()
	App.run()


