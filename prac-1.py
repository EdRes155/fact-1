from pathlib import Path
from subprocess import HIGH_PRIORITY_CLASS
from this import d
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
from borb.pdf.canvas.color.color import HexColor, X11Color
from borb.pdf.pdf import PDF
from decimal import Decimal
from datetime import datetime
import random

from bs4 import PageElement
from sqlalchemy import false

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
    tam = Decimal(8)
    n = Decimal(5)
    clt = random.randint(7000, 7800)

    #Agregar informacion
    layout.add(
        FixedColumnWidthTable(number_of_columns=3, number_of_rows=4, column_widths=[Decimal(1), Decimal(2), Decimal(1)])
        .add(TableCell(Paragraph(
            '%d' % random.randint(700000000,700100000),
            font='Helvetica-bold', font_size=Decimal(14),
            horizontal_alignment=Alignment.CENTERED,
            padding_bottom=n,
        )))
        .add(TableCell(Paragraph(
            'Remision de Factura',
            font='Helvetica-bold',
            font_size=Decimal(14),
            horizontal_alignment=Alignment.CENTERED,
            padding_bottom=n,
            ), col_span=2, background_color=HexColor('9D9D9D')))
        .add(TableCell(Image(
            Path('C:/Users/resen/Documents/fac-1/Sin-fondo.png'),
            width=Decimal(128),
            height=Decimal(48),
            horizontal_alignment=Alignment.CENTERED,
        ), row_span=3))
        .add(TableCell(Paragraph(
            'Ferreteria Fereemas',
            font='Helvetica-bold',
            font_size=Decimal(12),
            horizontal_alignment=Alignment.CENTERED
            ), col_span=2))
        .add(TableCell(Paragraph('Av. Abasolo #678 El Refugio, Ciudad Fernandez, San Luis Potosi, C.P. 79660',
        font='Helvetica',
        font_size=Decimal(10),
        horizontal_alignment=Alignment.CENTERED
        ), col_span=2))
        .add(TableCell(Paragraph('Email: ferremas70@gmail.com   Facebook: ferremas10   WhatsApp/Telf: 4871146873',
        font='Helvetica',
        font_size=Decimal(10),
        horizontal_alignment=Alignment.CENTERED
        ), col_span=2))
        .set_padding_on_all_cells(Decimal(1), Decimal(2), Decimal(1), Decimal(2))
        .no_borders()
    )
    

    layout.add(
        FixedColumnWidthTable(number_of_rows=9, number_of_columns=4)
        .add(TableCell(Paragraph(
            'Cliente: %d' % clt,
            font='Helvetica-bold',
            font_size=tam,
            padding_bottom=Decimal(2.5)
        ), col_span=2, background_color=HexColor('9D9D9D')))
        .add(TableCell(Paragraph(
            'Destinatario',
            font='Helvetica-bold',
            font_size=tam,
            padding_bottom=Decimal(2.5)
        ), col_span=2, background_color=HexColor('9D9D9D')))
        .add(TableCell(Paragraph(
            'Heriberto Resendiz Rodriguez',
            font='Helvetica',
            font_size=tam,
            padding_bottom=False,
            padding_top=False
        ), col_span=2))
        .add(TableCell(Paragraph(
            'Edwin Missael Resendiz Rostro', 
            font='Helvetica',
            font_size=tam,
            padding_bottom=False,
            padding_top=False
        ), col_span=2))
        .add(TableCell(Paragraph(
            'Av Abasolo #678',
            font='Helvetica',
            font_size=tam,
        ), col_span=2))
        .add(TableCell(Paragraph(
            'Av Abasolo #678',
            font='Helvetica',
            font_size=tam,
        ), col_span=2))
        .add(TableCell(Paragraph(
            'El Refugio, Ciudad Fernandez',
            font='Helvetica',
            font_size=tam,
        ), col_span=2))
        .add(TableCell(Paragraph(
            'El Refugio, Ciudad Fernandez',
            font='Helvetica',
            font_size=tam,
        ), col_span=2))
        .add(TableCell(Paragraph(
            "San Luis Potosi, Mexico",
            font='Helvetica',
            font_size=tam,
        ), col_span=2))
        .add(TableCell(Paragraph(
            'San Luis Potosi, Mexico',
            font='Helvetica',
            font_size=tam,
        ), col_span=2))
        .add(TableCell(Paragraph(
            'C.P. 79660',
            font='Helvetica',
            font_size=tam,
            ), col_span=2))
        .add(TableCell(Paragraph(
            'C.P. 79660',
            font='Helvetica',
            font_size=tam,
            ), col_span=2))
        .add(TableCell(Paragraph(
            'RFC: RERH761211H76',
            font='Helvetica',
            font_size=tam,
            ), col_span=2))
        .add(TableCell(Paragraph(
            ' ',
            font='Helvetica',
            font_size=tam,
            ), col_span=2))
        .add(TableCell(Paragraph(
            'Telf. 4871036922',
            font='Helvetica',
            font_size=tam,
            ), col_span=2))
        .add(TableCell(Paragraph(
            ' ',
            font='Helvetica',
            font_size=tam,
            ), col_span=2))
        .add(TableCell(Paragraph(
            'Email: heriberto.rodriguez123@hotmail.com',
            font='Helvetica',
            font_size=tam,
            ), col_span=2))
        .add(TableCell(Paragraph(
            ' ',
            font='Helvetica',
            font_size=tam,
            ), col_span=2))
        .set_padding_on_all_cells(Decimal(0.5), Decimal(0.5), Decimal(0.5), Decimal(0.5))
        .no_borders()
    )

    layout.add(
        FixedColumnWidthTable(number_of_columns=3, number_of_rows=2, column_widths=(Decimal(1), Decimal(2), Decimal(1)))
        .add(TableCell(Paragraph(
            'Inicio de credito',
            font='Helvetica',
            font_size=tam,
            padding_bottom=Decimal(2.5),
            horizontal_alignment=Alignment.CENTERED
        ), background_color=HexColor('9D9D9D')))
        .add(TableCell(Paragraph(
            'Condicion de pago',
            font='Helvetica',
            font_size=tam,
            padding_bottom=Decimal(2.5),
            horizontal_alignment=Alignment.CENTERED
        ), background_color=HexColor('9D9D9D')))
        .add(TableCell(Paragraph(
            'Vencimiento',
            font='Helvetica',
            font_size=tam,
            padding_bottom=Decimal(2.5),
            horizontal_alignment=Alignment.CENTERED
        ), background_color=HexColor('9D9D9D')))
        .add(Paragraph(
            '%d/%d/%d' % (now.day, now.month, now.year),
            font='Helvetica',
            font_size=tam,
            padding_bottom=Decimal(2.5),
            horizontal_alignment=Alignment.CENTERED
        ))
        .add(Paragraph(
            '15 Dias',
            font='Helvetica',
            font_size=tam,
            padding_bottom=Decimal(2.5),
            horizontal_alignment=Alignment.CENTERED
        ))
        .add(Paragraph(
            '%d/%d/%d' % (now.day+15, now.month, now.year),
            font='Helvetica',
            font_size=tam,
            padding_bottom=Decimal(2.5),
            horizontal_alignment=Alignment.CENTERED
        ))
        .set_padding_on_all_cells(Decimal(1), Decimal(1), Decimal(1), Decimal(1))
        .no_borders()
    )

    layout.add(
        FixedColumnWidthTable(number_of_columns=5, number_of_rows=1, column_widths=(Decimal(0.8), Decimal(2.5), Decimal(0.6), Decimal(0.5), Decimal(0.8)))
        .add(Paragraph(
            'Codigo',
            font='Helvetica-bold',
            font_size=tam,
            horizontal_alignment=Alignment.CENTERED,
            padding_bottom=Decimal(2.5),
            padding_top=Decimal(0.02)
        ))
        .add(Paragraph(
            'Descripcion',
            font='Helvetica-bold',
            font_size=tam,
            horizontal_alignment=Alignment.CENTERED,
            padding_bottom=Decimal(2.5),
            padding_top=Decimal(0.02)
        ))
        .add(Paragraph(
            'Precio Unitario',
            font='Helvetica-bold',
            font_size=tam,
            horizontal_alignment=Alignment.CENTERED,
            padding_bottom=Decimal(2.5),
            padding_top=Decimal(0.02)
        ))
        .add(Paragraph(
            'Cantidad',
            font='Helvetica-bold',
            font_size=tam,
            horizontal_alignment=Alignment.CENTERED,
            padding_bottom=Decimal(2.5),
            padding_top=Decimal(0.02)
        ))
        .add(Paragraph(
            'Importe',
            font='Helvetica-bold',
            font_size=tam,
            horizontal_alignment=Alignment.CENTERED,
            padding_bottom=Decimal(2.5),
            padding_top=Decimal(0.02)
        ))
        .set_padding_on_all_cells(Decimal(1), Decimal(1), Decimal(1), Decimal(1))
        .set_background_color_on_all_cells(HexColor('9D9D9D'))
        .no_borders()
    )

    layout.add(
        FixedColumnWidthTable(number_of_columns=5, number_of_rows=10, column_widths=(Decimal(0.8), Decimal(2.5), Decimal(0.6), Decimal(0.5), Decimal(0.8)))
        .add(Paragraph(
            'CEMMOC',
            font='Helvetica',
            font_size=tam,
            padding_bottom=Decimal(2.5),
            horizontal_alignment=Alignment.CENTERED
        ))
        .add(Paragraph(
            'Bulto Cemento Moctezuma 50KGS',
            font='Helvetica',
            font_size=tam,
            padding_bottom=Decimal(2.5),
        ))
        .add(Paragraph(
            '$  205.00',
            font='Helvetica',
            font_size=tam,
            padding_bottom=Decimal(2.5),
            horizontal_alignment=Alignment.RIGHT
        ))
        .add(Paragraph(
            '10',
            font='Helvetica',
            font_size=tam,
            padding_bottom=Decimal(2.5),
            horizontal_alignment=Alignment.CENTERED
        ))
        .add(Paragraph(
            '$  2050.00',
            font='Helvetica',
            font_size=tam,
            padding_bottom=Decimal(2.5),
            horizontal_alignment=Alignment.RIGHT
        ))
        .add(Paragraph(
            'CEMMOC',
            font='Helvetica',
            font_size=tam,
            padding_bottom=Decimal(2.5),
            horizontal_alignment=Alignment.CENTERED
        ))
        .add(Paragraph(
            'Bulto Cemento Moctezuma 50KGS',
            font='Helvetica',
            font_size=tam,
            padding_bottom=Decimal(2.5),
        ))
        .add(Paragraph(
            '$  205.00',
            font='Helvetica',
            font_size=tam,
            padding_bottom=Decimal(2.5),
            horizontal_alignment=Alignment.RIGHT
        ))
        .add(Paragraph(
            '10',
            font='Helvetica',
            font_size=tam,
            padding_bottom=Decimal(2.5),
            horizontal_alignment=Alignment.CENTERED
        ))
        .add(Paragraph(
            '$  2050.00',
            font='Helvetica',
            font_size=tam,
            padding_bottom=Decimal(2.5),
            horizontal_alignment=Alignment.RIGHT
        ))
        .add(Paragraph(
            'CEMMOC',
            font='Helvetica',
            font_size=tam,
            padding_bottom=Decimal(2.5),
            horizontal_alignment=Alignment.CENTERED
        ))
        .add(Paragraph(
            'Bulto Cemento Moctezuma 50KGS',
            font='Helvetica',
            font_size=tam,
            padding_bottom=Decimal(2.5),
        ))
        .add(Paragraph(
            '$  205.00',
            font='Helvetica',
            font_size=tam,
            padding_bottom=Decimal(2.5),
            horizontal_alignment=Alignment.RIGHT
        ))
        .add(Paragraph(
            '10',
            font='Helvetica',
            font_size=tam,
            padding_bottom=Decimal(2.5),
            horizontal_alignment=Alignment.CENTERED
        ))
        .add(Paragraph(
            '$  2050.00',
            font='Helvetica',
            font_size=tam,
            padding_bottom=Decimal(2.5),
            horizontal_alignment=Alignment.RIGHT
        ))
        .add(Paragraph(
            'CEMMOC',
            font='Helvetica',
            font_size=tam,
            padding_bottom=Decimal(2.5),
            horizontal_alignment=Alignment.CENTERED
        ))
        .add(Paragraph(
            'Bulto Cemento Moctezuma 50KGS',
            font='Helvetica',
            font_size=tam,
            padding_bottom=Decimal(2.5),
        ))
        .add(Paragraph(
            '$  205.00',
            font='Helvetica',
            font_size=tam,
            padding_bottom=Decimal(2.5),
            horizontal_alignment=Alignment.RIGHT
        ))
        .add(Paragraph(
            '10',
            font='Helvetica',
            font_size=tam,
            padding_bottom=Decimal(2.5),
            horizontal_alignment=Alignment.CENTERED
        ))
        .add(Paragraph(
            '$  2050.00',
            font='Helvetica',
            font_size=tam,
            padding_bottom=Decimal(2.5),
            horizontal_alignment=Alignment.RIGHT
        ))
        .add(Paragraph(
            'CEMMOC',
            font='Helvetica',
            font_size=tam,
            padding_bottom=Decimal(2.5),
            horizontal_alignment=Alignment.CENTERED
        ))
        .add(Paragraph(
            'Bulto Cemento Moctezuma 50KGS',
            font='Helvetica',
            font_size=tam,
            padding_bottom=Decimal(2.5),
        ))
        .add(Paragraph(
            '$  205.00',
            font='Helvetica',
            font_size=tam,
            padding_bottom=Decimal(2.5),
            horizontal_alignment=Alignment.RIGHT
        ))
        .add(Paragraph(
            '10',
            font='Helvetica',
            font_size=tam,
            padding_bottom=Decimal(2.5),
            horizontal_alignment=Alignment.CENTERED
        ))
        .add(Paragraph(
            '$  2050.00',
            font='Helvetica',
            font_size=tam,
            padding_bottom=Decimal(2.5),
            horizontal_alignment=Alignment.RIGHT
        ))
        .add(Paragraph(
            'CEMMOC',
            font='Helvetica',
            font_size=tam,
            padding_bottom=Decimal(2.5),
            horizontal_alignment=Alignment.CENTERED
        ))
        .add(Paragraph(
            'Bulto Cemento Moctezuma 50KGS',
            font='Helvetica',
            font_size=tam,
            padding_bottom=Decimal(2.5),
        ))
        .add(Paragraph(
            '$  205.00',
            font='Helvetica',
            font_size=tam,
            padding_bottom=Decimal(2.5),
            horizontal_alignment=Alignment.RIGHT
        ))
        .add(Paragraph(
            '10',
            font='Helvetica',
            font_size=tam,
            padding_bottom=Decimal(2.5),
            horizontal_alignment=Alignment.CENTERED
        ))
        .add(Paragraph(
            '$  2050.00',
            font='Helvetica',
            font_size=tam,
            padding_bottom=Decimal(2.5),
            horizontal_alignment=Alignment.RIGHT
        ))
        .add(Paragraph(
            'CEMMOC',
            font='Helvetica',
            font_size=tam,
            padding_bottom=Decimal(2.5),
            horizontal_alignment=Alignment.CENTERED
        ))
        .add(Paragraph(
            'Bulto Cemento Moctezuma 50KGS',
            font='Helvetica',
            font_size=tam,
            padding_bottom=Decimal(2.5),
        ))
        .add(Paragraph(
            '$  205.00',
            font='Helvetica',
            font_size=tam,
            padding_bottom=Decimal(2.5),
            horizontal_alignment=Alignment.RIGHT
        ))
        .add(Paragraph(
            '10',
            font='Helvetica',
            font_size=tam,
            padding_bottom=Decimal(2.5),
            horizontal_alignment=Alignment.CENTERED
        ))
        .add(Paragraph(
            '$  2050.00',
            font='Helvetica',
            font_size=tam,
            padding_bottom=Decimal(2.5),
            horizontal_alignment=Alignment.RIGHT
        ))
        .add(Paragraph(
            'CEMMOC',
            font='Helvetica',
            font_size=tam,
            padding_bottom=Decimal(2.5),
            horizontal_alignment=Alignment.CENTERED
        ))
        .add(Paragraph(
            'Bulto Cemento Moctezuma 50KGS',
            font='Helvetica',
            font_size=tam,
            padding_bottom=Decimal(2.5),
        ))
        .add(Paragraph(
            '$  205.00',
            font='Helvetica',
            font_size=tam,
            padding_bottom=Decimal(2.5),
            horizontal_alignment=Alignment.RIGHT
        ))
        .add(Paragraph(
            '10',
            font='Helvetica',
            font_size=tam,
            padding_bottom=Decimal(2.5),
            horizontal_alignment=Alignment.CENTERED
        ))
        .add(Paragraph(
            '$  2050.00',
            font='Helvetica',
            font_size=tam,
            padding_bottom=Decimal(2.5),
            horizontal_alignment=Alignment.RIGHT
        ))
        .add(Paragraph(
            'CEMMOC',
            font='Helvetica',
            font_size=tam,
            padding_bottom=Decimal(2.5),
            horizontal_alignment=Alignment.CENTERED
        ))
        .add(Paragraph(
            'Bulto Cemento Moctezuma 50KGS',
            font='Helvetica',
            font_size=tam,
            padding_bottom=Decimal(2.5),
        ))
        .add(Paragraph(
            '$  205.00',
            font='Helvetica',
            font_size=tam,
            padding_bottom=Decimal(2.5),
            horizontal_alignment=Alignment.RIGHT
        ))
        .add(Paragraph(
            '10',
            font='Helvetica',
            font_size=tam,
            padding_bottom=Decimal(2.5),
            horizontal_alignment=Alignment.CENTERED
        ))
        .add(Paragraph(
            '$  2050.00',
            font='Helvetica',
            font_size=tam,
            padding_bottom=Decimal(2.5),
            horizontal_alignment=Alignment.RIGHT
        ))
        .add(Paragraph(
            'CEMMOC',
            font='Helvetica',
            font_size=tam,
            padding_bottom=Decimal(2.5),
            horizontal_alignment=Alignment.CENTERED
        ))
        .add(Paragraph(
            'Bulto Cemento Moctezuma 50KGS',
            font='Helvetica',
            font_size=tam,
            padding_bottom=Decimal(2.5),
        ))
        .add(Paragraph(
            '$  205.00',
            font='Helvetica',
            font_size=tam,
            padding_bottom=Decimal(2.5),
            horizontal_alignment=Alignment.RIGHT
        ))
        .add(Paragraph(
            '10',
            font='Helvetica',
            font_size=tam,
            padding_bottom=Decimal(2.5),
            horizontal_alignment=Alignment.CENTERED
        ))
        .add(Paragraph(
            '$  2050.00',
            font='Helvetica',
            font_size=tam,
            padding_bottom=Decimal(2.5),
            horizontal_alignment=Alignment.RIGHT
        ))
        .set_padding_on_all_cells(Decimal(1), Decimal(1), Decimal(1), Decimal(1))
        .even_odd_row_colors(X11Color('LightGray'), X11Color('White'))
        .no_borders()
    )

    layout.add(
        FixedColumnWidthTable(number_of_columns=2, number_of_rows=3, column_widths=(Decimal(3), Decimal(1)))
        .add(Paragraph(
            'Subtotal:',
            font='Helvetica-bold',
            font_size=tam,
            padding_bottom=Decimal(2.5),
            horizontal_alignment=Alignment.RIGHT
        ))
        .add(Paragraph(
            '$  205000.00',
            font='Helvetica',
            font_size=tam,
            padding_bottom=Decimal(2.5),
            horizontal_alignment=Alignment.RIGHT
        ))
        .add(Paragraph(
            'Anticipo:',
            font='Helvetica-bold',
            font_size=tam,
            padding_bottom=Decimal(2.5),
            horizontal_alignment=Alignment.RIGHT
        ))
        .add(Paragraph(
            '$  00.00',
            font='Helvetica',
            font_size=tam,
            padding_bottom=Decimal(2.5),
            horizontal_alignment=Alignment.RIGHT
        ))
        .add(Paragraph(
            'Total:',
            font='Helvetica-bold',
            font_size=tam,
            padding_bottom=Decimal(2.5),
            horizontal_alignment=Alignment.RIGHT
        ))
        .add(Paragraph(
            '$  205000.00',
            font='Helvetica',
            font_size=tam,
            padding_bottom=Decimal(2.5),
            horizontal_alignment=Alignment.RIGHT
        ))
        .set_padding_on_all_cells(Decimal(1), Decimal(1), Decimal(1), Decimal(1))
        .no_borders()
    )

    #Importar
    with open('prueba.pdf', 'wb') as pdf_file_handle:
        PDF.dumps(pdf_file_handle, doc)

if __name__ == '__main__':
    main()