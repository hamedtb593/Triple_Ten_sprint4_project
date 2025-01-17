import streamlit as st
import pandas as pd
import plotly.express as px
import base64

# loading the dataset 
df = pd.read_csv('vehicles_us.csv')
# Extracting the manufacturer from the model column
df['manufacturer'] = df['model'].apply(lambda x: x.split()[0])
# drop rows with missing values on the model_year column
df = df.dropna(subset=['model_year'])
# Convert 'price' to numeric, coercing invalid values to NaN
df["price"] = pd.to_numeric(df["price"], errors='coerce')
# Drop rows where 'price' is NaN
df = df.dropna(subset=["price"])
# Convert 'price' to int64 after handling NaNs
df["price"] = df["price"].astype("int64")

# Actual Web app that the user can see.
st.title('Interactive Vehicle Stats Dashboard')

st.markdown('''
            Welcome to the **Vehicle Data Explorer**, an interactive tool for exploring and comparing vehicle data.  
            Gain insights into vehicle pricing, attributes, and trends with just a few clicks.  
            
            **Features:**
            - **Explore Data:** Filter vehicles by model year and brand.
            - **Compare Prices:** Analyze price distributions between two brands.
            - **Visualize Trends:** See color and type distributions by brand.

            **Data Source:** [TripleTen](https://triplet.com/)
            ''')

# Chose a dataset based on User's Input
st.sidebar.title("Customize Your Analysis")
st.sidebar.markdown("Select the model year and vehicle brands to refine your analysis.")
st.sidebar.header('User Input Features')  # sidebar is a vertical column on the left side of the web app - This is the title of the side bar
selected_year = st.sidebar.selectbox('Model Year', list(reversed(range(1908,2019))))  # selectbox is a dropdown menu for the sidebar


# Performing web scraping of vehicle data
@st.cache_data  # This function will be cached so that it will only
def load_data(manufacturer):
    data = df[df['manufacturer'] == manufacturer]
    return data

# Display the data  
vehicle_list = load_data(selected_year)

# Side bar Vehicle Selection
sorted_unique_manufacturer = sorted(df['manufacturer'].unique())
selected_vehicle = st.sidebar.multiselect('Brand', sorted_unique_manufacturer, sorted_unique_manufacturer)

# Filtering the data
df_selected_vehicle = df[(df['manufacturer'].isin(selected_vehicle)) & (df['model_year'] == selected_year)]

# Add a warning if no data is selected:
if df_selected_vehicle.empty:
    st.warning("No vehicles match the selected filters. Please adjust your choices.")

st.header('Display Vehicle(s) Data')
st.write('Data Dimension: ' + str(df_selected_vehicle.shape[0]) + ' rows and ' + str(df_selected_vehicle.shape[1]) + ' columns.')
st.dataframe(df_selected_vehicle)

# Downloading Selected Data Function
def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
    href = f'<a href="data:file/csv;base64,{b64}" download="vehicle_selected_data.csv">Download Your Selected Data as CSV File</a>'
    return href

st.markdown(filedownload(df_selected_vehicle), unsafe_allow_html=True)

# Add a horizontal line
st.markdown('---')

#################################### Price Distribution ########################################
st.subheader('Price Distribution Overview')
st.markdown("Choose between a scatter plot or histogram to visualize vehicle price data. Scatter plots include brand names for better insights.")

#add a checkbox if a user wants to see the data in log scale
scatter_plots = st.checkbox('Scatter Plots with Brand Name', value=False)
if scatter_plots:
    fig1=px.scatter(df, x='price', y='manufacturer', title='Price Distribution in Scatter Plot with Brand Name', labels={'price': 'Price/USD', 'manufacturer': 'Brand'})
else:
    fig1 = px.histogram(df, x='price', title='Price Distribution in Histogram Plot', labels={'price': 'Price/USD', 'index': 'Index'})
st.plotly_chart(fig1)

# Add a horizontal line
st.markdown('---')

################################### Compare Price Section ########################################
st.header('Compare Price Distribution between 2 Brands')
st.markdown('''
            Select two brands to compare their price distribution.
            ''')
#get a list of car manufacturers
manufac_list = sorted(df['manufacturer'].unique())
#get user's inputs from a dropdown menu

col1, col2 = st.columns(2) # using this line to create two columns

with col1:  # using this with to ensure the selectbox is placed inside the first column
    manufacturer1 = st.selectbox(label='Select the 1st Brand', # title of the select box
                              options=manufac_list, # options listed in the select box
                              index=manufac_list.index('acura') # default pre-selected option
                              )
# repeat for the second dropdown menu
with col2:
    manufacturer2 = st.selectbox(label='Select the 2nd Brand', #title of the select box
                             options= manufac_list, # option listed in the select box
                             index= manufac_list.index('bmw') #default pre-selected option
                             )
#filter the dataframe
mask_filter = (df['manufacturer'] == manufacturer1) | (df['manufacturer'] == manufacturer2)
df_filtered = df[mask_filter]

#add a checkbox if a user wants to normalize the histogram
normalize = st.checkbox('Show Histogram as Percentage', value=True)

if normalize:
    histnorm = 'percent'
else:
    histnorm = None
    
    
# Create a plotly histogram figure
fig = px.histogram(df_filtered, 
                   x='price', 
                   color='manufacturer', 
                   histnorm=histnorm,
                   barmode='overlay',)

# display the figure with streamlit
st.write(fig)

st.markdown('---')


################################### Vehicle Make by Brand Section ##################################
st.header('Vehicle Brand by Color')
st.markdown('''
            The following plot shows the distribution of vehicle types by color for each brand.
            Click on the color name to remove it from histogram.
            ''')
fig= px.histogram(df, x=df['manufacturer'], color='paint_color', title='Distribution of Vehicle Type', labels={'manufacturer': 'Brand', 'paint_color': 'Paint Color'})
st.write(fig)


st.markdown('---')
st.markdown("**Created with ❤️ using Streamlit and Plotly**")





