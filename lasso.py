import tensorflow.keras as tfk
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


class Linear(tfk.Model):
    def __init__(self):
        super().__init__()
        self.linear = tfk.layers.Dense(1)

    def call(self, inputs, training=None, mask=None):
        return self.linear(inputs)


class Loss(tfk.Model):
    def __init__(self):
        super().__init__()
        self.loss = tfk.losses.MeanSquaredError()

    def call(self, inputs, training=None, mask=None):
        pred, label = inputs
        return self.loss(pred, label)


def generate_data(num, a, b):
    x = np.linspace(0, 10, num).reshape((-1, 1))
    y = x * a + b + np.random.randn(*x.shape)
    plt.scatter(x, y)
    plt.show()
    return x, y


x, y = generate_data(100, 1, 3)
model = Linear()
loss = Loss()
optimizer = tfk.optimizers.SGD()

dtst = tf.data.Dataset.from_tensor_slices((x, y))
dtst = dtst.batch(32).prefetch(1)


@tf.function
def train_step(x, y):
    with tf.GradientTape() as tape:
        pred = model(x)
        l = loss((pred, y))
    gradients = tape.gradient(l, model.trainable_variables)
    optimizer.apply_gradients(zip(gradients, model.trainable_variables))


for epoceh in range(200):
    for xb, yb in dtst:
        train_step(xb, yb)

print(model.linear.weights)
