# Use the official MongoDB image as the base image
FROM mongo:7.0.7

# Set environment variables (optional, for configuration)
ENV MONGO_INITDB_ROOT_USERNAME=admin
ENV MONGO_INITDB_ROOT_PASSWORD=password

# Copy initialization scripts (optional, for seeding data or creating users)
# This directory is automatically processed by MongoDB on container startup
# COPY ./docker-entrypoint-initdb.d/ /docker-entrypoint-initdb.d/

# Expose the default MongoDB port
EXPOSE 27017

# The entrypoint and command are usually defined by the base image,
# so you typically don't need to explicitly define them unless
# you want to override the default behavior.
# ENTRYPOINT ["mongod"]
# CMD ["--bind_ip_all"]