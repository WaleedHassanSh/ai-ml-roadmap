# AI/ML Roadmap

This document contains the detailed learning path for this repository.

The roadmap is designed to progress from programming and computer science fundamentals toward machine learning, deep learning, modern AI systems, deployment, and research.

## Status Legend

- ✅ Complete
- 🟡 In Progress
- ⬜ Planned

---

# Phase 00 — Setup and Learning Workflow ✅

## Goal

Build a reliable development and learning environment before starting the technical curriculum.

## Topics

- Terminal basics
- Linux/shell workflow
- File organization
- Git
- GitHub
- Jupyter
- Virtual environments
- Basic debugging
- Documentation habits

## Completion Goal

Be able to work comfortably from the terminal, organize files, use Git for version control, and push work to GitHub.

---

# Phase 01 — Python Programming ✅

## Goal

Become comfortable solving programming problems and building small programs independently using Python.

## Topics

- Variables and data types
- Expressions
- Input/output
- Conditionals
- Loops
- Functions
- Scope
- Exceptions
- Libraries and packages
- File I/O
- CSV
- Regular expressions
- Object-oriented programming
- Unit testing

## Practical Work

- CS50P
- Python exercises
- Python mini-projects
- TradeTrack

## Completion Goal

Be able to design, implement, debug, and test small Python programs without relying on step-by-step instructions.

---

# Phase 02 — Computer Science Foundations ✅

## Goal

Develop the foundational computer science knowledge required for algorithms, systems, databases, software development, and AI/ML engineering.

## Topics

- C programming
- Arrays and strings
- Algorithms
- Memory
- Pointers
- Data structures
- Python
- SQL
- HTML
- CSS
- JavaScript
- Flask
- Database-backed applications

## Practical Work

- CS50x
- CS foundation exercises
- Problem-solving practice
- SQL projects
- StudyFlow

## Completion Goal

Understand how programs, memory, basic data structures, algorithms, databases, and simple web applications work at a foundational level.

---

# Phase 03 — Mathematics Foundations ✅

## Goal

Build the mathematical foundation required to understand machine learning rather than only use ML libraries.

## Main Areas

### Linear Algebra

- Vectors
- Matrices
- Matrix operations
- Linear transformations
- Systems of equations
- Span
- Basis
- Rank
- Orthogonality
- Projections
- Eigenvalues
- Eigenvectors
- PCA
- SVD concepts

### Calculus

- Functions
- Limits
- Derivatives
- Partial derivatives
- Gradients
- Chain rule
- Optimization

### Probability and Statistics

- Probability rules
- Conditional probability
- Bayes' theorem
- Random variables
- Probability distributions
- Expectation
- Variance
- Covariance
- Sampling
- Central Limit Theorem
- Confidence intervals
- Hypothesis testing
- Correlation
- Regression concepts

## Completion Goal

Understand the mathematical ideas used in optimization, regression, dimensionality reduction, probability models, and neural networks.

---

# Phase 04 — Algorithms, Databases, and Systems 🟡

## Goal

Strengthen the computer science and software-engineering foundations that become important when building larger AI/ML systems.

Phase 04 is a CS depth track. Algorithms and practical SQL are important foundations, while database internals, operating systems, networking, and distributed systems are complementary skills and are not strict prerequisites for beginning later AI/ML phases.

## Learning Order

```text
Algorithms and Data Structures
        ↓
SQL and Databases
        ↓
Database Internals
        ↓
Operating Systems
        ↓
Computer Networks
        ↓
Distributed Systems
```

## Depth Strategy

### Deep

- Algorithms and data structures
- SQL and database usage

### Medium

- Operating systems
- Networking
- Database internals

### Introductory to Medium

- Distributed systems

## Key Principle

The goal is not to complete every exercise from every resource.

Focus on understanding the important concepts and completing selected exercises and projects that reinforce them.

## Completion Goal

Be able to reason about algorithmic efficiency, database-backed systems, operating-system fundamentals, networking, and the basic architecture of distributed applications.

---

# Phase 05 — Data Stack and Exploratory Data Analysis ⬜

## Goal

Become comfortable transforming raw data into clean, understandable datasets suitable for analysis and machine learning.

## Tools

- NumPy
- pandas
- Matplotlib
- Jupyter
- SQL

## Topics

- NumPy arrays
- Vectorized operations
- pandas DataFrames
- Missing data
- Data cleaning
- Data transformation
- Aggregation
- Joining datasets
- Exploratory data analysis
- Visualization
- Statistical summaries
- Feature inspection

## Project Requirement

Complete at least one real-data analysis project.

## Completion Goal

Be able to take a raw dataset, clean it, explore it, visualize it, and explain meaningful findings.

---

# Phase 06 — Classical Machine Learning ⬜

## Goal

Learn the core machine-learning workflow and major classical algorithms.

## Topics

### ML Foundations

- Supervised learning
- Unsupervised learning
- Training, validation, and test sets
- Generalization
- Underfitting
- Overfitting
- Bias and variance
- Regularization
- Feature engineering
- Data leakage

