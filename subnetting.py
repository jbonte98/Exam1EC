import ipaddress
import random

def main():
    n1 = ipaddress.ip_network('5.0.5.234/24')
    print(n1)
    #test_size_subnet()
    test_subnet()

def test_size_subnet():
    rand = random.randint(0,32)
    num_hosts = 2 ** rand
    print("What size subnet can accommodate up to %d hosts?"%num_hosts)
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
    return None

def test_subnet():
    addr1 = random.randint(0,255)
    addr2 = random.randint(0,255)
    rand3N = random.randint(0,255)
    rand3A = random.randint(0,255)
    rand4N = random.randint(0,255)
    rand4A = random.randint(0,255)
    host_bitsN = random.randint(0,32)
    host_bitsA = random.randint(0,32)
    network =
    print()

def number_of_hosts(num):
    return "{0:b}".format(num)

if __name__ == '__main__':
    main()
