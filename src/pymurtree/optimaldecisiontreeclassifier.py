from pymurtree.parameters import Parameters
import pandas
from . import lib

class OptimalDecisionTreeClassifier:
    def __init__(self,
                 time: int = 600,
                 max_depth: int = 3,
                 max_num_nodes: int = 7,
                 sparse_coefficient: float = 0.0,
                 verbose: bool = True,
                 all_trees: bool = True,
                 incremental_frequency: bool = True,
                 similarity_lower_bound: bool = True,
                 node_selection: int = 0,
                 feature_ordering: int = 0,
                 random_seed: int = 3,
                 cache_type: int = 0,
                 duplicate_factor: int = 1
                ) -> None:
        
        self.__params = Parameters(time, max_depth, max_num_nodes,
                                   sparse_coefficient, verbose,
                                   all_trees, incremental_frequency, 
                                   similarity_lower_bound, node_selection,
                                   feature_ordering, random_seed,
                                   cache_type, duplicate_factor)
    
        self.__tree = None
        #print(f"Using parameters: {self.__params}")


    def fit(self,
            x, y,
            time: int = None,
            max_depth: int = None,
            max_num_nodes: int = None,
            sparse_coefficient: float = None,
            verbose: bool = None,
            all_trees: bool = None,
            incremental_frequency: bool = None,
            similarity_lower_bound: bool = None,
            node_selection: int = None,
            feature_ordering: int = None,
            random_seed: int = None,
            cache_type: int = None,
            duplicate_factor: int = None) -> None:
        
        if time is not None:
            self.__params.time = time
        if max_depth is not None:
            self.__params.max_depth = max_depth
        if max_num_nodes is not None:
            self.__params.max_num_nodes = max_num_nodes
        if sparse_coefficient is not None:
            self.__params.sparse_coefficient = sparse_coefficient
        if verbose is not None:
            self.__params.verbose = verbose
        if all_trees is not None:
            self.__params.all_trees = all_trees
        if incremental_frequency is not None:
            self.__params.incremental_frequency = incremental_frequency
        if similarity_lower_bound is not None:
            self.__params.similarity_lower_bound = similarity_lower_bound
        if node_selection is not None:
            self.__params.node_selection = node_selection
        if feature_ordering is not None:
            self.__params.feature_ordering = feature_ordering
        if random_seed is not None:
            self.__params.random_seed = random_seed
        if cache_type is not None:
            self.__params.cache_type = cache_type
        if duplicate_factor is not None:
            self.__params.duplicate_factor = duplicate_factor

        print("py_add: ", lib.py_add(9, 10))

        # initialize tree
        # self.__tree = ...

        #print(x.shape)
        #print(y.shape)
        #print(f"Using parameters: {self.__params}")


    def predict():
        pass


    def score():
        pass