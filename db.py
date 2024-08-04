import numpy as np
#from nanoid import generate
class VectorDB:
    def __init__(self,):
        self.vector_data = {}
        self.vector_idx = {}

    def get_vector(self, key):
        return self.vector_data.get(key)

    def add_vector(self, key, vector):
        self.vector_data[key] = vector
        self.update_vector(key, vector)

    def update_vector(self, key, vector):
        # In this simple example, we use brute-force cosine similarity for indexing
        #NOTE: write a more efficient version of this. Perhaps nearest neighbour search
        for existing_id, existing_vector in self.vector_data.items():
            similarity = np.dot(vector, existing_vector) / (np.linalg.norm(vector) * np.linalg.norm(existing_vector))
            if existing_id not in self.vector_idx:
                self.vector_idx[existing_id] = {}
            self.vector_idx[existing_id][key] = similarity


    def cosine_similarity(self, query, count=1):
        """
            This process is used to determine how similar each vector in the vector_data is to a query_vector. and return the top N results

        """
        results = []
        for key, vector in self.vector_data.items():
            similarity = np.dot(query, vector) / (np.linalg.norm(query) * np.linalg.norm(vector))
            results.append((key, similarity))

        # Sort by similarity in descending order
        results.sort(key=lambda x: x[1], reverse=True)

        # Return the top N results
        return results[:count]

