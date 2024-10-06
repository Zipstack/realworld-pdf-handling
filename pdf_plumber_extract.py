import sys
import pdfplumber

def error_exit(msg):
    print("Fatal error: " + msg)
    exit(1)

def main():
    # Open the PDF file
    with pdfplumber.open(sys.argv[1]) as pdf:
        # Go through each page
        if "Apple_10-Q" in sys.argv[1]:
            pdf_pages = [pdf.pages[13]]
        else:
            pdf_pages = pdf.pages
        for page in pdf_pages:
            # Get tables from the current page
            table = page.extract_table()

            # Print the table data
            if table:
                for row in table:
                    print(row)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        error_exit("No file provided")
    main()
