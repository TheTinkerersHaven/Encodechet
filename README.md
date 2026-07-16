# :sparkles: Encodechet :sparkles:	
### Now rewritten in Rust!

Encodechet is a fun, lightweight, and entirely **useless** encoder/decoder for text files that uses the custom `.edch` format. It's perfect for anyone looking to experiment with a quirky encoding system or to confuse their friends with unreadable file formats!

Encodechet uses the latest and greatest LERPC (Low Efficiency Really Poor enCoding) encoding system to guarantee the worst results possible with maximum storage utilization. You're welcome.

## Features

- Encode text files into the custom `.edch` format;
- Decode `.edch` files back into readable text;
- Completely useless but oddly satisfying to use;
- Confuse your friends (or enemies) by sending them a totally garbage unreadable file;
- Get laughed at every time you open an encoded .edch file.

## Why Use Encodechet?

This project exists purely for fun and experimentation. If you're curious about creating custom file formats or encoding mechanisms, Encodechet is a great example to explore!

## Why the name Encodechet?

It's a portmanteau of the words "Encode" and "Déchet" (French for "garbage"). It sums up the project pretty well and sounds sick (hell yeah).

## Prerequisites

- [Rust](https://www.rust-lang.org/) and Cargo installed.
- The `dechetCode.json` mapping file must sit next to the executable (the program loads it from the current working directory at runtime).

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/TheTinkerersHaven/Encodechet.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Encodechet
   ```
3. Build the project:
   ```bash
   cargo build --release
   ```

## Usage

Run the program from the project directory (so it can find `dechetCode.json`):

```bash
cargo run --release
```

Then follow the on-screen prompts:
1. Enter the path to the file you want to process (must end in `.txt` or `.edch`).
2. Choose `1` to **encode** a `.txt` file into `.edch`, or `0` to **decode** a `.edch` file back into `.txt`.

### Encoding a Text File
```
Enter the path to the file that must be encoded or decoded:
hello.txt
Decode an .edch file (0) or encode a .txt file (1)? Write one of the numbers in brackets:
1
```
This produces `hello.edch` next to the original file.

### Decoding a `.edch` File
```
Enter the path to the file that must be encoded or decoded:
hello.edch
Decode an .edch file (0) or encode a .txt file (1)? Write one of the numbers in brackets:
0
```
This produces `hello.txt` next to the original file.

## Example

Input text file (`hello.txt`):
```
Hello, Encodechet!
```

Encoded file (`hello.edch`):
```
HAHAAHHHHHAAAAHHAHAAHHHAHAAHHHAAHHAAHAHAAAHAAAAAAHAHAHHAHHAAHHHHHHAAHAHHAAHHAHHHAAAHHHHAAAAHHHAAHAHHAHHAHHHHAAAAHHAAAAHAHHHHHHAAAAAAA
```

Decoded back to text:
```
Hello, Encodechet!
```

## How It Works

Each supported character is mapped to a fixed 7-byte code made of `H` and `A`
(see `dechetCode.json`). Encoding replaces every character with its 7-byte code;
decoding reads the file 7 bytes at a time and looks each code back up. Only the
97 characters listed in `dechetCode.json` are supported — any unknown character
or code prints a warning and is skipped.

The Rust implementation keeps the mapping in memory and processes the whole file
in a single buffered pass, writing the result once at the end.

## Contributing

Contributions are welcome! If you have ideas for improving Encodechet or want to add your own flavor of uselessness, feel free to submit a pull request. 

## License

Use this as freely as you'd like, but don't expect anyone to understand why you did.
Officially, it's the [MIT License](LICENSE).

## Acknowledgments

- [@TheTinkerersHaven](https://github.com/TheTinkerersHaven) for coming up with this completely useless project (I'm a genius I know) and for the Rust rewrite
- [@Fleny113](https://github.com/Fleny113) for most of the original Python code
