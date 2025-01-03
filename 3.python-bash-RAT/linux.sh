#!/bin/bash

# Define the log file where output will be saved
LOG_FILE="script_output.log"

# Clear the log file if it exists, or create a new one
> $LOG_FILE

# Define the content of the new script
cat > start_server_and_tunnel.sh << 'EOF'
#!/bin/bash

# Update Linux packages
echo "Updating package list..."
sudo apt update -y

# Install tmux, wget, and cloudflared
echo "Installing tmux, wget, and cloudflared..."
sudo apt install -y tmux wget cloudflared

# Start the Python HTTP server in the background
echo "Starting Python HTTP server on port 8000..."
python3 -m http.server 8000 &

# Start the Cloudflare Tunnel
echo "Starting Cloudflare Tunnel..."
cloudflared tunnel --url http://localhost:8000

echo "tmux, wget, and cloudflared have been installed, the Python HTTP server is running, and the Cloudflare Tunnel is active."
EOF

# Set executable permissions for the new script
chmod +x start_server_and_tunnel.sh

# Inform the user that the script has been created and is executable
echo "The script 'start_server_and_tunnel.sh' has been created and is now executable." >> $LOG_FILE

# Run the new script and log all output to the log file
./start_server_and_tunnel.sh >> $LOG_FILE 2>&1
