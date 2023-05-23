from keras.models import Sequential, model_from_json
from keras.layers import Conv2D, MaxPooling2D, Flatten
from keras.layers import Dense, Dropout
from keras.preprocessing.image import ImageDataGenerator

class neiron():

    def __init__(self):
        path = "D:\\Новая папка\\DataSets\\ALL\\IN"
        self.train_folder = path + '/train/'
        self.test_folder = path + '/test/'
        self.val_folder = path + '/val/'
        self.final_model = self.load()

    def learn(self):
        self.train_datagen = ImageDataGenerator(rescale=1. / 255,
                                                shear_range=0.2,
                                                zoom_range=0.2,
                                                horizontal_flip=True,
                                                rotation_range=40,
                                                width_shift_range=0.2,
                                                height_shift_range=0.2)

        self.test_datagen = ImageDataGenerator(rescale=1. / 255)

        self.training_set = self.train_datagen.flow_from_directory(self.train_folder,
                                                                   target_size=(150, 150),
                                                                   batch_size=32,
                                                                   class_mode='categorical')

        self.val_set = self.test_datagen.flow_from_directory(self.val_folder,
                                                             target_size=(150, 150),
                                                             batch_size=32,
                                                             class_mode='categorical')

        self.test_set = self.test_datagen.flow_from_directory(self.test_folder,
                                                              target_size=(150, 150),
                                                              batch_size=32,
                                                              class_mode='categorical')

        self.model = Sequential()

        self.model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(150, 150, 3), padding='same'))
        self.model.add(MaxPooling2D(pool_size=(2, 2)))

        self.model.add(Conv2D(32, (3, 3), activation='relu', padding='same'))
        self.model.add(MaxPooling2D(pool_size=(2, 2)))
        self.model.add(Dropout(0.25))

        self.model.add(Conv2D(64, (3, 3), activation='relu', padding='same'))
        self.model.add(MaxPooling2D(pool_size=(2, 2)))

        self.model.add(Conv2D(64, (3, 3), activation='relu', padding='same'))
        self.model.add(MaxPooling2D(pool_size=(2, 2)))
        self.model.add(Dropout(0.25))

        self.model.add(Conv2D(128, (3, 3), activation='relu', padding='same'))
        self.model.add(MaxPooling2D(pool_size=(2, 2)))

        self.model.add(Conv2D(128, (3, 3), activation='relu', padding='same'))
        self.model.add(MaxPooling2D(pool_size=(2, 2)))
        self.model.add(Dropout(0.25))

        self.model.add(Flatten())
        self.model.add(Dense(256, activation='relu'))
        self.model.add(Dropout(0.5))
        self.model.add(Dense(4, activation='sigmoid'))

        self.model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

        model_train = self.model.fit_generator(self.training_set,
                                               steps_per_epoch=421,
                                               epochs=15,
                                               validation_data=self.val_set,
                                               validation_steps=6)

        test_accuracy = self.model.evaluate_generator(self.test_set, steps=31)
        print('Testing Accuracy: {:.2f}%'.format(test_accuracy[1] * 100))

    def save(self):
        self.model
        print("Сохраняем сеть")
        model_json = self.model.to_json()
        json_file = open("../composites/load.json", "w")
        json_file.write(model_json)
        json_file.close()
        self.model.save_weights("load.h5")
        print("Сохранение сети завершено")

    def load(self):
        json_file = open("load.json", "r")
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = model_from_json(loaded_model_json)
        loaded_model.load_weights("load.h5")
        loaded_model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        return loaded_model