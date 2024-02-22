FROM vvangari/kafka-0.10.1.0:latest

# Copy the script into the image
COPY edit_server_properties.sh /usr/local/bin/

# Make the script executable
RUN chmod +x /usr/local/bin/edit_server_properties.sh

# Run the script
RUN /usr/local/bin/edit_server_properties.sh