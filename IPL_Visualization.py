import pandas as pd
import matplotlib.pyplot as plt
from screeninfo import get_monitors

# IPL 2025 ka data load karen
# Aapko apne actual IPL data file ka path yahan dena hoga
# Example: 'ipl_2025_data.csv' (CSV file)

df = pd.read_csv('IPL_data.csv')

# Data ko inspect karen
print("First few rows of the data:")
print(df.head())

# Data ko clean karen (agar zaroorat ho)
df = df.dropna()  # Remove missing values (if any)

# Get the screen's width and height
monitor = get_monitors()[0]  # Get primary monitor
screen_width = monitor.width
screen_height = monitor.height

# Scatter Plot: Runs vs Wickets (Player performance)
plt.figure(figsize=(screen_width / 100, screen_height / 100))  # Adjust figure size to screen resolution
plt.scatter(df['Runs'], df['Wickets'], color='blue')
plt.title('Runs vs Wickets (IPL 2025)')
plt.xlabel('Runs')
plt.ylabel('Wickets')

# Make the plot full-screen
manager = plt.get_current_fig_manager()
manager.full_screen_toggle()

plt.show()

# Pie Chart: Team-wise performance distribution
team_performance = df['Team'].value_counts()
team_performance.plot(kind='pie', autopct='%1.1f%%', startangle=90, figsize=(8, 8))
plt.title('Team Performance in IPL 2025')
plt.ylabel('')  # Remove y-axis label for better appearance

# Make the plot full-screen
manager = plt.get_current_fig_manager()
manager.full_screen_toggle()

plt.show()

# Bar Chart: Top 10 players by runs (Example)
top_players_runs = df.groupby('Player')['Runs'].sum().nlargest(10)
top_players_runs.plot(kind='bar', color='green', figsize=(screen_width / 100, screen_height / 100))
plt.title('Top 10 Players by Runs (IPL 2025)')
plt.xlabel('Player')
plt.ylabel('Runs')
plt.xticks(rotation=45)

# Make the plot full-screen
manager = plt.get_current_fig_manager()
manager.full_screen_toggle()

plt.show()

# Scatter plot of Strike Rate vs Runs (Another performance indicator)
plt.figure(figsize=(screen_width / 100, screen_height / 100))  # Adjusting figure size to full-screen resolution
plt.scatter(df['Strike Rate'], df['Runs'], color='orange')
plt.title('Strike Rate vs Runs (IPL 2025)')
plt.xlabel('Strike Rate')
plt.ylabel('Runs')

# Make the plot full-screen
manager = plt.get_current_fig_manager()
manager.full_screen_toggle()

plt.show()

# Line plot for a team's performance over the season (Example for one team)
# Replace 'TeamName' with the actual team name
team_data = df[df['Team'] == 'TeamName']  # Filter data for a particular team
team_data['Match Number'] = range(1, len(team_data) + 1)  # Match numbers for x-axis

plt.figure(figsize=(screen_width / 100, screen_height / 100))  # Adjusting figure size to full-screen resolution
plt.plot(team_data['Match Number'], team_data['Runs'], marker='o', color='purple')
plt.title('Team Performance over Matches (Runs) - IPL 2025')
plt.xlabel('Match Number')
plt.ylabel('Runs')

# Make the plot full-screen
manager = plt.get_current_fig_manager()
manager.full_screen_toggle()

plt.show()
