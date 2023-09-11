# Conversational-Systems

To run the DeepHaven IDE, run the following script: 

```bash
from deephaven_server import Server
import os

my_dh_key = <your key here>

s = Server(jvm_args=[f"-Dauthentication.psk={my_dh_key}"]).start()
```

Here, now the my_dh_key would be the token, remember it!!

Run the `http://localhost:10000` in your browser and enter the token to login.
Input the further scripts in the IDE and run them.