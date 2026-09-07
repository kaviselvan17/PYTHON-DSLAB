{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPYv4teGt5tSkKQsnDUOVZj",
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
        "<a href=\"https://colab.research.google.com/github/kaviselvan17/kaviselvan.g/blob/main/traversal.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "qcG0xw_sxoOD"
      },
      "outputs": [],
      "source": [
        "class Node:\n",
        "  def __init__(self,data):\n",
        "    self.data=data\n",
        "    self.next=None\n",
        "class LinkedList:\n",
        "  def __init__(self):\n",
        "    self.head=None\n",
        "  def printList(self):\n",
        "    temp=self.head\n",
        "    while(temp):\n",
        "      print(temp.data)\n",
        "      temp=temp.next\n",
        "if __name__==\"__main__\":\n",
        "  llist=LinkedList()\n",
        "\n",
        "  llist.head=Node(1)\n",
        "  second=Node(2)\n",
        "  third=Node(3)\n",
        "\n",
        "  llist.head.next=second\n",
        "  second.next=third\n",
        "\n",
        "  llist.printList()"
      ]
    }
  ]
}
