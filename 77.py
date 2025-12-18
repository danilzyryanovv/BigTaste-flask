import requests
import re

flags = ["read", "write", "append", "url"]

class MyFile:
    def __init__(self, name, f):
        if f not in flags:
            print("Unsupported command")
        if not name:
            print("Empty name")
        self.name = name
        self.flag = f
        self.url_content = None

    def read(self):
        if self.flag not in ["read", "write", "append"]:
            print("Unsupported command")
            return None
        try:
            f = open(self.name, mode='r', encoding='utf-8')
            a = f.read()
            f.close()
            return a
        except FileNotFoundError:
            return "File not exists"
        except:
            return "Error reading file"
    
    def write(self, string):
        if self.flag not in ["write", "append"]:
            print("Unsupported command")
            return
        if self.flag == "write":
            f = open(self.name, mode='w', encoding='utf-8')
        elif self.flag == "append":
            f = open(self.name, mode='a', encoding='utf-8')
        f.write(string)
        f.close()
    
    def read_url(self):
        if self.flag != "url":
            return "Unsupported command"
        try:
            s = requests.get(self.name)
            self.url_content = s.text
            s.close()
            return s.text
        except requests.ConnectionError:
            return "Website not found"
        except:
            return "Error reading URL"
    
    def count_urls(self):
        if self.flag != "url":
            return "Wrong command"
        if self.url_content is None:
            content = self.read_url()
            if content in ["Website not found", "Error reading URL", "Unsupported command"]:
                return 0
            self.url_content = content
        url_pattern = r'https?://[^\s<>"\']+'
        urls = re.findall(url_pattern, self.url_content)
        return len(urls)
    
    def write_url(self, filename):
        if self.flag != "url":
            return "Wrong command"
        try:
            f = open(filename, mode='w', encoding='utf-8')
            content = self.read_url()
            if content in ["Website not found", "Error reading URL", "Unsupported command"]:
                print("Cannot get URL content")
                f.close()
                return
            f.write(content)
            f.close()
        except requests.ConnectionError:
            print("Website not found")
        except:
            print("Error saving to file")
