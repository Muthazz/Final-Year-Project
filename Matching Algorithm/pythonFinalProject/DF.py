import pandas as pd

df = pd.DataFrame(columns=['NIC', 'Hand', 'Finger', 'Fingerprint'])

# Add the row with the image to the DataFrame
df.loc[0] = ['000000015F', 'Right', 'Thumb', "SOCOFing/Real/15__F_Right_thumb_finger.BMP"]
df.loc[1] = ['000000100M', 'Right', 'Ring', "SOCOFing/Real/100__M_Right_ring_finger.BMP"]
df.loc[2] = ['000000106M', 'Left', 'Thumb', "SOCOFing/Real/106__M_Left_thumb_finger.BMP"]
df.loc[3] = ['000000109F', 'Left', 'Index', "SOCOFing/Real/109__F_Left_index_finger.BMP"]
df.loc[4] = ['000000111M', 'Left', 'Ring', "SOCOFing/Real/111__M_Left_ring_finger.BMP"]
df.loc[5] = ['000000114F', 'Left', 'Middle', "SOCOFing/Real/114__F_Left_middle_finger.BMP"]
df.loc[6] = ['000000119F', 'Left', 'Little', "SOCOFing/Real/119__F_Left_little_finger.BMP"]
df.loc[7] = ['000000125M', 'Right', 'Middle', "SOCOFing/Real/125__M_Right_middle_finger.BMP"]
df.loc[8] = ['000000127F', 'Right', 'Little', "SOCOFing/Real/127__F_Right_little_finger.BMP"]
df.loc[9] = ['000000132M', 'Right', 'Index', "SOCOFing/Real/132__M_Right_index_finger.BMP"]

# Display the DataFrame
print(df)
