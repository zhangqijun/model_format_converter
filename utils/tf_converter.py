import onnx
import tensorflow as tf
import onnxruntime
import numpy as np
import onnx2tf
import tensorflow as tf
import os
# from tf2onnx import convert

def tf_to_onnx(tf_model_path, onnx_file_name):
    # convert()
    os.system(f'python3 -m tf2onnx.convert --saved-model {tf_model_path} --output {onnx_file_name}')
    return 1


def onnx_to_tf(onnx_file_name):
    save_model_name = os.path.splitext(onnx_file_name)[0] + '.tf'
    onnx2tf.convert(
        input_onnx_file_path=onnx_file_name,
        output_folder_path=save_model_name,
        copy_onnx_input_output_names_to_tflite=True,
        non_verbose=True,
    )


    return 1