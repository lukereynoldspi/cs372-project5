addrs_file = "tcp_addrs_"
data_file = "tcp_data_"
ZERO_BYTE = '0x00'


def checksum_tester():
    file_number = 0
    for i in range(10):
        pseudo_header = b''
        f = open(addrs_file + str(file_number) + ".txt", "r")
        f = f.read()
        ip_addresses = f.rstrip().split(" ")
        source_bytestring, destination_bytestring = tcp_bytestrings(ip_addresses[0], ip_addresses[1])
        pseudo_header = pseudo_header + source_bytestring + destination_bytestring

        with open(data_file + str(file_number) + ".dat", "rb") as fp:
            tcp_data = fp.read()
            tcp_length = len(tcp_data)

        file_number += 1

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
    checksum_tester()

if __name__ == "__main__":
    main()