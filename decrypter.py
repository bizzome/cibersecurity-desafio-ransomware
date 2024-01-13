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

# decryptography
key = b'thereistheransom'
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

# delete crazy file
os.remove(file_name)

# save modified file
new_file = 'healthy_file.txt'
new_file = open(f'{new_file}', 'wb')
new_file.write(decrypt_data)
new_file.close()
