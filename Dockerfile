FROM postgres:latest

# Set environment variables
ENV POSTGRES_PASSWORD=postgres
ENV POSTGRES_USER=ylim
ENV POSTGRES_DB=postgres

# Expose PostgreSQL port
EXPOSE 5432

# Default command to run when starting the container
CMD ["postgres"]