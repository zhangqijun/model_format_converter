import onnx
import tensorflow as tf
import onnxruntime
import numpy as np
import onnx2tf
import tensorflow as tf
import os
# from tensorflow.lite.python import interpreter as tflite_interpreter

def tf_to_onnx(tf_model_path, onnx_file_name):
    os.system(f'python3 -m tf2onnx.convert --saved-model {tf_model_path} --output {onnx_file_name}')
    return 1


def onnx_to_tf(onnx_file_name):

    onnx2tf.convert(
        input_onnx_file_path="model.onnx",
        output_folder_path="model.tf",
        copy_onnx_input_output_names_to_tflite=True,
        non_verbose=True,
    )


    return 1