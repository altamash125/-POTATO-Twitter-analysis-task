**POTATO Twitter Term Analysis:**
POTATO (Panel-based Open Term-level Aggregate Twitter Observatory) is a simple Twitter data analysis tool that allows users to search for a 
term (e.g., "COVID") and get aggregate statistics such as the number of tweets per day,
the number of unique users, and the average number of likes for tweets containing that term. This app is built with Streamlit, Pandas, and Python.

**Prerequisites**
Python 3.8+
Docker

Step1 :**Install Dependencies:**
git clone https://github.com/yourusername/potato-twitter-analysis.git
cd potato-twitter-analysis

Step 2 : **Create a virtual environment:**
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate


Step 3 :**Install required Python dependencies:**
pip install -r requirements.txt

Step 4 :**How to Run the Application Locally**
streamlit run app.py


Open the application: Once the app is running, it will automatically open in your browser. If not, go to http://localhost:8501 manually.

then Search term: "covid"
