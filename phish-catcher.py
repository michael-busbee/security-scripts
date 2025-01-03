import os
import argparse
import email
from email import policy
from email.parser import BytesParser
import hashlib

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

    # Scan once if input is a .eml file
    if os.path.isfile(input_path):
        if input_path.endswith(".eml"):
            report(input_path)
        else:
            print(f"Error: The file '{input_path}' is not a .eml file.")
    # Scan all .eml files if input is a directory
    elif os.path.isdir(input_path):
        for file_name in os.listdir(input_path):
            file_path = os.path.join(input_path, file_name)
            if os.path.isfile(file_path) and file_name.endswith(".eml"):
                report(file_path)

def parse(file_path):
    # Open the .eml file in binary mode
    with open(file_path, 'rb') as eml_file:
        # Parse the email using BytesParser with default policy
        try:
            msg = BytesParser(policy=policy.default).parse(eml_file)
        except Exception as e:
            print("Error parsing file")

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

    # Grab Attachments
    attachments = []
    for part in msg.iter_attachments():
        content_type = part.get_content_type()
        filename = part.get_filename()
        content = part.get_content()
        size = len(content) if content else 0
        attachments.append({
            'filename': filename,
            'content_type': content_type,
            'size': size,
            'content': content
        })

    headers_array = msg.items()

    return headers_array, body, attachments

def check_timestamp(headers):
    timestamp = headers['Date']
    print(f"Timestamp: {timestamp}")

def check_spoofed_from(headers, body, attachments):
    from_header = headers['From']
    reply_to_header = headers.get('Reply-To')

    # Check if file has Reply-To header
    if reply_to_header:
        reply_to_header = headers['Reply-To']
        if from_header != reply_to_header:
            print("'From' and 'Reply-To' headers are inconsistent:\n")
            print(f"From: {from_header}")
            print(f"Reply-To: {reply_to_header}")
    
def check_attachments(headers, body, attachments):
    
    for item in attachments:
        sha256_hash = hashlib.sha256(item['content']).hexdigest()
        print(f"Filename: {item['filename']}")
        print(f"Content Type: {item['content_type']}")
        print(f"Size: {item['size']}")
        print(f"sha256 hash: {sha256_hash}")

def check_IOCs(headers, body, attachments):
    
    #print(headers)
    print(body)
    return

def print_report_item(funct, headers, body, attachments):
    print()
    result = funct(headers, body, attachments)
    if result is not None:
        print(result)
    print()
    print("-" * 100)

def report(input_path):
    filename = input_path.replace("\\", "/").split("/")[-1]
    headers_array, body, attachments = parse(input_path)
    headers = dict(headers_array)
    red_flag_checks = [
        check_spoofed_from,
        check_attachments,
        check_IOCs
    ]

    print("=" * 100)
    print(f"\nReport of email: {filename}")
    check_timestamp(headers)
    print("-" * 100)

    # Only print checks that fail
    for check in red_flag_checks:
        if check(headers, body, attachments) != None:
            if attachments != []:
                print_report_item(check, headers, body, attachments)
    
    print()
    print("=" * 100)


if __name__ == "__main__":
    main()
