
# Random Algorithms and Data Structures

This project offers a comprehensive collection of algorithms and data structures for generating random variables and various combinatorial objects, including random partitions, subsets, Dyck words, Young tableaux, and binary trees. Each function is meticulously optimized for performance, with its corresponding time complexity clearly documented.

To ensure the uniformity and correctness of the generated random objects, the accompanying notebook [tests.ipynb](tests.ipynb) provides detailed visualizations and rigorous tests.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Functions and Complexities](#functions-and-complexities)
  - [Random Number Generation](#random-number-generation)
  - [Combinatorial Algorithms](#combinatorial-algorithms)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/FrederikBenirschke/univariate-random-generator.git
   ```

2. **Navigate to the project directory**:

   ```bash
   cd random-algorithms
   ```

3. **Install the required dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

## Functions and Complexities

Currently, the following random variables are implemented:

- Uniform, Normal, Exponential, Poisson, Bernoulli, Binomial, Geometric, \(	ext{Chi}^2\), Uniform distribution on the disk, and the circle.

### Random Number Generation

| Function                    | Runtime Complexity |
|-----------------------------|--------------------|
| `uniform(a, b)`             | O(1)               |
| `uniform_int(a, b)`         | O(1)               |
| `normal(mu, sigma)`         | O(1)               |
| `exponential(exp_lambda)`   | O(1)               |
| `poisson(lambda)`           | O(lambda)          |
| `bernoulli(p)`              | O(1)               |
| `binomial(n, p)`            | O(n)               |
| `geometric(p)`              | O(1)               |
| `chi_squared(k)`            | O(k)               |
| `uniform_disk(r)`           | O(1)               |
| `uniform_circle(r)`         | O(1)               |

### Combinatorial Algorithms

The package also provides functionality for the following random combinatorial objects:

- Permutations, Subsets, Partitions (ordered, unordered, fixed number of parts), Young tableaux, Dyck words, Binary trees

| Function                            | Runtime Complexity                              |
|-------------------------------------|-------------------------------------------------|
| `random_permutation(n)`             | O(n)                                            |
| `random_subset(n, k)`               | O(k)                                            |
| `random_partition_with_parts(n, k)` | O(k log k)                                      |
| `sample(lst, weights)`              | O(n)                                            |
| `number_partitions(n, max_part)`    | O(n * max_part)                                 |
| `random_partition(n, max_part)`     | O(n) (preprocessing: O(n * max_part))           |
| `random_ordered_partition(n)`       | O(n)                                            |
| `young_tableaux(partition, sort)`   | O(n)                                            |
| `random_young_tableaux(n)`          | O(n * max_part)                                 |
| `number_dyck_words(n)`              | O(n)                                            |
| `random_dyck_word(n)`               | O(n) (preprocessing: O(n^2))                    |
| `dyck_word_to_tree(word)`           | O(n)                                            |
| `random_binary_tree(n)`             | O(n) (preprocessing: O(n^2))                    |

## Examples

### Example 1: Generate a Random Uniform Number

```python
result = uniform(0, 1)
print(f"Random number uniformly distributed between 0 and 1: {result}")
```

### Example 2: Generate a Random Partition

```python
partition = random_partition(10, 5)
print(f"Random partition of 10 into parts not exceeding 5: {partition}")
```

### Example 3: Generate a Random Binary Tree

```python
tree = random_binary_tree(4)
print(f"Random binary tree with 4 nodes:
{tree}")
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with your improvements or suggestions.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
