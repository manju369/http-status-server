HTTP Status server returns the HTTP status code for the requested path. This server uses Python Flask module 


Code:
* All the main program and unittest codes are placed in `app` folder
* Required pip packages are kept in `app/pip-requirements.txt`


Deployment:

* Containerization: 

  ```docker buildx build --platform linux/amd64  -t manju369/flask-server:2 .```
  
*  Kubernetes: 
    
   ```kubectl apply -f /```

    creates deployment, service, ingress-rule and service-monitor(prometheus operated) resources
    
 
 * Requests and Response 
   
   Requests through `curl` command:

  ``` curl http://35.244.49.131.nip.io/codes
      curl http://35.244.49.131.nip.io/codes/update
      curl http://35.244.49.131.nip.io/codes/call-backend ```

   
   Response: 

   <img width="746" alt="Screenshot 2023-01-31 at 10 14 31 AM" src="https://user-images.githubusercontent.com/36835720/215667560-503e6692-4070-48e9-9127-aa6b9f2f1493.png">
