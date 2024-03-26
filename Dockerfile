FROM robd003/python3.10
LABEL authors="zqj"
ADD requirements.txt .
RUN pip3 install -r requirements.txt
RUN pip3 install https://paddle-wheel.bj.bcebos.com/2.6.0/linux/linux-cpu-mkl-avx/paddlepaddle-2.6.0-cp310-cp310-linux_aarch64.whl