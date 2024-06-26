import onnx
import tensorflow as tf
import numpy as np
import onnx2tf
import tensorflow as tf
import os


# from tf2onnx import convert

def tf_to_onnx(tf_model_path):
    # convert()

    onnx_file_name = tf_model_path + '.onnx'
    tflitemodelpath = os.path.join(tf_model_path, 'model_float32.tflite')
    os.system(f'python3 -m tf2onnx.convert --tflite {tflitemodelpath} --output {onnx_file_name}')
    print('ONNX model saved to {}'.format(onnx_file_name))
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


if __name__ == '__main__':
    onnx_to_tf('/home/zqj/model.onnx')
