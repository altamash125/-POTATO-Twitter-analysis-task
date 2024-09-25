import pandas as pd
import streamlit as st

# Load the dataset
file_path = 'data/correct_twitter_201904.tsv'  
df = pd.read_csv(file_path, sep='\t')

# Convert 'created_at' column to datetime once at the start
df['created_at'] = pd.to_datetime(df['created_at'], errors='coerce')

# Function to query tweets
def query_tweets(term, df):
    # Filter the tweets containing the search term in 'text' column
    filtered_df = df[df['text'].str.contains(term, case=False, na=False)]
    
    # Check if any tweets are found
    if filtered_df.empty:
        return None, 0, 0
    
    # Tweets per day
    daily_tweets = filtered_df.groupby(filtered_df['created_at'].dt.date).size()
    
    # Unique users
    unique_users = filtered_df['author_id'].nunique()
    
    # Average likes
    avg_likes = filtered_df['like_count'].mean()
    
    return daily_tweets, unique_users, avg_likes

# Main Streamlit app
def main():
    st.title("POTATO Twitter Term Analysis")

    # Input for the search term
    search_term = st.text_input("Enter search term:", value="")

    # Trigger query when the button is pressed
    if st.button("Search"):
        if search_term.strip():
            daily_tweets, unique_users, avg_likes = query_tweets(search_term, df)
            
            if daily_tweets is None:
                st.warning(f"No tweets found for the term '{search_term}'.")
            else:
                st.subheader(f"Results for '{search_term}':")
                st.write(f"Number of tweets per day:")
                st.dataframe(daily_tweets)
                st.write(f"Unique users: {unique_users}")
                st.write(f"Average likes: {avg_likes:.2f}")
        else:
            st.error("Please enter a search term.")

if __name__ == "__main__":
    main()
