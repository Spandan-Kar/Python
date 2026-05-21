w = "Sony "*3
print(w)

line= '-' *30
print(line)

pattern= '*-'*5
print(pattern)

boy= "spandan"
girl= "eashita"
child= ""

for i in range(len(boy)):
    child += boy[i]
    child += girl[i]

print("Spandan and Eashita's child= ", child)

command= "G()(al)"
result= command.replace("()","o")
result= result.replace("(al)","al")
print(result)

ip_address= "192.168.1.1"
real_ip= ip_address.replace(".","[.]")
print("IP Address= ", real_ip)