### Algorithms

- Linear regression
- Logistic regression
- k-nearest neighbors
- Decision trees
- Random forests
- Gradient boosting
- Support vector machines
- Naive Bayes
- k-means clustering
- DBSCAN
- PCA

### Evaluation

- MAE
- MSE
- RMSE
- Accuracy
- Precision
- Recall
- F1
- ROC-AUC
- Confusion matrices
- Cross-validation

### Tooling

- scikit-learn
- preprocessing
- pipelines
- hyperparameter tuning

## Project Requirement

Complete end-to-end regression and classification work using real data.

## Completion Goal

Be able to independently take a tabular ML problem from raw data to an evaluated model while avoiding common problems such as leakage and incorrect validation.

---

# Phase 07 — Deep Learning with PyTorch ⬜

## Goal

Understand how neural networks are constructed, trained, evaluated, and debugged.

## Topics

- Tensors
- Datasets
- DataLoaders
- Neural-network layers
- Activation functions
- Loss functions
- Forward propagation
- Backpropagation
- Automatic differentiation
- Gradient descent
- Optimizers
- Training loops
- Validation
- Regularization
- Saving and loading models
- CNNs
- Embeddings
- Attention foundations

## Tool

- PyTorch

## Completion Goal

Be able to build and train neural networks without depending entirely on high-level training abstractions.

---

# Phase 08 — NLP, Computer Vision, and Transformers ⬜

## Goal

Move from general deep learning toward modern representation-learning and transformer-based systems.

## Topics

### NLP

- Text preprocessing
- Tokenization
- Embeddings
- Sequence representations

### Computer Vision

- Image tensors
- CNNs
- Transfer learning
- Image classification

### Transformers

- Attention
- Self-attention
- Transformer architecture
- Positional information
- Encoders
- Decoders
- Pretrained models
- Fine-tuning
- Transfer learning
- PEFT/LoRA concepts

## Tooling

- PyTorch
- Hugging Face Transformers
- Hugging Face Datasets
- Tokenizers

## Completion Goal

Understand transformer-based models well enough to use, fine-tune, evaluate, and reason about pretrained models.

---

# Phase 09 — LLMs, Generative AI, RAG, and Evaluation ⬜

## Goal

Learn how modern LLM-powered applications are designed and evaluated.

## Topics

- LLM APIs
- Prompt design
- Structured outputs
- Tool/function calling
- Embeddings
- Semantic search
- Vector databases
- Chunking
- Retrieval
- Reranking
- Retrieval-Augmented Generation
- LLM evaluation
- Hallucinations
- Reliability
- Safety
- Cost
- Latency

## Agentic AI

After understanding basic LLM systems:

- Tools
- State
- Workflows
- Agents
- Agentic RAG
- Memory
- Human-in-the-loop systems
- Agent evaluation
- Tracing and observability

## Completion Goal

Build AI applications that are not merely demos but can be systematically tested for retrieval quality, correctness, latency, cost, and failure cases.

---

# Phase 10 — MLOps, Deployment, and Cloud ⬜

## Goal

Learn how ML and AI systems move from experiments into maintainable applications.

## Topics

- APIs
- FastAPI
- Docker
- Automated testing
- CI/CD
- Experiment tracking
- Model versioning
- Data versioning
- Model serving
- Logging
- Monitoring
- Model drift
- Data drift
- Deployment
- Cloud fundamentals
- Scalable inference

## Completion Goal

Be able to package, deploy, monitor, and maintain an ML or AI application.

---

# Phase 11 — Research, Specialization, and Capstone ⬜

## Goal

Transition from broad AI/ML competency toward deeper specialization and research ability.

## Possible Specializations

- NLP
- Large Language Models
- Generative AI
- Foundation Models
- Multimodal learning
- Agentic AI
- LLM agents
- Reasoning
- Post-training
- Test-time learning
- Scaling
- ML systems

## Research Skills

- Reading research papers
- Reproducing results
- Designing experiments
- Ablation studies
- Benchmarking
- Scientific writing
- Research code
- Evaluation methodology

## Capstone

Complete one substantial project or research-oriented implementation combining multiple parts of the roadmap.

---

# Project Repository Strategy

This repository remains the complete learning archive.

For major phases, one strong project may be selected and moved or copied into a dedicated standalone GitHub repository.

Standalone project repositories should emphasize:

- the problem being solved
- architecture
- setup
- reproducibility
- testing
- evaluation
- results
- limitations
- demos/screenshots
- future improvements

The roadmap repository preserves the full learning process; standalone repositories showcase selected high-quality work.

---

# Phase Completion Rule

A phase is not considered complete simply because the associated videos or courses have been watched.

A completed phase should normally include some combination of:

1. Conceptual understanding
2. Exercises or problem solving
3. Practical implementation
4. Independent experimentation
5. At least one applied project when appropriate
6. Testing or evaluation
7. Revision of important concepts

The required depth depends on the phase and subject.
