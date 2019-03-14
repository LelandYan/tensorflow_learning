# _*_ coding: utf-8 _*_

# import numpy as np
# from sklearn import datasets
# from sklearn.pipeline import Pipeline
# from sklearn.preprocessing import StandardScaler
# from sklearn.svm import LinearSVC
# from sklearn.svm import SVC
# # import matplotlib.pyplot as plt
#
# # iris = datasets.load_iris()
# X = iris["data"][:,(2,3)]
# y = (iris["target"] == 2).astype(np.float64)
#
# svm_clf = Pipeline([
#     ("scaler",StandardScaler()),
#     ("linear_svc",LinearSVC(C=1,loss="hinge")),
# ])
# svm_clf.fit(X,y)
#
# print(svm_clf.predict([[5.5,1.7]]))

# large margin classification

# 实例一
# iris = datasets.load_iris()
# X = iris["data"][:, (2, 3)]
# y = iris["target"]


#
# # 选择类别为0或者1的数据
# setosa_or_versicolor = (y == 0) | (y == 1)
# X = X[setosa_or_versicolor]
# y = y[setosa_or_versicolor]
#
#
# svm_clf = SVC(kernel="linear",C=float("inf"))
# svm_clf.fit(X,y)
#
#
# # 实例二
# x0 = np.linspace(0, 5.5, 200)
# pred_1 = 5 * x0 - 20
# pred_2 = x0 - 1.8
# pred_3 = 0.1 * x0 + 0.5
#
#
# def plot_svc_decision_boundary(svm_clf, xmin, xmax):
#     w = svm_clf.coef_[0]
#     b = svm_clf.intercept_[0]
#
#     X0 = np.linspace(xmin, xmax, 200)
#     decision_boundary = -w[0] / w[1] * X0 - b / w[1]
#
#     margin = 1 / w[1]
#     gutter_up = decision_boundary + margin
#     gutter_down = decision_boundary - margin
#
#     svs = svm_clf.support_vectors_
#     plt.scatter(svs[:, 0], svs[:, 1], s=180, facecolors='#FFAAAA')
#     plt.plot(X0, decision_boundary, "k-", linewidth=2)
#     plt.plot(X0, gutter_up, "k--", linewidth=2)
#     plt.plot(X0, gutter_down, "k--", linewidth=2)


#
# plt.figure(figsize=(12, 2.7))
#
# plt.subplot(121)
# plt.plot(x0, pred_1, "g--", linewidth=2)
# plt.plot(x0, pred_2, "m-", linewidth=2)
# plt.plot(x0, pred_3, "r-", linewidth=2)
# plt.plot(X[:, 0][y == 1], X[:, 1][y == 1], "bs", label="Iris-Versicolor")
# plt.plot(X[:, 0][y == 0], X[:, 1][y == 0], "yo", label="Iris-Setosa")
# plt.xlabel("Petal length", fontsize=14)
# plt.ylabel("Petal width", fontsize=14)
# plt.legend(loc="upper left", fontsize=14)
# plt.axis([0, 5.5, 0, 2])
#
# plt.subplot(122)
# plot_svc_decision_boundary(svm_clf,0,5.5)
# plt.plot(X[:,0][y==1],X[:,1][y==1],"bs")
# plt.plot(X[:,0][y==0],X[:,1][y==0],"yo")
# plt.xlabel("Petal length", fontsize=14)
# plt.axis([0, 5.5, 0, 2])
# plt.show()


