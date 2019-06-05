from subprocess import Popen


processes = []

for counter in range(10):
    chrome_cmd = 'export BROWSER=chrome NODE_HUB_ADDRESS=192.168.112.2 && python project/sunnxt.py'
    firefox_cmd = 'export BROWSER=firefox NODE_HUB_ADDRESS=192.168.112.2 && python project/sunnxt.py'
    processes.append(Popen(chrome_cmd, shell=True))
    processes.append(Popen(firefox_cmd, shell=True))

for counter in range(10):
    processes[counter].wait()
