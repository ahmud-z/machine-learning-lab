from sklearn.linear_model import LogisticRegression as LR_sklearn
from LogisticRegression import Logistic_Regression_Scratch
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer
from sklearn.metrics import accuracy_score


b_cancer = load_breast_cancer()
X, y = b_cancer.data, b_cancer.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=1234
)

scratch_model = Logistic_Regression_Scratch(lr=0.01, iterations=1000)

scratch_model.fit(X_train, y_train)

y_pred = scratch_model.predict(X_test)

custom_accuracy = scratch_model.accuracy(y_test, y_pred)


# From cikit-learn's logistic regression model
model_sklearn = LR_sklearn()
model_sklearn.fit(X_train, y_train)
y_pred_sklearn = model_sklearn.predict(X_test)
accuracy_sklearn = accuracy_score(y_test, y_pred_sklearn)

print(f"Custom Logistic Regression Accuracy: {custom_accuracy:.2f}")
print(f"Scikit-learn Logistic Regression Accuracy: {accuracy_sklearn:.2f}")
