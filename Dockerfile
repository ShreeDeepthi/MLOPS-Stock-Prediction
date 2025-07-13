# Use a lightweight Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files into the image
COPY . .

# Expose Flask default port
EXPOSE 5000

# Run Flask app
CMD ["python", "app.py"]
