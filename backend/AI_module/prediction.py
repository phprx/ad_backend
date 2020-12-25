import os
# from PIL import Image
# import numpy as np
# from keras.utils import np_utils
# from keras.models import Sequential
# from keras.layers.core import Dense, Dropout, Activation, Flatten
# from keras.optimizers import SGD, RMSprop, Adam
# from keras.layers import Conv2D, MaxPooling2D
# import keras


# 找到所需要的图像文件并进行格式转换
def prepicture(picname):
    # 此处找到图片，picname即为文件名字，需要将前面的改成我们的文件路径
    img = Image.open('./' + picname)
    new_img = img.resize((100, 100), Image.BILINEAR)
    new_path = os.path.join('./backend/AI_module/test/', os.path.basename(picname))
    new_img.save(new_path)
    return new_path


# 读取转换后的文件
def read_image2(path):
    img = Image.open(path).convert('RGB')
    return np.array(img)


# view里面调用该方法即可获得分数
def predict_picture(picname):
    # 预处理图片 变成100 x 100
    new_path = prepicture(picname)
    x_test = []

    x_test.append(read_image2(new_path))

    x_test = np.array(x_test)

    x_test = x_test.astype('float32')
    x_test /= 255

    keras.backend.clear_session()  # 清理session反复识别注意
    # 构建模型
    model = Sequential()
    model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(100, 100, 3)))
    model.add(Conv2D(32, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))

    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))

    model.add(Flatten())
    model.add(Dense(256, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(2, activation='softmax'))

    sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
    model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])
    # 加载权重
    model.load_weights('./backend/AI_module/model/weights.h5')
    # 进行预测
    classes = model.predict_classes(x_test)[0]
    if classes == 0:
        return 0
    else:
        return 1
    # target = ['非立方体', '立方体']
    # print(target[classes])


# if __name__ == '__main__':
#     print(predict_picture('test5.png'))
