# Import necessary libraries
import pandas as pd
import numpy as np

# Load CSV data into a DataFrame
def load_data(file_path):
    """
    Loads data from a CSV file into a pandas DataFrame.
    
    Args:
    file_path (str): The path to the CSV file.
    
    Returns:
    pd.DataFrame: DataFrame with the loaded data.
    """
    # Read CSV into DataFrame
    data = pd.read_csv(file_path)
    return data

# Function to optimize and calculate additional metrics
def optimize_credit_data(df):
    """
    This function calculates total debt, credit utilization, and flags high-risk consumers.
    
    Args:
    df (pd.DataFrame): DataFrame containing the credit data
    
    Returns:
    pd.DataFrame: Updated DataFrame with new columns for TotalDebt, CreditUtilization, and RiskFlag
    """
    # Calculate total debt (credit debt + other debt)
    df['TotalDebt'] = df['creddebt'] + df['othdebt']

    # Calculate credit utilization ratio (credit card debt / income)
    df['CreditUtilization'] = df['creddebt'] / df['income']

    # Flag consumers as high risk if their debt-to-income ratio exceeds 15%
    df['RiskFlag'] = df['debtinc'] > 15

    return df

# Main function to execute the workflow
def main(file_path):
    """
    Main function to manage the workflow:
    1. Load data from CSV.
    2. Optimize the data with additional metrics.
    3. Print and save the updated DataFrame.
    
    Args:
    file_path (str): The path to the CSV file.
    """
    # Step 1: Load data
    df = load_data(file_path)
    
    # Step 2: Optimize data with additional metrics
    optimized_df = optimize_credit_data(df)
    
    # Step 3: Display the first few rows of the updated data
    print(optimized_df.head())
    
    # Optional: Save the updated data to a new CSV file
    optimized_df.to_csv('optimized_consumer_credit_data.csv', index=False)
    print("Optimized data saved to 'optimized_consumer_credit_data.csv'.")

# Example usage
if __name__ == "__main__":
    # Provide the path to your CSV file
    csv_file_path = 'bankloans.csv'  # Replace this with your actual file path
    print((np.array(main(csv_file_path))).shape)
    # Run the main function
    main(csv_file_path)

# Function to calculate correlations between numerical columns
def calculate_correlations(df):
    """
    This function calculates and returns the correlation matrix for the numerical columns
    in the DataFrame.
    
    Args:
    df (pd.DataFrame): DataFrame containing numerical data
    
    Returns:
    pd.DataFrame: Correlation matrix
    """
    # Select only numerical columns
    numerical_df = df.select_dtypes(include=['float64', 'int64'])
    
    # Calculate the correlation matrix
    correlation_matrix = numerical_df.corr()
    
    return correlation_matrix

# Main function to calculate consumer credit management and correlations
def main(file_path):
    """
    Main function to manage the workflow:
    1. Load data from CSV.
    2. Optimize the data with additional metrics.
    3. Calculate and print correlation matrix.
    
    Args:
    file_path (str): The path to the CSV file.
    """
    # Step 1: Load data
    df = load_data(file_path)
    
    # Step 2: Optimize data with additional metrics
    optimized_df = optimize_credit_data(df)
    
    # Step 3: Calculate and display correlations
    correlations = calculate_correlations(optimized_df)
    print("Correlation Matrix:")
    print(correlations)
    
    # Optional: Save correlation matrix to a CSV file
    correlations.to_csv('correlation_matrix.csv')
    print("Correlation matrix saved to 'correlation_matrix.csv'.")

# Example usage
if __name__ == "__main__":
    # Provide the path to your CSV file
    csv_file_path = 'bankloans.csv'  # Replace this with your actual file path
    
    # Run the main function
    main(csv_file_path)
