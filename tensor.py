import tensorflow as tf

# Generate some sample data
X_train = [1.0, 2.0, 3.0, 4.0, 5.0]
y_train = [2.0, 4.0, 6.0, 8.0, 10.0]

# Define the variables for the slope (weight) and intercept (bias)
W = tf.Variable(0.0)
b = tf.Variable(0.0)

# Define the input placeholder
X = tf.placeholder(dtype=tf.float32)

# Define the target placeholder
y = tf.placeholder(dtype=tf.float32)

# Define the linear regression model
y_pred = W * X + b

# Define the mean squared error loss function
loss = tf.reduce_mean(tf.square(y_pred - y))

# Define the learning rate and the optimizer (Gradient Descent)
learning_rate = 0.01
optimizer = tf.train.GradientDescentOptimizer(learning_rate)
train_op = optimizer.minimize(loss)

# Create a TensorFlow session
with tf.Session() as sess:
    # Initialize the variables
    sess.run(tf.global_variables_initializer())

    # Perform gradient descent iterations
    num_iterations = 1000
    for i in range(num_iterations):
        # Run a single iteration of gradient descent
        _, curr_loss, curr_W, curr_b = sess.run([train_op, loss, W, b], feed_dict={X: X_train, y: y_train})

        # Print the progress every 100 iterations
        if (i + 1) % 100 == 0:
            print(f"Iteration {i + 1}: Loss={curr_loss:.4f}, W={curr_W:.4f}, b={curr_b:.4f}")

    # Print the final learned parameters
    print("\nFinal Results:")
    print(f"Loss={curr_loss:.4f}, W={curr_W:.4f}, b={curr_b:.4f}")
