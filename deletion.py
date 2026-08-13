{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPVTnZWAkJZgXp3aMUNS9mN",
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
        "<a href=\"https://colab.research.google.com/github/kaviselvan17/kaviselvan.g/blob/main/deletion.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "e63IAsGVrZii",
        "outputId": "df0658e9-3970-451f-ad1a-abc5c799fa97"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Thu\n",
            "Tue\n",
            "Mon\n"
          ]
        }
      ],
      "source": [
        "class Node:\n",
        "  def __init__(self,data=None):\n",
        "    self.data=data\n",
        "    self.next=None\n",
        "\n",
        "class SLinkedList:\n",
        "  def __init__(self):\n",
        "    self.head=None\n",
        "\n",
        "  def Atbegining(self,data_in):\n",
        "    NewNode=Node(data_in)\n",
        "    NewNode.next=self.head\n",
        "    self.head=NewNode\n",
        "\n",
        "  def RemoveNode(self,Removekey):\n",
        "    HeadVal=self.head\n",
        "    if(HeadVal is not Node):\n",
        "      if(HeadVal.data==Removekey):\n",
        "        self.head=HeadVal.next\n",
        "        HeadVal=None\n",
        "        return\n",
        "      while(HeadVal is not  None):\n",
        "        if HeadVal.data==Removekey:\n",
        "          break\n",
        "        prev=HeadVal\n",
        "        HeadVal=HeadVal.next\n",
        "        if(HeadVal==None):\n",
        "          return\n",
        "        prev.next=HeadVal.next\n",
        "        HeadVal=None\n",
        "  def llistprint(self):\n",
        "    printval=self.head\n",
        "\n",
        "    while(printval):\n",
        "      print(printval.data)\n",
        "      printval=printval.next\n",
        "\n",
        "llist=SLinkedList()\n",
        "llist.Atbegining(\"Mon\")\n",
        "llist.Atbegining(\"Tue\")\n",
        "llist.Atbegining(\"Wed\")\n",
        "llist.Atbegining(\"Thu\")\n",
        "llist.RemoveNode(\"Tue\")\n",
        "llist.llistprint()\n"
      ]
    }
  ]
}