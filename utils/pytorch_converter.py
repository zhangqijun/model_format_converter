import onnx
from onnx import version_converter
import torch
from onnx2torch import convert
import os


def pytorch_to_onnx(model, onnx_file_name):
    torch.onnx.export(model, onnx_file_name, '')
    print('ONNX model saved to {}'.format(onnx_file_name))
    return 1


def onnx_to_pytorch(onnx_file_name, savemodel=True):
    # Load the ONNX model.
    model = onnx.load(onnx_file_name)
    # Convert the model to the target version.
    target_version = 13
    converted_model = version_converter.convert_version(model, target_version)
    # Convert to torch.
    torch_model = convert(converted_model)
    if savemodel:
        save_model_name = os.path.join(os.path.dirname(onnx_file_name), '.pth')
        torch.save(torch_model, save_model_name)

    return 1
