import onnx
from x2paddle.convert import onnx2paddle
import os


def paddle_to_onnx(model, onnx_file_name):
    paddle.load(model)
    paddle.onnx.export(model, onnx_file_name, '')
    print('ONNX model saved to {}'.format(onnx_file_name))
    return 1


def onnx_to_paddle(onnx_file_name):
    # Convert the model to the target .
    save_model_dir = os.path.join(os.path.dirname(onnx_file_name), '.paddle')
    onnx2paddle(onnx_file_name, save_model_dir)
    return 1