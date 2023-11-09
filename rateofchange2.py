import pandas as pd
import os

def calculate_expected_points_change(dataframes, position_filter=None, min_expected_points_average=5, rate_of_change_weeks=2):
    for i in range(len(dataframes)):
        dataframes[i].rename(columns={'Fantasy Points x-Pts': f'Fantasy Points x-Pts_{i + 1}'}, inplace=True)

    merged_df = dataframes[0]  # Start with the first DataFrame
    for i, df in enumerate(dataframes[1:], start=2):
        merged_df = merged_df.merge(df, on='Player', how='outer', suffixes=('', f'_{i}'))

    pos_column = pd.read_csv(csv_files[0], usecols=['Player', 'Pos'])
    merged_df = merged_df.merge(pos_column, on='Player', how='left')
    
    selected_columns = ['Player', 'Pos'] + [f'Fantasy Points x-Pts_{i}' for i in range(1, len(dataframes) + 1)]
    merged_df = merged_df[selected_columns]

    merged_df['Average_Expected_Points'] = merged_df[selected_columns[2:len(dataframes)-rate_of_change_weeks]].mean(axis=1)

    if position_filter:
        filtered_df = merged_df[merged_df['Pos'] == position_filter]
    else:
        filtered_df = merged_df

    filtered_df = filtered_df[filtered_df['Average_Expected_Points'] >= min_expected_points_average]

    change_columns = [f'Fantasy Points x-Pts_{i}' for i in range(1, len(dataframes) + 1)]
    non_zero_df = filtered_df[change_columns]

    # Calculate the rate of change based on the specified number of weeks
    recent_weeks = change_columns[-rate_of_change_weeks:]
    old_weeks = change_columns[:len(dataframes)-rate_of_change_weeks] 
    filtered_df['Rate_of_Change'] = (100 * (non_zero_df[recent_weeks].mean(axis=1, skipna=True) - non_zero_df[old_weeks].mean(axis=1, skipna=True)) / non_zero_df[old_weeks].mean(axis=1, skipna=True)).round(4)

    filtered_df['RecentWeeksAVG'] = non_zero_df[recent_weeks].mean(axis=1, skipna=True)

    sorted_df = filtered_df.sort_values(by='Rate_of_Change', ascending=False)

    return sorted_df[['Player', 'Pos', 'Average_Expected_Points', 'RecentWeeksAVG', 'Rate_of_Change']]

csv_directory = os.path.join(os.path.expanduser("~/Desktop"), "CSV")
csv_files = [os.path.join(csv_directory, f"week{i}.csv") for i in range(1, 10)]
dataframes = [pd.read_csv(file, usecols=['Player', 'Fantasy Points x-Pts']) for file in csv_files]


XP_df = calculate_expected_points_change(dataframes, position_filter='RB', min_expected_points_average=8, rate_of_change_weeks=2)



def calculate_expected_points_change_QB(dataframes, min_expected_points_average=5, rate_of_change_weeks=2):
    for i in range(len(dataframes)):
        dataframes[i].rename(columns={'Fantasy Points x-Pts': f'Fantasy Points x-Pts_{i + 1}'}, inplace=True)

    merged_df = dataframes[0]  # Start with the first DataFrame
    for i, df in enumerate(dataframes[1:], start=2):
        merged_df = merged_df.merge(df, on='Player', how='outer', suffixes=('', f'_{i}'))

    pos_column = pd.read_csv(csv_files[0], usecols=['Player'])
    merged_df = merged_df.merge(pos_column, on='Player', how='left')
    
    selected_columns = ['Player'] + [f'Fantasy Points x-Pts_{i}' for i in range(1, len(dataframes) + 1)]
    merged_df = merged_df[selected_columns]

    merged_df['Average_Expected_Points'] = merged_df[selected_columns[2:len(dataframes)-rate_of_change_weeks]].mean(axis=1)

    filtered_df = merged_df

    filtered_df = filtered_df[filtered_df['Average_Expected_Points'] >= min_expected_points_average]

    change_columns = [f'Fantasy Points x-Pts_{i}' for i in range(1, len(dataframes) + 1)]
    non_zero_df = filtered_df[change_columns]

    # Calculate the rate of change based on the specified number of weeks
    recent_weeks = change_columns[-rate_of_change_weeks:]
    old_weeks = change_columns[:len(dataframes)-rate_of_change_weeks] 
    filtered_df['Rate_of_Change'] = (100 * (non_zero_df[recent_weeks].mean(axis=1, skipna=True) - non_zero_df[old_weeks].mean(axis=1, skipna=True)) / non_zero_df[old_weeks].mean(axis=1, skipna=True)).round(4)

    filtered_df['RecentWeeksAVG'] = non_zero_df[recent_weeks].mean(axis=1, skipna=True)

    sorted_df = filtered_df.sort_values(by='Rate_of_Change', ascending=False)

    return sorted_df[['Player', 'Average_Expected_Points', 'RecentWeeksAVG', 'Rate_of_Change']]

csv_directory = os.path.join(os.path.expanduser("~/Desktop"), "QBCSV")
csv_files = [os.path.join(csv_directory, f"week{i}.csv") for i in range(1, 10)]
dataframes = [pd.read_csv(file, usecols=['Player', 'Fantasy Points x-Pts']) for file in csv_files]


QB_df = calculate_expected_points_change_QB(dataframes, min_expected_points_average=8, rate_of_change_weeks=4)
pd.options.display.max_rows = 100
print(QB_df)
