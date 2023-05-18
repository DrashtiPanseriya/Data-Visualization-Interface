import pandas as pd
import matplotlib.pyplot as plt
import io
import base64

def generate_visuals(csv_file):
    # Read the CSV file and perform data visualization
    data = pd.read_csv(csv_file)


    data['time'] = pd.to_datetime(data['time'], format='%d-%m-%Y %H:%M')

    # Line Chart for Average RPM over Time
    plt.figure(figsize=(10, 6))
    for device_id, device_data in data.groupby('Device_id'):
        plt.plot(device_data['time'], device_data['RPM'], label=f'Device {device_id}')
    plt.xlabel('Time')
    plt.ylabel('Average RPM')
    plt.title('Average RPM over Time')
    plt.legend()
    plt.show()
    

    # Bar Chart for Device-wise Efficiency
    plt.figure(figsize=(10, 6))
    device_efficiency = data.groupby('Device_id')['Total_rotations'].max() / data.groupby('Device_id')['On_time'].sum()
    plt.bar(device_efficiency.index, device_efficiency.values)
    plt.xlabel('Device ID')
    plt.ylabel('Efficiency')
    plt.title('Device-wise Efficiency')
    plt.show()
    
    # Stacked Area Chart for On-time and Off-time
    plt.figure(figsize=(10, 6))
    for device_id, device_data in data.groupby('Device_id'):
        plt.stackplot(device_data['time'], device_data['On_time'], device_data['Off_time'], labels=[f'Device {device_id} - On Time', f'Device {device_id} - Off Time'])
    plt.xlabel('Time')
    plt.ylabel('Duration')
    plt.title('On-time and Off-time')
    plt.legend()
    plt.show()
   

    # Scatter Plot for RPM and Total Rotations
    plt.figure(figsize=(10, 6))
    for device_id, device_data in data.groupby('Device_id'):
        plt.scatter(device_data['RPM'], device_data['Total_rotations'], label=f'Device {device_id}')
    plt.xlabel('RPM')
    plt.ylabel('Total Rotations')
    plt.title('RPM vs Total Rotations')
    plt.legend()
    plt.show()
    

    # Box Plot for RPM Distribution
    plt.figure(figsize=(10, 6))
    data.boxplot(column='RPM', by='Device_id')
    plt.xlabel('Device ID')
    plt.ylabel('RPM')
    plt.title('RPM Distribution')
    plt.show()
    

    # Heatmap for RPM by Device and Time
    pivot_data = data.pivot_table(index='time', columns='Device_id', values='RPM', aggfunc='mean')
    plt.figure(figsize=(10, 6))
    plt.imshow(pivot_data, cmap='hot', aspect='auto')
    plt.colorbar()
    plt.xlabel('Device ID')
    plt.ylabel('Time')
    plt.title('RPM by Device and Time')
    plt.show()
    

    # Histogram for RPM Frequency
    plt.figure(figsize=(10, 6))
    plt.hist(data['RPM'], bins=10)
    plt.xlabel('RPM')
    plt.ylabel('Frequency')
    plt.title('\RPM Frequency')
    plt.show()
    

    # Pie Chart for On-time vs. Off-time
    data['time'] = pd.to_datetime(data['time'], format='%d-%m-%Y %H:%M')

    # Group data by Device_id
    grouped_data = data.groupby('Device_id')

    num_devices = len(grouped_data)
    num_cols = 3  # Number of columns in the grid layout
    num_rows = (num_devices + num_cols - 1) // num_cols  # Number of rows in the grid layout

    # Create subplots for the pie charts
    fig, axes = plt.subplots(num_rows, num_cols, figsize=(12, 8))
    axes = axes.flatten()

    # Iterate over each device and create a pie chart in each subplot
    for i, (device_id, device_data) in enumerate(grouped_data):
        # Calculate the total on-time and off-time for the device
        total_on_time = device_data['On_time'].sum()
        total_off_time = device_data['Off_time'].sum()

        # Create a pie chart for each device
        labels = ['On Time', 'Off Time']
        sizes = [total_on_time, total_off_time]

        # Plot the pie chart in the corresponding subplot
        ax = axes[i]
        ax.pie(sizes, labels=labels, autopct='%1.1f%%')
        ax.set_title(f'Device {device_id}')

    # Adjust the spacing between subplots
    plt.tight_layout()

    # Display the grid of pie charts
    plt.show()
        