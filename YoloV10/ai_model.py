import argparse
from ultralytics import YOLO
from PIL import Image, ImageDraw
import os
import logging
import json
import requests
from io import BytesIO
from datetime import datetime

# 配置日志记录
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def download_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return Image.open(BytesIO(response.content))
    except Exception as e:
        logging.error(f"Failed to download image: {e}")
        return None

def process_image(image_path, is_url=False):
    logging.info(f"Processing image: {image_path}")

    # 定义保存结果图像的目录
    now = datetime.now()
    save_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'results', now.strftime('%Y%m'), now.strftime('%d'))
    os.makedirs(save_dir, exist_ok=True)

    try:
        if is_url:
            img = download_image(image_path)
            if img is None:
                raise ValueError("Image download failed")
            base_name = os.path.basename(image_path).split("?")[0]
        else:
            img = Image.open(image_path)
            base_name = os.path.basename(image_path)

        original_image_path = os.path.join(save_dir, base_name)
        img.save(original_image_path)
    except Exception as e:
        logging.error(f"Failed to load or save image: {e}")
        print(json.dumps({"success": False}))
        return

    try:
        # 加载预训练的 YOLOv10 模型
        model = YOLO("yolov10x.pt")

        # 执行对象检测
        results = model(original_image_path)

        # 获取检测结果
        boxes = results[0].boxes

        # 获取类别名称映射
        names = results[0].names

        # 检查是否有 'person' 类别的检测结果
        person_detected = any(names[int(box.cls.item())] == 'person' for box in boxes)

        # 根据检测结果将文件路径写入对应的日志文件
        if person_detected:
            result = {"success": True}
            logging.info(f"Person detected in: {image_path}")
        else:
            result = {"success": False}
            logging.info(f"No person detected in: {image_path}")

        # 将结果输出为 JSON
        print(json.dumps(result))
    except Exception as e:
        logging.error(f"Failed during YOLO processing: {e}")
        print(json.dumps({"success": False}))
    finally:
        # 删除处理完毕的图片文件
        try:
            os.remove(original_image_path)
            logging.info(f"Deleted image file: {original_image_path}")
        except Exception as e:
            logging.error(f"Failed to delete image file: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="YOLOv10 Object Detection")
    parser.add_argument("image_path", type=str, help="本地图像文件路径或网络图像URL")
    parser.add_argument("--url", action="store_true", help="如果处理网络图像，请添加此选项")
    args = parser.parse_args()
    process_image(args.image_path, args.url)
