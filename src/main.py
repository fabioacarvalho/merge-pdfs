from PySide6.QtWidgets import QDialog, QApplication, QFileDialog, QMessageBox
from design import Ui_Dialog
import PyPDF2 as pydf
import os
import sys


class MainDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        # Conectar botões às funções
        self.search_btn1.clicked.connect(lambda: self.get_file(1))
        self.search_btn2.clicked.connect(lambda: self.get_file(2))
        self.merge_btn.clicked.connect(self.merge_pdfs)

    def get_file(self, file_number):
        """Abre um diálogo para selecionar um arquivo PDF e exibe o caminho no QTextBrowser correspondente."""
        file_path, _ = QFileDialog.getOpenFileName(self, "Select PDF", "", "PDF Files (*.pdf)")
        if file_path:
            if file_number == 1:
                self.location1.setText(file_path)
            elif file_number == 2:
                self.location2.setText(file_path)

    def merge_pdfs(self):
        """Realiza o merge dos PDFs selecionados."""
        pdf1_path = self.location1.toPlainText()
        pdf2_path = self.location2.toPlainText()

        if not pdf1_path or not pdf2_path:
            QMessageBox.warning(self, "Warning", "Please select both PDF files before merging!")
            return

        # Perguntar onde salvar o arquivo resultante
        save_path, _ = QFileDialog.getSaveFileName(self, "Save Merged PDF", "", "PDF Files (*.pdf)")
        if not save_path:
            return

        try:
            # Realizar o merge dos PDFs
            pdf_writer = pydf.PdfWriter()

            for pdf_path in [pdf1_path, pdf2_path]:
                with open(pdf_path, "rb") as pdf_file:
                    reader = pydf.PdfReader(pdf_file)
                    for page in reader.pages:
                        pdf_writer.add_page(page)

            # Salvar o arquivo combinado
            with open(save_path, "wb") as output_file:
                pdf_writer.write(output_file)

            self.result_text.setText(f"Merged PDF saved at: {save_path}")
            QMessageBox.information(self, "Success", "PDFs merged successfully!")

            # Limpar os campos após o processo
            self.location1.clear()
            self.location2.clear()
            self.result_text.clear()
        except Exception as e:
            self.result_text.setText("An error occurred during the merging process.")
            QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainDialog()
    window.show()
    app.exec()
