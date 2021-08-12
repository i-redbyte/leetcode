# honestly took regex from:
# https://stackoverflow.com/questions/53497/regular-expression-that-matches-valid-ipv6-addresses
# ¯\_(ツ)_/¯
import re


class Solution:
    def validIPAddress(self, ip: str) -> str:
        rule_IPv6 = r'([0-9a-fA-F]{1,4})'
        patten_IPv6 = re.compile(r'^(' + rule_IPv6 + r'\:){7}' + rule_IPv6 + r'$')
        rule_IPv4 = r'([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'
        patten_IPv4 = re.compile(r'^(' + rule_IPv4 + r'\.){3}' + rule_IPv4 + r'$')
        if patten_IPv4.match(ip):
            return "IPv4"
        return "IPv6" if patten_IPv6.match(ip) else "Neither"


s = Solution()
print(s.validIPAddress("127.0.0.1"))
print(s.validIPAddress("255.255.255.256"))
print(s.validIPAddress("8.8.8.8"))
print(s.validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334"))
