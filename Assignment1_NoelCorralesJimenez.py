import matplotlib.pyplot as plt
import numpy as np
def cls(): return print("\033[2J\033[;H", end='')


cls()


x_data = np.array([35., 38., 31., 20., 22., 25., 17., 60., 8., 60.])
y_data = 2 * x_data + 50 + 5 * np.random.random(10)

bias_interval = np.arange(0, 100, 1)  # bias 0-99 in 1 increments
weight_interval = np.arange(-5, 5, 0.1)  # weight -5 - 4.9 in 0.1 increments
print(bias_interval)
print(weight_interval)

plot_size = np.zeros((len(bias_interval), len(weight_interval)))

for i in range(len(bias_interval)):
    for j in range(len(weight_interval)):
        b = bias_interval[i]
        w = weight_interval[j]
        plot_size[j][i] = 0
        for n in range(len(x_data)):
            plot_size[j][i] = plot_size[j][i] + (w*x_data[n]+b-y_data[n])**2
        plot_size[j][i] = plot_size[j][i] / len(x_data)


b = 0
w = 0

lr = .0001 # Our learning rate 
iterations = 10000

b_history = [b]
w_history = [w]

#Gradient descent model
for i in range(iterations):
    bg = 0.0
    wg = 0.0
    for n in range(x_data):
        bg = bg 
        wg = wg

    b = b - lr * bg
    w = w - lr * wg

    b_history.append(b)
    w_history.append(w)


plt.contourf(bias_interval, weight_interval, plot_size, 50,
             alpha=0.5, cmap=plt.get_cmap('gist_earth'))
plt.plot([50], [2], 'x', ms=12, markeredgewidth=3, color='orange')

plt.plot(b_history, w_history, 'o-', ms=2, lw=1, color='blue')
plt.xlim(0, 100)
plt.ylim(-5, 5)
plt.xlabel('bias', fontsize=16)
plt.ylabel('weight', fontsize=16)
plt.title('Assignment1_NoelCorralesJimenez')
plt.show()