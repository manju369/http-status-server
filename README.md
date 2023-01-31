HTTP Status server returns the HTTP status code for the requested path. This server uses Python Flask module 


Code:
* All the main program and unittest codes are placed in `app` folder
* Required pip packages are kept in `app/pip-requirements.txt`


Deployment:

* Containerization: 

  ```docker buildx build --platform linux/amd64  -t manju369/flask-server:2 .```
  
*  Kubernetes: 

    Hosting these services in my free tier GCP-GKE account

   ```kubectl apply -f /```

    creates deployment, service, ingress-rule and service-monitor(prometheus operated) resources
    
 
 * Sending Request:
   
   Requests through `curl` command:

  ``` 
      curl http://35.244.49.131.nip.io/codes
      curl http://35.244.49.131.nip.io/codes/update
      curl http://35.244.49.131.nip.io/codes/call-backend 
   ```

   
  * Response: 

<img width="746" alt="Screenshot 2023-01-31 at 10 14 31 AM" src="https://user-images.githubusercontent.com/36835720/215667560-503e6692-4070-48e9-9127-aa6b9f2f1493.png">


Prometheus and Grafana DashBoards:


<img width="1439" alt="Screenshot 2023-01-31 at 9 31 15 AM" src="https://user-images.githubusercontent.com/36835720/215668069-24260f8e-c1af-4c96-b3c4-0695bb0db894.png">

<img width="1381" alt="Screenshot 2023-01-31 at 9 54 27 AM" src="https://user-images.githubusercontent.com/36835720/215668131-03b80f52-4004-4625-a8d1-b3aba08af863.png">



