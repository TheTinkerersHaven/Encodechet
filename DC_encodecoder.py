import json

# Load the dechetCode into memory as a dictionary
with open("dechetCode.json", "r") as f:             
    dechetCode = json.loads(f.read())

# Request input file path
inPath = input("Enter the path to the file: ")      

# Load the input file's contents into a string
try:                                                
    with open(inPath, "r") as f:
        text = f.read()
except:
    raise Exception("Error while reading file. Are you sure you wrote the correct path?")

# Get the choice of the user
choice=int(input("Decode an .edch file (0) or encode a .txt file (1)? Write one of the numbers in brackets: "))

# Encode/decode the file based on the choice
match choice:
    case 0:
        print("Decoding file...")           # Status message

        output = ""                         # Replace our beautiful dechetCode with some measly ASCII letters (ew)
        for i in range(0, len(text), 7):
            segment = text[i:i+7]
            for letter, code in dechetCode.items():
                if code == segment:
                    output += letter
                    break
                    
        outPath = inPath[:-4] + "txt"       # Replace the .edch extension with the .txt extension
    case 1:
        print("Encoding file...")           # Status message

        output = ""                         # Replace ASCII letters (if you use Unicode you stink) with our fantastic and totally useful dechetCode
        for char in text:
            output += dechetCode[char]
        
        outPath = inPath[:-3] + "edch"      # Replace the .txt extension with the .edch extension

# Create the output file
try:                                                
    with open(outPath, "w") as f:
        f.write(output)
except:
    raise Exception("Error while writing to output file.")
