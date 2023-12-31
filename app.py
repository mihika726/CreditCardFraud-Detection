{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "02308e66",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: streamlit in c:\\users\\mihik\\anaconda3\\lib\\site-packages (1.28.2)\n",
      "Requirement already satisfied: watchdog>=2.1.5 in c:\\users\\mihik\\anaconda3\\lib\\site-packages (from streamlit) (2.1.6)\n",
      "Requirement already satisfied: pillow<11,>=7.1.0 in c:\\users\\mihik\\anaconda3\\lib\\site-packages (from streamlit) (9.2.0)\n",
      "Requirement already satisfied: tenacity<9,>=8.1.0 in c:\\users\\mihik\\anaconda3\\lib\\site-packages (from streamlit) (8.2.3)\n",
      "Requirement already satisfied: typing-extensions<5,>=4.3.0 in c:\\users\\mihik\\anaconda3\\lib\\site-packages (from streamlit) (4.3.0)\n",
      "Requirement already satisfied: tzlocal<6,>=1.1 in c:\\users\\mihik\\anaconda3\\lib\\site-packages (from streamlit) (5.2)\n",
      "Requirement already satisfied: blinker<2,>=1.0.0 in c:\\users\\mihik\\anaconda3\\lib\\site-packages (from streamlit) (1.7.0)\n",
      "Requirement already satisfied: numpy<2,>=1.19.3 in c:\\users\\mihik\\anaconda3\\lib\\site-packages (from streamlit) (1.21.5)\n",
      "Requirement already satisfied: rich<14,>=10.14.0 in c:\\users\\mihik\\anaconda3\\lib\\site-packages (from streamlit) (13.7.0)\n",
      "Requirement already satisfied: protobuf<5,>=3.20 in c:\\users\\mihik\\anaconda3\\lib\\site-packages (from streamlit) (4.25.1)\n",
      "Requirement already satisfied: packaging<24,>=16.8 in c:\\users\\mihik\\anaconda3\\lib\\site-packages (from streamlit) (21.3)\n",
      "Requirement already satisfied: pandas<3,>=1.3.0 in c:\\users\\mihik\\anaconda3\\lib\\site-packages (from streamlit) (1.4.4)\n",
      "Requirement already satisfied: tornado<7,>=6.0.3 in c:\\users\\mihik\\anaconda3\\lib\\site-packages (from streamlit) (6.1)\n",
      "Requirement already satisfied: cachetools<6,>=4.0 in c:\\users\\mihik\\anaconda3\\lib\\site-packages (from streamlit) (5.3.2)\n",
      "Requirement already satisfied: validators<1,>=0.2 in c:\\users\\mihik\\anaconda3\\lib\\site-packages (from streamlit) (0.22.0)\n",
      "Requirement already satisfied: pyarrow>=6.0 in c:\\users\\mihik\\anaconda3\\lib\\site-packages (from streamlit) (14.0.1)\n",
      "Requirement already satisfied: altair<6,>=4.0 in c:\\users\\mihik\\anaconda3\\lib\\site-packages (from streamlit) (5.1.2)\n",
      "Requirement already satisfied: requests<3,>=2.27 in c:\\users\\mihik\\anaconda3\\lib\\site-packages (from streamlit) (2.28.1)\n",
      "Requirement already satisfied: pydeck<1,>=0.8.0b4 in c:\\users\\mihik\\anaconda3\\lib\\site-packages (from streamlit) (0.8.1b0)\n",
      "Requirement already satisfied: python-dateutil<3,>=2.7.3 in c:\\users\\mihik\\anaconda3\\lib\\site-packages (from streamlit) (2.8.2)\n",
      "Requirement already satisfied: click<9,>=7.0 in c:\\users\\mihik\\anaconda3\\lib\\site-packages (from streamlit) (8.0.4)\n",
      "Requirement already satisfied: importlib-metadata<7,>=1.4 in c:\\users\\mihik\\anaconda3\\lib\\site-packages (from streamlit) (4.11.3)\n",
      "Requirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in c:\\users\\mihik\\anaconda3\\lib\\site-packages (from streamlit) (3.1.40)\n",
      "Requirement already satisfied: toml<2,>=0.10.1 in c:\\users\\mihik\\anaconda3\\lib\\site-packages (from streamlit) (0.10.2)\n",
      "Requirement already satisfied: jinja2 in c:\\users\\mihik\\anaconda3\\lib\\site-packages (from altair<6,>=4.0->streamlit) (2.11.3)\n",
      "Requirement already satisfied: toolz in c:\\users\\mihik\\anaconda3\\lib\\site-packages (from altair<6,>=4.0->streamlit) (0.11.2)\n",
      "Requirement already satisfied: jsonschema>=3.0 in c:\\users\\mihik\\anaconda3\\lib\\site-packages (from altair<6,>=4.0->streamlit) (4.16.0)\n",
      "Requirement already satisfied: colorama in c:\\users\\mihik\\anaconda3\\lib\\site-packages (from click<9,>=7.0->streamlit) (0.4.5)\n",
      "Requirement already satisfied: gitdb<5,>=4.0.1 in c:\\users\\mihik\\anaconda3\\lib\\site-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.11)\n",
      "Requirement already satisfied: zipp>=0.5 in c:\\users\\mihik\\anaconda3\\lib\\site-packages (from importlib-metadata<7,>=1.4->streamlit) (3.8.0)\n",
      "Requirement already satisfied: pyparsing!=3.0.5,>=2.0.2 in c:\\users\\mihik\\anaconda3\\lib\\site-packages (from packaging<24,>=16.8->streamlit) (3.0.9)\n",
      "Requirement already satisfied: pytz>=2020.1 in c:\\users\\mihik\\anaconda3\\lib\\site-packages (from pandas<3,>=1.3.0->streamlit) (2022.1)\n",
      "Requirement already satisfied: six>=1.5 in c:\\users\\mihik\\anaconda3\\lib\\site-packages (from python-dateutil<3,>=2.7.3->streamlit) (1.16.0)\n",
      "Requirement already satisfied: charset-normalizer<3,>=2 in c:\\users\\mihik\\anaconda3\\lib\\site-packages (from requests<3,>=2.27->streamlit) (2.0.4)\n",
      "Requirement already satisfied: urllib3<1.27,>=1.21.1 in c:\\users\\mihik\\anaconda3\\lib\\site-packages (from requests<3,>=2.27->streamlit) (1.26.11)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\mihik\\anaconda3\\lib\\site-packages (from requests<3,>=2.27->streamlit) (2022.9.14)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\users\\mihik\\anaconda3\\lib\\site-packages (from requests<3,>=2.27->streamlit) (3.3)\n",
      "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in c:\\users\\mihik\\anaconda3\\lib\\site-packages (from rich<14,>=10.14.0->streamlit) (2.17.2)\n",
      "Requirement already satisfied: markdown-it-py>=2.2.0 in c:\\users\\mihik\\anaconda3\\lib\\site-packages (from rich<14,>=10.14.0->streamlit) (3.0.0)\n",
      "Requirement already satisfied: tzdata in c:\\users\\mihik\\anaconda3\\lib\\site-packages (from tzlocal<6,>=1.1->streamlit) (2023.3)\n",
      "Requirement already satisfied: smmap<6,>=3.0.1 in c:\\users\\mihik\\anaconda3\\lib\\site-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (5.0.1)\n",
      "Requirement already satisfied: MarkupSafe>=0.23 in c:\\users\\mihik\\anaconda3\\lib\\site-packages (from jinja2->altair<6,>=4.0->streamlit) (2.0.1)\n",
      "Requirement already satisfied: attrs>=17.4.0 in c:\\users\\mihik\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (21.4.0)\n",
      "Requirement already satisfied: pyrsistent!=0.17.0,!=0.17.1,!=0.17.2,>=0.14.0 in c:\\users\\mihik\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.18.0)\n",
      "Requirement already satisfied: mdurl~=0.1 in c:\\users\\mihik\\anaconda3\\lib\\site-packages (from markdown-it-py>=2.2.0->rich<14,>=10.14.0->streamlit) (0.1.2)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install streamlit\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "94cff3e5",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "b0cd51c3",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2023-11-27 23:02:55.578 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\mihik\\anaconda3\\lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    }
   ],
   "source": [
    "# create Streamlit app\n",
    "st.title(\"Credit Card Fraud Detection Model\")\n",
    "st.write(\"Enter the following features to check if the transaction is legitimate or fraudulent:\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "3e906515",
   "metadata": {},
   "outputs": [],
   "source": [
    "# create input fields for user to enter feature values\n",
    "input_df = st.text_input('Input All features')\n",
    "input_df_lst = input_df.split(',')\n",
    "# create a button to submit input and get prediction\n",
    "submit = st.button(\"Submit\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "7e2aaa06",
   "metadata": {},
   "outputs": [],
   "source": [
    "if submit:\n",
    "    # get input feature values\n",
    "    features = np.array(input_df_lst, dtype=np.float64)\n",
    "    # make prediction\n",
    "    prediction = model.predict(features.reshape(1,-1))\n",
    "    # display result\n",
    "    if prediction[0] == 0:\n",
    "        st.write(\"Legitimate transaction\")\n",
    "    else:\n",
    "        st.write(\"Fraudulent transaction\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5977a200",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
