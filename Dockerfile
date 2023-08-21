# Use the official Python image
FROM python:3

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy the requirements file to the container
COPY requirements.txt ./

# Install the required packages
RUN apt-get update && apt-get install -y \
    python3-tk \
    && pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Set the display environment variable to allow GUI interactions
ENV DISPLAY=:0

# Run the main.py script
CMD [ "python", "main.py" ]
