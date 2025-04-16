import os
import sys
from dataclasses import dataclass
from src.exception import CustomException
from src.logger import logging
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src.utils import save_object


@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join("artifacts", "preprocessor.pkl")


class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_object(self):
        """
        Creates and returns a preprocessor object for data transformation.

        This method constructs a data transformation pipeline for both numerical
        and categorical features. The numerical pipeline applies median imputation
        and standard scaling, while the categorical pipeline applies most frequent
        imputation, one-hot encoding, and scaling without centering.

        Returns:
          ColumnTransformer: A preprocessor object that applies the defined
          transformations to numerical and categorical columns.

        Raises:
          CustomException: If an error occurs during the creation of the
          preprocessor object.
        """
        try:
            numerical_columns = ["writing_score", "reading_score"]
            categorical_columns = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course",
            ]

            num_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="median")),
                    ("scaler", StandardScaler()),
                ]
            )

            categorical_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="most_frequent")),
                    ("onehotencoder", OneHotEncoder()),
                    ("scaler", StandardScaler(with_mean=False)),
                ]
            )

            logging.info("Numerical columns standardization completed")
            logging.info("Categorical columns encoding completed")

            preprocessor = ColumnTransformer(
                transformers=[
                    ("num_pipeline", num_pipeline, numerical_columns),
                    ("categorical_pipeline", categorical_pipeline, categorical_columns),
                ]
            )
            return preprocessor
        except Exception as e:
            raise CustomException(e, sys)

    def initiate_data_transformation(self, train_path, test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            logging.info("Read train and test data completed")
            logging.info("Obtaining preprocessing object")
            preprocessing_obj = self.get_data_transformer_object()
            target_column_name = "math_score"
            input_features_train_df = train_df.drop(
                columns=[target_column_name], axis=1
            )
            target_feature_train_df = train_df[target_column_name]

            input_features_test_df = test_df.drop(columns=[target_column_name], axis=1)
            target_feature_test_df = test_df[target_column_name]
            logging.info("Applying preprocessing object on training and testing data")
            input_feature_train_arr = preprocessing_obj.fit_transform(
                input_features_train_df
            )
            input_feature_test_arr = preprocessing_obj.transform(input_features_test_df)

            train_arr = np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)
            ]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]
            logging.info("Saved preprocessing object")

            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj,
            )

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            )
        except Exception as e:
            raise CustomException(e, sys)


if "__name__" == "__main__":
    obj = DataTransformation()
    train_arr, test_arr, preprocessor_obj_file_path = obj.initiate_data_transformation(
        "artifacts/train.csv", "artifacts/test.csv"
    )
    print("Train Array:", train_arr)
    print("Test Array:", test_arr)
    print("Preprocessor Object File Path:", preprocessor_obj_file_path)