def encode(text):
    """gets english text from a file and encodes it
      using ASCII characters, and writes the encoded
      text to a file"""

    # Encode the passed in text and append to encoded.txt
    encoded = ''
    for letter in text:
        encoded = encoded + ' ' + str(ord(letter))

    print(encoded)

    # Write the encoded text to encoded.txt file
    try:
        file_open = open("encoded.txt", 'a')
    except:
        print("Unable to open encode file!")

    file_open.write(encoded)

    file_open.close()
# End encode() Function


def decode(ascii):
    """gets the passed in ascii code and changes
    it back into english text"""

    decoded = ''
    ascii = ascii[1:]
    for x in ascii.split():
        decoded = decoded + chr(int(x))

    # Print the decoded message (not written to file)
    print(decoded)
# End decode() Function


def encode_decode(sel):
    """gets data from a file and either encodes it 
    or decodes it using ascii characters.
    Pass in either 'encode' or 'decode'  """

    # Encode the contents of english.txt (written to file)
    if sel == 'encode':
        try:
            open_file = open('english.txt', 'r')
        except:
            print('There was an error opening the english file.')

        for line in open_file:
            encode(line)

        open_file.close()

    # Decode the contents of encoded.txt and print the output 
    elif sel == 'decode':

        # Read the encoded text from the encoded.txt file
        try:
            file_open = open("encoded.txt", 'r')
        except:
            print("During decoding, unable to open encoded file!")
        # Send the encoded to the decode() function
        for line in file_open:
            decode(line)
        file_open.close()
        print('Completed Decoding the file.')

    else:
        print('Invalid argument.')

encode_decode('decode')