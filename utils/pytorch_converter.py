import onnx
from onnx import version_converter
import torch
from onnx2torch import convert
import os


def pytorch_to_onnx(model_path):
    onnx_file_name = os.path.splitext(model_path)[0]+'.onnx'
    model = torch.load(model_path)
    dummy_input1 = torch.randn(1)
    dummy_input2 = torch.randn(1)
    torch.onnx.export(model,(dummy_input1,dummy_input2), onnx_file_name, '')
    print('ONNX model saved to {}'.format(onnx_file_name))
    return 1


def onnx_to_pytorch(onnx_file_name, savemodel=True):

    # Convert to torch.
    torch_model = convert(onnx_file_name)
    if savemodel:
        save_model_name = os.path.splitext(onnx_file_name)[0]+'.pth'
        torch.save(torch_model, save_model_name)
    print('torch model saved to {}'.format(save_model_name))
    return 1
