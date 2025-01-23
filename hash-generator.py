import hashlib
from pathlib import Path

def prehash(user_input):
    # Initialize the output as an empty byte string
    output_as_bytes = b""

    try:
        # Try to create a Path object for file checking
        input_path = Path(user_input)

        if input_path.is_file():
            # If the input is a file, read its contents
            try:
                with open(input_path, 'rb') as file:
                    output_as_bytes = file.read()
            except (IOError, OSError) as e:
                # Handle file reading errors
                print(f"Warning: Unable to read file '{user_input}': {e}")
                output_as_bytes = b""
        else:
            # If not a file, treat input as a string
            output_as_bytes = user_input.encode('utf-8')
    except Exception as e:
        # Handle any exceptions that occur during Path creation or encoding
        print(f"Warning: An error occurred while processing input: {e}")
        output_as_bytes = b""

    # The function always flows to this point
    return output_as_bytes

def md5_hash(data):
    return hashlib.md5(data).hexdigest()

def sha256_hash(data):
    return hashlib.sha256(data).hexdigest()

def main():
    import sys
    if len(sys.argv) < 3:
        print("Usage: python3 hash-generator.py <algorithm> <input>")
        return

    algorithm = sys.argv[1].lower()
    user_input = sys.argv[2]

    # Process input through prehash
    data = prehash(user_input)

    # Generate hash based on the selected algorithm
    if algorithm == "md5":
        print(md5_hash(data))
    elif algorithm == "sha256":
        print(sha256_hash(data))
    else:
        print(f"Warning: Unsupported algorithm '{algorithm}'. Use 'md5' or 'sha256'.")

if __name__ == "__main__":
    main()
