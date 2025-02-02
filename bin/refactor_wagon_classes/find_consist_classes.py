import ast
import os

TRAIN_FILE = "src/train.py"
OUTPUT_FILE = "./tmp/consist_classes_list.txt"

def parse_class_hierarchy(file_path):
    """Parses a Python file and extracts all classes and their parent relationships."""
    with open(file_path, "r", encoding="utf-8") as f:
        tree = ast.parse(f.read())

    class_hierarchy = {}

    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            class_name = node.name
            parent_classes = [base.id for base in node.bases if isinstance(base, ast.Name)]
            class_hierarchy[class_name] = parent_classes

    return class_hierarchy

def build_inheritance_tree(class_hierarchy):
    """Builds a parent-to-children inheritance tree."""
    from collections import defaultdict

    inheritance_tree = defaultdict(list)
    for class_name, parents in class_hierarchy.items():
        for parent in parents:
            inheritance_tree[parent].append(class_name)

    return inheritance_tree

def find_subclasses(root_class, inheritance_tree):
    """Recursively finds all subclasses of a given root class."""
    discovered = set()

    def recurse(class_name):
        if class_name not in discovered:
            discovered.add(class_name)
            for child in inheritance_tree.get(class_name, []):
                recurse(child)

    recurse(root_class)
    discovered.discard(root_class)  # Exclude the root class itself
    return discovered

def find_consist_classes():
    """Finds all subclasses of Consist using AST and writes them to a file."""
    # Step 1: Parse all classes and their parents
    class_hierarchy = parse_class_hierarchy(TRAIN_FILE)

    # Step 2: Build the inheritance tree
    inheritance_tree = build_inheritance_tree(class_hierarchy)

    # Step 3: Find all subclasses of `Consist`
    consist_classes = find_subclasses("Consist", inheritance_tree)

    # Step 4: Write results to a file
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        for class_name in sorted(consist_classes):
            f.write(class_name + "\n")

    print(f"✅ Found {len(consist_classes)} subclasses of `Consist`.")
    print(f"📄 Class names written to {OUTPUT_FILE}")

if __name__ == "__main__":
    find_consist_classes()
