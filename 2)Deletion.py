{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMCkeBFJ8i1mN7h71QlUg6c",
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
        "<a href=\"https://colab.research.google.com/github/kaviselvan17/PYTHON-DSLAB/blob/main/2)Deletion_py.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "npeueKO-je_V"
      },
      "outputs": [],
      "source": [
        "class Node:\n",
        "    def __init__(self, data):\n",
        "        self.data = data\n",
        "        self.next = None\n",
        "\n",
        "\n",
        "class CreateList:\n",
        "    def __init__(self):\n",
        "        self.head = None\n",
        "        self.tail = None\n",
        "\n",
        "    # Add node\n",
        "    def add(self, data):\n",
        "        newNode = Node(data)\n",
        "\n",
        "        if self.head is None:\n",
        "            self.head = newNode\n",
        "            self.tail = newNode\n",
        "            newNode.next = self.head\n",
        "        else:\n",
        "            self.tail.next = newNode\n",
        "            self.tail = newNode\n",
        "            self.tail.next = self.head\n",
        "\n",
        "    # Delete node from the end\n",
        "    def deleteEnd(self):\n",
        "        if self.head is None:\n",
        "            return\n",
        "\n",
        "        # If only one node is present\n",
        "        if self.head == self.tail:\n",
        "            self.head = None\n",
        "            self.tail = None\n",
        "            return\n",
        "\n",
        "        current = self.head\n",
        "\n",
        "        # Find the second-last node\n",
        "        while current.next != self.tail:\n",
        "            current = current.next\n",
        "\n",
        "        self.tail = current\n",
        "        self.tail.next = self.head\n",
        "\n",
        "    # Display circular linked list\n",
        "    def display(self):\n",
        "        if self.head is None:\n",
        "            print(\"List is empty\")\n",
        "            return\n",
        "\n",
        "        current = self.head\n",
        "\n",
        "        while True:\n",
        "            print(current.data, end=\" \")\n",
        "            current = current.next\n",
        "\n",
        "            if current == self.head:\n",
        "                break\n",
        "\n",
        "        print()\n",
        "\n",
        "\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "\n",
        "    cl = CreateList()\n",
        "\n",
        "    cl.add(1)\n",
        "    cl.add(2)\n",
        "    cl.add(3)\n",
        "    cl.add(4)\n",
        "\n",
        "    print(\"Original List:\")\n",
        "    cl.display()\n",
        "\n",
        "    while cl.head is not None:\n",
        "        cl.deleteEnd()\n",
        "\n",
        "        print(\"Updated List:\")\n",
        "        cl.display()"
      ]
    }
  ]
}
