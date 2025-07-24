# Terms
<ins>Key Terms talked about in a video</ins> [link to youtube video](https://www.youtube.com/watch?v=k7RM-ot2NWY)
* Basis vectors
* Linear Combination of Vectors
* Span of vectors
* Linearly Independent and Dependent vectors

# Terms used in Quiz
* **Pivot columns**: A pivot is defined as
    * A row with a leading one
    * That one is the first non-zero entry in the row (reading from left to right)
    * It is used to eliminate entries above and below it (has zeros above and below it)
* **Subspace**: A subset of a vector space.
     * A proper subset has fewer elements than the vector space.
     * A improper subset has exactly the same elements as the vector space.
* **Span**: The set of all vectors you can create using those vectors through linear combinations
* Additvity & Homogeneity
* Dilation (scaling)
* **L2 Norm (aka the Euclidean norm)**: The length or distance from the orgin
* **Null Space**: When you multiply a matrix by a vector and the output is a zero vector
* Contradiction or no contradictions in a matrix in reduced row echelon form (RREF)
* **Orthogonal vectors**: When the dot product of two vectors is zero
* **Basis of a vector space**: Satisfies 3 conditions
    * spans the space
    * is linearly independent
    * has exactly n elements where n is the dimension of the spaces

# Discussion
> Concepts of vector space and basis are important to understand this week.  The important goal in ML is to discover the best basis set to describe the input dataset and to solve ML problem. Let's discuss: When a vector can be a basis for a vector subspace?

## Vector Subspaces and Basis

Based on the lecture and quiz, there are three requirements that must be satisfied for a vector to be a basis for a vector subspace:

1. **Spans the space**  
2. **Is linearly independent**  
3. **Has exactly _n_ elements**, where _n_ is the dimension of the finite-dimensional space ℝⁿ  
   (for example, in the quiz, set **S** was a subset of **V**, a 5-dimensional vector space or ℝ⁵, which means that **S** must have 5 elements)

---

### Concepts Clarified (from solving question 5 in the quiz)

---

### 🔹 Subspace

The problem stated how "**S is a subset of V**". I was initially confused because I assumed that if **S** is a subset of **V**, it must have fewer than 5 elements.

However, after further research, I realized that there are **two types of subsets**:

- **Proper Subset**: Has fewer elements than the vector space.  
  _Notation_: `A ⊂ B`

- **Improper Subset**: Has exactly the same elements as the vector space.  
  _Notation_: `A = B`

---

### 🔹 What does it mean for the vectors in the set to be linearly independent?

There are no vectors in the set (i.e., the basis set) that can be written as a linear combination of the others.  
So **none of the vectors in the set are linearly dependent** on one another.

---

### 🔹 What does it mean for basis vectors to span a vector space?

It means that the basis vectors can be used to **construct every vector in that space via linear combinations**.

So basically, the vectors in the basis form an **independent set** of vectors that can be used to create a **system of linear equations with a unique solution** for any vector in the space.

---
