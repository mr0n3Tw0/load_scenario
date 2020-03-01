# locust_scenarios
Locust load test scenario

locustfile.py - scenario file, before start need to download locust, for sure use virtualenv!.

1. Create virtualnev environment - $ virtualenv env
   
   activate virualenv environment - $ source env/bin/activate

2. Download locust - $ pip install locust
   
   if you have a troulbes with gcc compiler run it: 
         
         $ sudo apt install python3-dev
         
         $ sudo apt install libevent-dev
   
example for advanced packaging tool (Ubuntu, Debian etc.)

3. Start scenario - $ locust 
   
   and open http://127.0.0.1
   
   take port from CLI when you start locust, exemple of CLI output: Starting web monitor at http://*:8089
   
4. Define "Number of total users to simulate", "Hatch rate (users spawned/second)", "Host" (host for this scenario - https://bash.im)
