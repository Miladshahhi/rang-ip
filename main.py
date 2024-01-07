import ipaddress

def ip_range_to_list(ip_range):
    ip_list = []
    network = ipaddress.IPv4Network(ip_range, strict=False)
    
    for ip in network:
        ip_list.append(str(ip))
    
    return ip_list

if __name__ == "__main__":
    with open("input.txt", "r") as input_file:
        input_ranges = input_file.read().splitlines()
    
    ip_list = []
    
    for ip_range in input_ranges:
        ip_list.extend(ip_range_to_list(ip_range))
    
    output_file = "ip.txt"
    with open(output_file, "w") as file:
        for ip in ip_list:
            file.write(ip + ":3389\n")
    
    print(f"آی‌پی‌ها در فایل '{output_file}' ذخیره شد.")