# import numpy as np
# from sklearn.svm import SVC
# import matplotlib.pyplot as plt
# # Sensitivity to feature scales
# import tensorflow as tf
# Xs = np.array([[1, 50], [5, 20], [3, 80], [5, 60]]).astype(np.float64)
# ys = np.array([0, 0, 1, 1])
# svm_clf = SVC(kernel="linear", C=100)
# svm_clf.fit(Xs, ys)
#
# plt.figure(figsize=(12, 3.2))
# plt.show()
# plt.subplot(121)
# plt.plot(Xs[:, 0][ys == 1], Xs[:, 1][ys == 1], "bo")
# plt.plot(Xs[:, 0][ys == 0], Xs[:, 1][ys == 0], "ms")
# plot_svc_decision_boundary(svm_clf, 0, 6)
# plt.xlabel("$x_0$", fontsize=20)
# plt.ylabel("$x_1$  ", fontsize=20, rotation=0)
# plt.title("Unscaled", fontsize=16)
# plt.axis([0, 6, 0, 90])
#
# from sklearn.preprocessing import StandardScaler
#
# scaler = StandardScaler()
# X_scaled = scaler.fit_transform(Xs)
# svm_clf.fit(X_scaled, ys)
#
# plt.subplot(122)
# plt.plot(X_scaled[:, 0][ys == 1], X_scaled[:, 1][ys == 1], "bo")
# plt.plot(X_scaled[:, 0][ys == 0], X_scaled[:, 1][ys == 0], "ms")
# plot_svc_decision_boundary(svm_clf, -2, 2)
# plt.xlabel("$x_0$", fontsize=20)
# plt.title("Scaled", fontsize=16)
# plt.axis([-2, 2, -2, 2])
#
# # plt.show()
#
# # sensitivity to outliers
# X_outliers = np.array([[3.4, 1.3], [3.2, 0.8]])
# y_outliers = np.array([0, 0])
# Xo1 = np.concatenate([X, X_outliers[:1]], axis=0)
# yo1 = np.concatenate([y, y_outliers[:1]], axis=0)
# Xo2 = np.concatenate([X, X_outliers[1:]], axis=0)
# yo2 = np.concatenate([y, y_outliers[1:]], axis=0)
#
# svm_clf2 = SVC(kernel="linear", C=10 ** 9)
# svm_clf2.fit(Xo2, yo2)
#
# plt.figure(figsize=(12, 2.7))
#
# plt.subplot(121)
# plt.plot(Xo1[:, 0][yo1 == 1], Xo1[:, 1][yo1 == 1], "bs")
# plt.plot(Xo1[:, 0][yo1 == 0], Xo1[:, 1][yo1 == 0], "yo")
# plt.text(0.3, 1.0, "Impossible!", fontsize=24, color="red")
# plt.xlabel("Petal length", fontsize=14)
# plt.ylabel("Petal width", fontsize=14)
# plt.annotate("Outlier",
#              xy=(X_outliers[0][0], X_outliers[0][1]),
#              xytext=(2.5, 1.7),
#              ha="center",
#              arrowprops=dict(facecolor='black', shrink=0.1),
#              fontsize=16,
#              )
# plt.axis([0, 5.5, 0, 2])
#
# plt.subplot(122)
# plt.plot(Xo2[:, 0][yo2 == 1], Xo2[:, 1][yo2 == 1], "bs")
# plt.plot(Xo2[:, 0][yo2 == 0], Xo2[:, 1][yo2 == 0], "yo")
# plot_svc_decision_boundary(svm_clf2, 0, 5.5)
# plt.xlabel("Petal length", fontsize=14)
# plt.annotate("Outlier",
#              xy=(X_outliers[1][0], X_outliers[1][1]),
#              xytext=(3.2, 0.08),
#              ha="center",
#              arrowprops=dict(facecolor='black', shrink=0.1),
#              fontsize=16,
#              )
# plt.axis([0, 5.5, 0, 2])
#
# # plt.show()
#
# iris = datasets.load_iris()
# X = iris["data"][:, (2, 3)]
# y = (iris["target"] == 2).astype(np.float64)
#
# svm_clf = Pipeline([
#     ("scaler", StandardScaler()),
#     ("linear_svc", LinearSVC(C=1, loss="hinge", random_state=42)),
# ])
# svm_clf.fit(X,y)
# res = svm_clf.predict([[5.5,1.7]])
#
#
# scaler = StandardScaler()
# svm_clf1 = LinearSVC(C=1,loss="hinge",random_state=42)
# svm_clf2 = LinearSVC(C=100,loss="hinge",random_state=42)
# scaler_svm_clf1 = Pipeline([
#     ("scaler",scaler),
#     ("linear_svc",svm_clf1),
# ])
# scaler_svm_clf2 = Pipeline([
#     ("scaler",scaler),
#     ("linear_svc",svm_clf2),
# ])
# scaler_svm_clf1.fit(X,y)
# scaler_svm_clf2.fit(X,y)
#
# b1 = svm_clf1.decision_function([-scaler.mean_ / scaler.scale_])
#
#
# plt.figure(figsize=(12,3.2))
# plt.subplot(121)
# plt.plot(X[:, 0][y==1], X[:, 1][y==1], "g^", label="Iris-Virginica")
# plt.plot(X[:, 0][y==0], X[:, 1][y==0], "bs", label="Iris-Versicolor")
# plot_svc_decision_boundary(svm_clf1, 4, 6)
# plt.xlabel("Petal length", fontsize=14)
# plt.ylabel("Petal width", fontsize=14)
# plt.legend(loc="upper left", fontsize=14)
# plt.title("$C = {}$".format(svm_clf1.C), fontsize=16)
# plt.axis([4, 6, 0.8, 2.8])
#
# plt.subplot(122)
# plt.plot(X[:, 0][y==1], X[:, 1][y==1], "g^")
# plt.plot(X[:, 0][y==0], X[:, 1][y==0], "bs")
# plot_svc_decision_boundary(svm_clf2, 4, 6)
# plt.xlabel("Petal length", fontsize=14)
# plt.title("$C = {}$".format(svm_clf2.C), fontsize=16)
# plt.axis([4, 6, 0.8, 2.8])


