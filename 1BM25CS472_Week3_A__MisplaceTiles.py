{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPI4hIHMMbdp42QtnbVTlzx",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/vishnu062006/ai-lab/blob/main/1BM24CS332_Week3_A*_MisplaceTiles.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-5ZpkvxeY0Y5",
        "outputId": "5ef66fb1-dffd-4ad8-dc11-31f2738cad9b"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Misplaced Tiles - Steps: 14\n"
          ]
        }
      ],
      "source": [
        "\n",
        "\n",
        "import heapq\n",
        "\n",
        "GOAL_STATE = (1, 2, 3, 4, 5, 6, 7, 8, 0)\n",
        "\n",
        "class Node:\n",
        "    def __init__(self, state, g, h, parent=None):\n",
        "        self.state = state\n",
        "        self.g = g # Depth\n",
        "        self.h = h # Misplaced tiles count\n",
        "        self.f = g + h\n",
        "        self.parent = parent\n",
        "\n",
        "    def __lt__(self, other):\n",
        "        return self.f < other.f\n",
        "\n",
        "def get_neighbors(state):\n",
        "    neighbors = []\n",
        "    zero_idx = state.index(0)\n",
        "    row, col = divmod(zero_idx, 3)\n",
        "    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]\n",
        "\n",
        "    for dr, dc in moves:\n",
        "        nr, nc = row + dr, col + dc\n",
        "        if 0 <= nr < 3 and 0 <= nc < 3:\n",
        "            new_idx = nr * 3 + nc\n",
        "            state_list = list(state)\n",
        "            state_list[zero_idx], state_list[new_idx] = state_list[new_idx], state_list[zero_idx]\n",
        "            neighbors.append(tuple(state_list))\n",
        "    return neighbors\n",
        "\n",
        "def count_misplaced(state, goal):\n",
        "    # h(n): Number of tiles out of place (excluding 0)\n",
        "    return sum(1 for i in range(9) if state[i] != 0 and state[i] != goal[i])\n",
        "\n",
        "def solve_misplaced(initial_state):\n",
        "    open_set = []\n",
        "    initial_node = Node(initial_state, g=0, h=count_misplaced(initial_state, GOAL_STATE))\n",
        "    heapq.heappush(open_set, initial_node)\n",
        "    closed_set = set()\n",
        "\n",
        "    while open_set:\n",
        "        current = heapq.heappop(open_set)\n",
        "\n",
        "        if current.state == GOAL_STATE:\n",
        "            path = []\n",
        "            while current:\n",
        "                path.append(current.state)\n",
        "                current = current.parent\n",
        "            return path[::-1]\n",
        "\n",
        "        closed_set.add(current.state)\n",
        "\n",
        "        for neighbor in get_neighbors(current.state):\n",
        "            if neighbor in closed_set:\n",
        "                continue\n",
        "            g = current.g + 1\n",
        "            h = count_misplaced(neighbor, GOAL_STATE)\n",
        "            heapq.heappush(open_set, Node(neighbor, g, h, parent=current))\n",
        "\n",
        "    return None\n",
        "\n",
        "# Test Run\n",
        "if __name__ == \"__main__\":\n",
        "    initial = (1, 2, 3, 4, 0, 5, 6, 7, 8)\n",
        "    path = solve_misplaced(initial)\n",
        "    print(f\"Misplaced Tiles - Steps: {len(path) - 1}\")"
      ]
    }
  ]
}