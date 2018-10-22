import os

def test():
    os.system("gnome-terminal -e 'bash -c \"ls; exec bash\"'")

if __name__ == '__main__':
    test()