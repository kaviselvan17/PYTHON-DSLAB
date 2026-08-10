{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPtSWbVqA00F1aoIKHp6SIj",
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
        "<a href=\"https://colab.research.google.com/github/kaviselvan17/kaviselvan.g/blob/main/creation.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "class Node:\n",
        "    def __init__(self,data):\n",
        "        self.data=data\n",
        "        self.next=None\n",
        "class LinkedList:\n",
        "    def __init__(self):\n",
        "        self.head=None\n",
        "    def push(self,new_data):\n",
        "        new_node=Node(new_data)\n",
        "        new_node.next=self.head\n",
        "        self.head=new_node\n",
        "    def insertAfer(self,previous_node,new_data):\n",
        "        if (previous_node is None):\n",
        "            print(\"the given previous node must in linked list\")\n",
        "            return\n",
        "        new_node=Node(new_data)\n",
        "        new_node.next=previous_node.next\n",
        "        previous_node.next=new_node\n",
        "    def append(self,new_node):\n",
        "        new_node=Node(new_node)\n",
        "        if self.head is None:\n",
        "            self.head=new_node\n",
        "            return\n",
        "        last=self.head\n",
        "        while(last.next):\n",
        "            last=last.next\n",
        "            last.next=new_node\n",
        "    def printlist(self):\n",
        "        temp=self.head\n",
        "        while(temp):\n",
        "            print(temp.data)\n",
        "            temp=temp.next\n",
        "if __name__=='main':\n",
        "    llist=LinkedList()\n",
        "    llist.append(6)\n",
        "    llist.push(7)\n",
        "    llist.push(1)\n",
        "    llist.insertAfter(llist.head.next,8)\n",
        "    print(\"created linked list is:\")\n",
        "    llist.printlist()\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "AfVSOtGLYB_Y"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}