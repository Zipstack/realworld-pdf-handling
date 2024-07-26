import sys
from dotenv import load_dotenv
import os

import unstructured_client
from unstructured_client.models import operations, shared

def error_exit(error_message):
    print(error_message)
    sys.exit(1)

def main():
    client = unstructured_client.UnstructuredClient(
        api_key_auth=os.getenv("UNSTRUCTURED_API_KEY"),
        server_url=os.getenv("UNSTRUCTURED_API_URL"),
    )

    filename = sys.argv[1]
    with open(filename, "rb") as f:
        data = f.read()

    req = operations.PartitionRequest(
        partition_parameters=shared.PartitionParameters(
            files=shared.Files(
                content=data,
                file_name=filename,
            ),
            # --- Other partition parameters. ---
            strategy=shared.Strategy.AUTO,
            languages=['eng'],
        ),
    )

    try:
        res = client.general.partition(request=req)
        print("\n".join([str(el["text"]) for el in res.elements]))
    except Exception as e:
        print(e)

if __name__ == "__main__":
    load_dotenv()
    if len(sys.argv) < 2:
        error_exit("No file provided")
    main()
