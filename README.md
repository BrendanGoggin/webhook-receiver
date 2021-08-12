# webhook-receiver

Lightweight python server for receiving webhooks.

### Commands

```bash
# Create virtual environment and activate it
python3 -m venv ./venv/
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start app, listening on port 9999 for example
./app.py 9999

# Expose port to internet via ngrok
# (Note: to install ngrok, either do `brew install --cask ngrok` or visit https://ngrok.com/download)
ngrok http 9999

# You can now copy+paste the ngrok URL to subscribe it to webhooks.
# You can view incoming requests via the ngrok web UI, for which it will provide a URL.

# app.py will log webhook info to stdout. You may want to redirect app.py output to a file.
# The following command will start app.py, listen on port 9999, append stdout and stderr to log.txt,
# and will run in the background.
./app.py 9999 >> log.txt 2>&1 &
```

### Running and Debugging with VSCode

Add the following `.vscode/launch.json` file:

```json
{
  // Use IntelliSense to learn about possible attributes.
  // Hover to view descriptions of existing attributes.
  // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python: run app",
      "type": "python",
      "request": "launch",
      "program": "${workspaceFolder}/app.py",
      "args": ["9999"],
      "justMyCode": false
    }
  ]
}
```

Now you can run the `webhook-receiver` in VSCode, and use breakpoints + the debugger.
For more info: [https://code.visualstudio.com/docs/python/debugging](https://code.visualstudio.com/docs/python/debugging)
