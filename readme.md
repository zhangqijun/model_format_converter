# background
Due to the different format saving modes between current mainstream deep learning frameworks, but the frameworks themselves do not provide the ability to convert mutually. Therefore, we have developed this format conversion software, which can bring the following advantages:
* Cross-platform compatibility: Different deep learning frameworks (such as TensorFlow, PyTorch, onnx) have their own model storage formats. A format conversion tool allows models to be smoothly migrated between different frameworks and platforms, ensuring the continuity of research and development.
* Resource sharing and collaboration: Researchers and developers often need to share models between different teams and projects. A unified format conversion tool can make models built with different frameworks easier for others to understand and use, promoting resource sharing and collaboration.
* Avoiding duplicated work: For the same model, if you want to replicate or debug it in different frameworks, you may need to manually reconstruct it. The format conversion tool can reduce this duplicated work and improve development efficiency.
# introduction

The model format conversion software is a tool that facilitates the conversion of AI model files between different frameworks, supporting the reading of model structures and weight values, and the conversion from one framework format to another.
# model type support
1.tensorflow - onnx

2.onnx - tensorflow

3.pytorch - onnx

4.onnx - pytorch

5.paddle - onnx

6.onnx - paddle

# enviroment
```bash
docker build -t model_format_converter .
docker run -it --rm -v XXXX:/model model_format_converter mfc --help 
```
# debug install 
```bash
python3 setup.py develop --user
```
# how to use

```bash
mfc --help
mfc -m sample_model/model.onnx -t onnx2pytorch
mfc -m sample_model/model.onnx -t onnx2tf
mfc -m sample_model/model.onnx -t onnx2paddle

mfc -m sample_model/model.pt -t pytorch2onnx
mfc -m sample_model/model.pdparams -t paddle2onnx
mfc -m sample_model/model.tf -t tf2onnx

```