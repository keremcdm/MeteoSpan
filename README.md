## 🌤️ MeteoSpan

MeteoSpan is a simple Python application that retrieves past and future weather data through the Meteorology General Directorate (MGM) API.  

It asks the user how many days forward and backward they want to check, fetches the data accordingly, and prints it to the console.  

## 🚀 Features

- Get forward and backward day count from the user  
- Fetch data from the MGM API within the specified date range  
- Print JSON data in a readable format to the console  
- Provide meaningful warnings for invalid parameter inputs  
- Optional: JSON/CSV export, graphical output  

## 📋 To-Do List

1. **Project Planning**  
   - Defining the purpose: retrieving past/future weather data from the MGM API  
   - Defining parameters to be taken from the user:  
     - How many days back?  
     - How many days forward?  
     - City/location information?  

2. **Technical Research**  
   - Reviewing MGM API documentation  
   - Learning required key, endpoint, and limits  
   - If MGM access is restricted, exploring alternative services (e.g., Open-Meteo)  

3. **Project Setup**  
   - Preparing Python environment (`venv`, `requirements.txt`)  
   - Folder structure:  
     - `main.py` (entry point)  
     - `api_client.py` (MGM API calls)  
     - `utils.py` (helper functions)  

4. **User Interaction (CLI)**  
   - User questions:  
     - “How many days forward would you like to check?”  
     - “How many days backward would you like to check?”  
     - “Which city/coordinates would you like to query?”  

5. **Date Range Calculation**  
   - Creating forward/backward date range starting from today  
   - Preparing ranges as a list  

6. **API Integration**  
   - Connecting to the MGM API and fetching data for the specified date range  
   - Retrieving raw JSON data  
   - Implementing error handling  

7. **Data Processing**  
   - Converting JSON data into a readable format  
   - Printing to console in the format `date – temperature – weather condition`  

8. **Output**  
   - Formatted table output in the console  
   - Optional: CSV/JSON export  

9. **Testing & Validation**  
   - Testing with small and large date ranges  
   - Providing correct warnings for invalid parameters  

10. **Development (Optional Enhancements)**  
    - Displaying past and future data in different colors  
    - Graphical output (e.g., temperature curve)  
    - Allowing parameters to be passed as command-line arguments  
