# EIFF
This is a Basic Hexadecial Image File Format.
Named: Eduardo's Image File Format (EIFF)
EIFF is a custom image file format designed to store images in RGBA using hexadecimal values.

## Features

- **Write EIFF**: Convert PNG images to EIFF format.
- **Read EIFF**: Convert EIFF format back to PNG images.
- **Simple and Efficient**: Uses hexadecimal representation for RGBA values.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Eduardo7881/EIFF.git && cd EIFF
    ```

2. Install the required dependencies:
    You must have PIL and struct installed.

## Usage

### Writing EIFF Files

To convert a PNG image to an EIFF file, use the `write_eiff` function:

```python
from EIFF_util import write_eiff

input_png_path = 'path/to/your/image.png'
output_eiff_path = 'path/to/your/image.eiff'

write_eiff(input_png_path, output_eiff_path)
```

To read a EIFF file, use:

```python
from EIFF_util import read_eiff

input_eiff_path = 'path/to/your/image.eiff'
output_png_path = 'path/to/your/image_output.png'

image = read_eiff(input_eiff_path)
image.save(output_png_path)
```

## Interface
I made a basic text user interface (tui) using inputs.


how to launch (Linux/macOS):
```bash
python3 main.py
```


how to launch (Windows):
```bash
python main.py
```


on both systems, python must be on PATH


here to make something we have a code spinnet:

```python
from EIFF_util import write_eiff, read_eiff

def main():
    while True:
        print("EIFF")
        print("1. Read")
        print("2. Compile")
        print("3. Exit")
        input_entry = input("Select an option: ")
        
        try:
            input_entry = int(input_entry)
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue
        
        if input_entry == 1:
            input_entry1 = input("File path: ")
            image = read_eiff(input_entry1)
            output_path = input("Save as (output PNG path): ")
            image.save(output_path)
            print(f"Image saved as {output_path}")
        elif input_entry == 2:
            input_entry2 = input("File PNG Path (input): ")
            input_entry3 = input("File EIFF Path (output): ")
            write_eiff(input_entry2, input_entry3)
            print(f"Image compiled and saved as {input_entry3}")
        elif input_entry == 3:
            exit(0)
        else:
            print("Invalid input! Try again.")
            print()

if __name__ == "__main__":
    main()

```

## License
EIFF is free for everyone to use, but the code cannot be modified. All rights reserved.

## Contributing
Contributions are welcome, but any changes will be managed by me. If you find a issue submit it.

## Contact
For questions or support, please contact [eduardopna0@gmail.com].
