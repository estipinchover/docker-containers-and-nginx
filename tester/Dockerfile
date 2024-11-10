# tester/Dockerfile
FROM python:3.9-slim

# Install requirements
RUN pip install requests

# Copy test script
COPY test.py /app/
WORKDIR /app

# Run tests
CMD ["python", "test.py"]





## Use slim version for smaller image size
#FROM python:3.9-slim
#
## Add labels for better maintainability
#LABEL maintainer="Your Name "
#LABEL description="Test container for Nginx servers"
#
## Set working directory
#WORKDIR /app
#
## Install requirements
#RUN pip install --no-cache-dir requests
#
## Copy test script
#COPY test.py .
#
## Set Python to run in unbuffered mode
#ENV PYTHONUNBUFFERED=1
#
## Run tests
#CMD ["python", "test.py"]