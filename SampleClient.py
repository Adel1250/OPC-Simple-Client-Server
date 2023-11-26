from opcua import Client

# Define the handler class
class MyHandler:
    @staticmethod
    def datachange_notification(node, val):
        print("DataChange Notification for node {}: New Value - {}".format(node, val))

# Connect to the OPC UA server
client = Client("opc.tcp://127.0.0.1:4841/freeopcua/server/")
client.connect()

try:
    # Get the variable node using the full NodeId
    var_node_id = "ns=2;i=2"  # Adjust the NodeId based on your server's structure
    var = client.get_node(var_node_id)

    # Create the handler instance
    handler = MyHandler()

    # Monitor the variable changes
    subscription = client.create_subscription(100, handler)
    subscription.subscribe_data_change(var)

    # Keep the client alive
    while True:
        pass

finally:
    # Disconnect the client when done
    client.disconnect()
    print("Client disconnected")
