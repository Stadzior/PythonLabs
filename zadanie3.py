import npyscreen


class TestApp(npyscreen.NPSAppManaged):

	def onStart(self):
		self.addForm("MAIN", MainForm, name = "Zadanie 3",)

class MainForm(npyscreen.ActionForm):

	ml = None
	ms = None

	def create(self):
		self.ms = self.add(npyscreen.TitleSelectOne, max_height=7, value = [0,], name="Wybierz opcje:", values = ["Laduj baze z pliku","Zapisz baze do pliku", "Dodaj nowy wpis do bazy", "Usun wpis z bazy", "Wyswietl zawartosc bazy"], scroll_exit=True)
		self.add(npyscreen.FixedText, value = """Wpisz liste imion i nazwisko oddzielonych przecinkiem!\n""")
		self.ml = self.add(npyscreen.MultiLineEdit, max_height=5, rely=9)
	
	def on_ok(self):
		if self.ms.value[0] == 0:
			try:
				the_selected_file = npyscreen.selectFile()
			except:
				npyscreen.notify_confirm("Wybrany plik zawiera dane w nieobslugiwanym formacie", title="Blad ladowania bazy")
		elif self.ms.value[0] == 1:
			npyscreen.notify_confirm(self.buildMessageString(sorted(self.divideNames(self.ml.value), key=lambda x:x[1])))

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

    #	def spawn_file_dialog(self):
	#	the_selected_file = npyscreen.selectFile()
	#	npyscreen.notify_wait('That returned: {}'.format(the_selected_file), title='results')	

	def buildMessageString(self, names):
		string = ""
		for value in names:
			string += value[0] + " " + value[1] + "\n"

		return string
		

if __name__ == "__main__":
	App = TestApp()
	App.run()


