# This should only be run directly and located one directory above the project
# This automatically updates the project and rebuilds the docker image

# Prune unused Docker images
echo y | docker image prune

# Move the .env file to a temporary location
mv profitgreen-api/.env .env

# Remove the existing project directory
rm -rf profitgreen-api

# Clone the latest version of the project from GitHub
git clone https://github.com/aLEGEND21/profitgreen-api.git

# Move the .env file back to the project directory
mv .env profitgreen-api/.env

# Change to the project directory
cd profitgreen-api

# Build the Docker image
sudo docker build -t profitgreen-api .

# Remove any existing container with the same name
sudo docker rm -f profitgreen-api

# Run the new Docker container
sudo docker run -d --name profitgreen-api -p 3004:3004 --network=nginx-proxy profitgreen-api