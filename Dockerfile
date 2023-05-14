FROM python:3.9-slim-buster

# Install Postfix
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y postfix && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install dependencies
RUN pip install flask flask-mail pymongo

# Copy the application code
WORKDIR /app
COPY app /app

# Expose the required ports
EXPOSE 3099 25

# Configure the entrypoint
CMD ["./entrypoint.sh"]
