import networkx as nx
import matplotlib.pyplot as plt
from time import sleep
from matplotlib.animation import FuncAnimation

def create_vertical_graph_animation(word_list):
    G = nx.Graph()
    pos = {}

    # Initialize variables
    current_index = 1
    upper_node_position = (0, 0)
    lower_node_position = (0, -1)

    def update(frame):
        nonlocal current_index, upper_node_position, lower_node_position

        word = word_list[frame]

        # Add upper node
        G.add_node(current_index, label=word)
        pos[current_index] = upper_node_position

        # Increment index
        current_index += 1

        # Add lower node
        G.add_node(current_index, label=word)
        pos[current_index] = lower_node_position

        # Add edge between upper and lower nodes
        G.add_edge(current_index - 1, current_index)

        # Update positions for the next iteration
        upper_node_position = lower_node_position
        lower_node_position = (upper_node_position[0], upper_node_position[1] - 1)

        # Increment index for the next lower node
        current_index += 1

        # Draw the graph
        ax.clear()
        nx.draw(G, pos, labels=nx.get_node_attributes(G, 'label'), node_size=1000, node_color='black', edge_color='black', font_size=24, font_color='white', ax=ax)
        fig.set_facecolor('green')  # Set the background color
        ax.set_facecolor('green')  # Set the background color


    # Create animation
    fig, ax = plt.subplots()
    ax.set_facecolor('#eeefff')
    ani = FuncAnimation(fig, update, frames=len(word_list), interval=1000, repeat=False)

    plt.show()

# Example usage
word_list = ["a", "close", "up", "of", "a", "television", "screen", "with", "a", "lot", "of", "different", "pictures"]
create_vertical_graph_animation(word_list)

