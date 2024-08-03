import os
from PyPDF2 import PdfReader, PdfWriter


def split_pdf(input_pdf_path, start_page=1, end_page=None):
    # Open the PDF file
    with open(input_pdf_path, 'rb') as file:
        reader = PdfReader(file)
        total_pages = len(reader.pages)

        if end_page is None:
            end_page = total_pages

        # Create a directory named after the PDF file
        pdf_name = os.path.splitext(os.path.basename(input_pdf_path))[0]
        output_dir = os.path.join(os.path.dirname(input_pdf_path), pdf_name)
        os.makedirs(output_dir, exist_ok=True)

        # Create PDF writers for odd and even pages
        odd_writer = PdfWriter()
        even_writer = PdfWriter()

        # Add pages to the respective writers
        for i in range(start_page - 1, end_page):
            page = reader.pages[i]
            if (i + 1) % 2 == 1:
                odd_writer.add_page(page)
            else:
                even_writer.insert_page(page, 0)  # Insert at the beginning to reverse order

        # Check if the number of odd pages is greater than even pages
        if len(odd_writer.pages) > len(even_writer.pages):
            # Add a blank page to the beginning of the even pages
            even_writer.insert_blank_page(index=0)

        # Save the odd pages
        odd_output_path = os.path.join(output_dir, f'odd_pages.pdf')
        with open(odd_output_path, 'wb') as odd_output_file:
            odd_writer.write(odd_output_file)

        # Save the even pages
        even_output_path = os.path.join(output_dir, f'even_pages_reversed.pdf')
        with open(even_output_path, 'wb') as even_output_file:
            even_writer.write(even_output_file)

        print(f'Odd pages saved to: {odd_output_path}')
        print(f'Even pages saved to: {even_output_path}')


# Example usage
pdf_path = r'C:/Users/zeyad/Documents/Books/SelfImprove/Drawing For Beginners  The Ultimate Crash Course to Learning the Basics of How to Draw In No Time (Taggart, Amy) (Z-Library).pdf'
split_pdf(pdf_path, start_page=40, end_page=100)
