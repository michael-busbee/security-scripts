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

   
    list_email_headers(input_path)


def details(file_path):
    # Open the .eml file in binary mode
    with open(file_path, 'rb') as eml_file:
        # Parse the email using BytesParser with default policy
        msg = BytesParser(policy=policy.default).parse(eml_file)
    
    # Extract headers
    subject = msg['subject']
    from_email = msg['from']
    to_email = msg['to']
    date = msg['date']

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

    # Print extracted information
    print("Subject:", subject)
    print("From:", from_email)
    print("To:", to_email)
    print("Date:", date)
    print("\nBody:\n", body)

def list_email_headers(file_path):
    # Open the .eml file in binary mode
    with open(file_path, 'rb') as eml_file:
        # Parse the email using BytesParser with default policy
        msg = BytesParser(policy=policy.default).parse(eml_file)
    
    # Get all headers as a list of (header_name, value) tuples
    headers = msg.items()

    # Print all headers
    print("Email Headers:")
    for header, value in headers:
        print(f"{header}: {value}")


if __name__ == "__main__":
    main()
