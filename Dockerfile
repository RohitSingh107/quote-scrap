
# Use a base image with Python pre-installed
FROM python:3.8

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files into the container
COPY . .

# Expose the port your Flask app will listen on (replace 8000 with your desired port)
EXPOSE 8080

# Command to start the Flask app (adjust as needed, e.g., if your app file is named app.py)
CMD ["python", "app.py"]
