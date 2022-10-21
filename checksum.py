file = "tcp_addrs_"
file_number = 0
for i in range(10):
    f = open(file + str(file_number) + ".txt", "r")
    print(f.read()) 
    file_number += 1