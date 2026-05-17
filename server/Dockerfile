# Use a lightweight, official Python base image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Prevent Python from writing .pyc files to disk and buffer stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 1. Copy ONLY the requirements file first
COPY requirements.txt /app/

# 2. Now run the install (Docker can find the file now!)
RUN pip install --no-cache-dir -r requirements.txt

# 3. Copy the rest of your application files
COPY app.py /app/
COPY templates/ /app/templates/

# Expose the port Flask runs on
EXPOSE 5000

# Start the Flask server
CMD ["python", "app.py"]