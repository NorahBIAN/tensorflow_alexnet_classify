import tensorflow as tf
from alexnet import alexnet
import matplotlib.pyplot as plt

class_name = ['cat', 'dog']

def test_image(path_image, num_class):
    img_string = tf.read_file(path_image)
    img_decoded = tf.image.decode_png(img_string, channels=3)
    img_resized = tf.image.resize_images(img_decoded, [227, 227])
    img_resized = tf.reshape(img_resized, shape=[1, 227, 227, 3])
    fc8 = alexnet(img_resized, 1, 2)
    score = tf.nn.softmax(fc8)
    max = tf.argmax(score, 1)
    saver = tf.train.Saver()
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        saver.restore(sess, "./tmp/checkpoints/model_epoch18.ckpt")
        print(sess.run(fc8))
        prob = sess.run(max)[0]
        plt.imshow(img_decoded.eval())
        plt.title("Class:" + class_name[prob])
        plt.show()


test_image('G:/Lab/Data_sets/catanddog/validate/dog.504.jpg', num_class=2)