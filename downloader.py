import os
import argparse
import logging
import re

from urllib.parse import urlparse
import json
import requests



class App:
    def __init__(self, link, max_conn):
        print("initializing..")
        imglist = self.linkparser(link)
    def linkparser(self, link):
        param = urlparse(link)
        if (param.netloc == "www.artstation.com"):
            username = param.path[1:]
            r = requests.get("https://www.artstation.com/users/"+username+"/projects.json")
            srcs = json.loads(r.text)
            imglist = []
            for project in srcs.data:
                
                

def main():
    parser = argparse.ArgumentParser(description='Download Artworks.')
    parser.add_argument('-l', '--link', type=str, required=True)
    parser.add_argument('-d', '--debug', action='store_true', default=False)
    parser.add_argument('-m', '--max_conn', type=int, default=5)
    args = parser.parse_args()
    app = App(args.link, args.max_conn)
    # app = App("https://www.artstation.com/alicejaunet", args.max_conn)
    

if __name__ == '__main__':
    main()
