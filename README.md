Chaale, let's try and understand how vector database works.

Basically, from what I understand.

1. first, vectorize all words into all sentences as token arrays and aggregate them (`vocab_vector`).
2. the query string should be vectorized as well (`query_vector`).
3. Perform cosine similarity search of the `query_vector` on the `vocab_vector`

### Cosine similarity

$$\text{For each } \mathbf{v}_i \in V:$$
$$\text{similarity}_i = \frac{\mathbf{q} \cdot \mathbf{v}_i}{|\mathbf{q}| |\mathbf{v}_i|}$$
$$R = {(i, \text{similarity}_i) : \mathbf{v}_i \in V}$$

Where:

- $V$ is the `vocab_vector`
- $\mathbf{v}_i$ is the $i$-th vector in $V$
- $\mathbf{q}$ is the `query_vector`
- $|\mathbf{q}|$ and $|\mathbf{v}_i|$ represent the L2 norms of the respective vectors
- $R$ is the set of results, containing pairs of vector identifiers and their corresponding similarities

I don't know if this is right. However when we are done. We will compare it with well known vector databases.

---

Yo I don't know if it works. Works for small dataset but goes off for larger datasets. Most likely due to the way I update vectors. It overwrites already previously tokens. Also I have no idea how to delete a vector. Is that even possible
