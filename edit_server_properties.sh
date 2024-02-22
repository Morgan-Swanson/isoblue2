PROPERTY="log.retention.hours"
NEW_VALUE="-1"

# Path to the server.properties file
CONFIG_FILE="/opt/kafka_2.11-0.10.1.0/config/server.properties"

# Check if the property already exists in the file
if grep -q "^$PROPERTY" "$CONFIG_FILE"; then
    # Property exists, so replace its value
    sed -i "s/^$PROPERTY=.*/$PROPERTY=$NEW_VALUE/" "$CONFIG_FILE"
else
    # Property does not exist, so add it to the end of the file
    echo "$PROPERTY=$NEW_VALUE" >> "$CONFIG_FILE"
fi
