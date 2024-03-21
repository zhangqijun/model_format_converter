import argparse

from utils.tf_converter import tf_to_onnx, onnx_to_tf
from utils.paddle_converter import paddle_to_onnx, onnx_to_paddle
from utils.pytorch_converter import pytorch_to_onnx, onnx_to_pytorch


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', '-m', type=str, help='输入的模型文件路径', required=True)
    parser.add_argument('--model_convert_type', '-t', type=str,
                        choices=['tf2onnx', 'onnx2tf', 'pytorch2onnx', 'onnx2pytorch', 'paddle2onnx', 'onnx2paddle'],
                        help='转换的类型，可选为tf2onnx onnx2tf pytorch2onnx onnx2pytorch paddle2onnx onnx2paddle',
                        required=True)
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    if args.model_convert_type == 'tf2onnx':
        tf_to_onnx(args.model)
    elif args.model_convert_type == 'onnx2tf':
        onnx_to_tf(args)
    elif args.model_convert_type == 'pytorch2onnx':
        onnx_to_pytorch(args.model)
    elif args.model_convert_type == 'onnx2pytorch':
        onnx_to_pytorch(args.model)
    elif args.model_convert_type == 'paddle2onnx':
        paddle_to_onnx(args.model)
    elif args.model_convert_type == 'onnx2paddle':
        onnx_to_paddle(args.model)


if __name__ == '__main__':
    main()
