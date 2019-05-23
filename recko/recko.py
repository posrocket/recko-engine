import numpy as np
from scipy.spatial.distance import cosine


class ReckoEngine:
    def calculate_cos(self, main_item, second_item):
        similarity = 1 - cosine(main_item, second_item)
        return similarity

    def create_feature_matrix(self, transactions_list):
        matrix = {}
        length = len(transactions_list)
        index = 0

        for transaction in transactions_list:
            for item_record in transaction:
                variation_id = item_record[0]
                quantity = item_record[1]

                matrix_keys = matrix.keys()

                if variation_id not in matrix_keys:
                    vector = np.zeros(length, int)

                    vector[index] = quantity
                    matrix.update({variation_id: vector})
                else:
                    item_vector = matrix[variation_id]
                    item_vector[index] = quantity
                    matrix.update({variation_id: item_vector})
            index += 1
        return matrix

    def similar_items(self, matrix):
        similarity_values = {}

        for key_one in matrix:
            item_similarity = []
            frequency = np.count_nonzero(matrix[key_one])

            if frequency > 1:
                for key_two in matrix:
                    if key_one != key_two:

                        key_one_vector = matrix[key_one]
                        key_two_vector = matrix[key_two]

                        cos_similarity = calculate_cos(key_one_vector, key_two_vector)

                        if cos_similarity != 0:
                            item_similarity.append([key_two, cos_similarity])
                similarity_values.update({key_one: item_similarity})

        return similarity_values

    def __init__(self, transactions_list):
        feature_matrix = self.create_feature_matrix(transactions_list)
        similarity_list = self.similar_items(feature_matrix)

        return similarity_list
