# for REST
import tensorflow as tf

print(tf.config.list_physical_devices())

if __name__ == '__main__':
    from Data.PredictData import prepare_predict