import pandas as pd


# NIC format validation parameters
def validate_nic_format(nic):
    # NIC validation logic that makes sure to check if the length is either 10 or 12 characters
    if len(nic) != 10 and len(nic) != 12:
        return False
    return True


# Fingerprint data validation parameters
def validate_fingerprint_data(fingerprint_data):
    required_fingers = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
    provided_fingers = fingerprint_data.keys()
    if set(required_fingers) != set(provided_fingers):
        return False
    return True


def register_fingerprint(nic, fingerprint_data):
    # NIC format validation
    if not validate_nic_format(nic):
        print("Invalid NIC. Please enter a valid NIC.")
        return

    # Fingerprint data validation
    # Function derived from the scanner's library to capture the fingerprint
    fingerprint_data = capture_fingerprints()
    if not validate_fingerprint_data(fingerprint_data):
        print("Incomplete scan. Please place both hands and all fingers on the scanner.")
        return

    # Creates a DataFrame to store each fingerprint
    df = pd.DataFrame(columns=['NIC', 'Hand', 'Finger', 'Fingerprint'])

    # Loops the process through each finger and stores each fingerprint in the DataFrame
    for hand, fingers in fingerprint_data.items():
        for finger, fingerprint in fingers.items():
            # Stores the fingerprint in the DataFrame
            df = df.append({'NIC': nic, 'Hand': hand, 'Finger': finger, 'Fingerprint': fingerprint}, ignore_index=True)

    # Checks for existing files
    def df_exists():
        try:
            pd.read_csv('fingerprint_database.csv')
            return True
        except FileNotFoundError:
            return False

    # Saves the DataFrame to a CSV file
    df.to_csv('fingerprint_database.csv', mode='a', index=False, header=not df_exists())


# Example usage
nic = '1234567890'
handprints = {
    'Left': {'Thumb': 'left_thumb_fingerprint_data',
             'Index': 'left_index_fingerprint_data',
             'Middle': 'left_middle_fingerprint_data',
             'Ring': 'left_ring_fingerprint_data',
             'Pinky': 'left_pinky_fingerprint_data'},
    'Right': {'Thumb': 'right_thumb_fingerprint_data',
              'Index': 'right_index_fingerprint_data',
              'Middle': 'right_middle_fingerprint_data',
              'Ring': 'right_ring_fingerprint_data',
              'Pinky': 'right_pinky_fingerprint_data'}
}

register_fingerprint(nic, handprints)
