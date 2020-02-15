import ipaddress
import random

def main():
    ip1 = ipaddress.IPv4Address("10.0.5.234")
    test_size_subnet()

def test_size_subnet():
    rand = random.randint(0,32)
    num_hosts = 2 ** rand
    print("What size subnet can accommodate up to %d hosts?"%num_hosts)
    print("Fomat your answer in: \'--/{answer}\'")
    user_answer = input("Answer: ")
    if (user_answer == str(rand)):
        print("Correct!")
    else:
        print("Incorrect! The correct answer was %d"%rand)

def test_ip_address_to_network():
    return None

def test_subnet():
    print()

def number_of_hosts(num):
    return "{0:b}".format(num)

if __name__ == '__main__':
    main()
