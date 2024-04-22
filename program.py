# sets up dependencies
import scratchattach as scratch3
import os

# sets up secret values
username = os.getenv("username")
password = os.getenv("password")
projectID = os.getenv("projectID")

# connects, sends, and disconects
session = scratch3.login(username, password)
conn = session.connect_cloud(projectID)
conn.set_var("1", "4212024")
conn.disconnect()
