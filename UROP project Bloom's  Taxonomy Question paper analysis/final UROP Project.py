#!/usr/bin/env python
# coding: utf-8

# In[3]:


import os
import tkinter as tk
from tkinter import filedialog
from docx import Document
import matplotlib.pyplot as plt
from io import StringIO
from io import BytesIO
import sys

def plot_regression_line(key, rate):
    # plotting the actual points as scatter plot
    plt.scatter(key, rate, color="m", marker="o", s=30)
    # putting labels
    plt.xlabel('Bloom\'s Level')
    plt.ylabel('Rate')

    # Save the plot to a BytesIO buffer in binary mode
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    # Create a PhotoImage from the buffer and display it in the Tkinter window
    photo = tk.PhotoImage(data=buffer.getvalue())
    plt.clf()  # Clear the plot for the next use
    label = tk.Label(root, image=photo)
    label.image = photo
    label.pack()

def get_blooms_level(text):
    dic={1:['Choose','Define','Describe','Find','Give','How','Label','List','Match','Name','Omit','Recall','Relate','Select','Show','Spell','Tell','What','When','Where','Which','Who','Why','Write','choose','define','describe','find','give','how','label','list','match','name','omit','recall','relate','select','show','spell','tell','what','when','where','which','who','why','Write'],
                 2:['Clarify','Classify','Compare','Contrast','Demonstrate','Explain','Extend','Illustrate','Infer','Interpret','Outline','Relate','Rephrase','Show','Summarize','Translate','clarify','classify','compare','contrast','demonstrate','explain','extend','illustrate','infer','interpret','outline','relate','rephrase','show','summarize','translate'],
                 3:['Apply','Build','Choose','Construct','Develop','Experiment with','Identify','Interview','Makeuseof','Model','Organize','Plan','Select','Solve','Utilize','Use','Using','apply','build','choose','construct','develop','experiment with','identify','interview','make use of','model','organize','plan','select','solve','utilize','use','using'],
                 4:['Analyze','Assume','Categorize','Classify','Compare','Conclusion','Contrast','Discover','Dissect','Distinguish','Divide','Examine','Function','Inference','Inspect','Justify','List','Motive','Relationships','Simplify','Survey','Take part in','Test for','Theme','analyze','assume','categorize','classify','compare','conclusion','contrast','discover','dissect','distinguish','divide','examine','function','inference','inspect','justify','list','motive','relationships','simplify','survey','take part in','test for','theme'],
                 5:['Agree','Appraise','Assess','Award','Choose','Compare','Conclude','Criteria','Criticize','Decide','Deduct','Defend','Determine','Disprove','Estimate','Evaluate','Explain','Importance','Influence','Interpret','Judge','Justify','Mark','Measure','Opinion','Perceive','Prioritize','Prove','Rate','Recommend','Rule on','Select','Support','Value','agree','appraise','assess','award','choose','compare','conclude','criteria','criticize','decide','deduct','defend','determine','disprove','estimate','evaluate','explain','importance','influence','Interpret','judge','justify','mark','measure','opinion','perceive','prioritize','prove','rate','recommend','rule on','select','support','value'],
                 6:['Adapt','Brief','Briefly','Build','Change','Choose','Combine','Compile','Compose','Construct','Create','Delete','Design','Develop','Discuss','Elaborate','Estimate','Formulate','Happen','Imagine','Improve','Invent','Make up','Maximize','Minimize','Modify','Original','Originate','Plan','Predict','Propose','Solution','Solve','Suppose','Test','Theory','adapt','brief','briefly','build','change','choose','combine','compile','compose','construct','create','delete','design','develop','discuss','elaborate','estimate','formulate','happen','imagine','improve','invent','make up','maximize','minimize','modify','original','originate','plan','predict','propose','solution','solve','suppose','test','theory']}

    for key, list_of_words in dic.items():
        any_word_in_string = any(word in text for word in list_of_words)
        if any_word_in_string:
            return key
    return None


def process_document(file_path):
    doc = Document(file_path)
    blooms_levels = []
    for para in doc.paragraphs:
        print(para.text)
        blooms_level = get_blooms_level(para.text)
        if blooms_level is not None:
            print("The Bloom's level is: ", blooms_level)
            blooms_levels.append(blooms_level)
    
    if blooms_levels:
        plot_regression_line(blooms_levels, list(range(1, len(blooms_levels)+1)))


def open_file_dialog():
    file_path = filedialog.askopenfilename(filetypes=[("Word Documents", "*.docx")])
    if file_path:
        process_document(file_path)

def main():
    global root
    root = tk.Tk()
    root.title("Bloom's Level Analyzer")
    root.geometry("700x800")

    open_button = tk.Button(root, text="Upload the Question Paper Document ", command=open_file_dialog)
    open_button.pack(pady=20)

    # Create a Text widget to display the output in the Tkinter window
    text_output = tk.Text(root, wrap=tk.WORD, width=100, height=100)
    text_output.pack()

    def print_to_textbox(text):
        text_output.insert(tk.END, text + "\n")
        text_output.see(tk.END)

    # Redirect the standard output to the Tkinter Text widget
    sys.stdout = StringIO()
    sys.stdout.write = lambda x: print_to_textbox(x)

    root.mainloop()

if __name__ == "__main__":
    main()


# In[ ]:




