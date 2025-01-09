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

logStep = int(len(text) / 100 / 100)   # Do a log every 0.01%

# Encode/decode the file based on the choice
match choice:
    case 0:
        print("Decoding file...")           # Status message

        outPath = inPath[:-4] + "txt"       # Replace the .edch extension with the .txt extension

        # Reverse the dict to make O(1) the lookup for the decoded character
        oppositeMapping = {code: letter for letter, code in dechetCode.items()}

        # Create the output file
        try:
            with open(outPath, "w") as f:
                for i in range(len(text)):
                    # We do this only every 7 characters as the other times we would match characters incorrectly
                    if i % 7 == 0:
                        # Replace ASCII letters (if you use Unicode you stink) with our fantastic and totally useful dechetCode
                        segment = text[i:i+7]
                        f.write(oppositeMapping[segment])

                    if i % logStep == 0:
                        print(f"{i / len(text) * 100:.3}%", end="\r")
        except:
            raise Exception("Error while writing to output file.")

    case 1:
        print("Encoding file...")           # Status message

        outPath = inPath[:-3] + "edch"      # Replace the .txt extension with the .edch extension

        # Create the output file
        try:
            with open(outPath, "w") as f:
                for i in range(len(text)):
                    f.write(dechetCode[text[i]])   # Replace ASCII letters (if you use Unicode you stink) with our fantastic and totally useful dechetCode
                    if i % logStep == 0:
                        print(f"{i / len(text) * 100:.3}%", end="\r")
        except:
            raise Exception("Error while writing to output file.")

# We need to use some spaces at the end to clear remaining numbers from before
print(f"100%     ")
