# Base Image
FROM python:alpine

# Change working directory to folder mounted to the volume
WORKDIR /clientdata

# Port from which the container will talk
EXPOSE 8786

# Include the python script to receive the file
ADD receive_data.py .

# Run the scipts
CMD [ "python", "./receive_data.py" ]