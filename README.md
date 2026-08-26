# Artificial Intelligence Lab Exercises

A collection of Artificial Intelligence and Machine Learning laboratory exercises completed using Python, Jupyter Notebook, PyTorch, scikit-learn, Pygame, Tkinter, and related libraries.

The repository covers classical AI algorithms, search techniques, constraint satisfaction, machine learning, neural networks, and introductory deep learning concepts.

## Lab Contents

| Lab       | Topic                                          | Main Exercises                                              |
| --------- | ---------------------------------------------- | ----------------------------------------------------------- |
| **Lab 1** | Search and Backtracking Algorithms             | Maze solving, Sudoku solving, Dijkstra shortest-path search |
| **Lab 2** | Adversarial Search and Constraint Satisfaction | Minimax, backtracking, graph colouring and CSP              |
| **Lab 3** | Graph Data and Recommendations                 | Research-paper network generation and graph visualisation   |
| **Lab 4** | Similarity and Machine Learning                | Jaccard similarity, cosine similarity, TF-IDF and KNN       |
| **Lab 5** | Probabilistic Machine Learning                 | Naive Bayes classification and Bayesian Networks            |
| **Lab 6** | Support Vector Machines                        | SVM classification, margins and kernel methods              |
| **Lab 7** | PyTorch Fundamentals                           | Tensors, autograd, neural networks and training             |
| **Lab 8** | Neural Network Classification                  | Titanic survival prediction using PyTorch                   |
| **Lab 9** | Convolutional Neural Networks                  | CNN fundamentals, convolution and feature extraction        |

## Repository Structure

```text
AI-LABS/
│
├── LAB 1/
│   ├── maze_solver.py
│   ├── sudoku_solver.py
│   └── dijkstra_route_finder.py
│
├── LAB 2/
│   ├── adversarial_search.py
│   ├── backtracking.py
│   ├── csp_graph_coloring.py
│   └── backtracking_report.docx
│
├── LAB 3/
│   ├── network_generator.ipynb
│   ├── network_data.json
│   ├── network_visualization.html
│   └── lab_report.ipynb
│
├── LAB 4/
│   ├── similarity_analysis.ipynb
│   └── research_papers_network.csv
│
├── LAB 5/
│   ├── naive_bayes_classification.ipynb
│   ├── dataset.csv
│   └── bayesian_network.py
│
├── LAB 6/
│   └── svm.ipynb
│
├── LAB 7/
│   └── pytorch_fundamentals.ipynb
│
├── LAB 8/
│   ├── titanic_neural_network.ipynb
│   └── titanic.csv
│
├── LAB 9/
│   └── cnn.ipynb
│
├── .gitignore
└── README.md
```

## Lab 1: Search and Backtracking Algorithms

### `maze_solver.py`

Visual maze-solving exercise demonstrating search and path-finding concepts.

### `sudoku_solver.py`

Sudoku solver using the backtracking algorithm with a graphical Pygame interface.

### `dijkstra_route_finder.py`

Interactive route-finding exercise implementing Dijkstra's shortest-path algorithm.

## Lab 2: Adversarial Search and Constraint Satisfaction

### `adversarial_search.py`

Tic-Tac-Toe implementation where the computer selects moves using the Minimax algorithm and adversarial search techniques.

### `backtracking.py`

Interactive exercise demonstrating backtracking and systematic search.

### `csp_graph_coloring.py`

Constraint Satisfaction Problem implementation using graph colouring and backtracking.

### `backtracking_report.docx`

Supporting report explaining the implementation and concepts behind the backtracking algorithm.

## Lab 3: Graph Data and Recommendations

### `network_generator.ipynb`

Generates and analyses a synthetic research-paper network containing relationships between papers and research attributes.

### `network_data.json`

Graph data generated and used by the network exercise.

### `network_visualization.html`

Browser-based visualisation of the generated research network.

### `lab_3_report.docx`

Supporting documentation and report for Lab 3.

## Lab 4: Similarity Analysis

### `similarity_analysis.ipynb`

Explores similarity and recommendation techniques including:

* Jaccard similarity
* Cosine similarity
* TF-IDF vectorisation
* K-Nearest Neighbours
* Research-paper similarity analysis

### `research_papers_network.csv`

Dataset used for similarity analysis and experimentation.

## Lab 5: Naive Bayes and Bayesian Networks

### `naive_bayes_classification.ipynb`

Machine Learning exercise using Gaussian Naive Bayes for classification, including data preprocessing, model training and evaluation.

### `dataset.csv`

Dataset used for the classification exercise.

### `bayesian_network.py`

Python implementation demonstrating Bayesian Networks and probabilistic relationships between variables.

## Lab 6: Support Vector Machines

### `svm.ipynb`

Support Vector Machine exercises covering concepts such as:

* Separating hyperplanes
* Maximum-margin classification
* Support vectors
* Soft-margin classification
* Kernel methods

## Lab 7: PyTorch Fundamentals

### `pytorch_fundamentals.ipynb`

Introduction to PyTorch and neural network development covering:

* Tensors
* Tensor operations
* Automatic differentiation
* Computation graphs
* Neural network layers
* Data loaders
* Model training

## Lab 8: Neural Network Classification

### `titanic_neural_network.ipynb`

Titanic passenger survival analysis and prediction using a neural network built with PyTorch.

The notebook covers data preprocessing, model creation, training and prediction.

### `titanic.csv`

Titanic passenger dataset used for model training and evaluation.

## Lab 9: Convolutional Neural Networks

### `cnn.ipynb`

Introduction to Convolutional Neural Networks and their core concepts, including:

* Convolution operations
* Kernels and filters
* Feature maps
* CNN architecture
* Feature extraction

## Technologies Used

* Python
* Jupyter Notebook
* PyTorch
* scikit-learn
* Pandas
* NumPy
* Matplotlib
* Pygame
* Tkinter
* pgmpy

## Running the Project

Clone the repository:

```bash
git clone https://github.com/dilasha68/AI-LABS.git
cd AI-LABS
```

Python exercises can be executed using:

```bash
python filename.py
```

Jupyter Notebook exercises can be opened using:

* Jupyter Notebook
* JupyterLab
* Visual Studio Code
* Google Colab

Required Python libraries vary between labs and can be installed as needed using `pip`.

Some exercises use graphical interfaces through Pygame or Tkinter and therefore require a desktop environment.

## About

This repository contains practical Artificial Intelligence coursework covering classical search algorithms, constraint satisfaction, graph-based data, machine learning, probabilistic models, neural networks and deep learning fundamentals.
