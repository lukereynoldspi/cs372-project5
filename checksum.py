addrs_file = "tcp_addrs_"
data_file = "tcp_data_"
ZERO_BYTE = b'0x00'
PTCL = b'0x06'

def tcp_pseudo_header(file_number):
    pseudo_header = b''
    f = open(addrs_file + str(file_number) + ".txt", "r")
    f = f.read()
    ip_addresses = f.rstrip().split(" ")
    source_bytestring, destination_bytestring = tcp_bytestrings(ip_addresses[0], ip_addresses[1])
    pseudo_header = pseudo_header + source_bytestring + destination_bytestring + ZERO_BYTE + PTCL

    with open(data_file + str(file_number) + ".dat", "rb") as fp:
        tcp_data = fp.read()
        tcp_length = len(tcp_data)

def tcp_bytestrings(source, destination):
    source = source.split(".")
    destination = destination.split(".")
    source_bytestring = b''
    destination_bytestring = b''
    for byte in source:
        byte = int(byte).to_bytes(1, byteorder ='big')
        source_bytestring = source_bytestring + byte
    for byte in destination:
        byte = int(byte).to_bytes(1, byteorder ='big')
        destination_bytestring = destination_bytestring + byte
    return source_bytestring, destination_bytestring

def main():
    file_number = 0
    for file_number in range(10):
        tcp_pseudo_header(file_number)
        file_number += 1

if __name__ == "__main__":
    main()