import sys
from dotenv import load_dotenv
from unstract.llmwhisperer.client import LLMWhispererClient, LLMWhispererClientException

def error_exit(error_message):
    print(error_message)
    sys.exit(1)

def extract_text_from_pdf(file_path, pages_list=None):
    llmw = LLMWhispererClient()
    try:
        result = llmw.whisper(file_path=file_path, pages_to_extract=pages_list)
        extracted_text = result["extracted_text"]
        return extracted_text
    except LLMWhispererClientException as e:
        error_exit(e)

def main():
    load_dotenv()
    if len(sys.argv) < 2:
        error_exit("No file provided")
    file_path = sys.argv[1]
    if "Apple_10-Q" in file_path:
        extracted_text = extract_text_from_pdf(file_path, pages_list=[13])
    else:
        extracted_text = extract_text_from_pdf(file_path)

    print(extracted_text)


if __name__ == "__main__":
    main()
