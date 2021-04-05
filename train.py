import tensorflow as tf

def createModel():
    return tf.keras.models.Sequential([
        tf.keras.layers.Dense(1000, input_dim=767, activation='relu'),
        tf.keras.layers.Dense(1000, activation='relu'),
        tf.keras.layers.Dense(1000, activation='relu'),
        tf.keras.layers.Dense(1)
    ])