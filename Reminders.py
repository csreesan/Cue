import openpyxl


class Reminders:
    """ Reads from excel of tasks.
    """

    def __init__(self, name, sheet_name):
        self.name = name
        self.sheet_name = sheet_name
        self.wb = openpyxl.load_workbook('%s.xlsx' % self.sheet_name)
        self.sheet = self.wb.get_sheet_by_name('Sheet1')
        self.compose()

    def compose(self):
        msg = ''
        i = 2
        task = self.sheet.cell(row=i, column=1).value
        while task:  # due date should be adjusted in this
            due = self.sheet.cell(row=i, column=2).value
            msg += "%s due on %s<br>" % (task, due)
            i += 1
            task = self.sheet.cell(row=i, column=1).value
        msg = "Today you have %d things to do:<br>" % (i - 2) + msg
        return msg