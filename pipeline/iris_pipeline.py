import kfp
from kfp import dsl
from kfp.dsl import component, Output, Input, Artifact

@component(
    packages_to_install=["scikit-learn", "pandas", "numpy"],
    base_image="python:3.11"
)
def load_and_preprocess(
    train_path: Output[Artifact],
    test_path: Output[Artifact]
):
    import json
    from sklearn.datasets import load_iris
    from sklearn.model_selection import train_test_split
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.2, random_state=42
    )
    with open(train_path.path, "w") as f:
        json.dump({"X": X_train.tolist(), "y": y_train.tolist()}, f)
    with open(test_path.path, "w") as f:
        json.dump({"X": X_test.tolist(), "y": y_test.tolist()}, f)
    print("Data preprocessed successfully.")

@component(
    packages_to_install=["scikit-learn", "numpy"],
    base_image="python:3.11"
)
def train_model(
    train_path: Input[Artifact],
    model_path: Output[Artifact]
):
    import json, pickle
    from sklearn.ensemble import RandomForestClassifier
    with open(train_path.path) as f:
        data = json.load(f)
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(data["X"], data["y"])
    with open(model_path.path, "wb") as f:
        pickle.dump(clf, f)
    print("Model trained successfully.")

@component(
    packages_to_install=["scikit-learn", "numpy"],
    base_image="python:3.11"
)
def evaluate_model(
    test_path: Input[Artifact],
    model_path: Input[Artifact]
) -> float:
    import json, pickle
    from sklearn.metrics import accuracy_score
    with open(test_path.path) as f:
        data = json.load(f)
    with open(model_path.path, "rb") as f:
        clf = pickle.load(f)
    acc = accuracy_score(data["y"], clf.predict(data["X"]))
    print(f"Accuracy: {acc:.4f}")
    return acc

@dsl.pipeline(name="Iris Classification Pipeline")
def iris_pipeline():
    load_task  = load_and_preprocess()
    train_task = train_model(train_path=load_task.outputs["train_path"])
    evaluate_model(
        test_path=load_task.outputs["test_path"],
        model_path=train_task.outputs["model_path"]
    )

if __name__ == "__main__":
    from kfp import compiler
    compiler.Compiler().compile(
        pipeline_func=iris_pipeline,
        package_path="iris_pipeline.yaml"
    )
    print("Compiled: iris_pipeline.yaml")
