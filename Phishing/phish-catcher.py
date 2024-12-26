import argparse
import email
from email import policy
from email.parser import BytesParser

def main():
    parser = argparse.ArgumentParser(
        description="A script with multiple flags for input, output, and more."
    )
    
    # Add the -h/--help flag (this is automatically added by argparse)

    # Add -i/--input flag to specify input path
    parser.add_argument(
        '-i', '--input', 
        type=str, 
        required=True, 
        help="Specify the input file path."
    )

    # Add -o/--output flag to specify output path
    parser.add_argument(
        '-o', '--output', 
        type=str, 
        required=False, 
        help="Specify the output file path."
    )

    # Placeholder for future flags
    # parser.add_argument('-x', '--example', help="Example flag for future use.")
   
    args = parser.parse_args()

    input_path = args.input
    output_path = args.output

    report(input_path)

def parse(file_path):
    # Open the .eml file in binary mode
    with open(file_path, 'rb') as eml_file:
        # Parse the email using BytesParser with default policy
        msg = BytesParser(policy=policy.default).parse(eml_file)

    # Extract email body
    if msg.is_multipart():
        # Get the text/plain part
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                body = part.get_content()
                break
        else:
            body = None
    else:
        body = msg.get_content()
    
    headers = msg.items()

    # Return extracted body
    return headers, body

def headers(file_path):
    # Open the .eml file in binary mode
    with open(file_path, 'rb') as eml_file:
        # Parse the email using BytesParser with default policy
        msg = BytesParser(policy=policy.default).parse(eml_file)
    
    # Get all headers as a list of (header_name, value) tuples
    
    # Print all headers
    """print("Email Headers:")
    for header, value in headers:
        print(f"{header}: {value}")"""

def report(input_path):
    filename = input_path.replace("\\", "/").split("/")[-1]
    headers, body = parse(input_path)
    headers_dict = dict(headers)

    print(f"\nReport of email: {filename}\n")
    print("=" * 100)
    print()
    print(f"From: {headers_dict['From']}")
    print(f"Return-Path: {headers_dict['Return-Path']}")

if __name__ == "__main__":
    main()
