def pseudo_header_bytestrings(source, destination):
    print(source)
    source_bytestring = source.split(".")
    destination_bytestring = destination.split(".")
    
    return source_bytestring, destination_bytestring

addrs_file = "tcp_addrs_"
data_file = "tcp_data_"
file_number = 0

for i in range(10):
    f = open(addrs_file + str(file_number) + ".txt", "r")
    f = f.read()
    ip_addresses = f.split(" ")
    pseudo_header_bytestrings(ip_addresses[0], ip_addresses[1])
    with open(data_file + str(file_number) + ".dat", "rb") as fp:
        tcp_data = fp.read()
        tcp_length = len(tcp_data)  # <-- right here

    file_number += 1


