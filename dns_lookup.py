import dns.resolver

domain = input("Enter your Domain Name: ")

print("[+] Getting DNS info for {}  ...".format(domain))
try:
    for a in dns.resolver.resolve(domain, "A"):
        print("[*] A Record: {}".format(a.to_text()))

    for ns in dns.resolver.resolve(domain, "NS"):
        print("[*] NS Record: {}".format(ns.to_text()))

    for mx in dns.resolver.resolve(domain, "MX"):
        print("[*] MX Record: {}".format(mx.to_text()))        

    for txt in dns.resolver.resolve(domain, "TXT"):
        print("[*] TXT Record: {}".format(txt.to_text())) 

    for aaaa in dns.resolver.resolve(domain, "AAAA"):
        print("[*] AAAA Record: {}".format(aaaa.to_text()))
                 



except Exception as Error:
    print(Error)   