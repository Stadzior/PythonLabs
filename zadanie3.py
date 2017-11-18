import npyscreen


class TestApp(npyscreen.NPSAppManaged):

	def onStart(self):
		self.addForm("MAIN", MainForm, name = "Zadanie 3")
		self.addForm("ADD", AddRecordForm, name = "Add new record")
		self.addForm("REMOVE", RemoveRecordForm, name = "Remove record")

class MainForm(npyscreen.ActionForm):
	ms = None
	db = None
	gd = None
	def create(self):
		self.ms = self.add(npyscreen.TitleSelectOne, max_height=7, value = [0,], name="Wybierz opcje:", values = ["Laduj baze z pliku","Zapisz baze do pliku", "Dodaj nowy wpis do bazy", "Usun wpis z bazy"], scroll_exit=True)
		self.gd = self.add(npyscreen.GridColTitles, relx = 20, rely=10, width=50, col_titles = ['Imie', 'Nazwisko'])
		self.gd.hidden = True
	def on_ok(self):
		if self.ms.value[0] == 0:
			try:
				with open(npyscreen.selectFile(),'r') as f:
					content = f.readlines()
				self.db = [x.strip().split(" ") for x in content]
				self.refresh_grid()
			except Exception as e:
				npyscreen.notify_confirm("Ladowanie bazy z pliku nie powiodlo sie.\n\n{}".format(str(e)), title="Blad ladowania bazy")
		elif self.ms.value[0] == 1:
			try:
				with open(npyscreen.selectFile(),'w') as f:
					for row in self.db:
						print('{} {}'.format(row[0],row[1]),file=f)
			except Exception as e:
				npyscreen.notify_confirm("Zapis bazy do pliku nie powiodl sie.\n\n{}".format(str(e)), title="Blad zapisu bazy")
		elif self.ms.value[0] == 2:
			self.parentApp.switchForm('ADD')
		elif self.ms.value[0] == 3:
			self.parentApp.getForm('REMOVE').ms.values = ['{} {}'.format(row[0],row[1]) for row in self.db] 
			self.parentApp.switchForm('REMOVE')
	def on_cancel(self):
		exit()
	
	def refresh_grid(self):
		self.gd.values = []
		for row in self.db:
			self.gd.values.append(row)
		self.gd.hidden = len(self.gd.values) == 0

class AddRecordForm(npyscreen.ActionPopup):
	nameTextEdit = None
	surnameTextEdit = None

	def create(self):
		self.add(npyscreen.FixedText, value = "Imie:\n", rely=1)
		self.nameTextEdit = self.add(npyscreen.MultiLineEdit, max_height=5, rely=2)
		self.add(npyscreen.FixedText, value = "Nazwisko:\n",rely=3)
		self.surnameTextEdit = self.add(npyscreen.MultiLineEdit, max_height=5, rely=4)
	def on_ok(self):
		mainForm = self.parentApp.getForm('MAIN')
		row = [self.nameTextEdit.value, self.surnameTextEdit.value]
		if len(row[0]) > 0 or len(row[1]) > 0:
			mainForm.db.append(row)
			mainForm.refresh_grid()
			self.nameTextEdit.value = ""
			self.surnameTextEdit.value = ""
		else:
			npyscreen.notify_confirm("Nie ma czego zapisac.", title="Blad dodawania rekordu")
		self.parentApp.switchFormPrevious();
	def on_cancel(self):
		self.parentApp.switchFormPrevious();

class RemoveRecordForm(npyscreen.ActionPopup):
	ms = None
	def create(self):
		self.ms = self.add(npyscreen.TitleSelectOne, max_height=7, value = [0,], name="Wybierz rekord:", scroll_exit=True)
	def on_ok(self):
		mainForm = self.parentApp.getForm('MAIN')
		selectedRowIndex = self.ms.value[0]
		if selectedRowIndex > -1:
			mainForm.db.pop(selectedRowIndex)
			mainForm.refresh_grid()
		else:
			npyscreen.notify_confirm("Nie wybrano zadnego rekordu", title="Blad usuwania rekordu")
		self.parentApp.switchFormPrevious();
	def on_cancel(self):
		self.parentApp.switchFormPrevious();

if __name__ == "__main__":
	App = TestApp()
	App.run()





