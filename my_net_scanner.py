import scapy.all as scapy
import optparse

def input_object():

    parse_object = optparse.OptionParser()
    parse_object.add_option("-i","--ip",dest="ip_adress",help="enter ip adress")
    (user_input,arguments) = parse_object.parse_args()
    if not user_input.ip_adress:
        print("Enter ip adress")
    return user_input.ip_adress

def scan_my_network(ip_adress):

    arp_requests_packet = scapy.ARP(pdst=ip_adress)

    brodcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

    combined_packet = brodcast_packet/arp_requests_packet

    (answered_list,unanswered_list) = scapy.srp(combined_packet,timeout=1)

    answered_list.summary()

user_input_ip = input_object()

scan_my_network(ip_adress=user_input_ip)


''' https://i.hizliresim.com/pxu1zit.png
https://i.hizliresim.com/dzc3a7z.png
https://i.hizliresim.com/fcxgu32.png
https://i.hizliresim.com/2bz3otq.png
'''
