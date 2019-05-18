import re


# def cleanCLRFspace(content):
# 	noCLContext = content.replace('\n','')
# 	noSpaceCLRFcontext = noCLContext.strip()
# 	return noSpaceCLRFcontext

def readFile():
    ipf = open('./content.txt', 'r')
    return ipf


def getLineIP(ipf):
    ipList = set()
    texts = ipf.readlines()
    for text in texts:
        ips = re.findall(r'\d+\.\d+?\.\d+?\.\d+?', text)
        for ip in ips:
            ipList.add(ip)
    return ipList


def ip2c(ipNoDup):
    ipset = set()
    for ip in ipNoDup:
        ipset.add(re.findall(r'\d+?\.\d+?\.\d+?\.', ip)[0] + '0/24')
    iplist = list(ipset)
    iplist.sort()
    return iplist


def saveContext(s):
    wfile = open('./result.txt', 'w')
    for i in s:
        wfile.write(i + '\n')
    wfile.close()


if __name__ == '__main__':
    ipf = readFile()
    ipList = getLineIP(ipf)
    iplist = ip2c(ipList)
    saveContext(iplist)