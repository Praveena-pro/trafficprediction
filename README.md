# Traffic_Prediction

<h2>Introduction</h2>

<p>The provided code is designed to perform traffic prediction based on historical traffic data and geographical information about road segments. The code uses Python and several data science libraries, including pandas, numpy, and scikit-learn, to preprocess data, train a machine learning model, and visualize the results on a map. The goal of this project is to predict traffic speeds on various road segments, leveraging historical data and spatial relationships between connected road segments.</p>

<h2>Description</h2>

> Part 1: Data Preparation and Connection Matrix Creation
  - The first part of the code, implemented in the `file()` function, prepares the data by creating a connection matrix that represents the relationship between different road segments. This matrix is stored in a CSV file for later use.


> 1. Reading Data:
  * The code reads two CSV files: `connected_data.csv` and `data.csv`.
  * `connected_data.csv` contains `edgeId` and `connected_edges`, which indicate the connections between road segments.
  * `data.csv` contains traffic data, including `edgeId` and various traffic-related metrics.

> 2. Creating the Connection Matrix:
  * The code iterates through the `edgeId` list, creating a connection matrix where each cell indicates whether two road segments are connected (`1`), the same (`X`), or not connected (`-`).
  * The connection matrix is stored as a list of lists and written to a CSV file, `file.csv`.
> Part 2: Traffic Prediction and Visualization

- The second part of the code, implemented in the finmethod() function, uses the connection matrix and historical data to predict traffic speeds on various road segments and visualize the results on a map.

> 1. Reading Data:
  - The code reads the `file.csv`, `connected_data.csv`, and `data.csv` files again.
  - It extracts `edgeId` and `connected_edges` information to understand the relationships between road segments.

> 2. Identifying Connected Road Segments:
  - For each road segment, the code identifies its connected road segments based on the connection matrix.

> 3. Preparing Training and Testing Data:
  + The code prepares the training and testing data by extracting relevant traffic metrics for the connected road segments.
  + It uses these metrics to form feature vectors (`X`) and target values (`Y`).

> 4. Training a Machine Learning Model:
  * A simple linear regression model is trained using the feature vectors and target values.
  * The model is trained to predict traffic speeds based on the historical data of connected road segments.

> 5. Making Predictions:
  - The trained model is used to predict traffic speeds on the test data.
  - The predictions are stored in a list.

> 6. Visualization:
  - The code uses the Folium library to create a map visualization of the predicted traffic speeds.
  - Each road segment is displayed on the map, and the predicted speed is shown as a marker on the segment.

> 7. Saved Results:
  - After the traffic prediction process, the code generates several output files within the same directory:
    > I. Map Visualization:
      * The code utilizes the Folium library to create an interactive map visualization, displaying the predicted traffic speeds on various road segments. This visualization is saved as an HTML file named `my_map.html`.
    > II. Prediction Results:
      * The predicted traffic speeds for each road segment, along with their corresponding IDs, are stored in a JSON file named Road_Data.json.
   
<h1>Code Execution</h1>

[Data Acquisition Link](#)

## Version
```
Python >= 3.7.0 or anaconda
```

## Usage
Installation and Cloning Project:
```
git clone https://github.com/Jagadeeswar-reddy-c/Traffic_Prediction.git
cd Traffic_Prediction
pip install -r requirements.txt
```

> Instructiona
To execute the complete solution, follow these steps:
1. Run `road_matric_file.py`:
   * This script prepares the data and creates the connection matrix, which is saved in a CSV file.
```
python road_matric_file.py
```
2. Run `Road_Traffic_Prediction.py`:
   * This script uses the connection matrix and historical data to predict traffic speeds and visualize the results.
```
python Road_Traffic_Prediction.py
```


<h2>Key Features</h2>

 1. `Data Integration`: Seamlessly integrates multiple datasets, including historical traffic data and spatial information about road segments.
 2. `Connection Matrix Creation`: Constructs a connection matrix to represent the relationships between different road segments, facilitating the analysis of spatial connections.
 3. `Machine Learning Modeling`: Utilizes machine learning techniques, such as linear regression, to train predictive models based on historical data and spatial relationships.
 4. `Predictive Visualization`: Generates an interactive map visualization that displays predicted traffic speeds on various road segments, enhancing the understanding of traffic patterns.
 5. `Output Formats`: Produces output in various formats, including CSV for the connection matrix, JSON for prediction results, and HTML for the interactive map, enabling easy interpretation and further analysis.
 6. `Scalability`: Offers opportunities for scalability and extension by incorporating more sophisticated modeling approaches and additional datasets for improved accuracy and insights.
 7. `Real-world Application`: Demonstrates applicability in real-world scenarios by providing insights into traffic patterns and facilitating informed decision-making for traffic management and urban planning.

<h2>Summary</h2>

The code offers a comprehensive solution for traffic prediction, covering all stages from data preparation to visualization. It effectively utilizes spatial connections between road segments and historical traffic data to generate predictions. The resulting outputs consist of a CSV file containing the connection matrix, an interactive map displaying predicted traffic speeds, and a JSON file housing the prediction results. This approach can be further enhanced by incorporating advanced models and additional datasets to enhance accuracy and gain deeper insights into traffic patterns.

<h2>Conclusion</h2>

In conclusion, the provided code presents a robust framework for traffic prediction, demonstrating proficiency in data handling, analysis, and visualization. By leveraging the spatial relationships between road segments and historical traffic data, the code successfully generates predictions for traffic speeds. The output includes a comprehensive set of files, including a CSV file containing the connection matrix, an interactive map showcasing predicted traffic speeds, and a JSON file encapsulating prediction results. This methodology exhibits potential for further refinement and expansion through the integration of advanced modeling techniques and the incorporation of additional datasets. Overall, the code represents a promising approach for understanding and forecasting traffic patterns, with opportunities for continual improvement and application in real-world scenarios.
