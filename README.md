# 🌳 BST Visualizer

A simple and clean Binary Search Tree visualizer built with Python and Tkinter.

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

---

## ✨ Features

- 🔵 **Insert** nodes with visual feedback
- 🔍 **Search** for values in the tree
- 🛤️ **Show Path** from root to any node
- ❌ **Delete** nodes while maintaining BST properties
- 📊 **Three traversals**: Inorder, Preorder, Postorder
- 🎲 **Random tree** generator for testing
- 🎨 **Clean and intuitive** interface

---

## 🚀 Quick Start

### Run the Application

```bash
python main.py
```

That's it! The visualizer will open.

---

## 📖 How to Use

### Insert Values
1. Type a number in the input field
2. Press **Enter** or click **Insert**
3. Watch the tree update!

### Search
1. Enter a value
2. Click **Search**
3. Check the output to see if it exists

### Show Path
1. Enter a value
2. Click **Show Path**
3. See the route from root to that node!
   - Example: `50 → 25 → 37`

### Delete
1. Enter a value
2. Click **Delete**
3. The tree restructures automatically

### Traversals
- **Inorder**: Click to see sorted order
- **Preorder**: Click to see root-first order
- **Postorder**: Click to see children-first order

### Quick Actions
- **Random Tree**: Generate a tree with 7-12 random nodes
- **Clear**: Start fresh with an empty tree

---

## 📁 Project Structure

```
bst-visualizer/
│
├── core/                    # Logic folder
│   └── bst.py              # BST implementation
│
├── gui/                     # Interface folder
│   └── visualizer.py       # GUI code
│
├── main.py                  # Run this file!
└── README.md               # You are here
```

**Simple and organized:**
- `core/` = Tree logic only
- `gui/` = Visual interface only

---

## 💡 Example Usage

Try inserting these values to build a balanced tree:
```
50, 25, 75, 12, 37, 62, 87
```

Result:
```
       50
      /  \
    25    75
   / \    / \
  12 37  62 87
```

---

## ⚙️ Requirements

- Python 3.7 or higher
- Tkinter (usually comes with Python)

### Install Tkinter (if needed)

**Ubuntu/Debian:**
```bash
sudo apt-get install python3-tk
```

**macOS:**
```bash
brew install python-tk
```

**Windows:**
Tkinter is included with Python by default.

---

## 🎯 What is a Binary Search Tree?

A BST is a tree where:
- Each node has at most 2 children (left and right)
- Left child is smaller than parent
- Right child is larger than parent
- Makes searching very fast!

**Time Complexity:**
- Insert: O(log n) average
- Search: O(log n) average
- Delete: O(log n) average

---

## 🎨 Code Overview

### Core Logic (`core/bst.py`)
```python
class BST:
    def insert(value)     # Add a node
    def search(value)     # Find a node
    def delete(value)     # Remove a node
    def inorder()         # Left-Root-Right
    def preorder()        # Root-Left-Right
    def postorder()       # Left-Right-Root
```

### GUI (`gui/visualizer.py`)
- Canvas for drawing the tree
- Control panel with buttons
- Automatic layout calculation
- Real-time updates

---

## 🤝 Contributing

Feel free to:
- Report bugs
- Suggest features
- Submit pull requests

---

## 📄 License

MIT License - feel free to use this project however you want!

---

## 🎓 Perfect For

- **Students** learning data structures
- **Teachers** demonstrating algorithms
- **Developers** understanding BST operations
- **Anyone** curious about trees!

---

## 🌟 Tips

- Start with small numbers (1-100) for better visualization
- Try different insertion orders to see how tree shape changes
- Use Random Tree to explore different structures
- Inorder traversal always gives sorted output!

---

## 📞 Support

Having issues?
1. Make sure you have Python 3.7+
2. Check if Tkinter is installed
3. Run `python main.py` from the project folder

---

**Enjoy exploring Binary Search Trees!** 🌳

Made with ❤️ using Python and Tkinter