# https://www.hackerrank.com/challenges/ip-address-validation/problem


import re


# Inputs
standard_input = """35
1050:0:0:0:5:600:300c:326b
1050:0:0:0:5:600:300c:326a
1050:0:0:0:5:600:300c:326c
1051:0:0:0:5:600:300c:326b
22.231.113.64
22.231.113.164
255.231.111.64
253.231.111.64
1050:10:0:0:5:600:300c:326b
1050:10:0:0:5:600:300c:326a
1050:10:0:0:5:600:300c:326c
1051:10:0:0:5:600:300c:326b
22.21.113.61
22.21.113.162
255.21.111.63
253.21.111.69
1050:10:0:0:15:600:300c:326b
1050:10:0:10:5:600:300c:326a
1050:10:10:0:5:600:300c:326c
1051:110:0:0:5:600:300c:326b
22.211.113.64
22.212.113.164
255.213.111.64
253.214.111.64
1050:10:0:0:15:600:300c:326k
1050:10:0:0:15:600:300c:326g
1050:10:0:0:15:600:300c:326h
1050:10:0:0:15:600:300c:326i
22.211.113.364
22.212.113.3164
255.213.111.464
253.214.111.564
not an ip address
not an ipv4 Address
Not an IPv5 Address"""

for _ in range(int(input())):

    line = input().strip().lower()

    ipv4_pattern = r"(?:(?:\d{1,3})\.){3}\d{1,3}"
    # (000.){3}000 ~ (255.){3}255

    ipv6_pattern = r"^(?:(?:[\da-f]{1,4})\:){7}[\da-f]{1,4}$"
    # (0000:{7})0000 ~ (FFFF:{7})FFFF

    if re.match(ipv4_pattern, line):
        if all([int(part) <= 255 for part in re.findall(r"\d{1,3}", line)]):
            print("IPv4")
        else:
            print("Neither")

    elif re.match(ipv6_pattern, line):
        print("IPv6")

    else:
        print("Neither")

# IPv6
# IPv6
# IPv6
# IPv6
# IPv4
# IPv4
# IPv4
# IPv4
# IPv6
# IPv6
# IPv6
# IPv6
# IPv4
# IPv4
# IPv4
# IPv4
# IPv6
# IPv6
# IPv6
# IPv6
# IPv4
# IPv4
# IPv4
# IPv4
# Neither
# Neither
# Neither
# Neither
# Neither
# Neither
# Neither
# Neither
# Neither
# Neither
# Neither
