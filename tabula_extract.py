import sys
import tabula

def error_exit(msg):
    print("Fatal error: " + msg)
    exit(1)

def main():
    # Extract tables from the PDF
    if "Apple_10-Q" in sys.argv[1]:
        tables = tabula.read_pdf(sys.argv[1], pages=14)
    else:
        tables = tabula.read_pdf(sys.argv[1], pages='all')

    # Print the number of tables extracted
    print(f"Number of tables extracted: {len(tables)}")

    # Print the first table
    for table in tables:
        print(table)
        print("\n\n")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        error_exit("No file provided")
    main()
