# -Pie-Chart-Visualization-using-Matplotlib
This project demonstrates how to create a simple pie chart using Python’s matplotlib library. The chart represents the popularity distribution of different programming languages including Python, Java, Scala, and C#.

🚀 Features
Uses matplotlib for data visualization
Displays percentage values on each slice
Custom labels for each programming language
Adjustable starting angle and direction
Clean and simple code for beginners
🛠️ Requirements

Make sure you have Python installed along with the required library:
pip install matplotlib
📌 Code Explanation
labels: Contains the names of programming languages
sizes: Represents their respective percentages
plt.pie(): Creates the pie chart with:
autopct='%1.1f%%' to show percentages
counterclock=False to change direction
startangle=105 to rotate the chart
plt.show(): Displays the chart window

📷 Output

The program generates a pie chart showing:

Python: 45%
Java: 30%
Scala: 15%
C#: 10%
📚 Use Case

This project is useful for beginners learning data visualization in Python and can be extended for real-world data analysis tasks.
