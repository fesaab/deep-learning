input_height = 4
input_width = 4
filter_height = 2
filter_width = 2
S = 2
new_height = (input_height - filter_height)/S + 1
new_width = (input_width - filter_width)/S + 1
print("new_height: ", new_height)
print("new_width: ", new_width)



## Max pooling
print(np.array([0, 1, 2, 2.5]).max(), 
      ",", 
      np.array([0.5, 10, 1, -8]).max(),
      ",", 
      np.array([4, 0, 15, 1]).max(),
      ",", 
      np.array([5, 6, 2, 3]).max())

## Mean pooling
print(np.array([0, 1, 2, 2.5]).mean(), 
      ",", 
      np.array([0.5, 10, 1, -8]).mean(),
      ",", 
      np.array([4, 0, 15, 1]).mean(),
      ",", 
      np.array([5, 6, 2, 3]).mean())


## Running max pooling on tensorflow
import tensorflow as tf
import numpy as np

input_data = np.array(
    [
        [
            [0, 1, 0.5, 10],
            [2, 2.5, 1, -8],
            [4, 0, 5, 6],
            [15, 1, 2, 3]
        ]
    ]
)
print(input_data.shape)
print(input_data)


input = tf.placeholder(tf.float32, (None, 4, 4))
filter_shape = [1, 2, 2, 1]
strides = [1, 2, 2, 1]
padding = 'VALID'
pool = tf.nn.max_pool(input, filter_shape, strides, padding)

with tf.Session() as session:
    session.run(tf.global_variables_initializer())
    print(session.run(pool, feed_dict={input: input_data}))



