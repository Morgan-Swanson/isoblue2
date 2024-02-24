FROM vvangari/kafka-0.10.1.0:latest
COPY edit_server_properties.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/edit_server_properties.sh
COPY create_topics.sh /usr/local/bin
RUN chmod +x /usr/local/bin/create_topics.sh

# Run the script
RUN /usr/local/bin/edit_server_properties.sh
