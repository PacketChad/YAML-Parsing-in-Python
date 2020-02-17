#########################################
### Import of data from example files ###
###      leave these uncommented      ###
#########################################

# Imports the YAML module for use in our script
import yaml

# Opens the files ex1.yaml and loads the contents into 'result1'
with open('ex1.yaml') as ex1:
    result1 =  yaml.safe_load(ex1)

# Opens the files ex2.yaml and loads the contents into 'result2'
with open('ex2.yaml') as ex2:
    result2 = yaml.safe_load(ex2)

# Opens the files ex3.yaml and loads the contents into 'result3'
with open('ex3.yaml') as ex3:
    result3 = yaml.safe_load(ex3)

# Opens the files ex4.yaml and loads the contents into 'result4'
with open('ex4.yaml') as ex4:
    result4 = yaml.safe_load(ex4)


####################################################################
### Dictionary operations and printing out the results and types ###
###               Comment/Uncomment as needed                    ###
####################################################################

# Prints the specified variable
print(result4)

# Prints the type of the variable 'result1'
print (type(result1))

#items = list(result2.items())
print(items)
print(type(items))

keys = list(result4.keys())
print(keys)
print(type(keys))

count = 0
for device in keys:
    count += 1
print("Device Count: " + str(count))

values = list(result2.values())
print(values)
print(type(values))

print(values[0])

get = list(result2.get('switch1'))
print(get)
print(type(get))


#######################
### Print item info ###
#######################
print(items[2][0] + " has an IP address of " + (items[2][1]))


###############################
### Config template example ###
###############################
for device in keys:
    print(device + " config template")
    print("##################################################")
    print("config t")
    print("hostname " + device + ".domain.local")
    print("end")
    print("copy run start")
    print("exit")
    print("##################################################")


###############################
### Checks for IP in values ###
###############################
ip = "10.255.255.254"
print(ip in result2.values())


###############################
### Device inventory report ###
###############################
print("###########################")
print("Device Inventory Report")
print("###########################\n")
for device,ip in result2.items():
    print("Device Name: " + device + "\n")
    print("  IP Address: " + ip + "\n\n")
print("##################################")
print("End of Inventory")

print(result3)
print(type(result3))


#####################################
### Device site and managmenet IP ###
#####################################
for device in keys:
    print("Device Name: " + device)
    print("  Site: " + result3[device]['site'])
    print("  MgmtIP: " + result3[device]['mgmt_ip'])


###########################################
### Input to get site and management IP ###
###########################################
print('Enter a device:')
dev_input = input()
print("The device " + dev_input + " is located in " + result3[dev_input]['site'] + " and has a management IP of " + result3[dev_input]['mgmt_ip'])


################################
### Create list of all sites ###
################################
all_sites = []
for device in keys:
  if result3[device]['site'] not in all_sites:
      all_sites.append(result3[device]['site'])
print(all_sites)


###############################################
### Print interfaces, descriptions, and IPs ###
###############################################
for device in keys:
    print("###################")
    print(device)
    for interface in result4[device]['interfaces']:
        print("\n" + interface)
        print("------------------")
        print("  " + result4[device]['interfaces'][interface]['description'])
        print("  " + result4[device]['interfaces'][interface]['ipv4addr'])
    print("###################")


##########################
### Interface counting ###
##########################
print('Enter a device:')
dev_input = input()
count = 0
for interface in result4[dev_input]['interfaces']:
    count += 1
print(dev_input + " has " + str(count) + " interface(s)")

#########################
### Print primary DNS ###
#########################
device = 'router2'
print(result4[device]['dns'][0]['dns_pri'])

print(type(result4[device]['dns'][0]))


#################################
### Standard config generator ###
#################################
print("########Standardized Config Generator########")
for device in keys:
    print("--------Currently on Device " + device + " --------")
    print("snmp-server location " + result4[device]['site'])
    print("ip domain-lookup")
    print("ip name-server " + result4[device]['dns'][0]['dns_pri'] + " " + result4[device]['dns'][1]['dns_sec'])
    for interface in result4[device]['interfaces']:
        print("interfrace " + interface)
        print("  description " + result4[device]['interfaces'][interface]['description'])
        print("  ip address " + result4[device]['interfaces'][interface]['ipv4addr'] + " 255.255.255.0")
    print("\n")
