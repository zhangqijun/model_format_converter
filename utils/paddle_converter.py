# import onnx
from x2paddle.convert import onnx2paddle
import os
# from paddle2onnx import program2onnx



def paddle_to_onnx(model_path):
    onnx_file_name = os.path.splitext(model_path)[0] + '.onnx'
    # program2onnx(f'',f'',f'')

    os.system(
        f'paddle2onnx --model_dir {model_path}/inference_model/ --model_filename model.pdmodel --save_file {onnx_file_name}')
    print('ONNX model saved to {}'.format(onnx_file_name))
    return 1


def onnx_to_paddle(onnx_file_name):
    # Convert the model to the target .
    save_model_dir = os.path.splitext(onnx_file_name)[0] + '_paddle'
    onnx2paddle(onnx_file_name, save_model_dir)
    print('paddle model saved to {}'.format(save_model_dir))
    return 1

if __name__ == '__main__':
    onnx_to_paddle('../sample_model/model.onnx')
    paddle_to_onnx('../sample_model/model_paddle')