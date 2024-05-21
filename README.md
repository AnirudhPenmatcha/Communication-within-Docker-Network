Communicating between containers in the same Docker Network

In order to run the containers there are a few steps to be performed first. 

1. Create a user defined network `docker network create Docker-Network`
2. Create a volume by the name "servervol" `docker volume create servervol`
3. Create a volume by the name "clientvol" `docker volume create clientvol`

Server:
1. Next navigate to the serverimage folder and run `docker build -t server-image .`
2. Once you're done building, run `docker run -itd -v servervol:/serverdata --network Docker-Network -p 8888:8888 --name server-container server-image`.

**Note:** Step 2 may not work sometimes. In which case, just deploy a busybox image container as it is in the Docker network and run `docker inspect Docker-Network`. Check for the busybox ip and comment the main funciton call in "send_data.py" and uncomment the ping line with busybox's ip address. Build the server image again and run. Check logs of the server-container using `docker logs server-container`. If you see pings, then close the server-container. Comment the ping line and uncomment the main function. Rebuild and run the container. This will fix the issue. I don't know why exactly this resolved the issue but pinging somehow fixes it.

3. If you'd like to interact with the server-container to check the contents of it, `docker exec -it server-container sh` and `ls && cat random_data.txt`

Client:
1. With the server-container running with similar output as in my report, next navigate to the clientimage folder and run `docker build -t client-image .`
2. Then run `docker run -v clientvol:/clientdata -itd --network Docker-Network -p 8786:8786 --name client-container client-image`
3. Check logs of the client-container using `docker logs client-container`.
4. After that run `docker exec -it client-container sh`
5. `docker exec -it client-container sh` and `ls && cat received_file.txt`. Voila!

Notice that the contents of the files in the server and client will be the same.
