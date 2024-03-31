Electric Vehicle Route Optimization
This project focuses on optimizing route planning for electric vehicle (EV) users by leveraging algorithmic solutions. The goal is to develop an application that, given a starting point and a network of nodes with charging stations, finds the shortest path to each charging station and recommends the most efficient route based on distance.

Setup
Clone the Repository: Clone this repository to your local machine using the following command:

git clone https://github.com/your-username/electric-vehicle-route-optimization.git
Install Python: Make sure you have Python 3 installed on your machine. If not, you can download it from the official Python website.

Navigate to Directory: Open a terminal and navigate to the directory where you cloned the repository:

cd electric-vehicle-route-optimization
Install Dependencies: Install the required Python dependencies by running the following command:

pip install -r requirements.txt
Execution
Run the Code: Execute the Python script route_optimization.py to run the application:

python route_optimization.py
View Output: The script will display the graph representing the network of nodes with their connections and distances. It will then calculate the shortest paths to charging stations from a specified starting node and recommend the most efficient route.

Interpret Output: Check the output displayed in the terminal. It will provide the shortest paths to charging stations from the specified starting node and recommend the most efficient route based on distance.

Customization
Input File: You can customize the network of nodes and their connections by modifying the network.txt file.
Starting Node: Change the starting node by modifying the starting_node variable in the route_optimization.py script.
Additional Charging Stations: If you have additional charging stations, you can add them to the network.txt file and mark them with an asterisk (*) for identification.
