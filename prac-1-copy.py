from borb.pdf.document.document import Document
from borb.pdf.page.page import Page
from borb.pdf.canvas.layout.page_layout.multi_column_layout import SingleColumnLayout
from borb.pdf.canvas.layout.page_layout.page_layout import PageLayout
from borb.pdf.canvas.layout.text.paragraph import Paragraph, Alignment
from borb.pdf.canvas.layout.table.fixed_column_width_table import FixedColumnWidthTable
from borb.pdf.pdf import PDF
from decimal import Decimal
from datetime import datetime
import random

def main():
    #Crear documento
    doc: Document = Document()

    #Crear pagina
    page: Page = Page()

    #Añadir pagina
    doc.append_page(page)

    #Seleccion de formato
    layout: PageLayout = SingleColumnLayout(page)

    now = datetime.now()
    text = 'Direccion'

    #Agregar informacion
    layout.add(
        FixedColumnWidthTable(number_of_rows=5, number_of_columns=3)
        .add(Paragraph(text))
        .add(Paragraph('%d/%d/%d' % (now.day, now.month, now.year)))
        .add(Paragraph('%d/%d/%d' % (now.day+15, now.month, now.year)))
        .add(Paragraph('[Ciudad, Estado, C.P.]'))
        .add(Paragraph('Factura #', font='Courier', horizontal_alignment=Alignment.RIGHT))
        .add(Paragraph('%d' % random.randint(1000, 10000)))

        .add(Paragraph('[Telefono]'))
        .add(Paragraph('Fecha de vencimiento', font='Courier', horizontal_alignment=Alignment.RIGHT))
        .add(Paragraph('%d%d%d' % (now.day+15, now.month, now.year)))

        .add(Paragraph('[Email Registrado]'))
        .add(Paragraph('ads'))
        .add(Paragraph('sad'))

        .add(Paragraph('[Sitio Web]'))
        .add(Paragraph('ds'))
        .add(Paragraph('sda'))
        .set_padding_on_all_cells(Decimal(2), Decimal(2), Decimal(2), Decimal(2))
        .no_borders()
    )

    #Importar
    with open('prueba.pdf', 'wb') as pdf_file_handle:
        PDF.dumps(pdf_file_handle, doc)

if __name__ == '__main__':
    main()