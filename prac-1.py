from pathlib import Path
from borb.pdf.document.document import Document
from borb.pdf.page.page import Page
from borb.pdf.canvas.layout.page_layout.multi_column_layout import SingleColumnLayout, MultiColumnLayout
from borb.pdf.canvas.layout.page_layout.page_layout import PageLayout
from borb.pdf.canvas.layout.text.paragraph import Paragraph
from borb.pdf.canvas.layout.layout_element import Alignment
from borb.pdf.canvas.layout.table.fixed_column_width_table import FixedColumnWidthTable
from borb.pdf.canvas.layout.table.flexible_column_width_table import (FlexibleColumnWidthTable,)
from borb.pdf.canvas.layout.table.table import TableCell
from borb.pdf.canvas.layout.image.image import Image
from borb.pdf.canvas.color.color import HexColor
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
    layout: PageLayout = MultiColumnLayout(page, number_of_columns=1, horizontal_margin=Decimal(5), vertical_margin=Decimal(5))

    now = datetime.now()
    text = 'Direccion'

    #Agregar informacion
    layout.add(
        FixedColumnWidthTable(number_of_columns=3, number_of_rows=4, column_widths=[Decimal(1), Decimal(2), Decimal(1)])
        .add(TableCell(Paragraph('%d' % random.randint(700000000,700100000), font='Helvetica-bold', font_size=Decimal(16), horizontal_alignment=Alignment.CENTERED)))
        .add(TableCell(Paragraph('Remision de Factura', font='Helvetica-bold', font_size=Decimal(16), horizontal_alignment=Alignment.CENTERED, padding_top=Decimal(0.02)), col_span=2, background_color=HexColor('9D9D9D')))
        .add(TableCell(Image(
            Path('G:\Otros ordenadores\Mi PC (1)\fac-1\prueba.pdf'),
            width=Decimal(128),
            height=Decimal(48),
            horizontal_alignment=Alignment.CENTERED,
        ), row_span=3))
        .add(TableCell(Paragraph('Ferreteria Fereemas', font='Helvetica-bold', font_size=Decimal(13), horizontal_alignment=Alignment.CENTERED), col_span=2))
        .add(TableCell(Paragraph('Av. Abasolo #678 El Refugio, Ciudad Fernandez, San Luis Potosi, C.P. 79660', font='Helvetica', font_size=Decimal(10), horizontal_alignment=Alignment.CENTERED), col_span=2))
        .add(TableCell(Paragraph('Email: ferremas70@gmail.com   Facebook: ferremas10   WhatsApp/Telf: 487 114 68 73', font='Helvetica', font_size=Decimal(10), horizontal_alignment=Alignment.CENTERED), col_span=2))
        .set_padding_on_all_cells(Decimal(1), Decimal(2), Decimal(1), Decimal(2))
        .no_borders()
    )
    

    layout.add(
        FixedColumnWidthTable(number_of_rows=5, number_of_columns=3)
        .add(Paragraph(text, font='Helvetica'))
        .add(Paragraph('Date', font='Helvetica', horizontal_alignment=Alignment.RIGHT))
        .add(Paragraph('%d/%d/%d' % (now.day, now.month, now.year), font='Helvetica'))

        .add(Paragraph('[Ciudad, Estado, C.P.]', font='Helvetica', text_alignment=Alignment.CENTERED, vertical_alignment=Alignment.TOP))
        .add(Paragraph('Factura #', font='Helvetica', horizontal_alignment=Alignment.RIGHT))
        .add(Paragraph('%d' % random.randint(1000, 10000), font='Helvetica'))

        .add(Paragraph('[Telefono]', font='Helvetica'))
        .add(Paragraph('Fecha de vencimiento', font='Helvetica', horizontal_alignment=Alignment.RIGHT))
        .add(Paragraph('%d/%d/%d' % (now.day+15, now.month, now.year), font='Helvetica'))

        .add(Paragraph('[Email Registrado]', font='Helvetica'))
        .add(Paragraph(' ', font='Helvetica'))
        .add(Paragraph(' ', font='Helvetica'))

        .add(Paragraph('[Sitio Web]', font='Helvetica'))
        .add(Paragraph(' ', font='Helvetica'))
        .add(Paragraph(' ', font='Helvetica'))

        .set_padding_on_all_cells(Decimal(2), Decimal(2), Decimal(2), Decimal(2))
        #.no_borders()
    )

    #Importar
    with open('prueba.pdf', 'wb') as pdf_file_handle:
        PDF.dumps(pdf_file_handle, doc)

if __name__ == '__main__':
    main()