# # Non-linear classification
# X1D = np.linspace(-4, 4, 9).reshape(-1, 1)
# print(X1D)
# X2D = np.c_[X1D, X1D**2]
# y = np.array([0, 0, 1, 1, 1, 1, 1, 0, 0])
# import matplotlib.pyplot
# # plt.figure(figsize=(11,4))
# pltfr.subplot(121)
# plt.grid(True, which='both')
# plt.axhline(y=0, color='k')
# plt.plot(X1D[:, 0][y==0], np.zeros(4), "bs")
# plt.plot(X1D[:, 0][y==1], np.zeros(5), "g^")
# plt.gca().get_yaxis().set_ticks([])
# plt.xlabel(r"$x_1$", fontsize=20)
# plt.axis([-4.5, 4.5, -0.2, 0.2])
import numpy as np
import matplotlib.pyplot as plt

# Non-linear classification
# X1D = np.linspace(-4, 4, 9).reshape(-1, 1)
# X2D = np.c_[X1D,X1D**2]
# y = np.array([0, 0, 1, 1, 1, 1, 1, 0, 0])
#
# plt.figure(figsize=(11,4))
#
# plt.subplot(121)
# plt.grid(True, which='both')
# plt.axhline(y=0, color='k')
# plt.plot(X1D[:, 0][y==0], np.zeros(4), "bs")
# plt.plot(X1D[:, 0][y==1], np.zeros(5), "g^")
# plt.gca().get_yaxis().set_ticks([])
# plt.xlabel(r"$x_1$", fontsize=20)
# plt.axis([-4.5, 4.5, -0.2, 0.2])
#
# plt.subplot(122)
# plt.grid(True, which='both')
# plt.axhline(y=0, color='k')
# plt.axvline(x=0, color='k')
# plt.plot(X2D[:, 0][y==0], X2D[:, 1][y==0], "bs")
# plt.plot(X2D[:, 0][y==1], X2D[:, 1][y==1], "g^")
# plt.xlabel(r"$x_1$", fontsize=20)
# plt.ylabel(r"$x_2$", fontsize=20, rotation=0)
# plt.gca().get_yaxis().set_ticks([0, 4, 8, 12, 16])
# plt.plot([-4.5, 4.5], [6.5, 6.5], "r--", linewidth=3)
# plt.axis([-4.5, 4.5, -1, 17])

# plt.show()

from sklearn.datasets import make_moons

X, y = make_moons(n_samples=100, noise=0.15, random_state=42)


def plot_dataset(X, y, axes):
    plt.plot(X[:, 0][y==0], X[:, 1][y==0], "bs")
    plt.plot(X[:, 0][y==1], X[:, 1][y==1], "g^")
    plt.axis(axes)
    plt.grid(True, which='both')
    plt.xlabel(r"$x_1$", fontsize=20)
    plt.ylabel(r"$x_2$", fontsize=20, rotation=0)

#
# plot_dataset(X, y, [-1.5, 2.5, -1, 1.5])
# plt.show()


from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.svm import LinearSVC

polynomial_svm_clf = Pipeline([
    ("poly_features", PolynomialFeatures(degree=3)),
    ("scaler", StandardScaler()),
    ("svm_clf", LinearSVC(C=10, loss="hinge", random_state=42))
])
polynomial_svm_clf.fit(X,y)

def plot_predictions(clf,axes):
    x0s = np.linspace(axes[0],axes[1],100)
    x1s = np.linspace(axes[2],axes[3],100)
    x0,x1 = np.meshgrid(x0s,x1s)
    X = np.c_[x0.ravel(),x1.ravel()]
    y_pred = clf.predict(X).reshape(x0.shape)
    y_decision = clf.decision_function(X).reshape(x0.shape)

    plt.contourf(x0,x1,y_pred,cmap=plt.cm.brg,alpha=0.2)
    plt.contourf(x0,x1,y_decision,cmap=plt.cm.brg,alpha=0.1)


plot_predictions(polynomial_svm_clf,[-1.5,2.5,-1,1.5])
plot_dataset(X,y,[-1.5,2.5,-1,1.5])
# plt.show()

from sklearn.svm import SVC

poly_knerl_svm_clf = Pipeline([
    ("scaler",StandardScaler()),
    ("svm_clf",SVC(kernel="poly",degree=3,coef0=1,C=5))
])
poly_knerl_svm_clf.fit(X,y)