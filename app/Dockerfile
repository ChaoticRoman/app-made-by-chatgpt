# Base image
FROM python:3.9-slim-buster

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the app
COPY app.py .

# Expose port
EXPOSE 8050

# Start the app
CMD ["python", "app.py"]
