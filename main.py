hex_value = input("Enter a hexadecimal value: ")

# Conversion from hexadecimal to binary
binary_value = bin(int(hex_value, 16))[2:].zfill(len(hex_value) * 4)

# Writing binary data to an .exe file
with open("output.exe", "wb") as output_file:
    for i in range(0, len(binary_value), 8):
        byte = binary_value[i:i + 8]
        output_file.write(int(byte, 2).to_bytes(1, "little"))

print("Conversion successful. The 'output.exe' file has been created.")
