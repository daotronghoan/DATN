# import cv2
# import numpy as np
# from tensorflow.keras.models import load_model
#
# # Danh sách các lớp
# categories = ["glioma", "meningioma", "notumor", "pituitary"]
#
# # Load mô hình
# model = load_model("brain_tumor_model.h5")
#
# def predict_single_image(img_path, model, threshold=0.9):
#     img = cv2.imread(img_path)
#     img = cv2.resize(img, (224, 224))
#     img = img / 255.0
#     img = np.expand_dims(img, axis=0)
#
#     pred = model.predict(img)
#     confidence = np.max(pred)
#     class_idx = np.argmax(pred)
#
#     if confidence < threshold:
#         return "Unknown"
#     else:
#         return categories[class_idx]
#
# # Đường dẫn ảnh cần dự đoán
# img_path = "C:/Users/ADMIN/Downloads/c060ca94-795f-40eb-97fa-bd1feb491017.png"
#
# # Dự đoán
# result = predict_single_image(img_path, model, threshold=0.8)
# print(f"Kết quả dự đoán: {result}")
# import matplotlib.pyplot as plt
# from tensorflow.keras.preprocessing.image import load_img
#
# # Hiển thị ảnh và nhãn dự đoán
# img = load_img(img_path, target_size=(224, 224))
# plt.imshow(img)
# plt.title(f"Dự đoán: {result}")
# plt.axis('off')
# plt.show()
#
#
# #
# # import os
# # import cv2
# # import numpy as np
# # import matplotlib.pyplot as plt
# # from tensorflow.keras.models import load_model
# # from tensorflow.keras.preprocessing.image import load_img
# #
# # # Danh sách các lớp
# # categories = ["glioma", "meningioma", "notumor", "pituitary"]
# #
# # # Load mô hình đã lưu
# # model = load_model("brain_tumor_model.h5")
# #
# #
# # def predict_image(img_path, model, threshold=0.5):
# #     img = cv2.imread(img_path)
# #     img = cv2.resize(img, (224, 224))
# #     img = img / 255.0
# #     img = np.expand_dims(img, axis=0)
# #
# #     pred = model.predict(img)
# #     confidence = np.max(pred)
# #     class_idx = np.argmax(pred)
# #
# #     if confidence < threshold:
# #         return "Unknown"
# #     else:
# #         return categories[class_idx]
# #
# #
# # # Thư mục chứa ảnh cần dự đoán
# # predict_dir = "D:/DATN/Test"
# #
# # # Lấy 10 ảnh đầu tiên trong thư mục Predict
# # image_files = [f for f in os.listdir(predict_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))][:10]
# #
# # # Tạo một lưới 2x5 để hiển thị 10 ảnh
# # fig, axes = plt.subplots(2, 5, figsize=(15, 6))
# #
# # for i, filename in enumerate(image_files):
# #     file_path = os.path.join(predict_dir, filename)
# #     predicted_label = predict_image(file_path, model, threshold=0.5)
# #
# #     img = load_img(file_path, target_size=(224, 224))
# #     ax = axes[i // 5, i % 5]
# #     ax.imshow(img)
# #     ax.set_title(f"Dự đoán: {predicted_label}")
# #     ax.axis('off')
# #
# # plt.tight_layout()
# # plt.show()

import cv2
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img
import matplotlib.pyplot as plt
from scipy.stats import entropy

# Danh sách các lớp
categories = ["glioma", "meningioma", "notumor", "pituitary"]

# Load mô hình đã huấn luyện
model = load_model("brain_tumor_model.h5")


def predict_single_image(img_path, model, confidence_threshold=0.9, entropy_threshold=1.2):
    img = cv2.imread(img_path)

    if img is None:
        print("Không thể đọc ảnh. Kiểm tra lại đường dẫn.")
        return "Invalid image"

    img = cv2.resize(img, (224, 224))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)

    # Dự đoán
    pred = model.predict(img)[0]  # Lấy mảng 1D
    confidence = np.max(pred)
    predicted_class_idx = np.argmax(pred)
    ent = entropy(pred)  # Tính entropy

    # In debug thông tin
    print(f"Dự đoán: {pred}")
    print(f"Xác suất cao nhất (confidence): {confidence:.4f}")
    print(f"Entropy: {ent:.4f}")

    if confidence < confidence_threshold or ent > entropy_threshold:
        return "Unknown"
    else:
        return categories[predicted_class_idx]


# Đường dẫn ảnh cần dự đoán
img_path = "C:/Users/ADMIN/Downloads/Screenshot_20250523-113201~2.png"

# Dự đoán
result = predict_single_image(img_path, model, confidence_threshold=0.9, entropy_threshold=1.2)
print(f"\n👉 Kết quả dự đoán: {result}")

# Hiển thị ảnh và nhãn dự đoán
img = load_img(img_path, target_size=(224, 224))
plt.imshow(img)
plt.title(f"Dự đoán: {result}")
plt.axis('off')
plt.show()
