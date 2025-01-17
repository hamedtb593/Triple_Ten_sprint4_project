Triple Ten Sprint 4 Project 
Git Hub URL
https://github.com/hamedtb593/Triple_Ten_sprint4_project

Web App URL At Render.com
https://triple-ten-sprint4-project.onrender.com/ 

Vehicle Explorer Web Application
Vehicle Explorer is an interactive web tool designed to simulate random data exploration and visualization for vehicle statistics. It allows users to explore and analyze vehicle data by applying filters, generating random subsets, and visualizing key metrics like price distributions, brand comparisons, and paint color distributions. The app utilizes Streamlit for the interface, with additional support from libraries like Pandas and Plotly for data manipulation and visualization.

Project Description
The Vehicle Explorer application is built to simulate the exploration of random events by working with a preloaded dataset of vehicles. This dataset includes details about vehicle prices, models, brands, transmission types, odometers, and more. Users can filter data by year and manufacturer to dynamically generate insights and visualize various aspects of the dataset.

Key Features:
Filter vehicle data based on year and brand.
Explore price distributions using histograms and scatter plots.
Compare price distributions between two selected brands.
View paint color distribution for different manufacturers.
Download filtered data as a CSV file for offline use.
Libraries and Tools Used
Streamlit: For building the interactive web interface.
Pandas: For data manipulation and preprocessing.
Plotly: For creating interactive visualizations.
Base64: For enabling CSV downloads.

How to Launch the Project Locally
Follow these steps to run the Vehicle Explorer application on your local machine:

Prerequisites:
Python 3.7 or higher.
Basic knowledge of Python and using the terminal.
Setup Instructions:
Clone the Repository:

git clone https://github.com/hamedtb593/Triple_Ten_sprint4_project.git

Install Dependencies: Use the requirements.txt file to install all necessary libraries:

pip install -r requirements.txt
Add the Dataset: Ensure the vehicles_us.csv dataset is in the project directory. This file contains the data used for simulations.

Run the Application: Launch the Streamlit app using the following command:

streamlit run app.py

Access the App: After running the above command, the app will open in your default web browser. If not, check the terminal for a local URL (e.g., http://localhost:8501) and open it manually.

Example Usage
Use the sidebar to filter data by vehicle brand and model year.
View and explore the filtered dataset in the main table.
Use interactive visualizations to gain insights into price distributions and brand comparisons.
Download your filtered dataset for further analysis.

