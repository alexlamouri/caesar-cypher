

# Define alphabet

ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def encode():

    # Prompt User for Decoded Input
    
    while True:
        input_file_name = input("Enter the name of the file to encode:\n")
        
        try:
            input_file = open(input_file_name, "r")
        
        except IOError:
            print("Cannot open input file\n")
            continue
    
        else:
            break
    
    
    # Prompt User for Encoded Output
    
    while True:
        output_file_name = input("Enter the name of the file to store the encoding:\n")
        
        try:
            output_file = open(output_file_name, "w")
            
        except IOError:
            print("Cannot open output file\n")
            continue
        
        else:
            break
    
    
    # Prompt User for Rotation
    
    while True:
        rotation = input("Enter a rotation integer in the range of 1-25:\n")  
        
        try:
            rotation = int(rotation)
            
        except ValueError:
            print("Rotation must be of type int\n")
            continue
        
        if (rotation > 1) and (rotation < 25):
            break
                
        else:
            print("Rotation must be in the range of 1-25\n") 
            continue
        
        
    # Encode the Input File to the Output File with given Rotation   
    
    rotation_alphabet = ALPHABET[rotation:] + ALPHABET[:rotation]

    for decoded_line in input_file:
        
        for decoded_letter in decoded_line:
            
            if decoded_letter in ALPHABET:

                index = ALPHABET.index(decoded_letter)
                encoded_letter = rotation_alphabet[index]
                
            else:
                encoded_letter = decoded_letter
                
            output_file.write(encoded_letter)
            
            
    # Close files 
            
    input_file.close()
            
    output_file.close()    
                
                
def decode():
    
    # Prompt User for Encoded Input
    
    while True:
        input_file_name = input("Enter the name of the file to decode:\n")
        
        try:
            input_file = open(input_file_name, "r")
        
        except IOError:
            print("Cannot open input file\n")
            continue
    
        else:
            break
    
    
    # Prompt User for Decoded Output
    
    while True:
        output_file_name = input("Enter the name of the file to store the decoding:\n")
        
        try:
            output_file = open(output_file_name, "w")
            
        except IOError:
            print("Cannot open output file:\n")
            continue
        
        else:
            break


    # Find Rotation

    letter_count = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    
    for encoded_line in input_file:
        
        for encoded_letter in encoded_line:
            
            if encoded_letter in ALPHABET:
                index = ord(encoded_letter) - ord("a")
                letter_count[index] += 1
                
    most_index = letter_count.index(max(letter_count))
    
    most_letter = ALPHABET[most_index]
    
    
    # Create rotation alphabet
    
    rotation = ord(most_letter) - ord("e")
    
    rotation_alphabet = ALPHABET[rotation:] + ALPHABET[:rotation]
    
    
    # Reset reading head
    
    input_file.seek(0)
    
    
    # Decode
    
    for encoded_line in input_file:
        
        for encoded_letter in encoded_line:
            
            if encoded_letter in ALPHABET:

                index = rotation_alphabet.index(encoded_letter)
                decoded_letter = ALPHABET[index]
                
            else:
                decoded_letter = encoded_letter
            
            output_file.write(decoded_letter)  
    
    
    # Close files 
            
    input_file.close()
    
    output_file.close()
    



# Prompt the user for command

if __name__ == "__main__":
    
    print("----------------------\n" + 
          "Welcome to cypher.exe\n" + 
          "----------------------\n")

    while True:
        command = input("--------------------------------------------\n" + 
                        "Please select one of the following commands:\n'e' to encode a file\n'd' to decode a file\n'q' to quit\n" + 
                        "--------------------------------------------\n")
    
        if command == "e":
            print("-----------------\n" + 
                  "COMMAND : Encode\n" + 
                  "-----------------\n")
            encode()
        
        elif command == "d":
            print("-----------------\n" + 
                  "COMMAND : Decode\n" + 
                  "-----------------\n")
            decode()
        
        elif command == "q":
            print("-----------------\n" + 
                  "COMMAND : Quit\n" + 
                  "-----------------\n")
            break
    
        else:
            print("------------------------\n" + 
                  "ERROR : Invalid command\n" +
                  "------------------------\n")
            continue
