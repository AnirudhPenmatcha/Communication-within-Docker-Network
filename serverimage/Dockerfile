# Base Image
FROM python:alpine

# Change working directory to folder mounted to the volume
WORKDIR /serverdata

# Include the python scripts to generate a text file of size 1KB and send it to client
ADD generate_random_text.py .
ADD send_data.py .

# Port from which the container will talk
EXPOSE 8888

# Run the scripts
CMD ["sh", "-c", "python ./generate_random_text.py && python ./send_data.py"]


