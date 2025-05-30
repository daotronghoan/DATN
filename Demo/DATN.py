import os
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.applications import DenseNet121
from tensorflow.keras.layers import Dense, Dropout, GlobalAveragePooling2D
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint

from google.colab import drive
drive.mount('/content/drive')

# =====================
# 1. Cấu hình đường dẫn
# =====================
data_dir = "/content/drive/My Drive/DATN"
train_dir = os.path.join(data_dir, "Training")
test_dir = os.path.join(data_dir, "Testing")
model_path = "brain_tumor_densenet.keras"  # lưu tạm trong /content

# =========================
# 2. Cấu hình Image Generator
# =========================
img_size = 224
batch_size = 64

train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=10,
    zoom_range=0.1,
    width_shift_range=0.1,
    height_shift_range=0.1,
    horizontal_flip=True
)

test_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(img_size, img_size),
    batch_size=batch_size,
    class_mode='categorical'
)

test_generator = test_datagen.flow_from_directory(
    test_dir,
    target_size=(img_size, img_size),
    batch_size=batch_size,
    class_mode='categorical',
    shuffle=False
)

# =====================
# 3. Tạo mô hình DenseNet121
# =====================
base_model = DenseNet121(weights="imagenet", include_top=False, input_shape=(img_size, img_size, 3))
base_model.trainable = False  # Freeze tầng gốc

x = GlobalAveragePooling2D()(base_model.output)
x = Dense(512, activation="relu")(x)
x = Dropout(0.3)(x)
output = Dense(4, activation="softmax")(x)

model = Model(inputs=base_model.input, outputs=output)

# =====================
# 4. Compile
# =====================
model.compile(optimizer=Adam(learning_rate=1e-4), loss='categorical_crossentropy', metrics=['accuracy'])

# =====================
# 5. Callbacks
# =====================
earlystop = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)
checkpoint = ModelCheckpoint(model_path, monitor='val_accuracy', save_best_only=True)

# =====================
# 6. Huấn luyện
# =====================
history = model.fit(
    train_generator,
    validation_data=test_generator,
    epochs=100,
    callbacks=[earlystop, checkpoint]
)

# =====================
# 7. Đánh giá & Lưu mô hình
# =====================
loss, acc = model.evaluate(test_generator)
print(f"Độ chính xác trên tập test: {acc * 100:.2f}%")

# Chép mô hình vào Drive
!cp /content/brain_tumor_densenet.keras "brain_tumor_densenet_final.keras"

# =====================
# 8. Vẽ đồ thị
# =====================
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(history.history["accuracy"], label="Train Accuracy")
plt.plot(history.history["val_accuracy"], label="Validation Accuracy")
plt.title("Accuracy")
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(history.history["loss"], label="Train Loss")
plt.plot(history.history["val_loss"], label="Validation Loss")
plt.title("Loss")
plt.legend()

plt.show()
