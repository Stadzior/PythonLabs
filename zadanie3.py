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
			self.parentApp.switchForm('REMOVE')

#			selectedRowIndex = self.gd.edit_cell[0]
#			deletionConfirmed = npyscreen.notify_ok_cancel("Jestes pewny, ze chcesz usunac {} {} z bazy?".format(self.db[selectedRowIndex][0],self.db[selectedRowIndex][1]), title='Usuwanie wpisu z bazy')
#			if deletionConfirmed:
#				self.db.pop(selectedRowIndex)	
#				self.refresh_grid()
	def on_cancel(self):
		exit()
	
	def refresh_grid(self):
		self.gd.values = []
		for row in self.db:
			self.gd.values.append(row)
		self.gd.hidden = len(self.gd.values) == 0

class AddRecordForm(npyscreen.ActionPopup):
#	ms = None

#	def create(self):
#		self.ms = self.add(npyscreen.TitleSelectOne, max_height=7, value = [0,], name="Wybierz rekord:", values = records, #scroll_exit=True)
	def on_ok(self):
		#self.parentApp.getForm('MAIN').wgName.value = self.myName.value
		self.parentApp.switchFormPrevious();
	def on_cancel(self):
		self.parentApp.switchFormPrevious();

class RemoveRecordForm(npyscreen.ActionPopup):
	ms = None
	records = None
	def create(self):
		self.ms = self.add(npyscreen.TitleSelectOne, max_height=7, value = [0,], name="Wybierz rekord:", values = ['A','B','C'], scroll_exit=True)
	def on_ok(self):
		#self.parentApp.getForm('MAIN').wgName.value = self.myName.value
		self.parentApp.switchFormPrevious();
	def on_cancel(self):
		self.parentApp.switchFormPrevious();

if __name__ == "__main__":
	App = TestApp()
	App.run()





