# Lesson 11: 9.Parameters
W=5
H=5
F=3
S=1
P=1
K=1
W_out = (W-F+2*P) / S + 1
print(W_out)
H_out = (H-F+2*P) / S + 1
print(H_out)
D_out = K
print(D_out)
V_out = W_out * H_out * D_out
print(V_out)

# Lesson 11: 10.Quiz Convolution Output Shape
input_width=32
input_height=32
filter_height=8
filter_width=8
S=2
P=1
new_height = (input_height - filter_height + 2 * P)/S + 1
new_width = (input_width - filter_width + 2 * P)/S + 1
print("new_height: ", new_height)
print("new_width: ", new_width)