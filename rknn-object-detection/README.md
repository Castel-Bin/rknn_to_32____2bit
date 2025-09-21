# rknn-object-detection

## 项目简介
该项目实现了基于RKNN模型的目标检测，能够识别可乐、雪碧和瓶装水。通过摄像头捕获实时视频流，并在检测到目标后，通过UART串口将目标信息发送给STM32。

## 文件结构
```
rknn-object-detection
├── src
│   ├── main.py          # 程序入口点
│   ├── camera.py        # 摄像头交互模块
│   ├── detector.py      # 目标检测模块
│   ├── uart_sender.py    # UART发送模块
│   └── types
│       └── index.py     # 类型和常量定义
├── requirements.txt      # 项目依赖
└── README.md             # 项目文档
```

## 功能说明
- **目标检测**：使用RKNN模型识别可乐（标签0）、雪碧（标签1）和瓶装水（标签2）。
- **实时视频捕获**：通过摄像头捕获视频帧，实时检测目标。
- **串口通信**：将检测到的目标通过UART1串口发送给STM32。

## 安装步骤
1. 克隆项目到本地：
   ```
   git clone <repository-url>
   cd rknn-object-detection
   ```
2. 安装依赖：
   ```
   pip install -r requirements.txt
   ```

## 使用说明
1. 启动程序：
   ```
   python src/main.py
   ```
2. 程序将自动启动摄像头并进行目标检测，检测到目标后将其标签发送至STM32。

## 注意事项
- 确保摄像头正常连接并可被识别。
- 根据需要调整串口设置以确保与STM32的通信正常。