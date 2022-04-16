from borb.pdf.document.document import Document
from borb.pdf.page.page import Page
from borb.pdf.canvas.layout.table.table import Table
from borb.pdf.pdf import PDF
from borb.pdf.canvas.layout.page_layout.page_layout import PageLayout
from borb.io.read.types import Decimal
from borb.pdf.canvas.layout.text.paragraph import Paragraph, Alignment
from borb.pdf.canvas.layout.page_layout.multi_column_layout import SingleColumnLayout
from datetime import datetime
import random

def _build_invoice_information():
    table_001 = Table(number_of_rows=5, number_of_columns=3)

    text='Direccion Empresa'

    table_001.add(Paragraph(text))
    table_001.add(Paragraph('Date', font='Courier', horizontal_alignment=Alignment.RIGHT))
    now = datetime.now()
    table_001.add(Paragraph('%d%d%d' % (now.day, now.month, now.year)))

    table_001.add(Paragraph('[Ciudad, Estado, C.P.]'))
    table_001.add(Paragraph('Factura #', font='Courier', horizontal_alignment=Alignment.RIGHT))
    table_001.add(Paragraph('%d' % random.randint(1000, 10000)))

    table_001.add(Paragraph('[Telefono]'))
    table_001.add(Paragraph('Fecha de vencimiento', font='Courier', horizontal_alignment=Alignment.RIGHT))
    table_001.add(Paragraph('%d%d%d' % (now.day+15, now.month, now.year)))

    table_001.add(Paragraph('[Email Registrado]'))
    table_001.add(Paragraph(''))
    table_001.add(Paragraph(''))

    table_001.add(Paragraph('[Sitio Web]'))
    table_001.add(Paragraph(''))
    table_001.add(Paragraph(''))

    table_001.set_padding_on_all_cells(Decimal(2), Decimal(2), Decimal(2), Decimal(2))
    table_001.no_borders()
    return table_001

#Crear el documento
doc: Document=  Document()

#Añadir paginas
page: Page = Page()
doc.append_page(page)

page_layout: PageLayout = SingleColumnLayout(page)
page_layout._vertical_margin = page.get_page_info().get_height() * Decimal(0.02)

#Añadir logo de la empresa
"""page_layout.add(
    Image(
        'C:/Users/resen/Documents/fac-1/Sin-fondo.png',
        width=Decimal(128),
        height=Decimal(128),
    )
)"""

#Datos de la empresa
page_layout.add(_build_invoice_information())
page_layout.add(Paragraph(' '))

#Importar Documento
with open('prueba.pdf', 'wb') as pdf_file_handle:
    PDF.dumps(pdf_file_handle, doc)
