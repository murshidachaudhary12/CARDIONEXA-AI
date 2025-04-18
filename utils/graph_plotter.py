import matplotlib.pyplot as plt

def generate_graph(score, save_path="graph.png"):
    labels = ['Heart Health', 'Remaining']
    sizes = [score, 100 - score]
    colors = ['green' if score >= 60 else 'red', 'lightgrey']
    
    plt.figure(figsize=(4, 4))
    plt.pie(sizes, labels=labels, colors=colors, startangle=90, autopct='%1.1f%%')
    plt.axis('equal')
    plt.savefig(save_path)
    plt.close()

