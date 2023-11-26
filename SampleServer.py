from opcua import Server, ua  # Import the ua module

import time

# Create an OPC UA server
server = Server()

# Set the endpoint for the server with security
server.set_endpoint("opc.tcp://127.0.0.1:4841/freeopcua/server/")

# Setup namespace
uri = "http://example.org"
idx = server.register_namespace(uri)

# Create a new object
obj = server.nodes.objects.add_object(idx, "MyObject")
var = obj.add_variable(idx, "MyVariable", 0.0)
var.set_writable()

# Start the server
server.start()

print("Server started at {}".format(server.endpoint))

try:
    while True:
        # Update the variable value every second
        new_value = var.get_value() + 1.0
        var.set_value(new_value)
        
        # Notify subscribers about the change
        var.set_attribute(ua.AttributeIds.Value, ua.DataValue(new_value))
        
        time.sleep(1)  # Sleep for one second before the next update

except KeyboardInterrupt:
    pass
finally:
    # Stop the server on program exit
    server.stop()
    print("Server stopped")
