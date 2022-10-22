ADDRS_FILE = "tcp_addrs_"
DATA_FILE = "tcp_data_"
ZERO_BYTE = 0
PTCL = 6 

def open_tcp_addrs(file_number):
    # Reads tcp_addr file
    tcp_addrs = open("tcp_addrs/" + ADDRS_FILE + str(file_number) + ".txt", "r")
    tcp_addrs = tcp_addrs.read()
    return tcp_addrs

def open_tcp_data(file_number):
    # Reads tcp_data file
    with open("tcp_data/" + DATA_FILE + str(file_number) + ".dat", "rb") as fp:
        tcp_data = fp.read()
    return tcp_data

def tcp_bytestrings(source, destination):
    # Returns source and destionation ip addresses as bytestrings
    source = source.split(".")
    destination = destination.split(".")
    source_bytestring = b''
    destination_bytestring = b''
    for byte in source:
        byte = int(byte).to_bytes(1, 'big')
        source_bytestring = source_bytestring + byte
    for byte in destination:
        byte = int(byte).to_bytes(1, 'big')
        destination_bytestring = destination_bytestring + byte
    return source_bytestring, destination_bytestring

def tcp_data_length(tcp_data):
    # Returns length of tcp_data
    tcp_length = len(tcp_data)
    tcp_length = tcp_length.to_bytes(1, 'big')
    return tcp_length

def tcp_pseudo_header(tcp_addrs, tcp_data):
    # Splits tcp_addrs data into array
    ip_addresses = tcp_addrs.rstrip().split(" ")
    source_bytestring, destination_bytestring = tcp_bytestrings(ip_addresses[0], ip_addresses[1])

    # Gets tcp header length in bytes
    tcp_length = tcp_data_length(tcp_data)
   
    # Concats source, destination, byte constants, amnd tcp byte length
    pseudo_header = source_bytestring + destination_bytestring + ZERO_BYTE.to_bytes(1, 'big') + PTCL.to_bytes(1, 'big') + tcp_length
    return pseudo_header

def tcp_checksum(tcp_data):
    # Splices checksum data into tcp_cksum
    tcp_cksum = tcp_data[16:18]

    # Makes a version of the tcp_data with 0 as the checksum
    tcp_zero_cksum = tcp_data[:16] + b'\x00\x00' + tcp_data[18:]
    if len(tcp_zero_cksum) % 2 == 1: # Adds 0 byte to odd numbers
        tcp_zero_cksum += b'\x00'

    return tcp_cksum, tcp_zero_cksum

def main():
    file_number = 0
    # Iterates over every file
    for file_number in range(10):
        tcp_addrs = open_tcp_addrs(file_number)
        tcp_data = open_tcp_data(file_number)

        # Makes pseudo header, and both checksums
        pseudo_header = tcp_pseudo_header(tcp_addrs, tcp_data)
        tcp_cksum, tcp_zero_cksum = tcp_checksum(tcp_data)

        file_number += 1

if __name__ == "__main__":
    main()