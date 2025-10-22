import tkinter as tk
from tkinter import filedialog
import re

def count_words(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            text = f.read()
    except FileNotFoundError:
        return None, "File not found."
    except Exception as e:
        return None, str(e)
    
    text = text.lower()
    words = re.findall(r'\b\w+\b', text)
    
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
            
    return dict(sorted(word_counts.items(), key=lambda item: item[1], reverse=True)), None


def browse_file():
    filepath = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if filepath:
        word_counts, error_message = count_words(filepath)
        if word_counts:
            results_text.delete('1.0', tk.END)
            for word, count in word_counts.items():
                results_text.insert(tk.END, f'{word}: {count}\n')
        else:
            results_text.delete('1.0', tk.END)
            results_text.insert(tk.END, error_message)


root = tk.Tk()
root.title("Word Frequency Counter")

browse_button = tk.Button(root, text="Browse File", command=browse_file)
browse_button.pack(pady=10)

results_text = tk.Text(root, height=20, width=50)
results_text.pack(pady=10)

root.mainloop()
