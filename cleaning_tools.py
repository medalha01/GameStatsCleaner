import pandas as pd


def get_element(lst, index):
    """
    Retrieves the element at the specified index from a list, if it exists and is not None.
    Returns 'Empty' if the index is out of bounds or the element is None.
    """
    if index <= len(lst) and lst[index - 1] is not None:
        return lst[index - 1]
    return "Empty"

def cleaning_null(path, new_cv_path):
    """
    Cleans the DataFrame by dropping rows where specific 'teamname' and 'ban' columns have null values,
    then replaces remaining nulls with 'None', and saves the cleaned DataFrame to a new CSV file.
    """
    df = pd.read_csv(path)
    for j in range (1,3):
        df = df.dropna(subset=[f'teamname{j}'])
        for m in range(1,6):
            df = df.dropna(subset=[f'ban{m}-{j}'])

    df = df.fillna("None")

    df.to_csv(new_cv_path, index=False)
    
def data_treatment(path, save_path):
    """
    Processes the CSV data from the specified path by selecting relevant columns, 
    aggregating and transforming data, and saving the processed data to a new CSV.
    """
    game_df = pd.read_csv(path)
    selected_columns = [
        "gameid", "league", "year", "split", "playoffs", "game", "patch", "playername", 
        "teamname", "champion", "ban1", "ban2", "ban3", "ban4", "ban5", "pick1", "pick2", 
        "pick3", "pick4", "pick5", "result"
    ]
    
    # Filtering the DataFrame to include only the selected columns
    modified_df = game_df[selected_columns]
    
    # Define aggregation functions for each column
    unique_list_agg = lambda x: x.unique().tolist()
    aggregation_functions = {
        'league': 'first', 'year': 'first', 'split': 'first', 'playoffs': 'first', 
        'game': 'first', 'patch': 'first', 'teamname': unique_list_agg, 
        'playername': list, 'champion': list, 'result': 'first'
    }
    # Add ban and pick columns with aggregation
    for col in ['ban', 'pick']:
        for i in range(1, 6):
            aggregation_functions[f'{col}{i}'] = unique_list_agg   
    grouped_df = modified_df.groupby('gameid').agg(aggregation_functions).reset_index()
    for i in range(1, 11):
        grouped_df[f'playername{i}'] = grouped_df['playername'].apply(get_element, index=i)
    for i in range(1, 3):
        grouped_df[f'teamname{i}'] = grouped_df['teamname'].apply(get_element, index=i)
        for col in ['ban', 'pick']:
            for j in range(1, 6):
                if col == 'ban':
                    grouped_df[f'{col}{j}-{i}'] = grouped_df[f'{col}{j}'].apply(get_element, index=i)
                else:
                    grouped_df[f'{col}{j}-{i}'] = grouped_df[f'{col}{j}'].apply(get_element, index=i+1)
    
    # Creating separate columns for blue and red champions based on the original order
    for i in range(1, 11):
        column_name = f'blue-champion{i}' if i <= 5 else f'red-champion{i-5}'
        grouped_df[column_name] = grouped_df['champion'].apply(get_element, index=i)
    
    # Dropping the original columns that are no longer needed after expansion
    columns_to_drop = ['playername', 'teamname', 'champion'] + [f'{col}{i}' for col in ['ban', 'pick'] for i in range(1, 6)]
    grouped_df.drop(columns_to_drop, axis=1, inplace=True) 
    
    # Saving the processed DataFrame to a CSV file
    grouped_df.to_csv(save_path, index=False)

##

    


