# List disk files according to a string
xlsFiles = [x for x in listdir() if 'xls_' in x] # Where 'xls_' is an expression

# Read different input files and store data frames in a dictionary
raw_data = {i: pd.read_excel(i) for i in xlsFiles}

# Create a new column with dictionary key data
for i in raw_data.keys():
    raw_data[i]['id'] = i

# Flatten dictionary into a data frame
flatten_data = pd.concat(raw_data.values(), ignore_index=True)
