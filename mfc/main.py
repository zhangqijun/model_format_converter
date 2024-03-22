import argparse


from utils.paddle_converter import paddle_to_onnx, onnx_to_paddle
from utils.pytorch_converter import pytorch_to_onnx, onnx_to_pytorch


def parse_args():
    parser = argparse.ArgumentParser(
        description='Self-Created Tools to convert deeplearning files from tf,pytorch,onnx,paddle to eachothers. The purpose of this tool is to solve the massive Transpose extrapolation problem in deeplearning models.')
    parser.add_argument('-m', '--model', type=str, help='输入的模型文件路径', required=True)
    parser.add_argument('-t', '--model_convert_type', type=str,
                        choices=['tf2onnx', 'onnx2tf', 'pytorch2onnx', 'onnx2pytorch', 'paddle2onnx', 'onnx2paddle'],
                        help='转换的类型，可选为tf2onnx onnx2tf pytorch2onnx onnx2pytorch paddle2onnx onnx2paddle',
                        required=True)
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    if args.model_convert_type == 'tf2onnx':
        from utils.tf_converter import tf_to_onnx
        tf_to_onnx(args.model)
    elif args.model_convert_type == 'onnx2tf':
        from utils.tf_converter import onnx_to_tf
        onnx_to_tf(args.model)
    elif args.model_convert_type == 'pytorch2onnx':
        pytorch_to_onnx(args.model)
    elif args.model_convert_type == 'onnx2pytorch':
        onnx_to_pytorch(args.model)
    elif args.model_convert_type == 'paddle2onnx':
        paddle_to_onnx(args.model)
    elif args.model_convert_type == 'onnx2paddle':
        onnx_to_paddle(args.model)


if __name__ == '__main__':
    main()
