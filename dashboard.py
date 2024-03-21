import streamlit as st
import psycopg2

def fetch_data_from_database():
    try:
        # Connect to the PostgreSQL database
        connection = psycopg2.connect(
            database="your_database",
            user="your_username",
            password="your_password",
            host="your_host",
            port="your_port"
        )

        # Create a cursor to execute SQL queries
        cursor = connection.cursor()

        # Execute a query to fetch data from the database
        cursor.execute("SELECT * FROM your_table")

        # Fetch all rows from the result set
        data = cursor.fetchall()

        return data
    except psycopg2.Error as e:
        st.error(f"Error: {e}")
    finally:
        # Close the database connection
        if connection:
            cursor.close()
            connection.close()

def main():
    st.title("Dashboard")

    # Fetch data from the database
    data = fetch_data_from_database()

    # Display the fetched data in the Streamlit app
    if data:
        st.write("Data from the database:")
        st.write(data)
    else:
        st.write("No data available.")

if __name__ == "__main__":
    main()
