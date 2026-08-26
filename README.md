# Artificial Intelligence Lab Exercises

A collection of Artificial Intelligence and Machine Learning laboratory exercises developed using Python, Jupyter Notebook, PyTorch, scikit-learn, Tkinter, Pygame, and related libraries.

The repository covers classical AI search techniques, constraint satisfaction, machine learning algorithms, neural networks, and deep learning concepts.

## Lab Contents

| Lab       | Topic                                    | Files                                                                            |
| --------- | ---------------------------------------- | -------------------------------------------------------------------------------- |
| **Lab 1** | Search and Backtracking Algorithms       | Maze solver, Sudoku solver, Dijkstra route finder                                |
| **Lab 2** | Adversarial Search, Backtracking and CSP | Minimax Tic-Tac-Toe, tree backtracking, constraint-satisfaction graph colouring  |
| **Lab 3** | Graph Data and Recommendation            | Synthetic research-paper network generation and similarity-based recommendations |
| **Lab 4** | Classical Machine Learning Similarity    | Jaccard similarity, cosine similarity, TF-IDF and KNN                            |
| **Lab 5** | Naive Bayes and Probabilistic Models     | Gaussian Naive Bayes classification and Bayesian Network examples                |
| **Lab 6** | Support Vector Machines                  | Hard-margin, soft-margin and kernel-based SVM implementations                    |
| **Lab 7** | Introduction to PyTorch                  | Tensors, autograd, neural networks, data loaders and model training              |
| **Lab 8** | Neural Network Classification            | Titanic survival analysis and prediction using PyTorch                           |
| **Lab 9** | Convolutional Neural Networks            | CNN architecture and fundamental convolution concepts                            |

## Repository Structure

### LAB 1

`import pygame.py`
Visual maze-solving exercise.

`second.py`
Sudoku solver using backtracking with Pygame visualisation.

`third.py`
Interactive route-finding application using Dijkstra's shortest-path algorithm.

### LAB 2

`adversial-serach.py`
Tic-Tac-Toe application where the AI selects moves using the Minimax algorithm with alpha-beta pruning.

`backtrack.py`
Interactive tree-search and backtracking visualisation.

`csp.py`
Constraint Satisfaction Problem implementation using graph colouring and backtracking.

`IMPLEMENTATION OF BACKTRACKING ALGORITHM.docx`
Lab report covering the backtracking implementation.

### LAB 3

`network_generator.ipynb`
Generates a synthetic research-paper network and explores relationships between papers, domains and methodologies.

`network_data.json`
Generated graph dataset used by the lab.

`index.html`
Browser-based visualisation of the generated network.

`lab 3 report.docx`
Lab report and supporting documentation.

### LAB 4

`lab.ipynb`
Explores Jaccard similarity, cosine similarity, TF-IDF vectorisation and nearest-neighbour techniques for research-paper similarity.

`research_papers_network.csv`
Dataset used by the notebook.

### LAB 5

`Naive-Bayesian-Classification-main/cancer.ipynb`
Machine Learning lab covering Gaussian Naive Bayes classification, data preprocessing and classification evaluation.

`Naive-Bayesian-Classification-main/dataset.csv`
Dataset used for the classification exercise.

`Naive-Bayesian-Classification-main/main.py`
Example Bayesian Network implementation using probabilistic graphical models.

### LAB 6

`lab.ipynb`
Support Vector Machine exercises covering separating hyperplanes, maximum margins, support vectors, soft margins and kernel methods.

### LAB 7

`code-part1.ipynb`
Introduction to PyTorch including tensors, tensor operations, computation graphs, automatic differentiation, multilayer neural networks, data loaders and training loops.

### LAB 8

`titanic_pytorch_merged_final.ipynb`
Titanic passenger survival analysis and prediction using a PyTorch neural network.

`titanic.csv`
Titanic passenger dataset used by the notebook.

### LAB 9

`LAB 9.ipynb`
Theory and explanation of Convolutional Neural Networks, including convolution, kernels, feature maps and CNN architecture.

## Technologies

* Python
* Jupyter Notebook
* PyTorch
* scikit-learn
* Pandas
* NumPy
* Matplotlib
* Tkinter
* Pygame
* pgmpy
* CVXOPT

## Running the Exercises

Clone the repository:

```bash
git clone https://github.com/dilasha68/AI-LABS.git
cd AI-LABS
```

Install the libraries required by the individual labs as needed.

Python scripts can be executed with:

```bash
python filename.py
```

Jupyter notebooks can be opened using Jupyter Notebook, JupyterLab, VS Code, or Google Colab.

Some Lab 1 and Lab 2 exercises use graphical interfaces and therefore require a desktop environment.

## About

This repository contains Artificial Intelligence coursework covering search algorithms, constraint satisfaction, machine learning, graph-based data, neural networks and deep learning through practical Python and Jupyter exercises.
