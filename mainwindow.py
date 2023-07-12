import sys
from PySide6.QtCore import QFile
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader

app = QApplication(sys.argv)

ui_file_name = "application.ui"
ui_file = QFile(ui_file_name)
loader = QUiLoader()
window = loader.load(ui_file)
ui_file.close()
if not window:
    print(loader.errorString())
    sys.exit(-1)
window.show()

sys.exit(app.exec())
