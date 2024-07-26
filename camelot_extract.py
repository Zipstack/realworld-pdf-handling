import sys
import camelot

def error_exit(msg):
    print("Fatal error: " + msg)
    exit(1)

def main():
    # Extract tables from the PDF
    tables = camelot.read_pdf(sys.argv[1])

    # Print the number of tables extracted
    print(f"Number of tables extracted: {len(tables)}")

    # Print the first table
    print(tables[0].df)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        error_exit("No file provided")
    main()
