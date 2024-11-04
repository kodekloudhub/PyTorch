"""
Build an annotations file to build our initial dataset. 

Using Pandas, create a CSV file named full_image_data.csv that contains 2 columns: file_path and label. 

file_path is the path to the image and label being the label to classify the image. 

The label is in the path of the image.
"""
import os
import glob
# Import Pandas
import ____ as ____

data = []

for file_path in glob.glob("data/*/*jpg"):
    # Extract the class label from the file path
    label = os.path.basename(os.path.dirname(____))
    # Append file path and label in a dictionary to data
    data.append({____: ____, ____: ____})

# Create a Dataframe from the data list 
df = ____.____(data)
# Save the Dataframe as a CSV file
df.to_csv(____, index=False)
