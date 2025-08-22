# Use official Python image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of the app
COPY *.py .

# Expose port
EXPOSE 5000

# Use Gunicorn to run the app
CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:5000", "app:app"]
