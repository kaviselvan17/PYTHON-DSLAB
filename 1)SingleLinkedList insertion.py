{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPcHpBf4huWTlK6ottJTUZu",
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
        "<a href=\"https://colab.research.google.com/github/kaviselvan17/kaviselvan.g/blob/main/insertion.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "collapsed": true,
        "id": "ad7xQ33foG-g",
        "outputId": "45764a0a-5a58-423e-ebc8-456cc3f35616"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Sun\n",
            "Mon\n",
            "Wed\n",
            "Wed\n"
          ]
        }
      ],
      "source": [
        "class Node:\n",
        "  def __init__(self,dataval=None):\n",
        "    self.dataval=dataval\n",
        "    self.nextval=None\n",
        "\n",
        "class SLinkedList:\n",
        "  def __init__(self):\n",
        "    self.headval=Node\n",
        "\n",
        "  def listprint(self):\n",
        "    printval=self.headval\n",
        "    while printval is not None:\n",
        "      print(printval.dataval)\n",
        "      printval=printval.nextval\n",
        "  def AtBegining(self,new_data):\n",
        "    NewNode=Node(new_data)\n",
        "    NewNode.nextval=self.headval\n",
        "    self.headval=NewNode\n",
        "\n",
        "list=SLinkedList()\n",
        "list.headval=Node(\"Mon\")\n",
        "e2=Node(\"Tue\")\n",
        "e2=Node(\"Wed\")\n",
        "e3 = Node(\"Wed\")\n",
        "list.headval.nextval=e2\n",
        "e2.nextval=e3\n",
        "list.AtBegining(\"Sun\")\n",
        "list.listprint()"
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "Eb0TQ3IqqOzd"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}
