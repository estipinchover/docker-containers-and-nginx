# nginx/Dockerfile
FROM ubuntu:22.04

# Install Nginx with minimal extra packages
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
    nginx \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

# Copy configuration files
COPY nginx.conf /etc/nginx/nginx.conf
COPY index.html /var/www/html/
COPY error.html /var/www/html/

# Expose ports
EXPOSE 80 8080

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]

# nginx/nginx.conf
events {
    worker_connections 1024;
}

http {
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;

    # First server - Custom HTML response
    server {
        listen 80;

        location / {
            root /var/www/html;
            index index.html;
        }
    }

    # Second server - Returns error code
    server {
        listen 8080;

        location / {
            return 404;
        }
    }
}
## Start from Ubuntu base image
#FROM ubuntu:22.04
#
## Set environment variables to reduce interaction during package installation
#ENV DEBIAN_FRONTEND=noninteractive
#
## Add labels for better maintainability
#LABEL maintainer="Your Name "
#LABEL description="Nginx server with dual configuration"
#
## Update and install Nginx with minimal extra packages
#RUN apt-get update && \
#    apt-get install -y \
#    nginx \
#    --no-install-recommends && \
#    # Clean up to reduce image size
#    apt-get clean && \
#    rm -rf /var/lib/apt/lists/* && \
#    # Remove default Nginx configuration
#    rm -rf /etc/nginx/sites-enabled/default
#
## Create necessary directories
#RUN mkdir -p /var/www/html/site1 && \
#    mkdir -p /var/log/nginx
#
## Create custom HTML content
#RUN echo "\n\
#\n\
#\n\
#    Welcome to Site 1\n\
#    \n\
#        body { font-family: Arial, sans-serif; margin: 40px; }\n\
#        h1 { color: #333; }\n\
#    \n\
#\n\
#\n\
#    Welcome to Site 1\n\
#    This is a custom HTML response from our Nginx server.\n\
#\n\
#" > /var/www/html/site1/index.html
#
## Copy Nginx configuration
#COPY conf/nginx.conf /etc/nginx/nginx.conf
#
## Verify Nginx configuration
#RUN nginx -t
#
## Expose ports
#EXPOSE 8080 8081
#
## Set up healthcheck
#HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
#    CMD nginx -t || exit 1
#
## Start Nginx
#CMD ["nginx", "-g", "daemon off;"]