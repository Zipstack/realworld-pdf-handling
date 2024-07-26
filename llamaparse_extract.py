import sys
from dotenv import load_dotenv

# bring in deps
from llama_parse import LlamaParse
from llama_index.core import SimpleDirectoryReader

def main():
    # set up parser
    parser = LlamaParse(
        result_type="markdown"  # "markdown" and "text" are available
    )

    # use SimpleDirectoryReader to parse our file
    file_extractor = {".pdf": parser}
    documents = SimpleDirectoryReader(input_files=[sys.argv[1]], file_extractor=file_extractor).load_data()
    # If it's the Apple 10-Q, only print the text of the 13th page
    if "Apple_10-Q" in sys.argv[1]:
        print(documents[13].text)
    else:
        for doc in documents:
            print(doc.text)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("No file provided")
    load_dotenv()
    main()
