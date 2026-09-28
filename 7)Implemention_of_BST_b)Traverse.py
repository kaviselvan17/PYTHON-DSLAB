{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNfMW7ecZI0z62dlC4QiKLk",
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
        "<a href=\"https://colab.research.google.com/github/kaviselvan17/PYTHON-DSLAB/blob/main/7)Implemention_of_BST_b)Traverse.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "id": "YErVfeVDnFka",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "f92ad46d-e562-4e87-a2f6-db0ab2604e6e"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "true\n",
            "false\n"
          ]
        }
      ],
      "source": [
        "INT_MIN = -2**32\n",
        "\n",
        "\n",
        "def canRepresentBST(pre):\n",
        "    s = []\n",
        "\n",
        "    root = INT_MIN\n",
        "\n",
        "    for value in pre:\n",
        "\n",
        "        if value < root:\n",
        "            return False\n",
        "\n",
        "        while len(s) > 0 and s[-1] < value:\n",
        "            root = s.pop()\n",
        "\n",
        "        s.append(value)\n",
        "\n",
        "    return True\n",
        "\n",
        "\n",
        "pre1 = [40, 30, 35, 80, 100]\n",
        "\n",
        "print(\"true\" if canRepresentBST(pre1) == True else \"false\")\n",
        "\n",
        "\n",
        "pre2 = [40, 30, 35, 20, 80, 100]\n",
        "\n",
        "print(\"true\" if canRepresentBST(pre2) == True else \"false\")"
      ]
    }
  ]
}