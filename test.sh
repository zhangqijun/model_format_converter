cd sample_model  &&
mfc -m model.onnx -t onnx2tf &&
mfc -m model.tf -t tf2onnx &&
mfc -m model.onnx -t onnx2paddle &&
mfc -m model_paddle -t paddle2onnx &&
mfc -m model.onnx -t onnx2pytorch &&
mfc -m model.pth -t pytorch2onnx
