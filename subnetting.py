import ipaddress
import random

def main():
    #test_size_subnet()
    #test_subnet()
    print(next(ipaddress.ip_network("10.0.5.0/24").hosts()))
    test_address_range()

def test_size_subnet():
    rand = random.randint(0,32)
    num_hosts = 2 ** rand
    print("What size subnet(hostmask) can accommodate up to %d hosts?"%num_hosts)
    while(True):
        user_answer = input("Answer: ").strip()
        try:
            response = int(user_answer)
            if(response < 0 or response > 32):
                print("Number must be within range 0-32")
                continue
            break
        except Exception:
            print("PLEASE ENTER AN INTEGER")
    if (response == rand):
        print("Correct!")
    else:
        print("Incorrect! The correct answer was %d"%rand)

def test_ip_address_to_network():
    while True:
        try:
            guess = input("Print as a properly formated address [0:255].[0:255].[0:255].[0:255]/[0:32]")
            guess_address = ipaddress.ip_address(guess)
            break
        except Exception:
            print("NOT A VALID IP ADDRESS")
    return None

def test_address_range():
    addr1 = random.randint(0,255)
    addr2 = random.randint(0,255)
    addr3 = random.randint(0,255)
    addr4 = random.randint(0,255)
    host_bits = random.randint(0,32)
    network_string = "%d.%d.%d.%d/%d"%(addr1,addr2,addr3,addr4,host_bits)
    network = ipaddress.ip_network(network_string,strict=False)
    print("What is the range of addresses in the subnet %s?"%(network))
    lowest = input("Lowest Address?")
    highest = input("Highest Address?")
    try:
        lowest_address = ipaddress.ip_address(lowest)
        highest_address = ipaddress.ip_address(highest)
    except Exception:
        print("One of the addresses was not properly formatted!")
    if(lowest == network and highest_address in network.hosts()):
        print("Correct!!!!")
    else:
        print("Wrong!!! Correct answer was %s through %s"%(network,"5343"))

def test_subnet():
    addr1 = random.randint(0,255)
    addr2 = random.randint(0,255)
    addr3N = random.randint(0,255)
    addr3A = random.randint(0,255)
    addr4N = random.randint(0,255)
    addr4A = random.randint(0,255)
    host_bitsN = random.randint(0,32)
    host_bitsA = random.randint(0,(host_bitsN+1))
    network_string = "%d.%d.%d.%d/%d"%(addr1,addr2,addr3N,addr4N,host_bitsN)
    network = ipaddress.ip_network(network_string,strict=False)
    address = ipaddress.ip_network("%d.%d.%d.%d/%d"%(addr1,addr2,addr3A,addr4A))
    answer = address in network.subnets()
    print("Is %s/%d a subnet of %s?"%(address,host_bitsA,network_string))
    while True:
        guess = input("True or False: ")
        if(guess == "True" or guess == "False"):
            break
        else:
            print("Not in the form True/False")
    if (str(answer) == guess):
        print("Correct!!!")
    else:
        print("Wrong!!! The correct answer was %s"%(str(answer)))

if __name__ == '__main__':
    main()
