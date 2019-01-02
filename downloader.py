import os
import argparse
import logging
import re

from urllib.parse import urlparse
import json
import requests



class App:
    def __init__(self, link, max_conn, file_path):
        print("initializing..")
        self.link = link
        self.file_path = file_path
        # self.pool_sema = BoundedSemaphore(value=max_connection)
    def linkparser(self, link):
        param = urlparse(link)
        imglist = []
        if (param.netloc == "www.artstation.com"):
            username = param.path[1:]
            srcs = json.loads(requests.get("https://www.artstation.com/users/"+username+"/projects.json").text)
            for project in srcs["data"]:
                artpage = json.loads(requests.get("https://www.artstation.com/projects/"+project["hash_id"]+".json").text)
                ite = 0
                for img in artpage["assets"]:
                    s = {}
                    s["title"] = username + "-" + project["title"]  + ("" if (ite == 0) else ("-"+str(ite)))
                    s["imageurl"] = img["image_url"]
                    imglist.append(s)
                    ite += 1
        return imglist

    def saveimg(self):
        imglist = self.linkparser(self.link)
        for img in imglist:
            try:
                if not os.path.exists(self.file_path):
                    logging.info('Folder "%s" unexisted, recreated',self.file_path)
                    os.makedirs(self.file_path)
                pat = re.compile(r'\.(.*?)\?\d[0-9]', re.S)
                file_suffix = re.findall(pat,(img["imageurl"]).split('/')[-1])[0]
                file_name = img["title"]
                filename = '{}{}{}.{}'.format(self.file_path,os.sep,file_name,file_suffix)
                
                im = requests.get(img["imageurl"])
                if im.status_code == 200:
                    open(filename, 'wb').write(im.content)
                    logging.debug('image saved: %s',filename)
            except IOError as e: logging.error('IOError : %s',e)
            except Exception as e: logging.error('Error : %s',e)




def main():
    parser = argparse.ArgumentParser(description='Download Artworks.')
    # parser.add_argument('-l', '--link', type=str, required=True)
    parser.add_argument('-d', '--debug', action='store_true', default=False)
    parser.add_argument('-m', '--max_conn', type=int, default=5)
    parser.add_argument('-t', '--target', type=str, default='img')
    args = parser.parse_args()
    if args.debug:
        logging.basicConfig(level=logging.DEBUG, \
                    format='[%(asctime)s][%(filename)s][%(lineno)s][%(levelname)s][%(process)d][%(message)s]')
    else:
        logging.basicConfig(level=logging.INFO, \
                    format='[%(asctime)s][%(levelname)s][%(message)s]')
    app = App(args.link, args.max_conn, args.target)
    # app = App("https://www.artstation.com/alicejaunet", args.max_conn, args.target)
    app.saveimg()

if __name__ == '__main__':
    main()
