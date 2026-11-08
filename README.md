# Neural Network X-O Recognition using Hebbian Learning

A simple neural network implementation in Python that recognizes **X and O patterns** using the Hebbian learning rule.

This project demonstrates how a single artificial neuron can learn patterns by adjusting its weights based on input-output associations, without using traditional error-based training algorithms.

## Project Overview

The neural network is designed to distinguish between two patterns:

- **X**
- **O**

Each pattern is represented as a 5 × 5 grid of symbols. The grid is converted into a numerical input vector and passed to a single neuron.

The network learns the relationship between the input patterns and their corresponding target values using the **Hebbian learning algorithm**.

## Neural Network Architecture

The project uses a single-layer neural network consisting of:

- 25 input features (one for each cell in the 5 × 5 grid).
- One output neuron.
- A weight for each input feature.
- A bias input and its corresponding weight.

### Input Representation

Each pattern is represented by a 5 × 5 matrix.

The symbols are converted into numerical values as follows:

| Symbol | Numerical Value |
|---|---:|
| `#` | 1 |
| `.` | -1 |
| Other characters | 0 |

The resulting matrix is flattened into a 25-element vector.

### Example Patterns

**X**

```text
#...#
.#.#.
..#..
.#.#.
#...#
```

**O**

```text
.###.
#...#
#...#
#...#
.###.
```

## Hebbian Learning Algorithm

The network uses the Hebbian learning rule, which is based on the principle:

**"Neurons that fire together, wire together."**

During training, the weights are adjusted according to the relationship between each input feature and its target output.

The weight update rule is:

\[
w_i^{new}=w_i^{old}+x_i \times y
\]

Where:

- \(w_i\): Weight associated with input \(i\).
- \(x_i\): Input feature.
- \(y\): Target output.

The bias weight is updated similarly:

\[
w_b^{new}=w_b^{old}+b \times y
\]

Where \(b\) is the bias input.

The implementation initializes the weights to zero and accumulates the contributions of the training samples.

After training, the resulting weights represent the learned association between the input patterns and their target values.

## Pattern Recognition

After training, a new pattern can be passed to the network.

The neuron calculates a weighted sum of its input features:

\[
net=\sum_{i=1}^{25}x_iw_i
\]

The resulting value is used as the network's recognition score.

The program evaluates the following:

1. The original X pattern.
2. The original O pattern.
3. Six additional patterns that differ from the training examples.

This allows the behavior of the trained network to be examined using both familiar and unfamiliar inputs.

## Project Structure

```text
Neural-Network-X-O-Recognition/
│
├── inputs/
│   ├── x.txt
│   └── o.txt
│
├── hebb.py
├── file_handling.py
├── inputs.txt
├── check-points.txt
├── test.py
├── main.py
└── doc.pdf
```

### Main Files

| File | Description |
|---|---|
| `hebb.py` | Implements the Hebbian learning algorithm and weight calculation. |
| `file_handling.py` | Reads training data and converts symbols into numerical values. |
| `inputs.txt` | Contains the paths to the training input files. |
| `inputs/x.txt` | Contains the X training pattern and its target value. |
| `inputs/o.txt` | Contains the O training pattern and its target value. |
| `test.py` | Defines the X, O, and additional test patterns. |
| `main.py` | Initializes the network, trains it, calculates weights, and evaluates test patterns. |
| `doc.pdf` | Project documentation. |

## Installation and Execution

### Requirements

- Python 3.x
- No external Python libraries are required.

### Run the Project

Clone the repository:

```bash
git clone https://github.com/sonia-heidary/Neural-Network-X-O-Recognition.git
```

Navigate to the project directory:

```bash
cd Neural-Network-X-O-Recognition
```

Run the program:

```bash
python main.py
```

The program will:

1. Read the training patterns.
2. Convert the input symbols into numerical values.
3. Train the network using Hebbian learning.
4. Calculate and display the learned weights.
5. Evaluate X and O patterns.
6. Evaluate additional patterns and display their recognition scores.

## Learning Objectives

This project demonstrates:

- Fundamental concepts of artificial neural networks.
- Implementation of a single-neuron network.
- Hebbian learning and its mathematical formulation.
- Weight and bias calculation.
- Converting symbolic patterns into numerical input vectors.
- Applying learned weights to recognize patterns.
- Evaluating neural network behavior with different input patterns.

---

**Author:** Sonia Heidary

**Repository:** [Neural-Network-X-O-Recognition](https://github.com/sonia-heidary/Neural-Network-X-O-Recognition)
