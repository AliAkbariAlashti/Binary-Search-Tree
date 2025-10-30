"""
Binary Search Tree - GUI Visualizer
"""

import tkinter as tk
from tkinter import ttk, messagebox
import random
import sys
import os

# Add core folder to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from core.bst import BST, Node


class BSTVisualizer(tk.Tk):
    """Simple BST Visualizer"""
    
    def __init__(self):
        super().__init__()
        self.title("BST Visualizer")
        self.geometry("1000x700")
        
        self.bst = BST()
        self.create_ui()
    
    def create_ui(self):
        """Create the user interface"""
        # Main layout
        main = ttk.Frame(self)
        main.pack(fill='both', expand=True)
        
        # Canvas for drawing
        self.canvas = tk.Canvas(main, bg='white')
        self.canvas.pack(side='left', fill='both', expand=True)
        
        # Control panel
        controls = ttk.Frame(main, width=250)
        controls.pack(side='right', fill='y', padx=10, pady=10)
        
        # Title
        ttk.Label(controls, text='BST Visualizer', font=('Arial', 16, 'bold')).pack(pady=10)
        
        # Input
        ttk.Label(controls, text='Enter value:').pack()
        self.value_entry = ttk.Entry(controls)
        self.value_entry.pack(fill='x', pady=5)
        self.value_entry.bind('<Return>', lambda e: self.insert())
        
        # Buttons
        ttk.Button(controls, text='Insert', command=self.insert).pack(fill='x', pady=2)
        ttk.Button(controls, text='Search', command=self.search).pack(fill='x', pady=2)
        ttk.Button(controls, text='Delete', command=self.delete).pack(fill='x', pady=2)
        ttk.Button(controls, text='Show Path', command=self.show_path).pack(fill='x', pady=2)
        
        ttk.Separator(controls).pack(fill='x', pady=10)
        
        # Traversals
        ttk.Label(controls, text='Traversals:', font=('Arial', 11, 'bold')).pack(pady=5)
        ttk.Button(controls, text='Inorder', command=self.show_inorder).pack(fill='x', pady=2)
        ttk.Button(controls, text='Preorder', command=self.show_preorder).pack(fill='x', pady=2)
        ttk.Button(controls, text='Postorder', command=self.show_postorder).pack(fill='x', pady=2)
        
        ttk.Separator(controls).pack(fill='x', pady=10)
        
        # Utilities
        ttk.Button(controls, text='Random Tree', command=self.random_tree).pack(fill='x', pady=2)
        ttk.Button(controls, text='Clear', command=self.clear).pack(fill='x', pady=2)
        
        # Output
        ttk.Label(controls, text='Output:', font=('Arial', 11, 'bold')).pack(pady=(10,5))
        self.output = tk.Text(controls, height=10, width=30)
        self.output.pack(fill='both', expand=True)
    
    def log(self, message):
        """Add message to output"""
        self.output.insert('end', f'{message}\n')
        self.output.see('end')
    
    def get_value(self):
        """Get value from entry"""
        try:
            return int(self.value_entry.get())
        except:
            messagebox.showerror('Error', 'Please enter a valid number')
            return None
    
    def insert(self):
        """Insert value"""
        value = self.get_value()
        if value is None:
            return
        
        node = self.bst.insert(value)
        if node:
            self.log(f'Inserted {value}')
            self.draw_tree()
        else:
            self.log(f'{value} already exists')
        self.value_entry.delete(0, 'end')
    
    def search(self):
        """Search for value"""
        value = self.get_value()
        if value is None:
            return
        
        node = self.bst.search(value)
        if node:
            self.log(f'Found {value}')
        else:
            self.log(f'{value} not found')
    
    def show_path(self):
        """Show path from root to node"""
        value = self.get_value()
        if value is None:
            return
        
        path = self.bst.get_path(value)
        if path:
            path_str = ' → '.join(map(str, path))
            self.log(f'Path to {value}: {path_str}')
        else:
            self.log(f'{value} not found')
    
    def delete(self):
        """Delete value"""
        value = self.get_value()
        if value is None:
            return
        
        deleted = self.bst.delete(value)
        if deleted:
            self.log(f'Deleted {value}')
            self.draw_tree()
        else:
            self.log(f'{value} not found')
        self.value_entry.delete(0, 'end')
    
    def show_inorder(self):
        """Show inorder traversal"""
        nodes = self.bst.inorder()
        values = [n.value for n in nodes]
        self.log(f'Inorder: {values}')
    
    def show_preorder(self):
        """Show preorder traversal"""
        nodes = self.bst.preorder()
        values = [n.value for n in nodes]
        self.log(f'Preorder: {values}')
    
    def show_postorder(self):
        """Show postorder traversal"""
        nodes = self.bst.postorder()
        values = [n.value for n in nodes]
        self.log(f'Postorder: {values}')
    
    def random_tree(self):
        """Generate random tree"""
        self.bst = BST()
        values = random.sample(range(1, 100), random.randint(7, 12))
        for v in values:
            self.bst.insert(v)
        self.draw_tree()
        self.log(f'Random tree: {sorted(values)}')
    
    def clear(self):
        """Clear tree"""
        self.bst = BST()
        self.draw_tree()
        self.log('Tree cleared')
    
    def draw_tree(self):
        """Draw the tree"""
        self.canvas.delete('all')
        if not self.bst.root:
            return
        
        # Calculate positions
        self.calculate_positions()
        
        # Draw edges
        self.draw_edges(self.bst.root)
        
        # Draw nodes
        self.draw_nodes(self.bst.root)
    
    def calculate_positions(self):
        """Calculate node positions"""
        positions = {}
        index = 0
        
        def assign(node, depth):
            nonlocal index
            if node.left:
                assign(node.left, depth + 1)
            positions[node] = (index, depth)
            index += 1
            if node.right:
                assign(node.right, depth + 1)
        
        assign(self.bst.root, 0)
        
        # Convert to pixel coordinates
        width = self.canvas.winfo_width() or 800
        spacing = max(50, width / (index + 1))
        
        for node, (idx, depth) in positions.items():
            node.x = 30 + idx * spacing
            node.y = 50 + depth * 80
    
    def draw_edges(self, node):
        """Draw tree edges"""
        if not node:
            return
        if node.left:
            self.canvas.create_line(node.x, node.y, node.left.x, node.left.y, width=2)
            self.draw_edges(node.left)
        if node.right:
            self.canvas.create_line(node.x, node.y, node.right.x, node.right.y, width=2)
            self.draw_edges(node.right)
    
    def draw_nodes(self, node):
        """Draw tree nodes"""
        if not node:
            return
        
        r = 20
        self.canvas.create_oval(
            node.x - r, node.y - r,
            node.x + r, node.y + r,
            fill='lightblue', outline='blue', width=2
        )
        self.canvas.create_text(
            node.x, node.y,
            text=str(node.value),
            font=('Arial', 10, 'bold')
        )
        
        self.draw_nodes(node.left)
        self.draw_nodes(node.right)


if __name__ == '__main__':
    app = BSTVisualizer()
    app.mainloop()