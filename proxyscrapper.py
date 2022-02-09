import os, time, requests;from colorama import Fore, Style
os.system('cls & mod 83, 22')
f = open('proxies.eagle', 'wb')
proxytype = input(f"{Fore.CYAN}{Style.BRIGHT}>{Fore.RESET} ProxyType [http/https/socks4/socks5]{Fore.CYAN}{Style.BRIGHT}:{Fore.RESET} ")
proxytype = 'http'
if proxytype not in ['http', 'https', 'socks4', 'socks5']
else:
  print("Invalid Choice")
  time.sleep(5)
  os.exit(0)
  rl = requests.get(f"https://api.proxyscrape.com/v2/?request=getproxies&protocol={proxytype}&timeout=50&country=all")
  f.write(r1.content)
  f.close()
  print(f"Successfully Scraped Proxies")
  input()