{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNOCYz7TCUYZEjZ5638DgqC",
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
        "<a href=\"https://colab.research.google.com/github/kaviselvan17/PYTHON-DSLAB/blob/main/Implemention_of_BST_a)Creation_A_Node.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "IxQih_bUjyOF",
        "outputId": "82a5f4a7-10a3-48e1-a072-859ee9a7afb3"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "Minimum value in BST is 1\n"
          ]
        }
      ],
      "source": [
        "class Node:\n",
        "\n",
        "    # Constructor to create a new node\n",
        "    def __init__(self, key):\n",
        "        self.data = key\n",
        "        self.left = None\n",
        "        self.right = None\n",
        "\n",
        "\n",
        "def insert(node, data):\n",
        "\n",
        "    if node is None:\n",
        "        return Node(data)\n",
        "\n",
        "    else:\n",
        "        if data <= node.data:\n",
        "            node.left = insert(node.left, data)\n",
        "        else:\n",
        "            node.right = insert(node.right, data)\n",
        "\n",
        "    return node\n",
        "\n",
        "\n",
        "def minValue(node):\n",
        "\n",
        "    current = node\n",
        "\n",
        "    while current.left is not None:\n",
        "        current = current.left\n",
        "\n",
        "    return current.data\n",
        "\n",
        "\n",
        "root = None\n",
        "\n",
        "root = insert(root, 4)\n",
        "insert(root, 2)\n",
        "insert(root, 1)\n",
        "insert(root, 3)\n",
        "insert(root, 6)\n",
        "insert(root, 5)\n",
        "\n",
        "print(\"\\nMinimum value in BST is %d\" % (minValue(root)))"
      ]
    }
  ]
}