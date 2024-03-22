import onnx
from x2paddle.convert import onnx2paddle
import os
import paddle


def paddle_to_onnx(model_path):
    onnx_file_name = os.path.splitext(model_path)[0] + '.onnx'
    model = paddle.load(model_path)
    # dummy_input1 = paddle.randn(1)
    # dummy_input2 = paddle.randn(1)
    paddle.onnx.export(model, onnx_file_name, '')
    print('ONNX model saved to {}'.format(onnx_file_name))
    return 1


def onnx_to_paddle(onnx_file_name):
    # Convert the model to the target .
    save_model_dir = os.path.splitext(onnx_file_name)[0] + '.paddle'
    onnx2paddle(onnx_file_name, save_model_dir)
    print('paddle model saved to {}'.format(save_model_dir))
    return 1
