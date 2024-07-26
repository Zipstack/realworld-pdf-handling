import sys
import pdfplumber

def error_exit(msg):
    print("Fatal error: " + msg)
    exit(1)

def main():
    # Open the PDF file
    with pdfplumber.open(sys.argv[1]) as pdf:
        # Go through each page
        for page in pdf.pages:
            # Get tables from the current page
            tables = page.extract_table()

            # Print the table data
            print(tables)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        error_exit("No file provided")
    main()
