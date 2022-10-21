ADDRS_FILE = "tcp_addrs_"
DATA_FILE = "tcp_data_"
ZERO_BYTE = b'0x00'
PTCL = b'0x06'

def tcp_pseudo_header(file_number):

    # Reads tcp_addr file, strips the ip addresses and returns them as source and destination bytestrings
    f = open(ADDRS_FILE + str(file_number) + ".txt", "r")
    f = f.read()
    ip_addresses = f.rstrip().split(" ")
    source_bytestring, destination_bytestring = tcp_bytestrings(ip_addresses[0], ip_addresses[1])

    # Gets tcp header length from tcp_data files
    with open(DATA_FILE + str(file_number) + ".dat", "rb") as fp:
        tcp_data = fp.read()
        tcp_length = len(tcp_data)
        tcp_length = tcp_length.to_bytes(1, byteorder ='big')
        tcp_cksum = tcp_data[16:18]
        tcp_zero_cksum = tcp_data[:16] + b'\x00\x00' + tcp_data[18:]

    # Concats source, destination, byte constants, amnd tcp byte length
    pseudo_header = source_bytestring + destination_bytestring + ZERO_BYTE + PTCL + tcp_length
    return pseudo_header

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